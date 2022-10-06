import numpy as np;
import random;

n = int(input("Enter the number of towers: "))
tower = []

choice = int(input("Enter 1 for random numbers and 2 for user input"))
max_height = 10

if choice == 1:
    for i in range (0,n):
        temp = random.randrange(0, max_height, 1)
        tower.append(np.random.randint(20, size=temp))

elif choice == 2:  
    print("Enter the matrix: ")
    arr = []
    ind = 0

    while ind < n:
        x = int(input(""))
        if x == -1:
            tower.append(np.array(arr))
            print(arr)
            temparr.clear()
            ind += 1
            continue
        else:
            arr.append(x)
else:
    print("Invalid Choice")
    quit()



for j in range (max_height, -1, -1):
    for i in range (0, n):
        try:
            print(tower[i][j], end="\t")
        except:
            print(" ", end="\t")
    print()

for i in range (0,n):
    for x in range(len(tower[i]) - 1):
        if(tower[i][x] > tower[i][x + 1]):
            print("Not a Rising Tower")
            quit()

print("It is a rising tower")
