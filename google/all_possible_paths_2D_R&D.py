class Solution:

    def get_paths_recur(self, curr_pos: tuple, endx_pos: int, endy_pos: int) -> int:

        paths = 0
        if curr_pos == (endx_pos, endy_pos):
            return 1

        if curr_pos[0] + 1 <= endx_pos:
            paths += self.get_paths_recur((curr_pos[0] + 1, curr_pos[1]), endx_pos, endy_pos)

        if curr_pos[1] + 1 <= endy_pos:
            paths += self.get_paths_recur((curr_pos[0], curr_pos[1] + 1), endx_pos, endy_pos)

        return paths

    def uniquePaths(self, m: int, n: int) -> int:
        res = self.get_paths_recur(curr_pos=(0, 0), endx_pos=n - 1, endy_pos=m - 1)
        print(res)
        return res

def using_growth_table(x_len, y_len):
    growth_table = [[1] for i in range(x_len)]
    growth_table[0] = [1 for i in range(y_len)]

    # -1 bc of I've already sum up y_len
    for xpos in range(1, x_len):
        for ypos in range(1, y_len):
            growth_table[xpos].append( growth_table[xpos-1][ypos] + growth_table[xpos][ypos-1])

    return growth_table[x_len-1][y_len-1]

def using_growth_table(x_len, y_len):
    growth_table = [1 for i in range(y_len)]

    ypos = 0
    while ypos < (x_len-1)*y_len:
        index = ypos % y_len
        ypos += 1

        if index == 0:
            continue
        growth_table[index] += growth_table[index-1]
    return growth_table[-1]


print(using_growth_table(5, 4))
print(using_growth_table(5, 5))
print(using_growth_table(6, 5))
print(using_growth_table(4, 4))


# Solution().uniquePaths(1,1)
# Solution().uniquePaths(2,2)
# Solution().uniquePaths(3,3)
# Solution().uniquePaths(4,4)
# Solution().uniquePaths(5,5)
# Solution().uniquePaths(6,6)


# print("---")
# Solution().uniquePaths(3,3)
# Solution().uniquePaths(3,4)
# Solution().uniquePaths(3,5)
# Solution().uniquePaths(3,6)
# print("---")
# Solution().uniquePaths(5,2)
# Solution().uniquePaths(5,3)
Solution().uniquePaths(5,4)
Solution().uniquePaths(5,5)
Solution().uniquePaths(5,6)
Solution().uniquePaths(4,4)

# Solution().uniquePaths(5,4)
# Solution().uniquePaths(6,4)
# Solution().uniquePaths(6,2)


