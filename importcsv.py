import csv


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=100):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


# Package class.
class Package:
    def __init__(self, id, vertex, address, city, state, zipcode, deadline, deadlineindicator, deliveredhour,
                 deliveredminute, weight, status, trucknum, loadtime, specialnotes):
        self.id = id
        self.vertex = vertex
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.deadlineindicator = deadlineindicator
        self.deliveredhour = deliveredhour
        self.deliveredminute = deliveredminute
        self.weight = weight
        self.status = status
        self.trucknum = trucknum
        self.loadtime = loadtime
        self.specialnotes = specialnotes

    def __str__(self):  # overwite print(package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s " % (
        self.id, self.vertex, self.address, self.city, self.state, self.zipcode, self.deadline, self.deadlineindicator,
        self.deliveredhour, self.deliveredminute, self.weight, self.status, self.trucknum, self.loadtime,
        self.specialnotes)


# Hash table instance
myHash = ChainingHashTable()


def loadPackageData(fileName):
    with open(fileName) as ptd:
        packageData = csv.reader(ptd, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pVertex = int(package[1])
            pAddress = package[2]
            pCity = package[3]
            pState = package[4]
            pZipcode = package[5]
            pDeadLine = package[6]
            pdeadlineindicator = package[7]
            pdeliveredhour = package[8]
            pdeliveredminute = package[9]
            pweight = package[10]
            pstatus = package[11]
            ptrucknum = package[12]
            ploadtime = package[13]
            pSpecialNotes = package[14]

            # package object
            p = Package(pID, pVertex, pAddress, pCity, pState, pZipcode, pDeadLine, pdeadlineindicator, pdeliveredhour,
                        pdeliveredminute, pweight, pstatus, ptrucknum, ploadtime, pSpecialNotes)
            # print(p)

            # insert it into the hash table
            myHash.insert(pID, p)
