c=0
#print(c)
for i in range(1,8,2):
    for j in range(0,i):
            if(c==0):
                  c=1
            else:
                  c=0
            print(c,end=" ")
    print()          