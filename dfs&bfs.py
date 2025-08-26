
tree = {
    'root': {
        'alpha': {
            'a1': {},
            'a2': {
                'a21': {},
                'a22': {}
            }
        },
        'beta': {
            'b1': {},
            'b2': {
                'b21': {
                    'b211': {}
                },
                'b22': {}
            }
        },
        'gamma': {
            'g1': {},
            'g2': {
                'g21': {},
                'g22': {
                    'g221': {},
                    'g222': {}
                }
            }
        }
    }
}

from collections import deque


def dfs(tree):
    for k in tree:
        print(k)
        if tree[k]:
            dfs(tree=tree[k])

def bfs(tree):
    d = deque()
    d.append(tree)
    
    while len(d) > 0:
        lvl = d.popleft()
        for el in lvl:
            print(el)
            d.append(lvl[el])
        # print(lvl)
        
def dfs2(tree):
    d = deque()
    d.append(tree)
    
    while len(d) > 0:
        lvl = d.pop()
        for el in lvl:
            print(el)
            d.append(lvl[el])
# dfs(tree)
dfs2(tree)
# bfs(tree)