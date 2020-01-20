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
        
  
