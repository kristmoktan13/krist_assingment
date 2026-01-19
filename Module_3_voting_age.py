age=int(input("Enter your age:"))
voting_age=18
if age>=voting_age:
    print("You can vote in Finnish Parlimentary Election.")
else:
    years_left=voting_age - age
    print(f"You cannot vote yet.You can vote in {years_left}years.")


