from typing import Any, Optional

"""
    I got this one in the first interview with goole that I failed.

    Description (made-up 1 year later): 
    {x} / x is an integer: multiplies the last char or set if in a parenthesis
    (yy): groups chars
"""
class Solution:
    def __call__(self, compressed_str: str) -> str:
        r = self._process(compressed_str=compressed_str)[0]
        groups = []
        return r

    def _process(self, compressed_str: str, pos: int = 0) -> tuple[str, int]:
        groups: list[list[int|str]] = []
        mul: int|str = ""
        is_mul: bool = False
        ic: int
        pointer: int
        pointer = ic = pos

        for ic, c in enumerate(compressed_str):
            if ic < pointer:
                continue

            match c:
                case "(":
                    # change scope, recursion
                    par_res, pointer = self._process(compressed_str=compressed_str, pos=ic+1)
                    groups.append([par_res, 1])
                    continue
                case ")":
                    ic += 1
                    if pos == 0:
                        raise Exception("Impossible event: Should be ignored, passed on the top of the loop.")
                    break

                case "{":
                    is_mul = True
                    # collect multiplier
                    continue
                case "}":
                    mul = int(mul)
                    groups[-1][1] = mul

                    # reset
                    is_mul = False
                    mul = ""
                    # close and apply multiplier
                    continue
                case _:
                    if is_mul:
                        mul += c
                        continue

                    # Base case
                    groups.append([c, 1])
                    continue
        
        return (self._build(groups=groups), ic)
    
    def _build(self, groups) -> str:
        res: str = ""
        for g in groups:
            res += g[0]*g[1]
        
        print(f"\n\n {res} \n\n")
        return res

if "__main__" == __name__:
    s = Solution()
    assert s("(a){3}") == "aaa"
    assert s("(ab){3}") == "ababab"
    assert s("(as(df))(ab){3}") == "asdfababab"
    assert s("x((ab){2}){2}") == "xabababab"
    assert s("x((ab){2}){2}q") == "xababababq"
