#CHECKING WHETHER NUMBER IS DIVISIBLE BY 7 and 5
n=int(input("ENTER THE NUMBER"))
if(n%5==0 and n%7==0):
	print("NUMBER IS DIVISIBLE BY BOTH 5 NAD 7")
elif(n%5==0 and n%7!=0):
	print("NUMBER IS DIVISIBLE BY ONLY 5")
elif(n%5!=0 and n%7==0):
	print("NUMBER IS DIVISIBLE BY ONLY 7")
else:
	print("NUMBER IS NOT DIVISIBLE BY BOTH 7 AND 5")			
