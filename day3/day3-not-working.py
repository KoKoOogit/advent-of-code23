import string

symbols = string.punctuation.replace(".","")

f = open("input-test.txt","r")

maps = []

part_numbers = []
def add_to_map(line):
    content = line.split("\n")[0]
    local_arr = []
    for i in content:
        local_arr.append(i)


    
    maps.append(local_arr)


def getHoriVertChars(row,col):
    #returns if adajacnet and aray of adjancent characters (right,left,up,down)
    up =""
    down=""
    left=""
    right=""

   

    is_possible = False
    active_row = maps[row]

    #check up down left right
    if row == 0:
        up = "end"
        if col == 0:
            down = maps[row+1][col]
            left = "end"
            right = maps[row][col+1]
        elif col == len(active_row)-1:
            right = "end"
            left = maps[row][col-1]
            down = maps[row+1][col]

        else:
            down = maps[row+1][col]
            left = maps[row][col-1]
            right = maps[row][col+1]

    elif row == len(maps)-1:
        down = "end"
        if col == 0:
            up = maps[row-1][col]
            left = "end"
            right = maps[row][col+1]
        elif col == len(active_row)-1:
            right = "end"
            left = maps[row][col-1]
            up = maps[row-1][col]

        else:
            up = maps[row-1][col]
            left = maps[row][col-1]
            right = maps[row][col+1]

    else:
        up = maps[row-1][col]
        left = maps[row][col-1]
        right = maps[row][col+1]
        down = maps[row+1][col]
    
    if left in symbols or right in symbols or up in symbols or down in symbols:
        is_possible = True
    
    return is_possible, [left, right, up, down]
    # return row,col, is_possible, [left,right,up,down]

#returns is_possible, [up_left,up_right,down_left,down_right]
def getDiagChars(char_info):
    right = char_info[1]
    left = char_info[0]
    up = char_info[2]
    down = char_info[3]
    is_possible = False
    up_right = ""
    up_left = ""
    down_left = ""
    down_right = ""
    #char row index is 0
    if left == "end":
        up_left = "end"
        down_left = "end"

        if up == "end":
            up_right = "end"
            down_right = maps[row+1][col+1]

        elif down == "end":
            down_right = "end"
            up_right= maps[row-1][col+1]

        else:
            up_right = maps[row-1][col+1]
            down_right = maps[row+1][col+1]
    
    elif right == "end":
        up_right = "end"
        down_right = "end"
        if up == "end":
            down_left = maps[row+1][col-1]
            up_left = "end"
        elif down == "end":
            down_left = "end"
            up_left = rows[col-1][col-1]
        else:
            up_left = maps[row-1][col-1]
            down_left = maps[row+1][col-1]
    
    else:
        if up == "end":
            up_left = "end"
            up_right = "end"
            down_left = maps[row+1][col-1]
            down_right = maps[row+1][col+1]
        if down == "end":
            up_left = maps[row-1][col-1]
            up_right = maps[row-1][col+1]
            down_left = "end"
            down_right = "end"
        else:
            up_left = maps[row-1][col-1]
            up_right = maps[row-1][col+1]
            down_left = maps[row+1][col-1]
            down_right = maps[row+1][col+1]

        if up_left in symbols or up_right in symbols or down_left in symbols or down_right in symbols:
            is_possible = True

    return is_possible,[up_left,up_right,down_left,down_right]

for line in f:
    add_to_map(line)


for row in range(0,len(maps)):
    isPossibleNumSeries = False
    numSeries = ""
    for col in range(0,len(maps[row])):
        if maps[row][col].isdigit():
            horiVertPossible, horiVertInfo = getHoriVertChars(row,col)
            diagPossible,diagInfo = getDiagChars(horiVertInfo)

            if diagPossible or horiVertPossible:
                isPossibleNumSeries = True
                numSeries += maps[row][col]
            else:
                if isPossibleNumSeries:
                    numSeries += maps[row][col]
        else:
            isPossibleNumSeries = False
            if len(numSeries) != 0 and numSeries[len(numSeries)-1] != " ":
                numSeries += " "

    if numSeries != "":
        part_numbers.append(numSeries)
    

print(part_numbers)