"""
# Imagine we design a simple file system metadata.
# There are 2 types of entities: 'file' and 'directory'.
# Each entity is given an integer 'entity id' and has a 'name'.
# File entities also have a 'size' field of how much space they consume in bytes.
# Directory entities have a list of 'children', representing entity ids inside them.
#
# Overall, we have the following structures:
#
# EntityId: int
# Entity = {
#   type: ‘file’ | ‘directory’
#   name: string
#   oneof {
#     size: int
#     children: [EntityId]
#   }
# }
#
# Filesystem: dictionary<EnftityId, Entity>
#
# Example:
# root (id=1)
#     dir (id=2)
#         file1 (id=4): 100b

#         file2 (id=5): 200b
#     file3 (id=3): 300b
# file7 (id=8): 10b
"""
def traverse_iter(fs, fo_id: int):
    next_nodes = [fo_id]

    while next_nodes:
        node_id = next_nodes.pop()
        node = fs[node_id]

        yield node_id, node
        if node['type'] == 'file':
            #nothing to do
            ...
        elif node['type'] == 'directory':
            for child in node['children']:
                print(f"child: {child}")
                next_nodes.append(child)

def validate_fs(fs):
    """
        Properties: 
            - one root
            - no cycle
    """
    # no cycle => not passing twice for the same and completing the tree travesal
    # one root -> len(fs) == elements under fs[1]

    # Acutally I am also checking there is no more than one parent; due to, I am not allowing links (or hard links better said).
    visited = set()

    for el_id, el in traverse_iter(fs, 1):
        if el_id in visited:
            raise Exception(f"Wrong fs, thereis a cycle. {visited} - {el_id}")
        visited.add(el_id)

    if len(fs) != len(visited):
        raise Exception("There are dangling items")

    return True

def calc_size(fs: dict, fo_id: int) -> int:
    # always just one root entity that defines the top fs level
    size: int = 0
    for el_id, el in traverse_iter(fs, fo_id):
        if el["type"] == "file":
            size += el["size"]
    return size

fs = {
    1: {"type": "directory", "name": "root", "children": [2, 3, 8]},
    2: {"type": "directory", "name": "dir",  "children": [4, 5]},
    3: {"type": "file", "name": "file3", "size": 300},
    4: {"type": "file", "name": "file1", "size": 100},
    5: {"type": "file", "name": "file2", "size": 200},
    8: {"type": "file", "name": "file7", "size": 10},
}

assert validate_fs(fs) is True
assert calc_size(fs, 1) == 610
assert calc_size(fs, 2) == 300

# Imagine we design a simple file system metadata.
# There are 2 types of entities: 'file' and 'directory'.
# Each entity is given an integer 'entity id' and has a 'name'.
# File entities also have a 'size' field of how much space they consume in bytes.
# Directory entities have a list of 'children', representing entity ids inside them.
#
# Overall, we have the following structures:
#
# EntityId: int
# Entity = {
#   type: ‘file’ | ‘directory’
#   name: string
#   oneof {
#     size: int
#     children: [EntityId]
#   }
# }
#
# Filesystem: dictionary<EnftityId, Entity>
#
# Example:
# root (id=1)
#     dir (id=2)
#         file1 (id=4): 100b

#         file2 (id=5): 200b
#     file3 (id=3): 300b
# file7 (id=8): 10b
  

def validate_fs(fs):
  visited = set()
  
  def dfs(node_id: int):
    # access to object
    root = fs[node_id]
    
    if not node_id in visited:
      visited.add(node_id)
    else:
      return False
   
    if root["type"] == "directory":
      for child_id in root["children"]:
        # acc size of all the child dir 
        r = dfs(child_id)
        if r is False:
          return r
        
    return True

  return dfs(1) and len(visited) == len(fs)
  

cache = {}
def calc_size(fs: dict, fo_id: int) -> int:
  if fo_id in cache:
    return cache[fo_id]
  
  # access to object
  root = fs[fo_id]
  
  
  total_size: int = 0
  
  if root["type"] == "file":
    # base case: the element provided is a file
    return root["size"]
  elif root["type"] == "directory":
    
    for child_id in root["children"]:
      # acc size of all the child dir 
      total_size += calc_size(fs, child_id)
     
    
  cache[fo_id] = total_size
  return total_size
 

        
fs = {
    1: {"type": "directory", "name": "root", "children": [2, 3, 8]},
    2: {"type": "directory", "name": "dir",  "children": [4, 5]},
    3: {"type": "file", "name": "file3", "size": 300},
    4: {"type": "file", "name": "file1", "size": 100},
    5: {"type": "file", "name": "file2", "size": 200},
    8: {"type": "file", "name": "file7", "size": 10},
}

assert validate_fs(fs) is True
assert calc_size(fs, 1) == 610
assert calc_size(fs, 2) == 300 