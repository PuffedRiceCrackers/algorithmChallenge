


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        temp = self
        while temp != None:
            print(temp.val, " >", end="")
            temp = temp.next
        print('')


def addTwoNumbers(l1, l2):
    i1 = l1
    i2 = l2
    answerHead = None
    answerTail = None
    carry = False
    while (i1 != None or i2 != None) or (carry == True):
        if i1 == None and i2 == None:
            answerTail.next = ListNode(1)
        temp = carry == True and 1 or 0
        for iterator in [i1, i2]:
            if iterator:
                temp += iterator.val
        carry = False if temp < 10 else True
        temp = temp if temp < 10 else temp - 10
        if answerHead != None:
            answerTail.next = ListNode(temp)
            answerTail = answerTail.next
        else:
            answerHead = ListNode(temp)
            answerTail = answerHead
        try:
            i1 = i1.next
        except:
            pass
        try:
            i2 = i2.next
        except:
            pass
    return answerHead

l1 = ListNode(2)
prev = l1
for i in [4,3]:
    temp = ListNode(i)
    prev.next = temp
    prev = temp

l2 = ListNode(5)
prev = l2
for i in [6,4]:
    temp = ListNode(i)
    prev.next = temp
    prev = temp




l1.show()
l2.show()
k = addTwoNumbers(l1, l2)
k.show()       

# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8
# # Explanation: 342 + 465 = 807.