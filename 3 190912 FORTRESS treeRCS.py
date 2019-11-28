# RTE

class Node:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.parent = None
        self.children = []
        self.maxClimb = 0 # 해당 노드 기준으로, 요새를 넘어야 하는 최대 횟수
        self.maxDepth = 0 # 해당 노드 기준으로, 최대 깊이

class Tree:

    def __init__(self, node):
        self.root = node

    def insert(self, subTreeRoot, node):  # 내림차순으로 준다는 가정하에

        self.recursion = 0

        # case 1) subTreeRoot 에 자식이 있음
        if subTreeRoot.children:
            for child in subTreeRoot.children:
                d = ((child.x - node.x)** 2 + (child.y - node.y)** 2)**(1 / 2)
                
                # 조상을 찾음 - 조금 더 밑으로 거슬러 가기 위해 다시 부름
                if child.r - node.r >= d:
                    self.recursion = 1
                    self.insert(child, node)
                    return
            
            # case 2) subTreeRoot 에 자식이 있으나 sibling으로 들어가야 할 경우
            node.parent = subTreeRoot
            subTreeRoot.children.append(node)
            
        # case 3) subTreeRoot 에 자식이 없는 경우
        else:
            node.parent = subTreeRoot
            subTreeRoot.children.append(node)

    def find_max_climb(self, root):
        if root.children:
            temp = []
            for child in root.children:
                temp.append(self.find_max_climb(child))
            temp.append(root.maxClimb)
            return max(temp)
        else:
            return root.maxClimb

    # 최대 벽을 넘는 횟수 maxClimb는 maxDepth로 구해짐
    def calc_max_climb_depth(self, root):
        if root.children:
            temp = [self.calc_max_climb_depth(child) + 1 for child in root.children] 
            temp.sort(reverse=True)
            root.maxDepth = temp[0]

            # 자식이 1개인 경우, 2개 이상인 경우
            try:
                root.maxClimb = temp[0] + temp[1]
            except:
                root.maxClimb = temp[0]

            # root인 경우 아무것도 return하지 않는다
            if root == self.root:
                return
            else:
                return root.maxDepth 
  
        else:
            root.maxClimb = 0
            root.maxDepth = 0
            return root.maxDepth

numTests = int(input())
for test in range(numTests):

    # node 인풋 받기
    numForts = int(input())
    forts = []
    for fortsress in range(numForts):
        forts.append(list(map(int, input().split())))

    # tree 만들기
    forts.sort(key=lambda x: x[2], reverse=True)
    for i, fort in enumerate(forts):
        node = Node(*fort) # fort 의 정보로 node를 만듦 
        if i == 0:         # 최초의 경우는 tree를 만든다
            tree = Tree(node)
        else:
            tree.insert(tree.root, node)

    # max path 찾기
    tree.calc_max_climb_depth(tree.root)
    print(tree.find_max_climb(tree.root))