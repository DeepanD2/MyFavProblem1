Given an array N, sort it in ascending order till it reaches kth elements and after that sort it in descending order.
Input Size : N <= 100000
Sample Testcase :
INPUT
5 2
4 3 1 2 4
OUTPUT
3 4 4 2 1




a,b=input().split()
a,b=int(a),int(b)
c=list(map(int,input().split()))
for i in range(0,a-1):
  for j in range(i+1,a):
    if(c[i]>c[j] and i<b and j<b ):
      c[i],c[j]=c[j],c[i]
    elif(i>=b and j>=b and c[i]<c[j]):
      c[i],c[j]=c[j],c[i]
for i in c:
  print(i,end=" ")
      
