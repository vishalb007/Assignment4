from functools import reduce

def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Remove(no):
	return (no%2==0)

def Increase(no):
	return no*no

def Mul(a,b):
	return a+b

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