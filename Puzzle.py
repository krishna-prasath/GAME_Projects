#list1=[['-',1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
list1= [['-',1,2],[3,4,5],[6,7,8]]
import os
def random():
    import random
    global list1
    random.shuffle(list1)
    for i in range(len(list1)):
        random.shuffle(list1[i])
    for i in range(len(list1)):
        for j in range(len(list1)):
            print(list1[i][j],"\t",end="")
        print("\n")
    return list1
li=random()

while True:
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j]=="-":
                pos=[i,j]
                break
    a=int(input("enter the number"))
    os.system('cls')
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j]==a:
                pos1=[i,j]
                break
    if(pos[0]+1==pos1[0]and pos[1]==pos1[1])or(pos[0]==pos1[0]and pos[1]+1==pos1[1])or(pos[0]-1==pos1[0]and pos[1]==pos1[1]) or(pos[0]==pos1[0]and pos[1]-1==pos1[1]):
        li[pos[0]][pos[1]],li[pos1[0]][pos1[1]]=li[pos1[0]][pos1[1]],li[pos[0]][pos[1]]
    for i in range(len(li)):
        for j in range(len(li)):
            print(li[i][j],"\t",end="")
        print("\n")
    
    
