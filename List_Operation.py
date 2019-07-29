# encoding = utf8

class Node:
    val = None
    pNext = None

    def __init__(self, value):
        self.val = value

    def output(self):
        print(self.val)



class List:
    head = None
    tail = None

    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):

        node = Node(value)

        if None == self.head:
            self.head = node
            self.tail = node

        if None != self.tail:
            self.tail.pNext = node

        self.tail = node

    def reverse(self, start, end):

        if start > end:
            start, end = end, start

        dummy_node = Node(None)
        dummy_node.pNext = self.head
        prev_node = dummy_node

        for i in range(start - 1):
            prev_node = prev_node.pNext

        head_new = prev_node
        prev_node = prev_node.pNext
        cur_node = prev_node.pNext

        for i in range(end - start):
            prev_node.pNext = cur_node.pNext
            cur_node.pNext = head_new.pNext
            head_new.pNext = cur_node
            cur_node = prev_node.pNext

    def divide(self, value):

        left_dummy = Node(None)
        right_dummy = Node(None)

        if self.head == None:
            return

        leftCur = left_dummy
        rightCur = right_dummy
        pNode = self.head

        while pNode != None:

            if pNode.val < value:
                leftCur.pNext = pNode
                leftCur = pNode
            elif pNode.val >= value:
                rightCur.pNext = pNode
                rightCur = pNode
            
            pNode = pNode.pNext
        
        leftCur.pNext = right_dummy.pNext
        rightCur.pNext = None


    def addList(self, lst_other):

        if None == lst_other.head:
            return None

        lst_result = List()
        lst_result_cur = None
        tmp_Node = None

        lst_self_cur = self.head
        lst_other_cur = lst_other.head

        carry = False
        carryNext = False

        while True:

            if None == lst_self_cur and None == lst_other_cur:
                break

            if None == lst_self_cur:
                lst_result_cur.pNext = lst_other_cur
                break
            
            if None == lst_other_cur:
                lst_result_cur.pNext = lst_self_cur
                break

            val = int(lst_self_cur.val) + int(lst_other_cur.val)

            if val >= 10:
                val = val - 10
                carryNext = True

            tmp_Node = Node(val)
            if True == carry:
                tmp_Node.val = tmp_Node.val + 1

            if lst_result.head == None:
                lst_result.head = tmp_Node
                lst_result_cur = lst_result.head
            else:
                lst_result_cur.pNext = tmp_Node
                lst_result_cur = lst_result_cur.pNext

            lst_self_cur = lst_self_cur.pNext
            lst_other_cur = lst_other_cur.pNext
            carry = carryNext
            carryNext = False


        lst_result.tail = tmp_Node
        return lst_result

    def output(self):

        node = self.head
        while not None == node:
            print(node.val)
            node = node.pNext


if __name__ == '__main__':
    # node = Node(1)
    #
    # print(node.val)

    lst = List()

    lst.addNode(1)
    lst.addNode(4)
    lst.addNode(3)
    lst.addNode(2)
    lst.addNode(5)
    lst.addNode(2)

    lst.output()
    lst.reverse(2,4)

    lst.output()

    lst.divide(3)
    lst.output()

    lst_one = List()
    lst_two = List()

    lst_one.addNode(2)
    lst_one.addNode(4)
    lst_one.addNode(3)

    lst_two.addNode(5)
    lst_two.addNode(6)
    lst_two.addNode(4)
    lst_two.addNode(6)

    lst_result = lst_one.addList(lst_two)
    if not None == lst_result:
        lst_result.output()