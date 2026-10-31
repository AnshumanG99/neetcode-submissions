class Solution:
    def isValid(self, s: str) -> bool:
        
        seenstack = []
        valuemap = {"(" : ")", "{" : "}", "[" : "]"}

        for value in s:
            if value in valuemap:
                seenstack.insert(0, value)

            else:
                if seenstack and valuemap[seenstack[0]] == value:
                    seenstack.pop(0)

                else:
                    return False

        return len(seenstack) == 0 