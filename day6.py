import sys
import os

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("Not a file")
        sys.exit()
    data = parse_file(filepath)
    print(check_questions(data))
    return

def parse_file(filepath):
    with open(filepath) as f:
        data = f.read()
    data = data.split("\n\n")
    new_data = []
    for i in data:
        new_data.append(i.split("\n"))
    # print(new_data)
    return new_data

def check_questions(data):
    sum_q = 0
    for i in data:
        dict_q = {}
        for q in i:
            for s in q:
                if s not in dict_q:
                    dict_q[s] = 1
                else:
                    dict_q[s] += 1
        for key,val in dict_q.items():
            if val == len(i):
                sum_q += 1
    return sum_q


if __name__ == "__main__":
    main()