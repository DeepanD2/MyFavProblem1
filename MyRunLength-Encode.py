a=str(input())
b=[]
count=1
for i in range(0,len(a)):
  if(i==len(a)-1):
    b.append([a[i],str(count)])
  elif(a[i]==a[i+1]):
    count=count+1
  else:
    b.append([a[i],str(count)])
    count=1
for i in range(0,len(b)):
  print(b[i][0]+str(b[i][1]),end="")
