class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqdict = {}
        sortfreq = []
        answer = []

        for value in nums:
            if value in freqdict:
                freqdict[value] += 1
            else:
                freqdict[value] = 1
            
        
        for key, items in freqdict.items():
            sortfreq.append([items, key])
        
        sortfreq.sort()
        sortfreq.reverse()
        
        for i in range(k):
            answer.append(sortfreq[i][1])
        
        return answer
