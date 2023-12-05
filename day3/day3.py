import string
f = open("input-test.txt", "r")
visited = set()
symbols = string.punctuation.replace(".", "")
char_map = []
parts = ""
real_parts = []

def add_to_map(line):
    content = line.split("\n")[0]
    local_arr = []
    for i in content:
        if i in symbols:
            i = i.replace(i, "*")

        local_arr.append(i)

    char_map.append(local_arr)


def check_movement(row, col):
    right_movable = True
    left_movable = True
    up_movable = True
    down_movable = True
    up_right_movable = True
    down_right_movable = True
    up_left_movable = True
    down_left_movable = True
    if row == 0:
        up_movable = False
        up_right_movable = False
        up_left_movable = False
    if col == 0:
        left_movable = False
        up_left_movable = False
        down_left_movable = False

    if row == len(char_map)-1:
        down_movable = False
        down_left_movable = False
        down_right_movable = False

    if col == len(char_map[row]):
        right_movable = False
        up_right_movable = False
        down_right_movable = False

    return (
        left_movable,
        right_movable,
        up_movable,
        up_left_movable,
        up_right_movable,
        down_movable,
        down_left_movable,
        down_right_movable
    )


def get_row(row, col):
    current_char = char_map[row][col] if not char_map[row][col] in "*." else ""
    left_count = 0
    right_count = 0
    left_chars = ""
    right_chars = ""

    while char_map[row][col-left_count].isdigit():
        set_str = f"x{row}y{col-left_count}"
        if not set_str in visited:
            # visited.add(set_str)
            left_chars = char_map[row][col-left_count] + left_chars
        else:
            print(f"{current_char}: {set_str} is in set of left")
        left_count += 1

    while char_map[row][col+right_count].isdigit():

        set_str = f"x{row}y{col+right_count}"
        if not set_str in visited:
            # visited.add(set_str)
            right_chars += char_map[row][col+right_count]

        else:
            print(f"{current_char}: {set_str} is in set of right")
        right_count += 1

    final_row = left_chars[:-1]+current_char+right_chars[1:]
    real_parts.append(final_row)
    return final_row

for line in f:
    add_to_map(line)




for row in range(0, len(char_map)):
    for col in range(0, len(char_map[row])):
        if char_map[row][col] == "*":
            left_movable, right_movable, up_movable, up_left_movable, up_right_movable, down_movable, down_left_movable, down_right_movable = check_movement(
                row, col)
            if up_movable:
                parts += get_row(row-1, col)

            if up_right_movable:

                parts += get_row(row-1, col+1)

            if up_left_movable:

                parts += get_row(row-1, col-1)

            if down_left_movable:
                parts += get_row(row+1, col-1)

            if down_right_movable:
                parts += get_row(row+1, col+1)

            if down_movable:
                parts += get_row(row+1, col)

            if left_movable:
                parts += get_row(row, col-1)

            if right_movable:
                parts += get_row(row, col+1)

print(parts)