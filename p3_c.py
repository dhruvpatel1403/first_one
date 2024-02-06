n=int(input("Enter the value of n : "))
s=n
mul=1
while s>0 :
    mul = s*mul
    s=s-1

print(f"Factorial of {n} is {mul}")