s = 0
num = [ [10, 20], [1, 2, 3], [100, 200, 300, 40] ]
len(num)
for i in range(len(num)):
    print(num[i])
    s = 0

    for j in range(len(num[i])):
        s = s + num[i][j]
    print(s)
