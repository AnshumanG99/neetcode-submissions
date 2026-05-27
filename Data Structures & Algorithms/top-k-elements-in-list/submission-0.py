class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        sorted_freq = []
        answer = []

        for number in nums:
            if number in freq:
                freq[number] = 1 + freq[number]
            else:
                freq[number] = 1

        for key, value in freq.items(): 
            sorted_freq.append([value, key])
            
        sorted_freq.sort()
        sorted_freq.reverse()


        for i in range (k): 
            answer.append(sorted_freq[i][1])

        return answer