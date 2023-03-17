import csv
from hashTable import ChainingHashTable
import datetime

#Create Class for the Trucks
class Truck:
    def __init__(self, packages, time_left):
        self.packages = packages
        self.time_left = time_left
        self.time = time_left

#Creat Class for the Packages
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.start = None
        self.status = 'At Hub'
        self.deliver_time = None

    def __str__(self):
        return "Package ID: %s, " "Address: %s %s %s %s, Deadline: %s, Weight: %s, Schedule to leave: %s, Status: %s" % (
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.deadline,
            self.weight,
            self.start,
            self.status)

    #To update Delivery Status
    def update_status(self, input_time):
        if self.deliver_time < input_time:
            self.status = "Delivered at {}!".format(self.deliver_time)
            #self.status = self.deliver_time
        elif self.start > input_time:
            self.status = "At Hub!"
        else:
            self.status = "En Route!"
        if input_time >= datetime.timedelta(hours=int(10), minutes=int(20), seconds=int(00)) and self.id == 9:
            self.address = "410 S State St.r"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip = "84111"



#Read the package file and load into HashTable
def loadData(fileName, myHash):
    with open(fileName) as csvfile:                     #read the file
        read_csv = csv.reader(csvfile, delimiter=',')
        # next(read_csv)
        for row in read_csv:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = row[6]
            note = row[7]
            pkg = Package(id, address, city, state, zip, deadline, weight)

            myHash.insert(id, pkg)

#Read the address file
def loadAddressData(fileName, addressData):
    with open(fileName) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            addressData.append(row[2])

#read the distance file
def loadDistanceData(fileName, distanceData):
    with open(fileName) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            distanceData.append(row)


