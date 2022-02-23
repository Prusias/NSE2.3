import sys
from options import ScanOptions
from run import *

def main():

    options = ScanOptions()
    options.fill_from_arguments(sys.argv)
    run(options)

if __name__ == "__main__":
    main()


