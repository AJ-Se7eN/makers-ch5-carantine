# Hackerrank
"""https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=trees
"""

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           
def lca(root, v1, v2):
    node=root
    if node is None:
        return None
    if node.info>v1 and node.info>v2:
        return lca(node.left,v1,v2)
    elif node.info<v1 and node.info < v2:
        return lca(node.right,v1,v2)
    else:
        return node