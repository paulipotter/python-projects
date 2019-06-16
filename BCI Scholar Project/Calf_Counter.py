from __future__ import print_function import pymysql from Calf import * import csv, json, sys, os
''' Calf_counter.py creates and fills out the dictionary with the corresponding calf and contacts objects. 
The most important part is that it creates a dictionary with a key for each calf (101-170) with a *calf* object as value. 
The content of the *calf* object will be explained in Calf.py and below.'''


calf_list = {}
day = ZERO 

#  creates the dictionary that will be used throughout the program
def create_dict(total_study_days):
    # create new dict with INT as key and an object->(healthycount, sickcount, sick)
    # test Paula
    test=Calf(total_study_days)
    current_calf_tag = CALF_TAG_101
    print('Creating Dictionary...')

    #loop thru all 70 calves
    while current_calf_tag < CALF_TAG_171: #inner loop created contact instances, one per calf (excluding itself)
        calf_list[current_calf_tag] = {
        "sick_count":test.sickCount,
        "healthy_count":test.healthyCount,
        "sick":test.sick}
        current_calf_tag+= ONE

    # Create buddy properties
    current_calf_tag = CALF_TAG_101 
    while current_calf_tag < CALF_TAG_171:
        for i in range(CALF_TAG_101,CALF_TAG_171):
            calf_list[current_calf_tag][i]={"total_seconds":test.total_seconds,"seconds_by_day":test.seconds_by_day}
        calf_tag+= ONE

    #print(calf_list)
    return calf_list

# uses mysql to pull data and temporarily store it into an array as [calftag1, x, y, calftag2, x, y]
def pull_data(index):
    # pull data with mysql
    print("Pulling Data")
    db = pymysql.connect(host='mysql.cis.ksu.edu', user='paulipotter', passwd='', db='proj_bci')
    cursor = db.cursor()

    try:
        # this is going to pull all calftags that were .3 meters from each other for 1 second
        query = """
            SELECT a.calftag, b.calftag
            FROM rawrtls a, rawrtls b MySQL - proj_bci@mysql.cis.ksu.edu
            WHERE a.calftag < b.calftag
                AND ((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)) <= .09
                AND a.ts BETWEEN {commence} AND {adjourn}
                AND a.ts = b.ts;
        """.format(commence=index, adjourn=index + SECONDS)


        print("execure query",cursor.execute(query))
        contacts = []

        #  takes all tuple results and stores it in an list
        for i, row in enumerate(cursor.fetchall()):
            contacts.append(row)
    except:
        print(sys.exc_info())
        print('Error.')
        db.rollback()
        exit()

    db.close()
    return contacts


# imports the CSV file that states when the calves were shedding. this is added to each CALF object's sick list.
def health_status(calf_list):

    with open('shedding_times1.csv') as csv_file:
        print('Reading CSV...')

        read_csv = csv.reader(csv_file, delimiter=',')

        read_csv.next()

        # read each row and cell, correspond 0s and 1s to the health state of the given calf on the given day
        for row in read_csv:
            temp_list = []
            for i in range(1, 25):
                temp_list.append(row[i] == '1')
            calf_list[int(row[0])]['sick'] = []
            calf_list[int(row[0])]['sick'].extend(temp_list)
            #print('list', calf_list[int(row[0])]['sick'])
            #print('len', len(calf_list[int(row[0])]['sick']))
        #
        # for i in range(1, 25):
        #         calf_list[read_csv.line_num+99]["sick"].insert(i-1, row[i] == '1')
        #   #  print (read_csv.line_num+99)
        #     print(len(calf_list[(read_csv.line_num)+99]["sick"]))
        #
        print('Finished reading CSV...')
        #print(calf_list[101]["sick"])
        #print(calf_list[102]["sick"])
    return calf_list


#calf_contacts is the list of tuples obtained from the pull_data() function and day indicates which day we are in the loop right now
def add_counts(calf_contact, day):
    #key : calf_a
        #   "sick_count"
        #   "healthy_count"
        #   "sick"
        #    key: calf_b
            #   "total_seconds"
            #   "seconds_by_day"

    for calf_a, calf_b in calf_contact:
        elapsed_seconds = 0
        calf_a, calf_b = int(calf_a), int(calf_b)
        calf_list[calf_b]["sick_count" if calf_list[calf_a]["sick"][day] else 'healthy_count'] += 1
        calf_list[calf_a]["sick_count" if calf_list[calf_b]["sick"][day] else 'healthy_count'] += 1

        calf_list[calf_a][calf_b]["total_seconds"] += 1  # increase the buddy 'total seconds' by 1
        calf_list[calf_b][calf_a]["total_seconds"] += 1  # increase the buddy 'total seconds' by 1

        if day > 0:
            d = day
            while d > 0:
                s = calf_list[calf_b][calf_a]["seconds_by_day"][d]
                elapsed_seconds += s
            calf_list[calf_a][calf_b]["seconds_by_day"] = calf_list[calf_a][calf_b]["total_seconds"] - elapsed_seconds
            calf_list[calf_b][calf_a]["seconds_by_day"] = calf_list[calf_a][calf_b]["total_seconds"] - elapsed_seconds

        else:
            calf_list[calf_a][calf_b]["seconds_by_day"] = calf_list[calf_a][calf_b]["total_seconds"]
            calf_list[calf_b][calf_a]["seconds_by_day"] = calf_list[calf_a][calf_b]["total_seconds"]

    # print("right out of for loop, adding counts", str(calf_list[142][153]["seconds_by_day"]))
    # print("total seconds ", calf_list[142][153]["total_seconds"])


def export_data():
    if not os.path.exists("./results"):
        os.makedirs("./results")
        for calf in calf_list:

            filename =str(calf)+"_result.json"

            with open("./results/"+filename,"w") as f:
                json.dump(calf_list[calf],f, sort_keys = True, indent = 4, separators = (',',':'))

    print("The program has successfully exported all 70 JSON files")

    # with open('result.csv','w') as csvfile:
    #     fieldnames = ['Calf','Study Day']
    #     for calf in range(101,171):
    #         fieldnames.append(calf)
    #         fieldnames.append(str(calf).join(str(" Health Status")))
    #     w = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     w.writeheader()
    #     line = ""
    #
    #     for day in range(1, 29):
    #
    #         for calf in calf_list:
    #             for buddy in calf_list[calf]["contacts_by_day"][day]:
    #               #  line +=
