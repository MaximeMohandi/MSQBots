import _sqlite3 as sqlite
import exception as ex
import os


class MeterDatabase:
    """Connection to the nice meter database"""
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), 'nice_meter.db')
        self.conn = sqlite.connect(db_path)
        self.__create_meter_tables__()

    def __create_meter_tables__(self):
        """Create required tables for nice meters to register score"""
        cursor = self.conn.cursor()
        try:
            cursor.executescript('''
                CREATE TABLE IF NOT EXISTS meters (
                    id_meter INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_meter VARCHAR(255) NOT NULL,
                    rules_meter VARCHAR(255)
                );
                    
                CREATE TABLE IF NOT EXISTS participants (
                    id_participant INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_participant VARCHAR(255)
                );
                    
                CREATE TABLE IF NOT EXISTS score (
                    fk_meter INTEGER NOT NULL,
                    fk_participant INTEGER NOT NULL,
                    score INTEGER DEFAULT 0,
                    FOREIGN KEY(fk_meter) REFERENCES meters(id_meter),
                    FOREIGN KEY(fk_participant) REFERENCES participants(id_participant)
                );
            ''')

        except (sqlite.IntegrityError, sqlite.InternalError, sqlite.OperationalError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def insert_meter(self, name, rules):
        """Insert a meter into database

        Parameters
        -----------
            name: :class:`str`
                meter's name
            rules: :class:`str`
                meter's rules

        Returns
        -------
            :class:`int`
                Inserted element id

        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO meters (
                    name_meter,
                    rules_meter
                ) VALUES ( ?,  ?);
            ''', [name, rules])
            self.conn.commit()
            return cursor.lastrowid
        except (sqlite.DatabaseError, sqlite.InterfaceError, sqlite.OperationalError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def select_meters(self):
        """Select all meters in database

        Returns
        -------
            :class:`list`
                List of meters registered in database

        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT * FROM meters')
            return cursor.fetchall()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def select_one_meters_details(self, meter):
        """Select one meter with scoreboard
        Parameters
        -----------
            meter: :class:`str`
                meters's name
        Returns
        -------
            :class:`list`
                details on meters
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
            SELECT 
                m.name_meter,
                m.rules_meter,
                p.name_participant,
                s.score
            FROM meters m
            INNER JOIN score s ON s.fk_meter = m.id_meter
            INNER JOIN participants p ON p.id_participant = s.fk_participant
            WHERE m.name_meter = ?
            ''', [meter])
            return cursor.fetchall()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqbitsReporterException
        finally:
            cursor.close()

    def remove_meter(self, name):
        """Delete meter from database

        Delete all score link with the meter and the meter

        Parameters
        -----------
            name: :class:`str`
                meter to delete
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                DELETE FROM score 
                WHERE fk_meter = (
                    SELECT id_meter FROM meters
                    WHERE name_meter = ?
                )
            ''', [name])
            cursor.execute('DELETE FROM meters WHERE name_meter = ?', [name])
            return self.conn.commit()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def insert_participant(self, name):
        """Insert a participant into database

        Parameters
        -----------
            name: :class:`str`
                participant's name
        Returns
        -------
            :class:`int`
                Inserted element id
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO participants (name_participant)
                SELECT ?
                WHERE NOT EXISTS(SELECT 1 FROM participants WHERE name_participant = ?);
            ''', [name, name])
            self.conn.commit()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def select_participants_details(self):
        """Select all participants registered with details

            Get all participants with his meters and scores

            Returns
            -------
                :class:`list`
                    List of participant registered in database

            Raises
            -------
                MsqDataBaseError
                    An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT * 
                FROM participants p
                INNER JOIN score s ON s.fk_participant = p.id_participant
                INNER JOIN meters m ON m.id_meter = s.fk_meter 
            ''')
            return cursor.fetchall()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def select_one_participant_details(self, name):
        """Select designed participants registered with details

            Get participants with his meters and scores

            Parameters
            -----------
                name: :class:`str`
                    participant's name
            Returns
            -------
                :class:`dict`
                    List of participant registered in database

            Raises
            -------
                MsqDataBaseError
                    An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT 
                    p.name_participant,
                    s.score,
                    m.name_meter
                FROM participants p
                INNER JOIN score s ON s.fk_participant = p.id_participant
                INNER JOIN meters m ON m.id_meter = s.fk_meter 
                WHERE p.name_participant = ?
            ''', [name])
            return cursor.fetchall()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def select_one_participant(self, name):
        """Select designed participants registered with details

            Parameters
            -----------
                name: :class:`str`
                    participant's name
            Returns
            -------
                :class:`dict`
                    Participant registered in database
            Raises
            -------
                MsqDataBaseError
                    An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT * FROM participants
                WHERE name_participant = ?
            ''', [name])
            return cursor.fetchone()
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def insert_score(self, name_meter, name_participant):
        """Insert a new score into database

        Parameters
        -----------
            name_meter: :class:`str`
                name of the meter to link
            name_participant: :class:`str`
                name of the participant to score
        Returns
        -------
            :class:`int`
                last inserted id
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO score (
                    fk_meter,
                    fk_participant
                ) VALUES(
                    (SELECT id_meter FROM meters WHERE name_meter=?),
                    (SELECT id_participant FROM participants WHERE name_participant=?)
                );
            ''', [name_meter, name_participant])
            self.conn.commit()
            return cursor.lastrowid
        except (sqlite.DatabaseError, sqlite.InterfaceError):
            raise ex.MsqDataBaseError
        finally:
            cursor.close()

    def update_score(self, name_meter, name_participant, score):
        """Update existing score into database

        Parameters
        -----------
            name_meter: :class:`str`
                name of the meter
            name_participant: :class:`str`
                name of the participant
            score: :class:`int`
                the participant's score for the selected meter
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE score
                SET score = score + ?
                WHERE fk_meter = (
                    SELECT id_meter FROM meters WHERE name_meter=?
                )
                AND fk_participant = (
                    SELECT id_participant FROM participants WHERE name_participant=?
                );
            ''', [score, str(name_meter), name_participant])
            self.conn.commit()
            return cursor.lastrowid
        except (sqlite.DatabaseError, sqlite.InterfaceError) as err:
            print(err)
            raise ex.MsqDataBaseError
        finally:
            cursor.close()
