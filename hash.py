# hash table implementation using python

# This is the dictionary we are trying to implement using hash tables
data = {'Abel':90, 'Biruk':87, 'Kebede':91, 'Essayas':89, 'Debi':92,
        'Biniyam':65, 'Solomon':79, 'Almaz':88, 'Tariku':65, 'Micheal':78,
        'Racheal':70}

hash_table = [[] for i in range(20)]

def hashing_function(key):
    return ord(key[0])%20

for i in data.keys():
    location = hashing_function(i)
    j = 1
    while True:
        if hash_table[location] == []:
            hash_table[location] = [i, data[i]]
            break
        else:
            location = (location + j**2)%20
            j += 1
# now all values have been placed in the hash table
# and now to search for values

def search(key):
    location = hashing_function(key)
    j = 1
    while True:
        if hash_table[location][0] == key:
            return hash_table[location][1], location
            break
        else:
            location = (location + j**2)%20
            j += 1