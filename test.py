
from collections import deque

def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    q = deque()
    q.append([start])
    visited = set()

    while q:
        path = q.popleft()
        last = path[-1]

        if last == end:
            return path

        if last not in visited:
            visited.add(last)

            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for move in moves:
                next_move = (last[0] + move[0], last[1] + move[1])

                if is_traversable(lab, next_move) and next_move not in visited:
                    new_path = path + [next_move]
                    q.append(new_path)

    return []  # If no path is found

def is_traversable(lab, location):
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[0]):
        return lab[row][col] == ' '

def replace_at_index(s, new_char, index):
    return s[:index] + new_char + s[index + 1:]

# Example usage:
labyrinth = [
    "    0 0 0      ",
    "0   1 1 1 0 0 0",
    "     0 0 0   0 ",
    "0     1 1 1 0 0",
    "   0 0 0 0 0   "
]

start_location = (0, 0)
end_location = (4, 3)

path = bfs(labyrinth, start_location, end_location)

if path:
    print("Path found:", path)

    # Mark the path in the labyrinth with "X"
    for location in path:
        row, col = location
        if labyrinth[row][col] == " ":
            labyrinth[row] = replace_at_index(labyrinth[row], "X", col)

    for line in labyrinth:
        print(line)
else:
    print("No path found.")









lab = ["#######", "#     #", "#   ###", "# ### #", "#     #", "#######"]

def print_labyrinth(lab: list[str]):
    num_rows = len(lab)
    num_col = len(lab[0])




print(print_labyrinth(lab))

def print_labyrinth(lab: list[str]):
    if not lab:
        print("The labyrinth is empty.")
        return

    num_rows = len(lab)
    num_cols = len(lab[0]) if lab else 0

lab= [
    "#######",
    "#     #",
    "#   ###",
    "# ### #",
    "#     #",
    "#######"]

def print_labyrinth(lab: list[str]):
    num_rows = len(lab)
    num_columns = len(lab[0])

    print(' ', end="")
    columns = ''.join(str(i) for i in range(num_columns))
    print(f'{columns}')
    #for e in range(num_columns):
        #columns += str(e)
        #print("", columns)

    for row, char in enumerate(lab):
        print(f'{row}{char}{row}')
    print("", columns)

    #for row in lab:
        #print(row)