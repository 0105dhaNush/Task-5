Data = [10, 501, 22, 37, 100, 999, 87, 351]  # List containing some numbers

# Using filter() function with a lambda function to filter out elements greater than 4
Result = filter(lambda x: x > 4, Data)

# Converting the filtered result into a list and printing it
print(list(Result))


[10, 501, 22, 37, 100, 999, 87, 351]

the same output  explanation  the lambda function filters out elements greater than 4