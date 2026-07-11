# 🐛 Bug 1: Time Limit Exceeded
Cause : Used a nested loop iterating over the entire array twice, resulting in O(N²) time complexity per find call.
Lesson : Replaced the list + nested loop with a HashTable (dict) storing number frequencies
## Before (TLE):
```
self.array = []  # list

def find(self, value):
    for idx1, val1 in enumerate(self.array):
        for idx2, val2 in enumerate(self.array):  # O(N²)
            if idx1 != idx2 and val1 + val2 == value:
                return True
```

## After (Accepted):
```
self.array = {}  # dict (frequency map)

def find(self, value):
    for num in self.array:
        complement = value - num
        if complement == num:
            if self.array[num] > 1:   # handles duplicate case
                return True
        elif complement in self.array:
            return True
```
