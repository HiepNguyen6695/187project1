import argparse


def main():
        parser = argparse.ArgumentParser(description="Validates if some integers form a triangle")
        parser.add_argument('integers', metavar='Integers', type=int, nargs=3,
                            help='integers to form a triangle')
        arguments = parser.parse_args()
        #  if x <= 0 || y <= 0 || z <=0 error out and say why
        if (arguments.integers[0] <= 0 or arguments.integers[1] <= 0 or arguments.integers[2] <=0):
            raise ValueError("ERROR: Arguments must be > 0")
        #  else if (x > (y + z) || y > (x + z) || z > (x + y)) error out and say why
        elif (arguments.integers[0] > (arguments.integers[1] + arguments.integers[2]) or
            arguments.integers[1] > (arguments.integers[0] + arguments.integers[2]) or
            arguments.integers[2] > (arguments.integers[0] + arguments.integers[1])):
            raise ValueError("ERROR: Sum of any two sides must be larger than the remaining side")
        #  if(x == y && y == z) - Equilateral
        if arguments.integers[0] == arguments.integers[1] and arguments.integers[1] == arguments.integers[2]:
            print "This is an Equilateral Triangle"
        #  else if(x == y || x == z || y == z) { - this is an Isosceles Triangle
        elif (arguments.integers[0] == arguments.integers[1] or arguments.integers[0] == arguments.integers[2] or
              arguments.integers[1] == arguments.integers[2]):
            print "This is an Isosceles Triangle"
        #  else - must be a Scalene triangle
        else:
            print "This is a Scalene Triangle"



if __name__ == "__main__":
    main()