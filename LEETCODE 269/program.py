from collections import Counter
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjLst = defaultdict(set)
        indegree = Counter({c:0 for word in words for c in word})
        for i in range(len(words)-1):
            if len(words[i]) > len(words[i+1]) and words[i].startswith(words[i+1]):
                return ""
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in adjLst[words[i][j]]:
                        adjLst[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] += 1
                    break
        order = ""
        queue = []
        for letter in indegree :
            if indegree[letter]== 0:
                queue.append(letter)
        for letter in queue:
            order += letter
            for neighbor in adjLst[letter] :
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) == len(indegree):
            return order
        else :
            return ""
