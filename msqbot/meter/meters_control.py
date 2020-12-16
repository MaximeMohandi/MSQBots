import meter.meter_db as database
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
        """
        self.db.insert_meter(name, rules)
        for participant in participants:
            self.add_participant(participant, name)

    def remove_meter(self, meter):
        """Add a participant to a meter

        Parameters
        -----------
            meter: :class:`name`
                meter's name
        """
        self.db.remove_meter(meter)

    def add_rule(self, rule, meter):
        """ Add meter's rule

        :Parameters
        -----------
            rule: :class:`str`
                meter's rule
            meter: :class:`str`
                meter's name
        """
        self.db.insert_rule(meter, rule)

    def remove_rule(self, rule, meter):
        """ Remove a meter's rule

        :Parameters
        -----------
            rule: :class:`str`
                meter's rule
            meter: :class:`str`
                meter's name
        """
        self.db.delete_rule(meter, rule)

    def add_participant(self, name, meter):
        """Add a participant to a meter

        Parameters
        -----------
            name: :class:`str`
                participant's name
            meter: :class:`name`
                meter's name
        """
        self.db.insert_participant(name)
        self.db.insert_score(meter, name)

    def remove_participant(self, name, meter):
        """remove a participant from a meter

        Parameters
        -----------
            name: :class:`str`
                participant's name
            meter: :class:`name`
                meter's name
        """
        self.db.delete_participant_from(name, meter)

    def update_score(self, meter, participant, score):
        """update participant score

        Parameters
        -----------
            meter: :class:`str`
                meter's name
            participant: :class:`str`
                participant's name
            score: :class:`str`
                score number
        """
        self.db.update_score(meter, participant, score)

    def get_all_meters(self):
        """Get all meters

        Returns
        -------
            :class:`list`
                Dict of meters with participants count
        """
        meters = self.db.select_meters()
        return [meter[1] for meter in meters]

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
        """
        meter_detail = self.db.select_one_meters_details(meter)
        return{
            'meter': meter_detail[0][0],
            'rules': meter_detail[0][1],
            'participants': [{
                'name': detail[2],
                'score': detail[3]
            } for detail in meter_detail]
        }

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
        """
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
