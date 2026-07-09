#ask user for bill total and number of people
bill_total = float(input("Enter the bill total (ETB): "))
num_people = int(input("Enter number of people: "))

# Define a function to split the bill
def split_bill(total, people, tip_rate=0.10):
    tip = total * tip_rate
    grand_total = total + tip
    return grand_total / people

# Collect names of friends
friends = []
for i in range(num_people):
    name = input(f"Enter name of person {i+1}: ")
    friends.append(name)

# Print each person's share
for name in friends:
    share = split_bill(bill_total, num_people)
    print(f"{name} pays {share:.2f} ETB")
