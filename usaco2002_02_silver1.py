def possible(cow, picked_gifts, k):
    if k == N:
        return True
    if k == cow:
        return possible(cow, picked_gifts, k+1)
    for i in range(org_assignment[k]+1):
        gift = prefs[k][i]
        if gift not in picked_gifts:
            if possible(cow, picked_gifts.union({gift}), k+1):
                return True
    return False

def get_best(i):
    for j in range(org_assignment[i]):
        if possible(i, {prefs[i][j]}, 0):
            return prefs[i][j]+1
    return i+1

N = int(input())
prefs = []
org_assignment = []
for i in range(N):
    pref = list(map(lambda x: int(x)-1, input().split()))
    prefs.append(pref)
    org_assignment.append(pref.index(i))
for i in range(N):
    print(get_best(i))
