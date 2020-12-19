# class Heap():
#     def __init__(self, tree=[]):
#         self._tree = [None]
#         for value in tree:
#             self.push(value)

#     def push(self, value):
#         self._tree.append(value)
#         index = self.last_index
#         while index//2:
#             if self._tree[index] > self._tree[index//2]:
#                 break
#             self._tree[index], self._tree[index//2] = self._tree[index//2], self._tree[index]
#             index = index//2

#     def pop(self):
#         value = self._tree[1]
#         last_value = self._tree.pop()
#         if self.last_index:
#             self._tree[1] = last_value
#         index = 1
#         while index*2 <= self.last_index:
#             child_index = index*2 if index*2+1 > self.last_index or self._tree[index*2] < self._tree[index*2+1] else index*2+1
#             if self._tree[child_index] > self._tree[index]:
#                 break
#             self._tree[child_index], self._tree[index] = self._tree[index], self._tree[child_index]
#             index = child_index
#         return value

#     @property
#     def root(self):
#         return self._tree[1] if self.last_index else self._tree[0]

#     @property
#     def last_index(self):
#         return len(self._tree)-1

#     @property
#     def tree(self):
#         return self._tree


import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while len(scoville) >= 2:
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        count += 1        
        if scoville[0] >= K:
            break
    else:
        count = -1
    
    return count


print(solution([1, 2, 3, 9, 10, 12], 7)) #=> 2
print(solution([0, 0, 0, 0], 2)) #=> -1
