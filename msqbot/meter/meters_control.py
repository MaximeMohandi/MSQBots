import meter.meter_db as database
import exception as ex


class MeterControls:
    """Controller for meters"""
    def __init__(self):
        self.db = database.MeterDatabase()

    def create_meter(self, name, participants, rules):
        """Create a new meter

        Parameters
        -----------
            name: :class:`str`
                meter's name
            participants: :class:`list`
                start score for meter
            rules: :class:`str`
                meter's rules
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:

            self.db.insert_meter(name, rules)
            for participant in participants:
                self.add_participant(participant, name)
        except ex.MsqbitsReporterException:
            raise

    def add_participant(self, name, meter):
        """Add a participant to a meter

        Parameters
        -----------
            name: :class:`str`
                participant's name
            meter: :class:`name`
                meter's name
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:
            self.db.insert_participant(name)
            self.db.insert_score(meter, name)
        except ex.MsqbitsReporterException:
            raise

    def update_score(self, meter, participant, score):
        """update participant score

        Parameters
        -----------
            meter: :class:`str`
                meter's name
            participant: :class:`str`
                participant's name
            score: :class:`int`
                score number
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:
            self.db.update_score(meter, participant, score)
        except ex.MsqbitsReporterException:
            raise

    def get_all_meters(self):
        """Get all meters

        Returns
        -------
            :class:`list`
                Dict of meters with participants count
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:
            meters = self.db.select_meters()
            return [meter[1] for meter in meters]
        except ex.MsqbitsReporterException:
            raise

    def get_meter_scoreboard(self, meter):
        """Get the scoreboard for meter

        Parameters
        -----------
            meter: :class:`name`
                meter's name
        Returns
        -------
            :class:`dict`
                Dict of meters with participants count
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:
            meter_detail = self.db.select_one_meters_details(meter)
            return{
                'meter': meter_detail[0][0],
                'rules': meter_detail[0][1],
                'participants': [{
                    'name': detail[2],
                    'score': detail[3]
                } for detail in meter_detail]
            }
        except ex.MsqbitsReporterException:
            raise

    def get_participant_summary(self, name):
        """Get participants details on meter

        Parameters
        -----------
            name: :class:`str`
                participant's name
        Returns
        -------
            :class:`dict`
                Dict of meters with participants count
        Raises
        -------
            MsqDataBaseError
                An occurred with the query on the database
        """
        try:
            details = self.db.select_one_participant_details(name)
            summary = {
                'nom': details[0][0],
                'total_score': 0,
                'meters': []
            }
            for detail in details:
                summary['total_score'] += detail[1]
                summary['meters'].append({
                    'name': detail[2],
                    'score': detail[1]
                })
            return summary
        except ex.MsqbitsReporterException:
            raise