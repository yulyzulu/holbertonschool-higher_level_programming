#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numlen = len(sys.argv)
    if numlen == 1:
        print("{:d} arguments.".format(numlen - 1))
    elif numlen == 2:
        print("{:d} argument:".format(numlen - 1))
        print("{:d}: ".format(numlen - 1), sys.argv[1])
    else:
        print("{:d} arguments:".format(numlen - 1))
        for i in range(numlen):
            if i != 0:
                print("{:d}: ".format(i), sys.argv[i])
