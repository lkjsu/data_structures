from TrieNode import TrieNode

class Trie:
    root = TrieNode(-1, False)
    
    def insert(self, key):
        if not key:
            return

        current = self.root
        for letter in key:
            if current.children:
                for child in current.children:
                    if letter == child.value:
                        current = child
            else:
                newTrieNode = TrieNode(letter, False)
                current.children = [newTrieNode]
                current = newTrieNode
        current.isEndNode = True

    def search(self, key):
        if not key:
            return False

        current = self.root
        for letter in key:
            found = False
            for child in current.children:
                if letter == child.value:
                    current = child
                    found = True
            if not found:
                return False
        if current == self.root:
            return False
        if not current.isEndNode:
            return False
        return True

'''
    Sample Test cases to test against.
'''

trie = Trie()
trie.insert('the')
trie.insert('their')
trie.insert('there')
print(trie.search('te'))
print(trie.search('there'))
print(trie.search('the'))
print(trie.search('ther'))
print(trie.search('thei'))
print(trie.search('th'))
