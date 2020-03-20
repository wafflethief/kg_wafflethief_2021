import sys
from testMapping import isOneToOne
def main():
    x = isOneToOne(sys.argv[1], sys.argv[2])
    if x is True:
        print("true")
    if x is False:
        print("false")

main()
