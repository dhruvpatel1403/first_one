degree=input("Enter the name of degree : ")
experience=int(input("How many years you have experience of this job ? : "))
if degree == "BE" and experience < 5:
    print("Your Salary is 30000")
elif degree == "BE" and experience >= 5:
    print("Your Salary is 40000")
elif degree == "ME" and experience < 5:
    print("Your Salary is 50000")
elif degree == "ME" and experience >= 5:
    print("Your Salary is 60000")
else:
    print("Enter valid degree")