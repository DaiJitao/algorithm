""" 二叉树遍历非递归方法实现 """


class Node(object):
    def __init__(self, right=None, left=None, data=None):
        self.right = right
        self.data = data
        self.left = left


class BinaryTree(object):
    def __init__(self):
        pass


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):  # 压栈,一个一个往栈(列表)中推
        self.items.append(value)

    def pop(self):  # 弹栈,由于栈结构是先进后出,后进先出的原理,所弹出是倒序,有点类似list[::-1]方法
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0


"""前序遍历 非递归实现"""
def pre_print(root: Node):
    stack = Stack()
    stack.push(root)
    print(len(stack.items))
    while not stack.isEmpty():
        cur = stack.pop()
        # print(cur.data)
        if cur.right != None:
            stack.push(root.right)
        if cur.left != None:
            stack.push(root.left)
        print(len(stack.items))

##############################################################
# 求解二叉树中任意两个节点的最近公共祖先
##############################################################




#############################################################
if __name__ == "__main__":
    root = Node(data=1)
    n2 = Node(data=2)
    n3 = Node(data=3)
    n4 = Node(data=4)
    n5 = Node(data=5)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    pre_print(root)
