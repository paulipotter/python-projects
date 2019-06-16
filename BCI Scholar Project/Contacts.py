#  Author: Paula Mendez
#  email: paulipotter@ksu.edu
#  Contacts.py

''' Object *Contact* is inside of every calf object. It contains the second calf
contacted, the total seconds contacted during the study days and a list that 
contains the number of seconds contacted between calf *a* and calf *b* separated
by day'''

class Contacts:
    def __init__(self):  # int, int, list
        self.contact_buddy = 0
        #this number adds up all the items in the list below
        self.total_seconds = 0

        # each index represents a day and the number at that index is the amount of
        # contacts between those two calves during that day
        self.record_dates = []

    @staticmethod
    def increment_contact(self, day):
        self.total_seconds += 1
        self.record_dates[day-1] += 1

    def print_one(self) -> object:
        return str(self.contact_buddy) + ','  + str(self.total_seconds) + ',' + ",".join(str(item) for item in self.record_dates)
