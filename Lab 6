#Question 1
new_num = int(input("Enter number: "))
count = new_num
counter = 1
while new_num >= 0:
    new_num = int(input("Enter number: "))
    if new_num >= 0:
        count += new_num
        counter += 1
else:
    print(f"Average of positive integers entered: {count/counter}")
    

#Question 2
import random
i = 0
sum = 0
while (i <= 10 and sum < 25):
    sum += random.randrange(0,11)
    print(sum)
    i += 1

print('The loop ran',i, 'times before it exit the loop with value',sum)

#output:
##(random numbers assumption by question): 6, 2, 0, 5, 10, 8, 1, 7, 9
#6
#8
#8
#13
#23
#31
#The loop ran 6 times before it exit the loop with value 31


#Question 3
#Method 1 --> using isalpha() to determine if it is alphabetical but this means using replace(" ", "") to replace space
#Python also has isalnum() function to determine if it is alphanumeric
name = str(input("Enter name: "))
new_name = name.replace(" ", "")
while new_name.isalpha() is False:
    print("Invalid name")
    name = str(input("Enter name: "))
    new_name = name.replace(" ", "")
if new_name.isalpha() is True:
    print(f"Hello {name}!")
    

#Question 3
#Method 2
def name_check():
    name = str(input("Enter name: "))
    new_name = list(name.lower())
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " "]
    new_list = []
    for letters in new_name:
        if letters not in alphabet:
            new_list.append("False")
        else:
            new_list.append("True")
    while "False" in new_list:
        print("Invalid name")
        new_list = []
        name = str(input("Enter name: "))
        new_name = list(name.lower())
        for letters in new_name:
            if letters not in alphabet:
                new_list.append("False")
            else:
                new_list.append("True")
    if "False" not in new_list:
        return print(f"Hello {name}!")
        
name_check()


#Question 4
def randnumgame():
    import random
    user_num = str(input("Enter your guess (between 1 - 100): "))
    while user_num.isnumeric() is False:
        print("Wrong input.")
        user_num = str(input("Enter your guess (between 1 - 100): "))
    random_num = random.randint(1, 101)
    index = 1
    while int(user_num) != random_num:
        if int(user_num) > random_num:
            print("High! Try again.")
            user_num = str(input("Enter your guess (between 1 - 100): "))
            while user_num.isnumeric() is False:
                print("Wrong input.")
                user_num = str(input("Enter your guess (between 1 - 100): "))
            index += 1
        elif int(user_num) < random_num:
            print("Low! Try again.")
            user_num = str(input("Enter your guess (between 1 - 100): "))
            while user_num.isnumeric() is False:
                print("Wrong input.")
                user_num = str(input("Enter your guess (between 1 - 100): "))
            index += 1
    if int(user_num) == random_num:
        print("Congrats!")
        print(f"You guessed in {index} attempts!")
    play_again = (str(input("Do you want to play again? (Y/N)"))).lower()
    while play_again == "y":
        randnumgame()
    if play_again == "n":
        print("Bye!")
    return None #have to use return None to exit the function once the condition is met (i.e. "N")

randnumgame()


#Question 5
def binary():
    num = int(input("Enter a whole number: "))
    new_num = num
    new_list = []
    while new_num > 0:
        remainder = str(new_num%2)
        new_list.append(remainder)
        new_num = new_num//2
    binary = "".join(new_list[::-1])
    actual = bin(num)
    print("0b" + binary)
    print(f"Binary equivalent of {num} is {binary}")
    print(f"Actual binary equivalent of {num} is {actual}")
    return None

binary()


#Question 6
def multiply_func():
    print("Menu\n1. Choose a particular table to practice\n2. Practice with a random table\n3. Quit")
    user_input = str(input("Your choice? "))
    while user_input.isnumeric() is False:
        print("Invalid input")
        print("Menu\n1. Choose a particular table to practice\n2. Practice with a random table\n3. Quit")
        user_input = str(input("Your choice? "))
        
    def user_choice():
        mult_table = str(input("The multiplication table you wish to practice? "))
        while mult_table.isnumeric() is False:
            print("Invalid input")
            mult_table = str(input("The multiplication table you wish to practice? "))
        return mult_table
    
    def random_table():
        import random
        rand_num = random.randint(1, 11)
        return rand_num
        
    def table_generator():
        if int(user_input) == 1:
            mult_num = user_choice()
        elif int(user_input) == 2:
            random_table()
            mult_num = random_table()
            print(f"You will be quizzed on multiplication table: {mult_num}")
        elif int(user_input) == 3:
            return
        score = 0
        count = 1
        mult_range = range(1, 11)
        for i in mult_range:
            answer = str(input(f"{count} x {mult_num}: "))
            correct_ans = count * int(mult_num)
            while answer.isnumeric() is False:
                print("Invalid input")
                answer = str(input(f"{count} x {mult_num}: "))
            if int(answer) != correct_ans:
                print("Wrong!")
            elif int(answer) == correct_ans:
                print("Correct!")
                score += 1
            count += 1
        print(f"Your score: {score}/10")
        print("Menu\n1. Choose a particular table to practice\n2. Practice with a random table\n3. Quit")
        new_user_input = str(input("Your choice? "))
        while new_user_input.isnumeric() is False:
            print("Invalid input")
            print("Menu\n1. Choose a particular table to practice\n2. Practice with a random table\n3. Quit")
            new_user_input = str(input("Your choice? "))
        while int(new_user_input) != 3:
            table_generator()
        if int(new_user_input) == 3:
            print("Bye!")
    
    table_generator()
    
    if int(user_input) == 3:
        print("Bye!")
    return

