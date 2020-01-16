#Question 1
def get_numbers(num_list, min1, max1):
    new_list = []
    for nums in list1:
        if nums >= min1 and nums <= max1:
            new_list.append(nums)
    new_list.sort()
    return new_list



list1 = [4,10,12,28,24,18,5,20,15,21,30,22,21,14,17,28,26,24,6,8,15]
new_list = get_numbers(list1, 10, 20)

print("Original list", list1)
print("After function is called", new_list)


#Question 2
num1 = int(input("Enter integer number 1: "))
num2 = int(input("Enter integer number 2: "))
num3 = int(input("Enter integer number 3: "))
num4 = int(input("Enter integer number 4: "))
num5 = int(input("Enter integer number 5: "))
num6 = int(input("Enter integer number 6: "))
num7 = int(input("Enter integer number 7: "))
num8 = int(input("Enter integer number 8: "))
num9 = int(input("Enter integer number 9: "))
num10 = int(input("Enter integer number 10: "))

num_list = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]


def int_determine():
    num_list.sort()
    min1 = min(num_list)
    max1 = max(num_list)
    if len(num_list)%2 == 0:
        index = (len(num_list)//2) -1
        median = (num_list[index] + num_list[index+1])/2
    elif len(num_list)%2 != 0:
        index = (len(num_list)//2)
        median = (num_list[index])
    print(f"Minimum of numbers: {min1}")
    print(f"Maximum of numbers: {max1}")
    print(f"Median of numbers: {median}")
    return

int_determine()


#Question 3
def func1(str_list):
    str_list.append("durian")  
    out = []
    for i in str_list:
        if len(i) > 5:
            out.append(i)  
    return out

      
list1 = ["one", "apple", "six", "oranges", "bunch", "grapes"]
print ("Before :", list1)

#calling the function fun1
new_list = func1(list1)
print("After  :", list1)
print("New List:", new_list)

def func2(list_2d):
    list_2d.insert (1, [7,8])
    new_list = list_2d[1:] 
    new_list[1] = [10,11]
    return new_list
   
list1 = [[1,2], [3,4]]
list2 = [5,6]
list1.append(list2)

print ("Before :", list1)
list2 = func2(list1)
print ("After  :", list1)
print ("List2  :", list2)

#Output
# Before :["one", "apple", "six", "oranges", "bunch", "grapes"]
# After :["one", "apple", "six", "oranges", "bunch", "grapes", "durian"]
# New List:["oranges", "grapes", "durian"]
# Before :[[1,2], [3,4], [5,6]]
# After : [[1,2], [7,8], [3,4], [5,6]]
# List2 : [[7,8], [10,11], [5,6]]


#Question 4
def count_numbers(num_list):
    length = 0
    index = 0
    for i in range(len(num_list)):
        if type(num_list[i-1]) is list:
            new_length = len(num_list[i-1])
            length += new_length
        else:
            length += 1
    return length

print("Count of numbers", count_numbers([4,6,8,10,-3]))
print("Count of numbers", count_numbers([4,6,[1,2],10,[-1,-3]]))


#Question 5
def merge_lists(list1, list2):
    newlist = []
    list1 = list(dict.fromkeys(sorted(list1))) #since a dictionary cannot have duplicates, can use this method to remove duplicates
    #dict.fromkeys --> uses the elements in a list to create the keys --> dict.fromkeys(element, [value = optional])
    #the element determines what the key names will be from the list and the value is the value to be assigned to the keys
    #which can be another list
    list2 = list(dict.fromkeys(sorted(list2)))
    if len(list1) >= len(list2):
        newlist = list1
        for i in list2:
            if i not in list1:
                newlist.append(i)
    elif len(list2) >= len(list1):
        newlist = list2
        for x in list1:
            if x not in list2:
                newlist.append(x)
    return sorted(newlist)
    
    
print("Merging [1,2,3],[4,3,2]      :", merge_lists([1,2,3],[4,3,2]))
print("Merging [3,2,1],[2,6,4,10,4] :", merge_lists([3,2,1],[2,6,4,10,4]))
print("Merging [3,1,1],[]           :", merge_lists([3,1,1],[]))
print("Merging [],[9,7,2,7]         :", merge_lists([],[9,7,2,7]))


#Question 6
def get_user_info(name_list):
    index = 0
    new_list = []
    for i in name_list:
        new_list.append(tuple(name_list[index].split("@")))
        index += 1
    return new_list
    
def print_users(lister):
    for x in lister:
        print(x, sep = "\n")
    return
    
    
name_list = ["shaun.chew.2010@sis.smu.edu.sg","sitongchen.2011@economics.smu.edu.sg"]
users_tuple = get_user_info(name_list)

print("Users and their domain")
print_users(users_tuple)


#Question 7
def transpose(matrix):
    length = len(matrix)
    newlist = []
    counter = 0
    count1 = 0
    index = 0
    for i in matrix[0]:
        newlist.append([])
    while counter <= (length - 1):
        for x in matrix[0]:
            newlist[index].append(matrix[count1][index])
            count1 += 1
        count1 = 0
        index += 1
        counter += 1
    return newlist
    

original = [[1,2],[3,4]]
print ("Original :", original)
print ("Transposed:", transpose(original) )

original = [[1,2,3],[4,5,6],[7,8,9]]
print ("Original :", original )
print ("Transposed:", transpose(original) )

original = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print ("Original :", original )
print ("Transposed:", transpose(original) )


#Question 8
def is_magic_square(square):
    
    def all_nums(square):
        nums_list = [1,2,3,4,5,6,7,8,9]
        newlist = []
        index = 0
        counter = 8
        for i in square:
            newlist.extend(square[index])
            index += 1
        for x in nums_list:
            if newlist[counter] in nums_list and newlist.count(newlist[counter]) == 1:
                newlist.remove(newlist[counter])
                counter -= 1
        if len(newlist) == 0:
            return "no duplicates"
        else:
            return "duplicates"
    
    all_sum = 15
    index_count = 0
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0
    index6 = 0
    index7 = 2
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    counter = 0
    check1 = []
    check2 = []
    check3 = []
    check4 = []
    check5 = []
    check6 = []
    if all_nums(square) == "no duplicates":
        for i in square:
            if sum(square[index1]) == all_sum:
                check1.append("True")
            else:
                check1.append("False")
            index1 += 1
        for x in square:
            count1 += square[index2][0]
            if count1 == all_sum:
                check2.append("True")
            else:
                check2.append("False")
            count1 = 0
            index2 += 1
        for x in square:
            count2 += square[index3][1]
            if count2 == all_sum:
                check3.append("True")
            else:
                check3.append("False")
            count2 = 0
            index3 += 1
        for x in square:
            count3 += square[index4][2]
            if count3 == all_sum:
                check4.append("True")
            else:
                check4.append("False")
            count3 = 0
            index4 += 1
        for x in square:
            count4 += square[index5][index5]
            if count4 == all_sum:
                check5.append("True")
            else:
                check5.append("False")
            count4 = 0
            index5 += 1
        for x in square:
            count5 += square[index6][index7]
            if count5 == all_sum:
                check6.append("True")
            else:
                check6.append("False")
            count5 = 0
            index6 += 1
            index7 -= 1
        if "False" in (check1 or check2 or check3 or check4 or check5 or check6):
            return print(f"{square} magic square?: False")
        else:
            return print(f"{square} magic square?: True")
            
        
    elif all_nums(square) == "duplicates":
        return print(f"{square} magic square?: False")
    
    
    
        

is_magic_square([[4,3,8],[9,5,1],[2,7,6]])
is_magic_square([[4,9,2],[3,5,7],[8,1,6]])
is_magic_square([[6,1,8],[7,5,3],[2,9,4]])
is_magic_square([[5,5,5],[5,5,5],[5,5,5]])
is_magic_square([[2,6,7],[9,5,1],[4,3,8]])
is_magic_square([[10,4,1],[1,3,9],[2,6,5]])
