def main():
	no1=int(input("Enter 1 number : "))
	no2=int(input("Enter 2 number : "))
	x=lambda no1,no2:no1*no2
	print("Multiplication is : ",x(no1,no2))

if (__name__=="__main__"):
	main()