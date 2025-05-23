def rbel(tx,ty,cx,cy):
    r = 1
    if tx - 1 <= cx <= tx + 1:
        if ty - 1 <= cy <= ty + 1:
            return True
    return False

def moy(a):
    mx = 0
    ix, iy = 0,0
    for i in range(len(a)):
        ox, oy = a[i][0],a[i][1]
        if oy > mx:
            mx = oy
            ix = ox
            iy = oy
    return [ix,iy]

def main(k):
    mn = 10**10
    s = 0
    a = []
    for i in range(len(k)):
        tx, ty = k[i][0], k[i][1]
        for j in range(len(k)):
            cx, cy = k[j][0], k[j][1]
            if rbel(tx,ty,cx,cy) == True:
                s+=1
        if s < mn:
            a.clear()
            a = []
            mn = s
            a.append([tx,ty])
        elif s == mn:
            a.append([tx, ty])
    return moy(a)

print('第一做：')
s = open('27A.txt').readlines()
ak1,ak2,ak3,ak4 = [],[],[],[]
for i in s:
    s0 = i.split()
    x,y = float(s0[0]), float(s0[1])
    if x > 2:
        if y > 2: ak1.append([x,y])
        else: ak2.append([x,y])
    else:
        if y < 0: ak3.append([x,y])
        else: ak4.append([x,y])

ax1,ay1 = main(ak1)
ax2,ay2 = main(ak2)
ax3,ay3 = main(ak3)
ax4,ay4 = main(ak4)

print( (ax1+ax2+ax3+ax4)/4 *100_000 )
print( (ay1+ay2+ay3+ay4)/4 *100_000 )

print('第二做：')
s = open('27B.txt').readlines()
bk1,bk2,bk3,bk4,bk5,bk6,bk7 = [],[],[],[],[],[],[]
for i in s:
    s0 = i.split()
    x,y = float(s0[0]), float(s0[1])
    if x > 6:
        if y > 0: bk1.append([x,y])
        else: bk2.append([x,y])
    elif 1 < x < 6:
        if y > 1: bk3.append([x,y])
        else: bk4.append([x,y])
    elif -4 < x < 1:
        if y > -2: bk5.append([x,y])
        else: bk6.append([x,y])
    else: bk7.append([x,y])

bx1,by1 = main(bk1)
bx2,by2 = main(bk2)
bx3,by3 = main(bk3)
bx4,by4 = main(bk4)
bx5,by5 = main(bk5)
bx6,by6 = main(bk6)
bx7,by7 = main(bk7)

print( (bx1+bx2+bx3+bx4+bx5+bx6+bx7)/7 *100_000 )
print( (by1+by2+by3+by4+by5+by6+by7)/7 *100_000 )
