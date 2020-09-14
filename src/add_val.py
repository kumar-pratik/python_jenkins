import sys
from src.tools import sum

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("############")
    print("The result is " + str(sum(str(sys.argv[1]), str(sys.argv[2]))))
    print("############")
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("############")
    print("On 2 arguments allowed!")
    print("############")
    sys.exit(1)