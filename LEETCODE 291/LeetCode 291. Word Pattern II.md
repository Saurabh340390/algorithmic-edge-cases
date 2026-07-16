## 🐛 Bug 1  Missing return in recursive call
Before: ``` isMatch(sIndex+1, pIndex+len(word)) ```

Issue: The recursive call result was discarded; execution fell through to the for loop.
### Fix: 
Add return and use if isMatch(...): return True

## 🐛 Bug 2 — Wrong sIndex advancement
Before: ```sIndex+1```

Issue: Advanced sIndex by 1 instead of the matched word's length.
### Fix: 
```sIndex+len(word)```

## 🐛 Bug 3 — Infinite recursion 
Before: ```isMatch(sIndex, pIndex)```

Issue: Called with the same indices, causing infinite recursion → IndexError.
### Fix: ```isMatch(sIndex+len(newWord), pIndex+1)```

## 🐛 Bug 4 — Logic fall-through on already-mapped symbol

Before: When a symbol was already mapped and the substring matched but recursion failed, the code fell through to the for loop, 
which could overwrite the existing mapping and return a wrong True.
Example: pattern="aba", s="xyxy" → incorrectly returns True instead of False
### Fix :
```
if symbol in symbolMap:
    word = symbolMap[symbol]
    if s[sIndex:(sIndex+len(word))] == word:
        return isMatch(sIndex+len(word), pIndex+1)
    return False
```
