#Question 1:
def m1(string):
    new_string = ""
    for characters in string:
        if characters.isalpha() is True:
            new_string += characters
    return print(new_string)

#Test cases:
m1("I think, therefore I am! ")
m1("I think,therefore I am !")
m1(" apple-pie ")
m1("     you     see?  ")
m1("\t\n\\")
m1("")
m1("a b c 1 2 3 d # ? @ , \n")


#Question 2:
def m2(string):
    list1 = string.split() #helps to split the string provided into a list divided based on spaces
    for items in list1:
        if len(list1) < 2:
            return print("None")
        elif len(list1) >= 2:
            return print(list1[1])


m2("I think, therefore I am! ")
m2("I think,therefore I am !")
m2(" apple-pie ")
m2("     you     see?  ")
m2("     you     see ? ")
m2("")
m2("a b c")


#Question 3:
def m3(string):
    list1 = string.split()
    list1.reverse()
    if len(list1) >= 1:
        print(list1[0])
    else:
        print("None")
    
m3("I think, therefore I am! ")
m3("I think,therefore I am !")
m3(" apple-pie ")
m3("     you     see?  ")
m3("     you     see ? ")
m3("")
m3("a b c")
m3("oneWordOnly")
