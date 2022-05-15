
s = 0
points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
for p1 in points:
    for p2 in points:
        for p3 in points:
            v1 = (p2[0]-p1[0],p2[1]-p1[1])
            v2 = (p3[0]-p1[0],p3[1]-p1[1])
            area = abs(v1[0]*v2[1]-v1[1]*v2[0])/2
            s = max(area,s)
print(s)