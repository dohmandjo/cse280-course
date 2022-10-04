def union(A, B):
    result = set(A)
    for x in B:
        result.add(x)
    return result

def intersection(A, B):
    result = set()
    for x in A:
        if x in B:
            result.add(x)
    return result

def difference(A, B):
    result = set(A)
    for x in B:
        if x in A:
            result.remove(x)
    return result

def compliment(U, A):
    return difference(U,A)

def symmetric_difference(A, B):
    return union(difference(A,B), difference(B,A))

A={0,2,3}
B={2,3}
C={1,5,9}
U={0,1,2,3,4,5,6,7,8,9}
print(intersection(A,B))
print(union(A,B))
print(union(B,A))
print(union(A,C))
print(difference(A,B))
print(difference(B,A))
print(compliment(U,A))
print(compliment(U,B))
print(intersection(A,C))
print(symmetric_difference(A,B))

