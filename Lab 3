#Question 1
name = str(input("Enter your full name: "))
gender_type = str(input("Enter 'M' (male) of 'F' (female) for your gender: "))
if gender_type == "M" or gender_type == "m":
    gender = "Mr."
elif gender_type == "F" or gender_type == "f":
    gender = "Ms."
name_list = list(name.split(" "))
if len(name_list) == 2:
    print(f"Hello, {gender} {name_list[1].upper()} {name_list[0]}")
elif len(name_list) > 2:
    print(f"Hello, {gender} {name_list[0].upper()} {' '.join(name_list[1:])}")
elif len(name_list) < 2:
    print(f"Hello, {gender} {name_list[0]}")
    
    
#Question 2
line = str(input("Enter a line of text containing an email address: "))
email_find = list(line.split(" "))
email_list = []
def email_finder():
    count = 0
    for i in email_find:
        if "@" and "." in email_find[count]:
            email_list.append(email_find[count])
            count += 1
        else:
            count += 1
email_finder()
print(*email_list, sep = "\n")


#Question 3
text = str(input("Enter the string: ")).lower()
first = str(input("Enter the first character: "))
last = str(input("Enter the last character: "))
found = []
new_list = []
def text_split():
    for letters in text:
        new_list.append(letters)
    one = new_list.index(first.lower())
    two = new_list.index(last.lower())
    if first.lower() in new_list and last.lower() in new_list and two > one:
        for letters in new_list[0:two+1]:
            found.append(letters)
        new_string = "".join(found)
        return print(f"Substring [{new_string}] is found")
    else:
        return print("No such substring")
text_split()


#Question 4
user_input = str(input("Enter the string: "))
new_string = user_input.lower()
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
new_list = []
for letters in new_string:
    if letters in alphabets:
        new_list.append(letters)
def palindrome():
    if new_list[0:] == new_list[::-1]:
        return print(f'The string "{user_input}" is a palindrome')
    else:
        return print(f'The string "{user_input}" is not a palindrome')
palindrome()


#Question 5
str1 = str(input("Enter characters: ")).lower()
str2 = str(input("In string? ")).lower()
def bingo():
    for letters in list(str1):
        if letters in list(str2):
            return print("Bingo!")
        else:
            return print("Nope :(")
bingo()


#Question 6
card_number = str(input("Enter card number: "))
new_list = []
for nums in card_number:
    if (int(nums)*2) < 10:
        new_list.append(2*int(nums))
    elif (int(nums)*2) >= 10:
        new_list.append(2*int(nums)-9)
check_list = []
check_list.append(new_list[::2])
index = 0
for i in check_list:
    count = sum(check_list[index])
    index += 1
if count%10 == 0:
    print("This credit card is valid")
else:
    print("This credit card is invalid")
