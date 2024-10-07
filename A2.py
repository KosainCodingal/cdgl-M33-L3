def findWater(a):
    alen = len(a)
    lt = [0]*alen
    rt = [0]*alen
    water = 0

    lt[0] = a[0]
    for i in range(1, alen): lt[i] = max(lt[i-1], a[i])
    rt[alen-1] = a[alen-1]
    for i in range(alen-2, -1, -1): rt[i] = max(rt[i+1], a[i])

    for i in range(alen): water += min(lt[i], rt[i]) - a[i]
    return water

a = [0, 2, 1, 2, 2, 0, 2, 3, 0, 2, 1]
print("Water:", findWater(a))
        
