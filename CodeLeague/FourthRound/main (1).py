start = [int(item) for item in input().split()]
n, k = start[0], start[1]
wynik = start[1]
cords = []
for i in range(n):
    x = [int(item) for item in input().split()]
    index = x[0]//(k)
    try:
        cords[index].append([x[0],x[1]])
    except:
        for i in range(len(cords),index):
            cords.append([])
        cords.append([[x[0],x[1]]])
count = 0
for segment in cords:
    while segment:
        try:
            for point2 in cords[cords.index(segment)+1]:
                if (segment[0][1] - point2[1]) ** 2 + (segment[0][0] - point2[0]) ** 2 == wynik * wynik:
                    count += 1
        except:
            pass
        for point3 in segment:
            if (segment[0][1] - point3[1]) ** 2 + (segment[0][0] - point3[0]) ** 2 == wynik * wynik:
                count += 1
        segment.remove(segment[0])
print(int(count))
