class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):

    # l1, l2 중 하나가 None 인 경우 진행이 안되므로 미리 탈출
    if l1 == None and l2 == None:
        return None
    elif l1 == None or l2 == None:
        return l1 == None and l2 or l1

    iter1 = l1
    iter2 = l2
    answerHead = None
    answerTail = answerHead

    while iter1 and iter2:

        # 작은 것을 골라 temp = listNode() 를 만든다
        if iter1.val <= iter2.val:
            temp = ListNode(iter1.val)
            iter1 = iter1.next
        elif iter1.val > iter2.val:
            temp = ListNode(iter2.val)
            iter2 = iter2.next

        # temp 를 answerHead 의 마지막에 놓는다
        if not answerHead:
            answerHead = temp
            answerTail = answerHead 
        else:
            answerTail.next = temp
            answerTail = answerTail.next

    # l1, l2 의 길이가 다를 경우 남을 수 있으므로, 남아있는 것이 없을 때까지 붙여 넣는다
    if not iter1 and iter2:
        while iter2:
            answerTail.next = ListNode(iter2.val)
            answerTail = answerTail.next
            iter2 = iter2.next
    elif iter1 and not iter2:
        while iter1:
            answerTail.next = ListNode(iter1.val)
            answerTail = answerTail.next
            iter1 = iter1.next

    return answerHead


l1 = ListNode(1)
prev = l1
for i in []:
    temp = ListNode(i)
    prev.next = temp
    prev = temp

l2 = ListNode(1)
prev = l2
for i in [2]:
    temp = ListNode(i)
    prev.next = temp
    prev = temp

mergeTwoLists(l1,l2)