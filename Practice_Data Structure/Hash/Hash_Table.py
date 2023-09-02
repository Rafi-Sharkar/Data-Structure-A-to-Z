class Hash_Table:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def hash_function(self, value):
        return abs(value)%self.capacity
    
    def put(self, a):
        load_factor = self.size/self.capacity
        print(f"Load factor {a}: {load_factor}")
        if load_factor >= 0.6:
            self.rehash()
    
        hash_value = self.hash_function(a)

# Separate chaining
        if self.table[hash_value] is None:
            self.table[hash_value] = [a]
        else:
            self.table[hash_value].append(a)
        self.size += 1
    
    def delete(self, a):
        hash_value = self.hash_function(a)

        if self.table[hash_value] != None and a in self.table[hash_value]:
            self.table[hash_value].remove(a)
            self.size -= 1
    
    def find(self, a):
        hash_value = self.hash_function(a)

        if self.table[hash_value] != None and a in self.table[hash_value]:
            return True
        return False
    
    def rehash(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for bucket in self.table:
            if bucket is not None:
                for value in bucket:
                    # creating new Index
                    new_hash_value = abs(value)%new_capacity
                    if new_table[new_hash_value] is None:
                        new_table[new_hash_value] = [value]
                    else:
                        new_table[new_hash_value].append(value)
                    
            self.table = new_table
            self.capacity = new_capacity
    
    def print_table(self):
        for i in enumerate(self.table):
            print(f"Index: {i} - Value: {value}")
    def printhash(self):
        for i in self.table:
            print(i)
# Create a hash table
ht = Hash_Table()
ht.put(18)
ht.put(75)
ht.put(25)
ht.delete(18)
ht.delete(75)
ht.put(18)
ht.put(15)
ht.put(159)
if ht.find(25):
    ht.put(24)
    ht.delete(18)
else:
    ht.put(18)
if ht.size > 7:
    ht.put(24)
ht.delete(75)

# Print final state of the hash table
print("Final Hash Table:")
# ht.print_table()
ht.printhash()
print("Final Capacity:", ht.capacity)
print("Final Count:", ht.size)
print("Final Load Factor:", ht.size / ht.capacity)