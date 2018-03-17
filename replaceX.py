import argparse

# validate our string is well-formed
def validate_input(x_string):
    valid = True

    for c in x_string:
        # see if we run into unexpected input
        if c != "X" and c != "0" and c != "1":
            valid = False

    return valid

# input: Arbitrary length string
# output: Prints every permutation of the string
#   where "X" is replaced with "1" and "0"
def replace_x(x_string):
    # partition the string at first incidence of "X"
    p = x_string.partition("X")

    # base case: X is not in the string, print it
    if p[1] == "" and p[2] == "":
        print x_string

    # recursive case: replace X with 1 and 0, call the
    #   function on the new strings
    else:
        replace_x(p[0] + "1" + p[2])
        replace_x(p[0] + "0" + p[2])


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("x_string", help="An input string containing X's, 0's and 1's")
    args = parser.parse_args()

    # call our replace function on the passed argument
    if validate_input(args.x_string):
        replace_x(args.x_string)
    else:
        print "Input string is invalid"


if __name__ == "__main__":
    main()