multiply_func()


#Question 7
def tictactoe():
    print("Tic-Tac-Toe")
    print("Players, choose positions 0 to 8:")
    print("=======")
    print("|{0:<1}|{1:<1}|{2:<1}|".format(0,1,2))
    print("|{0:<1}|{1:<1}|{2:<1}|".format(3,4,5))
    print("|{0:<1}|{1:<1}|{2:<1}|".format(6,7,8))
    print("=======")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    new_board = board
    
    def board_gen():
        print("=======")
        print("|{0:<1}|{1:<1}|{2:<1}|".format(new_board[0],new_board[1],new_board[2]))
        print("|{0:<1}|{1:<1}|{2:<1}|".format(new_board[3],new_board[4],new_board[5]))
        print("|{0:<1}|{1:<1}|{2:<1}|".format(new_board[6],new_board[7],new_board[8]))
        print("=======")
        return
    
    def board_checkx():
        list1 = []
        if new_board[0] == new_board[1] and new_board[0] == new_board[2] and new_board[0] == "X":
            list1.append("True")
        elif new_board[3] == new_board[4] and new_board[4] == new_board[5] and new_board[4] == "X":
            list1.append("True")
        elif new_board[6] == new_board[7] and new_board[7] == new_board[8] and new_board[7] == "X":
            list1.append("True")
        elif new_board[0] == new_board[3] and new_board[3] == new_board[6] and new_board[3] == "X":
            list1.append("True")
        elif new_board[1] == new_board[4] and new_board[4] == new_board[7] and new_board[4] == "X":
            list1.append("True")
        elif new_board[2] == new_board[5] and new_board[5] == new_board[8] and new_board[5] == "X":
            list1.append("True")
        elif new_board[0] == new_board[4] and new_board[4] == new_board[8] and new_board[4] == "X":
            list1.append("True")
        elif new_board[2] == new_board[4] and new_board[4] == new_board[6] and new_board[4] == "X":
            list1.append("True")
        else:
            list1.append("False")
        if "True" in list1:
            return "Win"
        else:
            return "Lose"
            
    def board_checko():
        list2 = []
        if new_board[0] == new_board[1] and new_board[0] == new_board[2] and new_board[0] == "O":
            list2.append("True")
        elif new_board[3] == new_board[4] and new_board[4] == new_board[5] and new_board[4] == "O":
            list2.append("True")
        elif new_board[6] == new_board[7] and new_board[7] == new_board[8] and new_board[7] == "O":
            list2.append("True")
        elif new_board[0] == new_board[3] and new_board[3] == new_board[6] and new_board[3] == "O":
            list2.append("True")
        elif new_board[1] == new_board[4] and new_board[4] == new_board[7] and new_board[4] == "O":
            list2.append("True")
        elif new_board[2] == new_board[5] and new_board[5] == new_board[8] and new_board[5] == "O":
            list2.append("True")
        elif new_board[0] == new_board[4] and new_board[4] == new_board[8] and new_board[4] == "O":
            list2.append("True")
        elif new_board[2] == new_board[4] and new_board[4] == new_board[6] and new_board[4] == "O":
            list2.append("True")
        else:
            list2.append("False")
        if "True" in list2:
            return "Win"
        else:
            return "Lose"
    
    def alternate():
        while True:
            yield "X"
            yield "O"
            
    player = alternate()
    
    def move_input():
        move_dict = {}
        key_count = 1
        current_player = next(player)
        user_input = str(input(f"Player {current_player}, choose your position: "))
        while user_input.isnumeric() is False or int(user_input) > 8 or int(user_input) < 0:
            print("Invalid input")
            user_input = str(input(f"Player {current_player}, choose your position: "))
        while int(user_input) in move_dict.values():
            print("Tile already occupied, please select a different tile")
            user_input = str(input(f"Player {current_player}, choose your position: "))
        if user_input.isnumeric() is True and int(user_input) <= 8 and int(user_input) >= 0 and int(user_input) not in move_dict.values():
            move_dict[key_count] = int(user_input)
            new_board[move_dict[key_count]] = current_player
            board_gen()
            if current_player == "X":
                board_checkx()
                while board_checkx() != "Win" and board_checko() != "Win":
                    move_input()
            if current_player == "O":
                board_checko()
                while board_checkx() != "Win" and board_checko() != "Win":
                    move_input()  
            key_count += 1
        return
    
    move_input()
    
    if board_checkx() == "Win":
        print("Player X wins!")
    elif board_checko() == "Win":
        print("Player O wins!")
    if board_checko() == "Win" or board_checkx() == "Win":
        user_continue = str(input("Do you want to play again? (Y/N): "))
        while user_continue.isalpha() is False:
            print("Invalid input")
            user_continue = str(input("Do you want to play again? (Y/N): "))
        if user_continue.upper() == "Y" and user_continue.isalpha() is True:
            tictactoe()
        elif user_continue.upper() == "N" and user_continue.isalpha() is True:
            print("Goodbye!")
    
    return

tictactoe()


#Question 8:
list1 = [("Mike", 12), ("Scott", 20), ("Joseph", 28)]
list2 = [("John", 12), ("Kate", 15), ("Henry", 35)]
def merge(list1, list2):
    list1.extend(list2)
    new_list = list1
    def reorder(new_list):
        for i in range(0, len(new_list)-1):
            if new_list[i][1] > new_list[i+1][1]:
                new_list[i],new_list[i+1] = new_list[i+1],new_list[i]
        return new_list
    reorder(new_list)
    reorder(new_list)
    return print(new_list)

merge(list1, list2)
