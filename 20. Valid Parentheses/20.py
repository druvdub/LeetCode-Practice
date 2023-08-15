class Solution:

    '''
    Hash table + stack

    Time complexity: O(n)
    Space complexity: O(n)

    '''

    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = list()
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if len(stack) == 0 or brackets[char] != stack.pop():
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([)]"))  # False
    print(s.isValid("{[]}"))  # True
    print(s.isValid("]"))  # False
    print(s.isValid("(("))  # False
