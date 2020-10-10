
t = 6
res = []
res.append(1/t)

while 1:
    if len(res) < t:
        tmp = 1/t
        for i in res:
            tmp += 1/t * i
        res.append(tmp)
    else:
        tmp = 0
        for i in res[-t:]:
            # print(i)
            tmp += 1/t * i
        # print('--')
        res.append(tmp)
    print(res[-1])
    if len(res) == 2020:
        print(res[-1])
        break