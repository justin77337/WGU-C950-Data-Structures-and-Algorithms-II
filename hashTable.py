#Chaining HashTable Class
class ChainingHashTable:
    # Constructor with initial capacity of 40.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):

        self.table = []                             #initialize with empty list
        for i in range(initial_capacity):
            self.table.append([])

    #Insert new items to the HashTable
    def insert(self, key, item):
        bucket = int(key) % len(self.table)         #get the bucket list of where items will go
        bucket_list = self.table[bucket]

        for kv in bucket_list:                      #update key if it is already in the bucket
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]                     #if not, insert the item to the end of the bucket list
        bucket_list.append(key_value)
        return True

    #Search for an item with matching key in the HashTable
    def search(self, key):
        bucket = int(key) % len(self.table)         #get the bucket list where item would be
        bucket_list = self.table[bucket]

        for kv in bucket_list:                      #serach for the key in the bucket list
            if kv[0] == key:
                return kv[1]
        return None

    #Remove an item with matching key from the HashTable
    def remove(self, key):
        bucket = int(key) % len(self.table)         #get the bucket list where item will be removed from
        bucket_list = self.table[bucket]

        for kv in bucket_list:                      #remove item from the bucket list if it has matching key
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
