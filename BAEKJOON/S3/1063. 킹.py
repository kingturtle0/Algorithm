direct = {"R":[0,1], "L":[0,-1], "B":[1,0], "T":[-1,0], "RT":[-1,1], "LT":[-1,-1], "RB":[1,1], "LB":[1,-1]}

K, Q, N = input().split()
kx, ky = ord(K[0]) - 65, 8 - int(K[1])
qx, qy = ord(Q[0]) - 65, 8 - int(Q[1])
N = int(N)

for _ in range(N):
    dr = input()
    kny, knx = ky + direct[dr][0], kx + direct[dr][1]
    qny, qnx = qy + direct[dr][0], qx + direct[dr][1]

    if 0 <= kny < 8 and 0 <= knx < 8 and kny == qy and knx == qx:
        if 0 <= qny < 8 and 0 <= qnx < 8:
            qy, qx = qny, qnx
            ky, kx = kny, knx
    elif 0 <= kny < 8 and 0 <= knx < 8 and (kny != qy or knx != qx):
        ky, kx = kny, knx

k = "".join([chr(kx+65), str(8-ky)])
q = "".join([chr(qx+65), str(8-qy)])
print(k)
print(q)
