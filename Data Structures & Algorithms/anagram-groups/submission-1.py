class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        answer = []

        for test in strs:

            testvalues = [0] * 26

            for character in test:
                testvalues[ord(character) - ord("a")] = testvalues[ord(character) - ord("a")] + 1
                
            testvalues = tuple(testvalues)

            if testvalues in anagrams:
                anagrams[testvalues].append(test)
            else:
                anagrams[testvalues] = [test]
        
        for key, value in anagrams.items():
            answer.append(value)

        return answer


