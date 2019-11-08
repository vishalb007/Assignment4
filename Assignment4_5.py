from functools import reduce

def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Remove(no):
	for i in range(2,no):
		if(no%i==0):
			return 0
			break
		else:
			return 1
			break

def Increase(no):
	return no*2

def Mul(a,b):
	max=a
	if (b>a):
		max=b
	return max

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	print("Enter the elements")
	lis=GetElements(num)
	filterarr=list(filter(Remove,lis))
	print("List after filter : ",filterarr)
	modarr=list(map(Increase,filterarr))
	print("List after map : ",modarr)
	product=reduce(Mul,modarr)
	print("Product is : ",product)

if (__name__=="__main__"):
	main()