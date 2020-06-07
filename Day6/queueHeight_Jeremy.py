from typing import List

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    '''
    Inserting shortest first
    O(n) because we have to go through each value of people
    Runtime: ~750ms
    '''
    ans = [ None for i in range(len(people)) ]

    people.sort(key = lambda pair : (pair[0], -pair[1]))
    for p in people:
        candidateIndex = 0
        emptySpaceCount = 0
        while(ans[candidateIndex] != None or emptySpaceCount != p[1]):
            if ans[candidateIndex] == None:
                emptySpaceCount += 1
            candidateIndex += 1
        ans[candidateIndex] = p

    return ans

def alternate(people: List[List[int]]) -> List[List[int]]:
    '''
    Inserting tallest first
    Runtime: ~100ms
    '''
    people.sort(key=lambda pair : (-pair[0], pair[1]))

    ans = []
    for p in people:
        # insert will automatically expand the array
        # it will also shift other elements to the right 
        # when there's index conflicts
        ans.insert(p[1], p)
    return ans

if __name__ == "__main__":
    test = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(reconstructQueue(test))