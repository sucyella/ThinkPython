# Exercise 3-1 -- right_justify()
# Write a function named right_justify that takes a string names s as a parameter
# and prints the string with enough leading spaces
# so that the last letter of the string is in column 70 of the display


def right_justify(s):
    blank = " "
    name = s
    word = len(s)
    space = 70 - word
    print((blank * space), name)


# Exercise 3-2 -- do_twice()
# Modify do twice so that it takes two arguments, a function object and a value
# and calls the function twice, passing the value as an argument


def print_word(word):
    print(word)


def do_twice(function, value):
    for line in range(2):
        function(value)


do_twice(print_word, 'breakfast')

# Exercise 3-2.3 -- print_twice()
# copy the definition of print_twice()
# from earlier in this chapter


def print_twice(word):
    print(word)
    print(word)


# Exercise 3-2.4 -- do_twice_2()
# use the modified version of do_twice_2() to call print_twice()
# passing 'spam' as an argument


def do_twice_2(word):
    for line in range(2):
        print_twice(word)


do_twice_2('spam')


# Exercise 3-2.5 -- do_four()
# takes a function object and a value
# and calls the function four times, passing the value as a parameter
# there should be only two statements in the body of the function


def do_four(function, value):
    for line in range(4):
        function(value)


do_four(print_word, 'coffee')


# Exercise 3-3.1 -- grid()
# write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


def grid(corner, column, row):
    """
    corner: enter a corner character, e.g. +
    column: enter a column character, e.g. -
    row: enter a row character, e.g. |
    """
    cr_ch = corner
    co_ch = column
    ro_ch = row
    sp = ' '
    # print(cr_ch, (co_ch + sp) * 4, end='')
    # print(cr_ch, (co_ch + sp) * 4)
    # print(ro_ch + (sp * 9), end='')
    # print(ro_ch + (sp * 9))
    top = cr_ch + sp + (co_ch + sp) * 4
    top_two = top + cr_ch
    mid = ro_ch + (sp * 9) + ro_ch
    mid_two = (sp * 9) + ro_ch

    # print(top + top_two)
    # print(mid + mid_two)

    for cr in range(2):
        print(top + top_two)
        for ro in range(4):
            print(mid + mid_two)
    print(top + top_two)


grid('+', '-', '|')


# Exercise 3-3.2 -- grid_four()
# a function that draws a similar grid with four rows and four columns


def grid_four(corner, column, row):
    """
    corner: enter a corner character, e.g. +
    column: enter a column character, e.g. -
    row: enter a row character, e.g. |
    """
    cr_ch = corner
    co_ch = column
    ro_ch = row
    sp = ' '
    top = cr_ch + sp + ((co_ch + sp) * 4)
    col = ro_ch + (sp * 9)
    for co in range(4):
        print(top * 3 + cr_ch)
        for ro in range(4):
            print(col * 3 + ro_ch)
    print(top * 3 + cr_ch)


grid_four('+', '-', '|')
