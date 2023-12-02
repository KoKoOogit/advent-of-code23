inp = open("input.txt","r")


char_map = ["zero","one","two","three","four","five","six","seven","eight","nine"]


def get_first_last(replaced_string):
  

    ##chek if the string char are digits
    final_digits = []
    for char in replaced_string:
        if char.isdigit():
            final_digits.append(char)
    

    if len(final_digits) == 1:
        return int(final_digits[0] * 2)
    
    elif len(final_digits) == 0:
        return 0

    else:
        return int(final_digits[0] + final_digits[-1])

def replaceWithNumber(line):
    str_to_return = line
    for i in char_map:
        if i in str_to_return:
            num_index = str_to_return.find(i)
            str_to_return = str_to_return.replace(i,i[0]+str(char_map.index(i))+i[-1])

    return str_to_return

final_res = []
final_res_without_spelled_digits = 0
for line in inp:
    replaced = better_replaceWithNumber(line)

    final_res.append( get_first_last(replaced) )
    final_res_without_spelled_digits += get_first_last(line)


print(final_res_without_spelled_digits)
print(sum(final_res))


