#Question 1
# Author: <Han Qi En>
# write code for function is_factor here
def is_factor(n, f):
    if n%f == 0:
        return True
    else:
        return False

print('3 is a factor of 10?:', is_factor(10,3))
print('2 is a factor of 10?:', is_factor(10,2))


#Question 2
def m1(x):
  str_output = ''
  for i in range(1,x+1):
    str_output += str(x)
  print(str_output)

def m2(x):
  for i in range(1,x+1):
    m1(i)

#Output of m2(5):
#1
#22
#333
#4444
#55555

def func1(a):
  a += 1
  print('in func1: calling func2')
  func2(a, 1)
  print('in func1: called func2')
  return a

def func2(a, b):
  a = a * 10
  c = a + b 
  print('in func2')
  print(str(a) + ' + ' + str(b) + ' = ' + str(c))
  
a = func1(4)
print("called func1:",a)

#Output:
#in func1: calling func2
#in func2
#(in func2) 50 + 1 = 51 (since in func1, a += 1 hence a = 4 + 1 = 5)
#in func1: called func2
#called func1:5


#Question 3
m = int(input("Enter value for m: "))
n = int(input("Enter value for n: "))
def sum_of_powers(m, n):
    new_sum = 0
    for i in range(0, n+1):
        new_sum += m**i
    return print(f"Sum of all powers is {new_sum}")
sum_of_powers(m, n)


#Question 4
import math
def print_squares(mini, maxi):
    new_list = []
    for i in range(mini, maxi+1):
        if math.sqrt(i)%1 == 0.0:
            new_list.append(i)
    for x in range(len(new_list)):
        print(new_list[x], end = " ")
print_squares(10, 100)


#Question 5
s = str(input("Enter your string: "))
c = str(input("Enter your character: "))
def count_characters(s, c):
    new_list = []
    count = 0
    for letters in s:
        new_list.append(letters)
    for i in range(len(new_list)):
        if c == new_list[i]:
            count += 1
    if count > 0:
        return print(f"Number of characters '{c}' in '{s}': {count}")
    else:
        return print(f"Number of characters '{c}' in '{s}': None")
count_characters(s, c)


#Question 6
def get_sandwich(word):
    new_list = []
    for letters in word:
        new_list.append(letters)
    index = 0
    newer_list = []
    if len(new_list)%2 == 0:
        new_range = (range(len(new_list)//2))
    elif len(new_list)%2 != 0 and len(new_list) > 1:
        new_range = ((range(len(new_list)//2)))
    elif len(new_list) == 1:
        new_range = range(len(new_list))
    for i in new_range:
        if new_list[index] == new_list[(-index)-1]:
            newer_list.append(new_list[index])
            index += 1
        elif new_list[0] != new_list[-1]:
            newer_list.append("None")
    lister = []
    for alphabets in new_list:
        if "None" in newer_list:
            return "None"
        elif alphabets not in newer_list:
            lister.append(alphabets)
    return "".join(lister)
    
print("Sandwich substring: " + get_sandwich("toast"))
print(">" + get_sandwich("peep") + "<") #(it returns an empty string)
print(get_sandwich("robot"))
print(get_sandwich("ttoaott"))
print(get_sandwich("p")) 


#Question 7
def encode(sentence):
    new_string = ""
    for letters in sentence:
        new_string += hex(ord(letters)).replace("0x", "")
    return new_string

print("Encoded string:" + encode("Hello"))

def decode(hexa):
    newer_string = ""
    new_list = []
    newer_list = []
    index = 0
    for alphabets in hexa:
        new_list.append(alphabets)
    
    for i in range(len(hexa)-2):
        if index%2 == 0:
            new_hex = (new_list[index] + new_list[index+1])
            newer_list.append(int(new_hex, 16))
            index += 1
        elif index%2 != 0:
            index += 1
    count = 0
    for nums in newer_list:
        newer_string += chr(newer_list[count])
        count += 1
    return newer_string

print("After decoding:" + decode("68656c6c6f20576f726c6421"))
