def putDownTheQueen(x,y,mark):
    n=len(mark)
    dxList=[0,0,1,1,1,-1,-1,-1]
    dyList=[1,-1,0,1,-1,0,1,-1]
    for i in range(n):
        #有八个方向
        for j in range(8):
            dx=dxList[j]
            dy=dyList[j]
            if 0<=x + i * dx<n and 0<=y + i * dy<n:
                mark[x + i * dx][y + i * dy]=1

def display(mark):
    for i in range(8):
        for j in range(8):
            print(mark[j][i], end=" ")
        print()

mark=[[0 for i in range(8)]for i in range(8)]
# display(mark)
putDownTheQueen(2,3,mark)
print('________________________')
display(mark)
