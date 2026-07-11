class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dict = defaultdict(set)
        for word in dictionary :
            if len(word) <=2 :
                self.dict[word].add(word)
            else:
                abv = word[0] + str((len(word)-2)) + word[-1]
                self.dict[abv].add(word)

    def isUnique(self, word: str) -> bool:
        abv = ""
        if len(word) <=2 :
            abv = word
        else:
            abv = word[0] + str((len(word)-2)) + word[-1]

        if abv in self.dict :
            for string in self.dict[abv]:
                if word!= string:
                    return False
            return True
        return True
