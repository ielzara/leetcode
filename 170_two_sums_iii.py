class TwoSum:
    def __init__(self):
        self.values = []

    def add(self, number: int) -> None:
        return self.values.append(number)

    def find(self, value: int) -> bool:
        hashTable = {}

        for i, key in enumerate(self.values):
            complement = value - key
            if complement in hashTable:
                return True
            hashTable[key] = i


two_sums = TwoSum()

# Add numbers to the instance
two_sums.add(1)
two_sums.add(3)
two_sums.add(5)
two_sums.add(7)

# Test cases
# Case 1: Looking for two numbers that add up to 4 (should return True, because 1 + 3 = 4)
print(two_sums.find(4))  # Expected: True

# Case 2: Looking for two numbers that add up to 10 (should return True, because 3 + 7 = 10)
print(two_sums.find(10))  # Expected: True

# Case 3: Looking for two numbers that add up to 8 (should return False, no two numbers add up to 8)
print(two_sums.find(8))  # Expected: False

# Case 4: Looking for two numbers that add up to 14 (should return True, because 7 + 7 = 14)
print(two_sums.find(14))  # Expected: True
