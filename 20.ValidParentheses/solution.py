class Solution(object):
    def isValid(self, s):
        close_case = ["]", "}", ")"]
        open_case = ["[", "{", "("]

        stack = []
        for char in s:
            if(char in open_case):
                stack.append(char)
            elif(char in close_case):
                if(not stack):
                    return False
                else:
                    a = stack.pop()
                    if(char == "]" and a != "["):
                        return False
                    elif(char == "}" and a != "{"):
                        return False
                    elif(char == ")" and a != "("):
                        return False
        if(stack):
            return False
        return True


a = Solution()
print(a.isValid("[]{[]}"))
