## 🐛Bug 1: Only checking if abbreviation exists, ignoring the "same word" rule
My logic: If the abbreviation exists in the list → False, otherwise → True.

Problem: The problem says isUnique should return True if the abbreviation exists but all matching dictionary words are the same as the queried word 
E.g., isUnique("cake") should return True since "cake" is the only word with abbreviation "c2e".

**Fix:** Store the actual words per abbreviation, not just the abbreviation itself.


## 🐛Bug 2: Bug 2: word in self.dict check was insufficient
My logic: If the abbreviation exists and the word is in the dictionary → True.

Problem: This doesn't check whether other words share the same abbreviation.
E.g., isUnique("door") returned True because "door" is in the dictionary, but "deer" also has abbreviation "d2r" and is a different word → should be False.

**Fix:** Check that every word in the set for that abbreviation equals the queried word.


## 🐛Bug 3: Concatenating words into a string instead of using a set
My logic: self.dict[abv] += word — concatenated words into one long string (e.g., "deerdoor").

Problem: for string in self.dict[abv] iterated over individual characters ('d', 'e', 'e', 'r', ...), not words.
Comparing "cake" != 'c' always returned False.

**Fix:**  Use a set() as the dictionary value to store individual words.


## 🐛Bug 4: KeyError when accessing a non-existent key
My logic: self.dict[abv].add(word) without checking if the key exists.

Problem: The first time an abbreviation is encountered, the key doesn't exist in the dictionary, causing a KeyError.

**Fix:** Initialize the set before adding: use defaultdict(set).
