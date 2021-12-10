
# WHAT IS A TRIE?
# A trie is a tree-based data structure that organizes information in a hierarchy

# Properties:
# - It is a typically used to store or search strings in a space and time efficient way.
# - Any node in trie can store NON REPETATIVE multiple characters
# - Every node stores link of the next character of the string
# - Every node keeps track of 'end of string'

# Trie example:
#              |AB|  
#            /    \
#         |I|    |AIM|
#        /     /   |  \
#     |RT|   |R|  |L|  |.|
#    /      /       \
#  |.|    |.|       |.|


#HOW TO STORE 'AIR' and 'AIT" IN TRIE
#              |A|  First letter is A
#            /   
#         |I|  Second is I
#        /   
#     |RT|  Third can be either R or T
#    /   \
#  |.|   |.|  <= Blank node that show this is the end of stirng


# WHY WE NEED TRIE?
# To solve many standerd problems in efficient way
# - spelling checker (apps like Word tell if you misspell word)
# - Auto completion (Google Search, some mobile apps)


# COMMON OPERATIONS ON TRIE
# Creation of Trie
# Insertion of node to Trie
# Searching word in Trie
# Delete string from Trie



class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a string in a Trie
    # - Case 1: A trie is Blank 
    # - Case 2: New string's prefix is common to another strings prefix
    # - Case 3: New string's prefix is already present as complete string
    def insertString(self, word):
        current = self.root
        for letter in word:
            # Check if letter is in node childrens
            node = current.child.get(letter)
            # if not create it
            if not node:
                node = TrieNode()
                current.child.update({letter:node})
            # set current to node which store letter value
            current = node
        current.endString = True
        print(f'{word} successfully inserted')
        
    # SEARCHING FOR A STRING IN TRIE
    # Case 1: String does not exist in Trie
    # Case 2: String exists in Trie
    # Case 3: String is a prefix of another string, but it does not exists in a Trie (it does not have end of word)
    def search(self, word):
        currentNode = self.root
        for letter in word:
            node = currentNode.child.get(letter)
            # if node does not exist return false
            if not node: return False
            currentNode = node # update current node
            
        # Check if word is not a prefix 
        if currentNode.endOfString == True:
            return True
        else:
            return False
        
        
# DELETE A STRING FROM TRIE
# Deleting string from trie we start from the last letter of word and delete all that don't impact other words (to make sure that we delete only letters of our word not another that have similar prefix)
# Case 1: Some other prefix of string is same as tha one that wew want to delete. (delete => API, APPLE)
# Case 2: The string is a prefix of another string (delete => API, APIS)
# Case 3: Other string is a prefix of this string (delete => APIS, API) 
# Case 4:  Not any node depends on this String
def delete(root, word, index): # index defind index of characters in the word
    character = word[index]
    currentNode = root.child.get(character)   
    canThisNodeBeDeleted = False
    
    # Case 1
    if len(currentNode.child) > 1:    
        delete(currentNode, word, index+1)
        return False
    # Case 2
    if index == len(word) - 1: # this means we are at the last node
        if len(currentNode.child) >= 1: 
            currentNode.endOfString = False
            return False
        else: 
            root.child.pop(character) #remove character
            return True
    # Case 3
    if currentNode.endOfString == True: 
        delete(currentNode, word, index+1)
        return False
    
    canThisNodeBeDeleted = delete(currentNode, word, index+1)
    # Case 4
    if canThisNodeBeDeleted == True: 
        root.child.pop(character) #remove character
        return True
    else: 
        return False

















# Create new Trie
newTrie = Trie()
newTrie.insertString('App')
print('----------------Search_Trie_for_App------------------------')
print(newTrie.search('App'))
print('----------------Search_Trie_for_Api------------------------')
print(newTrie.search('Api'))
print('----------------Search_Trie_for_Ap-prefix------------------------')
print(newTrie.search('Ap'))
print('----------------Delete_App------------------------')
newTrie.insertString('Api')
delete(newTrie.root, 'App', 0)
print(f"Does App exist in Trie? => {newTrie.search('App')}")






