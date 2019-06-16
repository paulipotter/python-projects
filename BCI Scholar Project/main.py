from __future__ import print_function
from Calf_Counter import *
from sqltest import *
import json, pprint

''' The purpose of this project id to use a database of x-y coordinates of 70 calves to determine when they contacted (closer than a foot to each other)'''
''' The MySQL database stored in the CISLinux server at Kansas State University contains data corresponding to every second from 2016-05-07 00:00:00 to 2016-05-27 02:59:59  for every calf'''
''' 70 Calves * 86400 seconds * 20 days = ~120 Million rows of data'''

total_study_days = 24
contacts=[]

# big loop through all 2.5 ish seconds -- most likely a nested loop
# when seconds = 86400 -- day++
calf_list = create_dict(total_study_days)

#imports the csv file that contains shedding data
calf_list = health_status(calf_list)

window = 60*60 # window for grouping time default = 30 secs
frames = 86400/window #this gives total time frams in a day based on the window chosen

start = 1462597200 #  2016-05-07 00:00:00
end = 1464335999 #  2016-05-27 02:59:59 AM
index = start
day = 0

while day < total_study_days: #24:
    #day = (index - start) % 86400
    groupings = 0
    #loop through the frames
    while groupings < frames:
        # returns a list of pairs of contacts
        contacts = pull_data(index)

        index += window
        #increment the appropriate counts
        add_counts(contacts, day)

        groupings +=1

    day +=1
# export data to a CSV File
export_data()
