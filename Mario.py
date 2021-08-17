# This code is used for solving the Mario more problem which is like that if the input is 3
  #  #
 ##  ##
###  ###


import cs50

i = 0
while i < 1 or i > 8:
    Height = cs50.get_int("Height: ")
    i = Height    
# this is the first pyramid
for A in range(1, Height + 1):
    # i is for the blocks
    i = (A % Height)
    # j is for the spaces
    j = (Height-(A % Height))
    if i == 0:
        i = Height
    if j == Height:
        j = 0
    print(" " * j, end="")
    print("#" * i, end="  ")
    print("#" * i, end="")
    print('\n', end="")
