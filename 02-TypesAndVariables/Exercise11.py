income_father = int(input("Enter father’s income: "))
income_mother = int(input("Enter mother’s income: ")) 
number_family = int(input("Enter number of people in family: "))
total_income = income_father + income_mother
income_per_person = total_income/number_family
print(f"income of a family per person: {income_per_person}")
