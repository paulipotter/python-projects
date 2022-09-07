from constants import all 
class Calf:
    def __init__(self, total_study_days):
        self.sickCount = ZERO 		# this is count of seconds a cow has touched a sick cow
        self.healthyCount = ZERO  	# this is count of seconds a cow has touched a healthy cow
        self.sick = [] 			# this gives health status of a cow on a given day
        i = ZERO 
        index = CALF_TAG_101
       	# contact properties:
        self.buddy=[i for i in range(CALF_TAG_101,CALF_TAG_171)] # this gives list of cows that are present        
        self.total_seconds = ZERO 	# total seconds of contact with any buddy cow
        self.seconds_by_day = [ ZERO for _ in range(total_study_days)]


    #def print_one(self) -> object:
    #    return str(self.buddy) + ','  + str(self.total_seconds) + ',' + ",".join(str(item) for item in self.seconds_by_day)
