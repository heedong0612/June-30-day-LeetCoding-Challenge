from random import randint

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = dict()
        self.arr = []
        
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash.keys():
            return False

        self.arr.append(val)
        self.hash[val] = len(self.arr) - 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash.keys():
            return False

        index = self.hash[val]

        lastVal = self.arr[-1]
        self.hash[lastVal] = index
        self.arr[index] = lastVal
        
        self.arr.pop()
        self.hash.pop(val)


        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    # Init an empty set.
    randomSet = RandomizedSet()

    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.remove(0)

    # Returns false as 2 does not exist in the set.
    randomSet.remove(0)

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(0)

    # getRandom should return either 1 or 2 randomly.
    randomSet.getRandom()

    # Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(0)
    # print(randomSet.arr)
    # print(randomSet.hash)

    # 2 was already in the set, so return false.
    print(randomSet.insert(0))
    