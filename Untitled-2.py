my_list = [1, "hi", 3, "guvi"]

check_type = lambda lst: all(isinstance(elem, (int, str)) for elem in lst)

print(check_type(my_list))  # Output will be True