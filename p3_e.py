x=int(input("Enter the number : "))
rev=0
while x != 0:
    d=x%10
    rev=rev*10+d
    x //= 10
print(f"Reverse number is : {rev}")