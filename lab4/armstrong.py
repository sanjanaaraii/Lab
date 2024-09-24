for i in range(1,1001):
    n=i
    count=0
    sum=0
    while(n!=0):
        count+=1
        n=n//10
    n=i
    while(n!=0):
        d=n%10
        n=n//10
        sum=sum+d**count
    if(sum==i):
        print(f"{i} \n")