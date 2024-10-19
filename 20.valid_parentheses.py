class Solution:
    def isValid(self, s: str) -> bool:
        brackets={
            "}":"{",
            ']':'[',
            ')':'('
        }
        stack=[]
        
        for bracket in s:
#             if not stack:
#                 stack.append(bracket)
#             else:
                
#                 if brackets.get(bracket)==stack[-1]:
#                     stack.pop()
#                 else:
#                     stack.append(bracket)

            if stack and stack[-1]==brackets.get(bracket):
                stack.pop()
            else:
                stack.append(bracket)
                
        if not stack:
            return True
        else:
            return False