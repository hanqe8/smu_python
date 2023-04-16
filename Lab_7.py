#Question 1:
with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 11\\Lab 7\\words.txt") as new_file:
    content_list = new_file.readlines()
    vowel_list = ["a", "e", "i", "o", "u"]
    for words in content_list:
        count = 0
        distinct_vowels = []
        new_count = 0
        for characters in words:
            if characters in vowel_list and words.count(characters) > 1:
                distinct_vowels.append(characters)
            elif characters in vowel_list and words.count(characters) == 1:
                count += 1
        new_list = list(dict.fromkeys(distinct_vowels))
        new_count = count + len(new_list)
        print(words.replace("\n", " ") + str(new_count))
        
        
#Question 2:
with open ("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 11\\Lab 7\\phone.txt") as phone_file:
    phone_list = phone_file.readlines()
    new_list = []
    valid_check1 = ["1","2","3","4","5","6","7","8","9","0", "-"]
    valid_check2 = [6, 8, 9]
    valid_check3 = []
    final_list = ""
    for items in phone_list:
        new_num = items.replace("\n", "")
        if new_num[4] == "-" and len(new_num) == 9 and int(new_num[0]) in valid_check2:
            newer_num = new_num.replace("-","")
            if newer_num.isnumeric() is True:
                valid_num = newer_num[0:4:] + "-" + newer_num[4::]
                final_list += valid_num + "\n" #final_list will be string instead of list since write function below doesnt work with lists
                #.join() function also doesnt work so use += and + instead of join(valid_num + "\n")
    phone_file.close()
with open("out.txt", "w+") as new_file:
    new_file.write(final_list)
    new_file.close()
print("Writing valid phone numbers to out.txt ...\nDone.")


#Question 3:
with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 11\\Lab 7\\sales.txt") as sales_file:
    values = sales_file.readlines()
    count = 0
    from decimal import Decimal as D #import decimal to use the Decimal function (here denoted as "D" to make it easier to call function)
    #easier to use decimal than float since decimal is more accurate instead of relying on float which may not give exact value
    #can also set the number of digits that appear by using getcontext().prec = xxx (where xxx is the number of digits)
    for strings in values:
        sales_amount = D(strings[4:].replace("\n", ""))
        count += sales_amount
    sales_file.close()
    print(f"Total sales amount for the whole year: ${count}")
    
  
#Question 4:
with open("C:\\Users\\HanQE\\Desktop\\IS111\\IS111\\Week 11\\Lab 7\\talk.txt") as new_file:
    placeholder = new_file.readlines()
    string = ""
    for letters in placeholder:
        string += letters
    string1 = string.replace("\n", "♂")
    new_list = string1.split(" ")
    new_string = ""
    
    def scrambler(word):
        import random
        if word[-1].isalpha() is True and len(word) > 3 and "♂" not in word:
            string3 = ""
            word1 = random.sample(word[1:len(word)-1:], len(word)-2)
            for letters in word1:
                string3 += letters
            word2 = word[0] + string3 + word[-1]
        elif word[-1].isalpha() is False and len(word) > 4 and word[-2].isalpha() is True and "♂" not in word:
            string3 = ""
            word1 = random.sample(word[1:len(word)-2:], len(word)-3)
            for letters in word1:
                string3 += letters
            word2 = word[0] + string3 + word[len(word)-2::]
        elif "♂" in word and len(word) > 4:
            string3 = ""
            word1 = random.sample(word[2:len(word)-1:], len(word)-3)
            for letters in word1:
                string3 += letters
            word3 = word[0:2:] + string3 + word[-1]
            word2 = word3.replace("♂", "\n")
        elif "♂" in word:
            word2 = word.replace("♂", "\n")
        else:
            word2 = word
        return word2

    for words in new_list:
        new_word = scrambler(words)
        new_string += new_word + " "
        
    print(new_string)
