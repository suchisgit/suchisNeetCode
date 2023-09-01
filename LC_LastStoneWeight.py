import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while(len(stones)!=1 and len(stones)!=0):
            #print(stones)
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if(first!=second):
                heapq.heappush(stones,(first-second))
            #print(len(stones))
        if(len(stones)==0):
            return 0
        return -stones[0]
