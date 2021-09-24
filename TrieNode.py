'''
	This class is going to define the structure of a node in a Trie.
				
			       root
				|
				t
				|
				h
				|
				e
				| \
				r  i
				|  |
				e  r

	When creating the node we would like to instantiate using a syntax 
	like this TrieNode('a'). Terminating nodes should have a isEndNode
	flag which can be set to True if the node exists.

'''

class TrieNode:
    value = None
    children = None
    isEndNode = False
    
    def __init__(self, value, isEndNode):
        self.value = value
        self.isEndNode = isEndNode
