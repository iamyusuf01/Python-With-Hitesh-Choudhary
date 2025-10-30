# Q1. Find The Positive number and count =  [1, -2, 3, -4, 5, 6, -7, -8, 9]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9]
positive_number_count = 0

for num in numbers:
    if num > 0:
        postive_number_count += 1;
print("Final Count Of Positive Number Is: ", positive_number_count)