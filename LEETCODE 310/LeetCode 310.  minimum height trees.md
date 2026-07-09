# My mistake
## 🐛 Bug 1: One-directional adjacency list & degree
```
 ❌ My code
adjLst[v].append(u)
indegree[u] += 1

 ✅ Fix
adjLst[u].append(v)
adjLst[v].append(u)
degree[u] += 1
degree[v] += 1
```
## 🐛 Bug 2: list.pop(node) — index vs. value
```
 ❌ My code
nodesLst.pop(node)  # removes by INDEX, not value

 ✅ Fix: Use a counter instead
remaining = n
remaining -= leaf_count
```
## 🐛 Bug 3: BFS not processing layer by layer
```
❌ Your code
for node in queue:        # newly appended items mix in
    queue.append(...)

✅ Fix
leaf_count = len(queue)
for _ in range(leaf_count):
    node = queue.popleft()
```
## ⚠️ Redundant: Unnecessary n == 2 check
```
# ⚠️ Not needed
if n == 2:
    return [0, 1]
```
