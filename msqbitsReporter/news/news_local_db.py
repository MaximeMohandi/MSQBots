import _sqlite3 as db


class LocalDatabase:
    """Connection to the local database"""

    def __init__(self,):
        dataBasePath = "news/msqbreporter_database.db"
        self.conn = db.connect(dataBasePath)
        self.__create_news_table__()

    def __create_news_table__(self):
        """Create the tables composing the database"""
        cursor = self.conn.cursor()
        try:
            cursor.executescript('''
                CREATE TABLE IF NOT EXISTS categories (
                    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category_name TEXT NOT NULL
                );
                
                INSERT OR REPLACE INTO `categories` 
                    (`category_id`, `category_name`) 
                VALUES
                    (1, 'IT'),
                    (2, 'Monde'),
                    (3, 'Transport'),
                    (4, 'Jeux Vidéo');
                            
                CREATE TABLE IF NOT EXISTS newspapers (
                    newspaper_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    newspaper_title varchar(255) DEFAULT NULL,
                    newspaper_website varchar(255) DEFAULT NULL,
                    newspaper_rss_link varchar(255) NOT NULL,
                    newspaper_category int(11) NOT NULL,
                    FOREIGN KEY(newspaper_category) REFERENCES categories(category_id)
                );
            ''')
        except (db.IntegrityError, db.InternalError, db.OperationalError):
            raise

        finally:
            cursor.close()

    def insert_newspaper(self, title, website, rss_link, category_name):
        """Insert a new newspaper into the database

        Parameters
        -----------
            title: :class:`str`
                newspaper title
            website: :class:`str`
                newspaper website url
            rss_link: :class:`str`
                newspaper rss feed link
            category_name: :class:`str`
                newspaper category name

        Returns
        -------
            :class:`int`
                Inserted element id

        Raises
        -------
            DatabaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO newspapers (
                    newspaper_title, 
                    newspaper_website, 
                    newspaper_rss_link, 
                    newspaper_category
                ) VALUES ( ?,  ?,  ?,  (
                        SELECT c.category_id
                        FROM categories c
                        WHERE c.category_name = ?
                    )
                );
            ''', [title, website, rss_link, category_name])
            self.conn.commit()
            return cursor.lastrowid
        except (db.DatabaseError, db.InterfaceError):
            raise
        finally:
            cursor.close()

    def delete_newspaper(self, newspaper_name):
        """Delete a newspaper from the database

        Parameters
        -----------
            newspaper_name: :class:`str`
                name of the newspaper to delete

        Raises
        -------
            DatabaseError
                Error occurred on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''DELETE FROM newspapers WHERE newspaper_title = (?)''', [newspaper_name])
            self.conn.commit()
        except db.DatabaseError:
            raise
        finally:
            cursor.close()

    def select_newspapers(self):
        """Selected all the newspaper stored into the database

        Returns
        -------
            :class:`list`
                A list of newspapers stored on database

        Raises
        -------
            DatabaseError
                Error occurred on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT 
                    n.newspaper_title, 
                    c.category_name, 
                    n.newspaper_website, 
                    n.newspaper_rss_link
                FROM newspapers n
                INNER JOIN categories c ON c.category_id = n.newspaper_category
            ''')

            return cursor.fetchall()

        except db.DatabaseError:
            raise

        finally:
            cursor.close()

    def select_newspaper_by_title(self, title):
        """Select newspapers with the given title

        Parameters
        -----------
            title: :class:`str`
                Title of the newspaper wanted to select

        Returns
        -------
            :class:`list`
                List of all newspaper with the given title in database

        Raises
        -------
            DatabaseError
                Error occurred on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT 
                    n.newspaper_title, 
                    c.category_name, 
                    n.newspaper_website, 
                    n.newspaper_rss_link
                FROM newspapers n
                INNER JOIN categories c ON c.category_id = n.newspaper_category
                WHERE n.newspaper_title = ?
            ''', [title])

            return cursor.fetchall()

        except db.DatabaseError:
            raise
        finally:
            cursor.close()

    def select_newspaper_by_cat(self, category_name):
        """Select all the newspaper into the category

        Parameters
        -----------
            category_name: :class:`str`
                Newspaper category nam

        Returns
        -------
            :class:`list`
                A list of all newspaper with the given category

        Raises
        -------
            DatabaseError
                Error occurred on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT 
                    n.newspaper_title, 
                    c.category_name, 
                    n.newspaper_website, 
                    n.newspaper_rss_link
                FROM newspapers n
                INNER JOIN categories c ON c.category_id = n.newspaper_category
                WHERE c.category_name = ?
            ''', [category_name])
            return cursor.fetchall()

        except db.DatabaseError:
            raise
        finally:
            cursor.close()

    def select_categories(self):
        """Get all the categories stored into the database

        Returns
        -------
            :class:`list`
                A list of category available on the database

        Raises
        -------
            DatabaseError
                Error occurred on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT c.category_name
                FROM categories c
            ''')
            return cursor.fetchall()

        except db.DatabaseError:
            raise
        finally:
            cursor.close()

