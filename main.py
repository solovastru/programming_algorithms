# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
var_boolean = False
print(type(var_boolean))
var_boolean = False + True + True + False + False
print(var_boolean)

print(type(var_boolean))

file = open("var_boolean.txt", "w")
file.write("Hello Pycharm")
file.close()
print(type(file))

file = open("var_boolean.txt", "r")
print(file.read())



labyrinth = [
    219, 219, 219, 219, 219, 219, 219, 10,
    219, 32, 32, 32, 32, 32, 219, 10,
    219, 32, 32, 32, 219, 219, 219, 10,
    219, 32, 219, 219, 219, 32, 219, 10,
    219, 32, 32, 32, 32, 32, 219, 10,
    219, 219, 219, 219, 219, 219, 219, 10
]

my_string = ["Hello,",
             "World!"]
nr_string = len(my_string[0])
#nr_string_new = list(nr_string)
print(nr_string)

#for i in nr_string_new:
    #i = i + 1
    #print({i}, end="")

def print_labyrinth(lab: list[str]):
    # Calculate the number of rows and columns
    num_rows = len(lab)
    num_cols = len(lab[0]) if lab else 0  # Assuming all rows have the same length

    # Print information about the labyrinth's dimensions
    print(f"Labyrinth Size: {num_rows} rows x {num_cols} columns")

    # Print the top boundary of the labyrinth
    print('+' + '-' * num_cols + '+')

    # Print the labyrinth's content with additional information as needed

    # Print the bottom boundary of the labyrinth
    print('+' + '-' * num_cols + '+')


# Example usage:
labyrinth = [
    "##########",
    "#        #",
    "#  S  E  #",
    "#        #",
    "##########"
]

print_labyrinth(labyrinth)



print(len(my_string))
print(len(my_string[1]))

for index, character in enumerate(my_string):
    print(f"Index {index}: {character}")

text = "Hello"
for i in range(len(text)):
    print(f"{i}", end="")
    print(f"{text[i]}", end="")