from typing import List


class TreeNode(object):
    def __init__(self):
        self.nodes = {}  # 记录当前结点的子结点
        self.is_leaf = False  # 当前结点是否表示一个单词
        self.count = 0  # 单词树中单词的总量
        self.common_str = ''

    def insert(self, word):
        curr = self
        if word.strip() == '':
            curr.nodes[''] = TreeNode()
            curr = curr.nodes['']
        else:
            for c in word:
                if not curr.nodes.get(c, None):  # 如果不在字典树中
                    new_node = TreeNode()
                    curr.nodes[c] = new_node
                curr = curr.nodes[c]

        curr.is_leaf = True
        self.count += 1

    def insert_many(self, words):
        for word in words:
            self.insert(word)

    def search(self, word):
        curr = self
        try:
            for c in word:
                curr = curr.nodes[c]
        except:
            return False
        return curr.is_leaf


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return None

        tree = TreeNode()
        tree.insert_many(strs)

        node = tree
        res = ''
        while node:
            keyList = list(node.nodes.keys())
            if len(keyList) == 0:
                break

            if len(keyList) == 1:
                key = keyList[0]
                node = node.nodes.get(key)
                res += key
                if node.is_leaf == True:
                    break
            else:
                break
        return res


tree = TreeNode()
tree.insert_many(['apple', "app", "''"])
print(tree.count)
node = tree
res = ''
while node:
    keyList = list(node.nodes.keys())
    if len(keyList) == 0:
        break

    if len(keyList) == 1:
        key = keyList[0]
        node = node.nodes.get(key)
        res += key
        if node.is_leaf == True:
            break
    else:
        break

print(res)
