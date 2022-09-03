#print prime numbers from 1 to 200

start = 1
end =200
for n in range(start,end+1):
      if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n)