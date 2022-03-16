from TrieNode import TrieNode

class Trie:
    root = TrieNode(-1, False)
    
    def insert(self, key):
        if not key:
            return

        current = self.root
        index = ord(key) - ord('a')
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

    def delete_helper(self, key, limit, index, current_node):
        if index == limit - 1:
            if not current_node.children:
                current_node = None
                return True
            else:
                if current_node.isEndNode:
                    current_node.isEndNode = False
                    return True
        else:
            if key[index] == current_node.value:
                found = False
                for child in current_node.children:
                    if child == key[index+1]:
                        found = self.delete_helper(key, limit, index+1, current_node)
            self.delete_helper(key, limit, index+1, current_node)

    def delete(self, key):
        if not key:
            return False
        else:
            self.delete_helper(key, len(key), 0, self.root)

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
