class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        answer = []

        for check in strs:
            freq = [0] * 26

            for character in check:
                index = ord(character) - ord('a')
                freq[index] = 1 + freq[index]
            
            freq = tuple(freq)
            
            if freq in anagrams:
                anagrams[freq].append(check)
            else:
                anagrams[freq] = [check]
            
            
        for key, value in anagrams.items():
            answer.append(value)
        return answer





        # stored = {}
        # answer = {}

        # for check in strs:
        #     characters = []

        #     for character in check:
        #         characters.append(character)
            
        #     characters.sort()

        #     for key, value in stored.items():
        #         if value == characters:
        #             if check in answer or value in answer:
        #                 answer[check] = 
        #             answer[check] = key
            
        #     if 
            
        #     stored[check] = characters

        #     # if anagram in stored:
        #     #     answer.append([anagram, value])

        #     # stored.add(value)
        #     # print(anagram)

        # return answer