# TIC-TAC-TOE
import random
grid=[["_","_","_"],["_","_","_"],["_","_","_"]]
bid=[]
trace=0
def god(a,b):
    if (trace==0):
        q=random.randint(0,2)
        w=random.randint(0,2)
        return [q,w]
    
    elif ([a,b]==[0,0]):
        a1=[[0,1],[0,2],[1,0],[2,0],[1,1],[2,2]]
        tempo=random.choice(a1)
        return tempo
    elif ([a,b]==[0,1]):
        a2=[[0,0],[0,2],[1,1],[2,1]]
        tempo=random.choice(a2)
        return tempo
    elif ([a,b]==[0,2]):
        a3=[[0,1],[0,0],[1,2],[2,2],[2,0],[1,1]]
        tempo=random.choice(a3)
        return tempo
    elif ([a,b]==[1,0]):
        a4=[[0,0],[2,0],[1,1],[1,2]]
        tempo=random.choice(a4)
        return tempo
    elif ([a,b]==[1,1]):
        a5=[[0,1],[0,0],[0,2],[1,0],[1,2],[2,2],[2,0],[2,1]]
        tempo=random.choice(a5)
        return tempo
    elif ([a,b]==[1,2]):
        a6=[[0,2],[2,2],[1,1],[1,0]]
        tempo=random.choice(a6)
        return tempo
    elif ([a,b]==[2,0]):
        a7=[[0,0],[0,1],[2,1],[2,2],[1,1],[0,2]]
        tempo=random.choice(a7)
        return tempo
    elif ([a,b]==[2,1]):
        a8=[[1,1],[2,0],[2,2],[0,1]]
        tempo=random.choice(a8)
        return tempo
    elif ([a,b]==[2,2]):
        a9=[[0,1],[1,1],[2,1],[2,0],[0,2],[1,2]]
        tempo=random.choice(a9)
        return tempo
    
        
        
        
        
while True:
    for i in range(0,3):
        for j in range(0,3):
            print(grid[i][j],end="  ")
        print("\n")
    if((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="#") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="#")):
        print("you won !!!")
        break
    elif((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="O") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="O")):
        print("computer won !!!")
        break
    elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="#") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="#") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="#")):
        print("you won !!!")
        break
    elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="O") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="O") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="O")):
        print("computer won !!!")
        break
    elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="#") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="#") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="#")):
        print("you won !!!")
        break
    elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="O") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="O") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="O")):
        print("computer won !!!")
        break
    print("enter row column from 1 to 3")
    print("enter the location of slot... your symbol is '#'...")
    x=int(input("enter the row position   : "))
    y=int(input("enter the column position: "))
    if([x-1,y-1]) in bid :
        print("value alredy used...")
        continue
    grid[x-1][y-1]="#"
    bid.append([x-1,y-1])
    if(len(bid)==9):
        for i in range(0,3):
            for j in range(0,3):
                print(grid[i][j],end="  ")
            print("\n")
        if((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="#") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="O") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="O")):
            print("computer won !!!")
        elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="#") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="#") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="O") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="O") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="O")):
            print("computer won !!!")
        elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="#") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="#") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="O") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="O") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="O")):
            print("computer won !!!")
        break
    while True:
        computer=god((x-1),(y-1))
        l=computer[0]
        m=computer[1]
        if([l,m]) in bid:
            print("thinking...")
        else:
            grid[l][m]="O"
            bid.append([l,m])
            break
    if(len(bid)==9):
        for i in range(0,3):
            for j in range(0,3):
                print(grid[i][j],end="  ")
            print("\n")
        if((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="#") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]=="O") or (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]=="O")):
            print("computer won !!!")
        elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="#") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="#") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][0]=="O") or (grid[1][2]==grid[1][1] and grid[1][1]==grid[1][0] and grid[1][1]=="O") or (grid[2][2]==grid[2][1] and grid[2][1]==grid[2][0] and grid[2][2]=="O")):
            print("computer won !!!")
        elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="#") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="#") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="#")):
            print("you won !!!")
        elif((grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[0][0]=="O") or (grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[1][1]=="O") or (grid[2][2]==grid[1][2] and grid[1][2]==grid[0][2] and grid[2][2]=="O")):
            print("computer won !!!")
        break
    trace+=1
    
    