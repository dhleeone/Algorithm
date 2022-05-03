# 링크드 리스트

class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    node_arr = [Node() for _ in range(n)]
    for i in range(1, n):
        node_arr[i-1].next = node_arr[i]
        node_arr[i].prev = node_arr[i-1]

    curr = node_arr[k]
    stack = []

    for line in cmd:
        if line[0] == "U":
            num = int(line[2:])
            for _ in range(num):
                curr = curr.prev

        elif line[0] == "D":
            num = int(line[2:])
            for _ in range(num):
                curr = curr.next

        elif line[0] == "C":
            stack.append(curr)
            curr.removed = True
            bnd = curr.prev
            nnd = curr.next
            if bnd:
                bnd.next = nnd
            if nnd:
                nnd.prev = bnd
                curr = nnd
            else:
                curr = bnd
        else:
            node = stack.pop()
            node.removed = False
            bnd = node.prev
            nnd = node.next
            if bnd:
                bnd.next = node
            if nnd:
                nnd.prev =node

    answer = ""
    for i in range(n):
        if node_arr[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer