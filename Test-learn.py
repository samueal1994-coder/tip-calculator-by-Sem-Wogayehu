print("hey there!")
#this is a test
#the 4 data types( int, float, str, bool).
first_name="python"
#using f strings f means format to print the output
print(f"hello {first_name}!")
is_engineer = True

if is_engineer:
    print(f"you are definitely an engineer  !")
else:
    print(f"you are not!")
balance = float(input("enter balance here !"))
if balance>= 10 and balance <=15:
    print("the customer is premium")
elif balance >=5 and balance<=9:
    print("the customer is standard")
elif balance <=5 and balance >=0:
    print("basic customer")
else:
    print("error!!")
