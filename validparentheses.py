class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        char_dict = {"(":")", "[": "]", "{":"}"}
        stack = []
        for i in s:
            if i in char_dict:
                stack.append(i)
            elif len(stack) == 0 or char_dict[stack.pop()] != i:
                return False
        return len(stack) == 0
