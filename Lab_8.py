#Question 1:
price_info = {'pencil':0.80, 'pen':1.20, 'eraser':0.50 } 

#complete this function
def compute_bill(cart, pricing):
    from decimal import Decimal as D
    total_cost = 0
    if "pen" in cart: #don't need to search for "pen" in cart.keys(), will be faster than generating list of keys
        pen_cost = cart["pen"] * D(pricing["pen"])
        total_cost += pen_cost
    if "pencil" in cart:
        pencil_cost = cart["pencil"] * D(pricing["pencil"])
        total_cost += pencil_cost
    if "eraser" in cart:  
        eraser_cost = cart["eraser"] * D(pricing["eraser"])
        total_cost += eraser_cost
    return round(total_cost, 2)
        
jane_items = {'pen':10, 'eraser':2}
eric_items = {'pencil':12, 'eraser':5, 'pen':2}

print("Jane's bill amount $", compute_bill(jane_items, price_info))
print("Eric's bill amount $", compute_bill(eric_items, price_info))


#Question 2:

def capital_quiz():
    
    def dict_create():
        with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 12\\Lab 8\\capitals.txt") as capital_file:
            contents = capital_file.readlines()
            content_list = []
            capital_dict = {}
            for i in contents:
                content_list.append(str(i).replace("\n", ""))
            for j in content_list:
                string = str(j)
                colon_index = string.index(":")
                country = string[0:colon_index]
                capital = string[colon_index+1:]
                capital_dict[country] = capital
        return capital_dict
    
    dict_create()
    
    import random
    count = 1
    score = 0
    new_dict = dict_create()
    while count <= 10:
        quiz_country = random.choice(list(new_dict.keys()))
        user_input = str(input(f"{count}. What is the capital of {quiz_country}? "))
        while all(x.isalpha() or x.isspace() for x in user_input) is False:
            print("Invalid input")
            user_input = str(input(f"{count}. What is the capital of {quiz_country}? "))
        if all(x.isalpha() or x.isspace() for x in user_input) is True:
            if user_input.lower() == new_dict[quiz_country].lower():
                print("Correct!")
                score += 1
                count += 1
                new_dict.pop(f"{quiz_country}", None)
            elif user_input.lower() != new_dict[quiz_country].lower():
                print("Incorrect!")
                count += 1
                new_dict.pop(f"{quiz_country}", None)
    print(f"You got {score}/10 correct!")
    
    return
            

capital_quiz()


#Question 3:
with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 12\\Lab 8\\tempest.txt") as tempest_file:
    contents = tempest_file.readlines()
    new_string = ""
    letter_dict = {}
    print(new_string)
    for i in contents:
        new_sentence = str(i).replace("\n", " ")
        new_string += new_sentence
    new_list = new_string.split(" ")
    for j in new_list:
        if j[0].lower() not in letter_dict.keys():
            letter_dict[j[0].lower()] = 1
        elif j[0].lower() in letter_dict.keys():
            value = letter_dict[j[0].lower()]
            letter_dict[j[0].lower()] = value + 1
    for k in letter_dict:
        print(f"Words beginning with {k}: {letter_dict[k]}")
        
  
#Question 4:
#Author: Han Qi En

#write the function
def reverse_dict(dictionary):
    new_dict = {}
    for (key, value) in dictionary.items(): #using dict.items() returns a (key, value) tuple
        for items in value:
            # new_dict.setdefault(items, key) --> if this method is used, only one key:value will be in output
            #setdefault() method returns the value of a key (if the key is in dictionary).
            #If not, it inserts key with a value to the dictionary.
            #sample output:
            #{1: 'a', 2: 'a', 3: 'a', 4: 'c', 5: 'd', 6: 'd'}
            #{'Economics': 'Jane', 'Physics': 'Jane', 'Chemistry': 'Jane', 'Literature': 'Mark', 'Biology': 'Mark'}
            new_dict.setdefault(items, []).append(key) #this creates a new list each time and appends the key for each
    return new_dict


dict1 = reverse_dict( {"a":[1,2,3], "b":[1,2], "c":[3,4], "d":[5,6]} )

student_subjects  =  reverse_dict({ "Jane":["Economics","Physics","Chemistry"], "Mark":["Literature","Chemistry","Biology"], "Sarah":["Literature","Physics","Chemistry"]} )

print(dict1)
print()
print(student_subjects)


#Question 5:
with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 12\\Lab 8\\fifa_winners.txt") as fifa_file:
    contents = fifa_file.readlines()
    fifa_dict = {}
    fifa_list = []
    new_list = []
    for items in contents:
        for r in (("\t", ""), ("\n","")): #this helps to replace multiple substrings at once instead of using .replace for each term
            items = items.replace(*r)
        fifa_list.append(items[4::])
    fifa_list2 = list(dict.fromkeys(fifa_list)) #to remove any duplicate countries that won
    for countries in fifa_list2:
        win_count = fifa_list.count(countries)
        fifa_dict[countries] = win_count
        new_list.append((win_count, countries))
    new_list.sort(reverse = True)
    for i in range(0, 3):
        print(str(new_list[i][1]) + " " + str(new_list[i][0]))
