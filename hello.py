print("HELLO WORLD")
for i in range(1,10):
	print(i)

print("adding new things into these files")

n=131
temp=n;
d=0;
while(n>0):
	k=n%10
	d=d*10+k
	n=n//10	
if(d==temp):
	print("palindrome")
else:
	print("not a palindrome")	
