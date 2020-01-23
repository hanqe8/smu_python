#Question 1:
def get_color(code: str):
    if code.lower() == "r":
        return ("Red")
    elif code.lower() == "g":
        return ("Green")
    elif code.lower() == "b":
        return ("Blue")
    else:
        return ("Invalid")

print(get_color ('r'))
print(get_color('G'))
print(get_color('Blue Sky'))
print(get_color(''))


#Question 2:
def represent_numbers(start: int, end: int):
    new_list = []
    length = abs(start) + abs(end)
    #assumption that start is always smaller or equal to end
    count = start
    new_string = "#"
    if start < end:
        while count < end:
            for i in range(start, end+1):
                new_list.append("".join("-"*abs(count)))
                count += 1
        new_string = new_string.join(new_list)
        return new_string
    elif start == end:
        new_list.append("".join("-"*abs(start)))
        new_string = new_string.join(new_list)
        return new_string
    else:
        return ""
    
print(represent_numbers(1, 5))
print(represent_numbers(3, 5))
print(represent_numbers(-3, 1))
print(represent_numbers(1, 1))
print('[' + represent_numbers(3, 1) + ']')


