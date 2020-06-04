def twoCitySchedCost(costs):
    diffList = []
    middle = len(costs) // 2
    ans = 0
    for i, cost in enumerate(costs):
        res = cost[0] - cost[1]
        diffList.append([res, i])
    sortList = sorted(diffList)
    for j,elem in enumerate(sorted(diffList)):
        print(elem)
        if (j < middle):
            ans += costs[elem[1]][0]
        else:
            ans += costs[elem[1]][1]
    return ans