def divide_and_reorder(preOrder, inOrder):

    # Base Case
    if len(preOrder) <= 2:
        return list(reversed(preOrder))

    # Recursive call
    else:
        postOrder = []
        rootIdx = inOrder.index(preOrder[0])

        # left tree
        leftPreOrder = preOrder[1:rootIdx + 1]
        leftInOrder = inOrder[0:rootIdx]

        # right tree
        rightPreOrder = preOrder[rootIdx + 1:]
        rightInOrder = inOrder[rootIdx + 1:]

        postOrder.extend(divide_and_reorder(leftPreOrder, leftInOrder))
        postOrder.extend(divide_and_reorder(rightPreOrder, rightInOrder))
        postOrder.append(preOrder[0])
        return postOrder

tests = int(input())
for test in range(tests):
    numNode = int(input())
    preOrder = input().split()
    inOrder = input().split()
    postOrder = divide_and_reorder(preOrder, inOrder)
    print(' '.join(postOrder))


