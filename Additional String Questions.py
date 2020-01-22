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


#Question 4:
def m4(string: str, num: int): #can use this notation to define the TYPE of variable to be passed through function
    list1 = string.split()
    if len(list1) > (num - 1):
        return print(list1[num - 1])
    else:
        return print("None")
    
    
m4("I think, therefore I am! ", 3)
m4("I think,therefore I am !", 3)
m4(" apple-pie ", 2)
m4("     you     see?  ", 3)
m4("     you     see ? ", 3)
m4("", 1)
m4("a b c", 3)
m4("oneWordOnly", 1)


#Question 5:
def m5(word: str):
    list1 = word.split()
    if len(list1) > 1 or word.isalpha() is False:
        print("Invalid input")
    elif len(list1) == 1 and word.isalpha() is True:
        letter_list = []
        for letters in word:
            letter_list.append(letters.lower())
        letter_dict = list(dict.fromkeys(letter_list)) #converting to dict then list again to get rid of dupes
        if len(letter_dict) == len(letter_list): #check if it is the same no. of elements in each list
            return print("True")
        else:
            return print("False")
        
m5("dermatoglyphics")
m5("abcdefg")
m5("duh")
m5("string")
m5("jAva")
m5("jamboree")
m5("tooth")
m5("apple")


