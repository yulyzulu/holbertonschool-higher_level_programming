#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    numlen = len(sys.argv)
    for i in range(1, numlen):
        num = int(sys.argv[i])
        add = add + num
    print("{:d}".format(add))
