n = int(input())
l=[]
l.append(n)
for i in range(n*100):
    if n ==1:
        
        break
    
    elif n % 2==0:
        
        n = n/2
        l.append(int(n))
    elif n%2!=0:
        n = 3*n +1
        l.append(int(n))
    
for j in l:
    print(j,end=" ")
