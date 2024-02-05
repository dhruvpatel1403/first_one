x=input("x : ")
if x.isdigit() == True:
    print(f"{x} is Digit")
elif x.isalpha() == True:
    print(f"{x} is Character")
else:
    print(f"{x} is Special Symbol") 