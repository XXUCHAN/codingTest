class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.end = False
        self.children ={}
class Trie:
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            if current_node.end:
                return False
        if current_node.children:
            return False
        current_node.end = True
        return True

def solution(phone_book):
    answer = True
    trie = Trie()
    for nums in phone_book:
        answer = trie.insert(nums)
        if answer == False:
            return answer
    return answer