from collections import deque

labyrinth = [
    "#######",
    "#     #",
    "#   ###",
    "# ### #",
    "#     #",
    "#######"]
#Phase 1
def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    num_rows = len(lab)
    num_columns = len(lab[0])

    #print(' ', end="")
    columns = ''.join(str(i) for i in range(num_columns))
    print("", columns)

    for row, char in enumerate(lab):
        print(f'{row}{char}{row}')
    print("", columns)



def replace_at_index(s: str, r: str, idx: int) -> str:
    return s[:idx] + r + s[idx + len(r):]


#Phase 2

def prompt_integer(message: str)->int:
    user_input = input(message)
    while True:
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid number")
            user_input = input(message)


def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer(f"Row of {name}: ")
    column = prompt_integer(f"Column of {name}: ")
    return row, column



# Phase 3

def is_traversable(lab: list[str], location: tuple[int, int])->bool:
    row, column = location
    if 0 <= row < len(lab) and 0 <= column < len(lab[0]) and lab[row][column] == " ":
        return True
    else:
        return False




def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    q = deque()
    q.append([start])
    visited = set()

    while q:
        path = q.popleft()
        #del q[0]
        last = path[-1]

        if last == end:
            return path
        if last not in visited:
            visited.add(last)

            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for move in moves:
                next_move = (last[0] + move[0], last[1] + move[1])
                if is_traversable(lab, next_move) and next_move not in visited:
                    q.append(path + [next_move])

               

start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")
path = bfs(labyrinth, start_location, end_location)

 for row, line in enumerate(labyrinth):
                    for location in path:
                        if location[0] == row and labyrinth[row][location[1]] == " ":
                            labyrinth[row] = replace_at_index(labyrinth[row], "X", location[1])


print(print_labyrinth(labyrinth, path))
print(path)
