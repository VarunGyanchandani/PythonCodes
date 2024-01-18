def reverse_string_loop(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


string = input("Enter the string to be reversed: ")
print(reverse_string_loop(string))