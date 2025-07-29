class Solution:
    def isValid(self, s: str) -> bool:
        # O() = n
        stack = [None]
        open_set = ('{','(', '[') # C
        close_set = ('}',')', ']') # C
        chars_map = dict(zip(close_set, open_set)) # 2*2C
        for char in s: # S
            if char in open_set: # C -> Could be improved be using the hashmap
                stack.append(char) # C -> 1
            elif char in close_set:
                lc = stack.pop()
                print(lc)
                if lc != chars_map[char]:
                    return False

        return len(stack) == 1 and stack.pop() is None
