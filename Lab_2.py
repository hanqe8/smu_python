#Question 1
month = int(input("Enter Month.\n(1: January, 2: February)\nEnter number between 1 and 12 only."))
def month_day(month):
    if month <= 0:
        return "error, month is invalid"
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 28

if month <= 0:
    print("The month is invalid")
else:
    print(f"There are {month_day(month)} days in this month.")
    

#Question 2
sales = int(input("Enter monthly sales amount ($): "))
base = 2000
def commission():
    if sales < 10000:
        return 0.05
    elif 10000 <= sales < 15000:
        return 0.1
    elif 15000 <= sales < 18000:
        return 0.15
    elif sales >= 18000:
        return 0.18
percent = commission() * 100 
def total_pay():
    return base + (commission()*sales)
print(f"Commission rate for sales of sales amount ${sales} is {percent}%")
print(f"The monthly pay for the salesperson is ${total_pay()}")


#Question 3
# Author: <Han Qi En>
import random
num1 = random.randrange(1,10) 
num2 = random.randrange(1,10)
num3 = random.randrange(1,10)

input('Press <enter> key to start') #to pause and wait for user input
print()

print('*****************')
print('**', num1, '**', num2, '**', num3,'**')
print('*****************')

def message():
    if num1 == num2 or num2 == num3 or num3 == num1:
        return "2 of a kind"
    elif num1 == num2 and num1 == num3:
        return "Jackpot!"
    else:
        return "Try again!"
print(message())


#Question 4
number = int(input("Enter positive integer: "))
def perfectint():
    total = 0
    index_count = 0
    for i in range(1,number,1):
        while total < number:
            index_count += 1
            total += index_count
    return total
if perfectint() == number:
    print(f"Yes, {number} is a perfect number")
else:
    print(f"{number} is not a perfect number")
    

#Question 5
nums = int(input("Enter a binary number consisting of 1 & 0: "))
numbers = list(str(nums))
for i in numbers:
    if i == "0":
        print(False)
    elif i == "1":
        print(True)
        

#Question 6
income = int(input("Enter your personal income: "))
def incometax():
    if income < 20000:
        return 0
    elif income in range(20000, 30000):
        return min(((income-20000)*0.02), 200)
    elif income in range(30000, 40000):
        return min(((income-30000)*0.035), 350)
    elif income in range(40000, 80000):
        return min(((income-40000)*0.07), 2800)
    elif income in range(80000, 120000):
        return min(((income-80000)*0.115), 4600)
    elif income in range(120000, 160000):
        return min(((income-120000)*0.15), 6000)
    elif income in range(160000, 200000):
        return min(((income-160000)*0.18), 7200)
    elif income >= 20000:
        return ((income-20000)*0.2)
    else:
        return "Error"
def grosstax():
    if income < 20000:
        return 0
    elif income in range(20000, 30000):
        return 0
    elif income in range(30000, 40000):
        return 200
    elif income in range(40000, 80000):
        return 550
    elif income in range(80000, 120000):
        return 3350
    elif income in range(120000, 160000):
        return 7950
    elif income in range(160000, 200000):
        return 13950
    elif income >= 20000:
        return 21150
    else:
        return "Error"
total_tax = incometax() + grosstax()
print(f"Tax payable: ${total_tax}")


#Question 7
dollars = float(input("Enter amount in $: "))
five = 0
ten = 0
twenty = 0
fifty = 0
one = dollars//1
def coins():
    cents = dollars%1
    while cents > 0.5:
        cents -= 0.5
        fifty += 1
    else:
        while cents >= 0.2:
            cents -= 0.2
            twenty += 1
        else:
            if cents == 0.1:
                cents -= 0.1
                ten += 1
            else:
                if cents == 0.05:
                    cents -= 0.05
                    five += 1
if one > 0:
    print(f"Number of 1$: {one}")
elif fifty > 0:
    print(f"Number of 50c: {fifty}")
elif twenty > 0:
    print(f"Number of 20c: {twenty}")
elif ten > 0:
    print(f"Number of 10c: {ten}")
elif five > 0:
    print(f"Number of 5c: {five}")
    
    
#Question 8
number = int(input("Enter count of ascending sequence: "))
start = int(input("Enter the starting digit: "))
start_num = [start]
new_list = []
start_string = str(start)
for i in range(1, number):
    starter = start + 1
    new_list.append(starter)
    new_num = start_string.join(new_list)
    start_num.append(new_num)
    start += 1
print(start_num)
