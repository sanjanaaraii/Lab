n=int(input("enter number"))
div=1;
sum=0
for i in range(div,(n//2)+1):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("yes")
else:
    print("no")