# 🐛 Mistake 1 : Indegree inflated by duplicate edges

What happened: You used a set for adjLst (good — prevents duplicate edges), but you incremented indegree unconditionally. If the same edge t → f was discovered from two different word pairs, the edge was only stored once, but indegree['f'] was incremented twice. This meant f could never reach indegree 0 during BFS.

**Lesson**: When using a set for adjacency, always check if the edge is new before updating indegree:

```
if words[i+1][j] not in adjLst[words[i][j]]:
    adjLst[words[i][j]].add(words[i+1][j])
    indegree[words[i+1][j]] += 1
```

# 🐛 Mistake 2 : Missing prefix edge case

What happened: If a word is followed by its own prefix (e.g., "abcd" then "ab"), no valid ordering exists — you must return "". Your original code had no check for this.

**Lesson**: Always add this guard when comparing adjacent words:
```
if len(words[i]) > len(words[i+1]) and words[i].startswith(words[i+1]):
    return ""
```
