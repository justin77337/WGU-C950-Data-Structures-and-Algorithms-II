#Student Name: Justonna Naing
#Student ID: 001467971

from hashTable import ChainingHashTable
from readCSV import *
import datetime

#find distance between two addresses
def distancInBetween(add1, add2):
    vreturn = 0
    h = addressData.index(add1)
    j = addressData.index(add2)

    vreturn = distanceData[h][j]

    return float(vreturn)

#minimum distance from the current location
def min_distance(currentAddress, packages):
    minimum = 1000
    next_Address = ''
    next_id = 0

    for pkg_id in packages:
        pkg = myHash.search(pkg_id)
        address2 = pkg.address

        distance = distancInBetween(currentAddress, address2)

        if distance < minimum:
            minimum = distance
            next_Address = address2
            next_id = pkg_id

    return next_Address, next_id, minimum               #return nextAddress, nextID and minimumDistance Value


#Calculating the route with Greedy Algorithm
def deliveryPackages(truck):
    currentLocation = '4001 South 700 East'              #Start from Hub
    miles = 0

    # n^2
    while len(truck.packages) > 0:
        next_address, next_id, distance = min_distance(currentLocation, truck.packages)
        miles = miles + distance
        delivery_time = (distance / 18) * 60 * 60

        dts = datetime.timedelta(seconds=delivery_time)

        truck.time = truck.time + dts

        pkg = myHash.search(next_id)

        pkg.deliver_time = truck.time
        # pkg.start = "[Left from Hub at {}]".format(truck.time_left)
        pkg.start = truck.time_left

        truck.packages.remove(next_id)
        currentLocation = next_address

    return miles


#Load Data Into HashTable
myHash = ChainingHashTable()
loadData('WGUPS_Package_File.csv', myHash)

#Creating Array and Load Address Data
addressData = []
loadAddressData('addresses.csv', addressData)

#Creating Array and Load Distance Data
distanceData = []
loadDistanceData('distance_table.csv', distanceData)

#Manually Loading Packages Into the Trucks
t1 = [1, 13, 14, 15, 19, 20, 29, 30, 31, 34, 37, 40, 16, 35, 39, 10]
t2 = [3, 18, 38, 36, 6, 25, 28, 32]
t3 = [2, 4, 5, 7, 8, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 9]

#Truck 1
start_time = '08:00:00'
h, m, s = start_time.split(":")
time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
truck1 = Truck(t1, time_object)
t1miles = round(deliveryPackages(truck1), 2)

#Truck 2
start_time = '09:05:00'
h, m, s = start_time.split(":")
time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
truck2 = Truck(t2, time_object)
t2miles = round(deliveryPackages(truck2), 2)

#Truck 3
start_time = '11:00:00'
h, m, s = start_time.split(":")
time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
truck3 = Truck(t3, time_object)
t3miles = round(deliveryPackages(truck3), 2)


total_miles = t1miles + t2miles + t3miles               #Total Miles calculation


#User Interface Menu
class Main:
    while True:
        print("WGUPS Program: ")
        print("Enter 'R' to run the application: All other entries will quit the application:", end=" ")
        text = input().upper()
        if text == "R":
            try:
                # The user will be asked to enter a specific time
                user_time = input("Please enter a time to check status of packages with following format, HH:MM:SS: ")
                (h, m, s) = user_time.split(":")
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # The user will be asked if they want to see the status of all packages or only one
                choice = input(
                    "To view the status of an individual package please type 'I'. For a rundown of all"
                    " packages please type 'A'. ").upper()

                # If the user enters "I" the program will ask for an package ID
                if choice == "I":
                    print()
                    try:
                        # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                        solo_input = input("Enter the package ID (1 - 40): ")
                        package = myHash.search(int(solo_input))
                        package.update_status(convert_timedelta)
                        print(str(package))
                        print()
                    except ValueError:
                        print("Invalid Entry. Closing program.")
                        exit()

                # If the user types "A" the program will display all package information
                elif choice == "A":
                    print()
                    try:
                        for packageID in range(1, 41):
                            package = myHash.search(packageID)
                            package.update_status(convert_timedelta)
                            print(myHash.search(packageID))
                        print()
                        print("Truck 1 Miles: ", t1miles,"Truck 1 leave from the Hub at ", truck1.time_left, " Drive for ",truck1.time - truck1.time_left, "hours", " Finished at ", truck1.time)
                        print("Truck 2 Miles: ", t2miles,"Truck 2 leave from the Hub at ", truck2.time_left, " Drive for ",truck2.time - truck2.time_left, "hours",  " Finished at ", truck2.time)
                        print("Truck 3 Miles: ", t3miles,"Truck 3 leave from the Hub at ", truck3.time_left, " Drive for ",truck3.time - truck3.time_left, "hours",  " Finished at ", truck3.time)
                        print("Total Miles: ", total_miles)
                        print()
                    except ValueError:
                        print("Invalid Entry. Closing program.")
                        exit()
                else:
                    exit()
            except ValueError:
                print("Invalid Entry. Closing program.")
                exit()
        elif input != "start":
            print("Invalid Entry. Closing program.")
            exit()




