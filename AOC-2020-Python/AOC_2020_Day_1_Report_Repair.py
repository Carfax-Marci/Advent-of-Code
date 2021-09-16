# PART 1:
# checks, if two numbers from a list add up do a certain target_number and multiply those two numbers and print the product.

with open('G:/Programmier Stuff/Advent_of_Code/AOC_2020_Python/AOC_2020_Day_1_Report_Repair/Input.txt') as txt_file:
    txt_input = txt_file.readlines()

target_number = 2020
result = 5

# converts input list to int list
input = []
for number in txt_input:
    input.append(int(number))

def find_two_numbers_that_sum_to(target_number, input, result):
    searching_for = []
    for number in input:
        if(number in searching_for):
            print(number, target_number - number)
            print(result)
            result = number * (target_number - number)
            print(result)
            return True, result
        else:
            searching_for.append(target_number - number)

    return False

if(find_two_numbers_that_sum_to(target_number, input, result)):
    result = find_two_numbers_that_sum_to(target_number, input, result)
    print("RESULT")
    print(result)





## PART 2:
## checks, if three (x) numbers from a list add up do a certain target_number and multiply those two numbers and print the product.

#with open('G:/Programmier Stuff/Advent_of_Code/AOC_2020_Python/AOC_2020_Day_1_Report_Repair/Input.txt') as txt_file:
#    txt_input = txt_file.readlines()

#target_number = 2020

## converts input list to int list
#input = []
#for number in txt_input:
#    input.append(int(number))

#def find_three_numbers_that_sum_to(target_number, input):
#    for number in input:
#        if (not find_two_numbers_that_sum_to(target_number - number, input)):
#            print("Break")
#            break
#        else:
#            print("Return")
#            return number * find_two_numbers_that_sum_to(target_number - number, input)
        

#print(find_three_numbers_that_sum_to(target_number, input))