# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pych
myList = [1, 4, 12, 3, 8, 7, 3, 4]
total=0
for number in myList :
    if number % 3==0:
        total+=number

print(total)

alist = [10, 20, 30]
total=0
for item in range(len(alist)):
    total = total + 1

print (total)