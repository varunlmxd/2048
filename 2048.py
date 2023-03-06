import numpy as np
import random
from msvcrt import getch 
print("""           WELCOME TO 2048 GAME
         YOU HAVE TO MERGE THE SAME MULTIPLES OF TWO'S
         UNTIL YOU'LL REACH THE NUMBER 2048
         USE THE ARROW KEYS TO MOVE AND MERGE THE NUMBERS
         AND YOU'LL HAVE AN UNDO OPTION ALSO
         TO MAKE ODD'S IN YOUR FAVOUR BY CLICKING SPACE BAR""")
score=0
"""Generates random number form [2,4]"""
def rand():
    return(random.choice(arr_r))
"""Locates where 0 is present and update number form rand()"""
def rand_num_input():
    index=np.where(arr==0)
    if(len(index[0])==1):
        rand_index= 0
        arr[index[0][rand_index],index[1][rand_index]]=rand()
    if(len(index[0])):
        rand_index= random.randint(0,len(index[0])-1)
        arr[index[0][rand_index],index[1][rand_index]]=rand()


arr_r=np.array([2,4])
arr=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
rand_num_input()
rand_num_input()

undo=0
def remove_zero_left():
    flag=0
    for k in range(0,4):   
        for i in range(0,4):
            if(arr[k][i]==0):
                for j in range(i+1,4):
                    if(arr[k][j]!=0):
                        flag=1
                        arr[k][i]=arr[k][j]
                        arr[k][j]=0
                        break
    return flag

def remove_zero_right():
    flag=0
    for k in range(0,4):
        i=-1   
        while(i>=-4):
            if(arr[k][i]==0):
                j=i-1
                while(j>=-4):
                    if(arr[k][j]!=0):
                        flag=1
                        arr[k][i]=arr[k][j]
                        arr[k][j]=0
                        break
                    j=j-1
            i=i-1
    return flag 
    
def remove_zero_up():
    flag=0
    for k in range(0,4):   
        for i in range(0,4):
            if(arr[i][k]==0):
                for j in range(i+1,4):
                    if(arr[j][k]!=0):
                        flag=1
                        arr[i][k]=arr[j][k]
                        arr[j][k]=0
                        break
    return flag

def remove_zero_down():
    flag=0
    for k in range(0,4):
        i=-1   
        while(i>=-4):
            if(arr[i][k]==0):
                j=i-1
                while(j>=-4):
                    if(arr[j][k]!=0):
                        flag=1
                        arr[i][k]=arr[j][k]
                        arr[j][k]=0
                        break
                    j=j-1
            i=i-1
    return flag 

def left():
    global score
    flag=remove_zero_left()
    """remove zeros from arr and shift them"""
    print(flag)
    for i in range(0,4):
         for j in range (1,4):   
            if((arr[i][j]==arr[i][j-1]) and not(arr[i][j]==0 and arr[i][j-1]==0)) :
                flag=1
                arr[i][j-1]=arr[i][j]+arr[i][j-1]
                score+=arr[i][j]
                k=j
                while(k<3):
                     arr[i][k]=arr[i][k+1]
                     k=k+1
                arr[i][k]=0
    #print(arr)          
    if(flag):
        rand_num_input()

def right():
    global score
    flag=remove_zero_right()
    """remove zeros from arr and shift them"""
    print(flag)
    for i in range(0,4):
         j=3
         while(j>0):   
            if((arr[i][j]==arr[i][j-1]) and not(arr[i][j]==0 and arr[i][j-1]==0)) :
                flag=1
                arr[i][j]=arr[i][j]+arr[i][j-1]
                score+=arr[i][j]
                k=j-1
                while(k>0):
                     arr[i][k]=arr[i][k-1]
                     k=k-1
                arr[i][k]=0
            j=j-1
    #print(arr)
    if(flag):
        rand_num_input()

def up():
    global score
    flag=remove_zero_up()
    """remove zeros from arr and shift them"""
    print(flag)
    for i in range(0,4):
         for j in range (1,4):   
            if((arr[j][i]==arr[j-1][i]) and not(arr[j][i]==0 and arr[j-1][i]==0)) :
                flag=1
                arr[j-1][i]=arr[j][i]+arr[j-1][i]
                score+=arr[j][i]
                k=j
                while(k<3):
                     arr[k][i]=arr[k+1][i]
                     k=k+1
                arr[k][i]=0
    #print(arr)          
    if(flag):
        rand_num_input()             

def down():
    global score
    flag=remove_zero_down()
    """remove zeros from arr and shift them"""
    print(flag)
    for i in range(0,4):
         j=3
         while(j>0):   
            if((arr[j][i]==arr[j-1][i]) and not(arr[j][i]==0 and arr[j-1][i]==0)):
                flag=1
                arr[j][i]=arr[j][i]+arr[j-1][i]
                score+=arr[j][i]
                k=j-1
                while(k>0):
                     arr[k][i]=arr[k-1][i]
                     k=k-1
                arr[k][i]=0
            j=j-1
    #print(arr)
    if(flag):
        rand_num_input()

def check():
    #left
    for i in range(0,4):
         for j in range (1,4):   
            if((arr[i][j]==arr[i][j-1]) and not(arr[i][j]==0 and arr[i][j-1]==0)) :
                return 1
    #right
    for i in range(0,4):
         j=3
         while(j>0):   
            if((arr[i][j]==arr[i][j-1]) and not(arr[i][j]==0 and arr[i][j-1]==0)) :
                return 1
            j=j-1
    #up
    for i in range(0,4):
         for j in range (1,4):   
            if((arr[j][i]==arr[j-1][i]) and not(arr[j][i]==0 and arr[j-1][i]==0)) :
                return 1
    #down
    for i in range(0,4):
         j=3
         while(j>0):   
            if((arr[j][i]==arr[j-1][i]) and not(arr[j][i]==0 and arr[j-1][i]==0)):
                return 1
            j=j-1
    return 0

    
while True:
    print(arr)
    print("Score :",score)
    find=np.where(arr==2048)
    if(len(find[0])):
        print("Hola you got a 2048, Enjoyyy!!!!!!")
        exit()
    keycode = ord(getch())
    if keycode==224:
        keycode = ord(getch())    
        if keycode == 80: #Down arrow
                undo=np.copy(arr) 
                down()
        elif keycode == 72: #Up arrow
                undo=np.copy(arr)
                up()
        elif keycode == 75: #Left arrow
                undo=np.copy(arr) 
                left()
        elif keycode == 77: #Right arrow
                undo=np.copy(arr)
                right()
    elif keycode == 27:
                print("Forced Exit")
                exit()
    elif keycode == 32:
        arr= np.copy(undo)
    else:
        print("Not a valid key")
    
    find=np.where(arr==0)
    # print(not(len(find[0])))
    # print(not(check()))
    if( not(len(find[0])) and not(check())):
        print(arr)
        print("Game Over!")
        print("You can undo else press ESC to exit")