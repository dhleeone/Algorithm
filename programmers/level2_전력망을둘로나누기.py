import copy

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    compare_li = []
    result = 0
    for wr in wires:
        graph_c = copy.deepcopy(graph)
        graph_c[wr[0]].remove(wr[1])
        graph_c[wr[1]].remove(wr[0])

        visited = []
        stack = [wr[0]]
        while stack:
            val = stack.pop()
            for x in graph_c[val]:
                if x not in visited:
                    stack.append(x)
            visited.append(val)
        compare_li.append(len(visited))
        
    answer_li = []
    for i in range(len(compare_li)):
        result = abs(2*compare_li[i] - n)
        answer_li.append(result)       
    return min(answer_li)