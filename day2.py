import sys
import os 
import re

def main():
    filepath = sys.argv[1]
    count_valid = 0
    if not os.path.isfile(filepath):
        print("File %s is not correct", filepath)
        sys.exit()
    data = open(filepath, "r")
    for line in data:
        count_letter = 0
        entry = line.split(" ")
        indeces = entry[0].split("-")
        # print(bounds)
        a = int(indeces[0]) -1
        b = int(indeces[1]) -1
        passcode = entry[1].strip(":")
        # print(passcode)
        password = entry[2].strip("\n")
        if passcode == password[a]:
            count_letter += 1
        if passcode == password[b]:
            count_letter += 1
        if count_letter == 1:
            count_valid += 1
    print(count_valid)
    return None

if __name__ == "__main__":
    main()