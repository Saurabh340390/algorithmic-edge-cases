class TwoSum:

    def __init__(self):
        self.freq = {}
    def add(self, number: int) -> None:
        if number in self.freq:
            self.freq[number] += 1
        else:
            self.freq[number] = 1

    def find(self, value: int) -> bool:
        for num in self.freq:
            complement = value - num
            if complement == num:
                if self.freq[num] > 1:
                    return True
            elif complement in self.freq:
                return True
        return False 
