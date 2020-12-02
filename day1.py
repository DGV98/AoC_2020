import sys
import os 

def main():
    filepath = sys.argv[1]
    nums_list = []
    if not os.path.isfile(filepath):
        print("File %s is not correct", filepath)
        sys.exit()
    
    with open(filepath) as f:
        data = f.readlines()
    for i in data:
        nums_list.append(int(i.strip()))
    for i, num in enumerate(nums_list):
        k = i+1
        while k < len(nums_list):
            j = k+1
            num2 = nums_list[k]
            while j < len(nums_list):
                num3 = nums_list[j]
                if num + num2 + num3 == 2020:
                    print(num *num2*num3)
                    return None
                j += 1
            k +=1
    return None

if __name__ == "__main__":
    main()