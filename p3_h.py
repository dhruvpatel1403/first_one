x=int(input("Enter value : "))
rev=0
j=x
while x>0:
    a=x%10
    rev=rev*10+a
    x //= 10
if rev == j:
    print("Number is palindrom number...")
else:
    print("Number is not palindrom number")