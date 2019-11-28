# 런타임 오류

class Node:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.parent = None
        self.left = None
        self.right = None

class Tree:

    def __init__(self, node):
        self.root = node
        self.log = None
    
    # Binary Search
    def search(self, root, target):
        if root:
            if target.p < root.p:   # left subtree에 있다
                self.search(root.left, target)
            elif target.p > root.p: # right subtree에 있다
                self.search(root.right, target)
            else:  # root 와 일치한다
                return root
        else:                       # 이전 root가 leaf여서, 현재 root=None인 경우
            return None
    
    def rightMostOf(self, root):
        if root.right == None:
            return root
        else:
            self.rightMostOf(root.right)
            
    def delete(self, target):
        
        # 지울 노드
        node = self.search(self.root, target)

        if node == self.root:
            isRoot = True
        else:
            isRoot = False

        #자식이 2개 - left 서브트리의 rightMost 노드로, root를 대체시킴
        if node.left and node.right:  
            rightMostNode = self.rightMostOf(node.left)
            node.p = rightMostNode.p
            node.q = rightMostNode.q
            self.delete(rightMostNode)
            return node

        #자식이 1개 - 부모와 연결
        elif node.left or node.right:
            child = node.left and node.left or node.right
            if isRoot == False:
                # parent - child 관계정립
                if node.p < node.parent.p: 
                    node.parent.left = child
                    child.parent = node.parent
                elif node.p > node.parent.p:
                    node.parent.right = child
                    child.parent = node.parent 
            else:
                child.parent = None
                self.root = child
            return child

        #자식이 0개 - 바로 지움
        else:
            if isRoot == False:
                if node.p < node.parent.p:
                    node.parent.left = None
                elif node.p > node.parent.p:
                    node.parent.right = None
            else:
                self.root = None
            return None

    # 쉽게 insert할 수 있는 경우만 넘겨줌
    def insert(self, root, node):
        if root == None:  # 아무것도 없는데 넣는 경우
            self.root = node
        else:
            if node.p < root.p:
                root.left = node
                node.parent = root
            elif node.p > root.p:
                root.right = node
                node.parent = root

    def apply(self, root, node, deleted):
        parent = root.parent

        # root 에게 진 경우 - 못들어 가고 종료
        if node.p < root.p and node.q < root.q:

            self.log.append(self.log[-1]) # 최초로 진 것일 것이므로 delete를 생각할 필요가 없음
            return

        # root 와 양립가능한 경우
        # (1) L tree 에 속함
        elif node.p < root.p and node.q > root.q: 
            
            # L subtree가 있을 경우 RCS, 없을 경우 insert/종료
            if root.left:
                self.apply(root.left, node, deleted)
            else:                                            
                self.insert(root, node)
                self.log.append(self.log[-1] + 1 - deleted)
                return

        # (2) R tree 에 속함    
        elif node.p > root.p and node.q < root.q:  
            
            # R subtree가 있을 경우 RCS, 없을 경우 insert/종료
            if root.right:
                self.apply(root.right, node, deleted)
            else:                                            
                self.insert(root, node)
                self.log.append(self.log[-1] + 1 - deleted)
                return

        # root 를 이긴 경우 - 해당 root delete후, 새로 올라온 root 에 대해서 RCS        
        elif node.p > root.p and node.q > root.q:

            newRoot = self.delete(root)
            deleted += 1
            
            # 새로운 자식이 밑에서 올라옴 - 그 자식에 대해 다시 apply
            if newRoot:
                self.apply(newRoot, node, deleted)
            
            # 자식이 없었던 경우, parent 밑으로 들어가게 - 하나 지우고 다시 추가한 거라 log는 그대로임
            else:
                self.insert(parent, node)
                self.log.append(self.log[-1] - deleted)
            return

tests = int(input())
for test in range(tests):

    # 입력부
    participants = []
    applicants = int(input())
    for count in range(applicants):
        temp = list(map(int, input().split()))
        participants.append(temp)
 
    # 트리만들기
    for i, participant in enumerate(participants):
        node = Node(*participant)
        if i == 0:
            tree = Tree(node)
            tree.log = [1]
        else:
            tree.apply(tree.root, node, 0)

    print(sum(tree.log))