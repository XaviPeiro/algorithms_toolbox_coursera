from typing import Optional


class Solution:
    def __call__(self, compressed_str: str):
        # operations = {
        #     "{": "}"
        # }
        op_stack: list = []
        vals = []
        res = ""
        r_s = reversed(compressed_str)
        for i in r_s:
            m_val = ""
            if i == "}":
                # apply mul
                while (n_c := next(r_s)) != "{":
                    # if > 1 digit not working, but details
                    multiplier = n_c
                else:
                    assert next(r_s) == "("
                    # while (n_c := next(r_s)) !=
            elif i == ")":
                # apply agg
                ...

    def __call__(self, compressed_str: str):
        mul_val: Optional[int] = None
        ops_stack = [""]

        it_c_s = iter(compressed_str)
        for c in it_c_s:
            if c == "{":
                mult_val = int(next(it_c_s))
                continue
            elif c == "}":
                ops_stack[-1] *= mult_val
                mul_val = None
                tmp = ops_stack.pop()
                ops_stack[-1] = ops_stack[-1] + tmp
            elif c == "(":
                ops_stack.append("")
            elif c == ")":
                ...
            else:
                ops_stack[-1] += c

        print("".join(ops_stack))
        return "".join(ops_stack)

if "__main__" == __name__:
    s = Solution()
    assert s("(a){3}") == "aaa"
    assert s("(ab){3}") == "ababab"
    assert s("(as(df))(ab){3}") == "asdfababab"
    assert s("x((ab){2}){2}") == "xabababab"
    assert s("x((ab){2}){2}q") == "xababababq"
