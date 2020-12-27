import sys
import os
COUNT = -1

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("Not a file")
        sys.exit()
    bags = parse_file(filepath)
    # print(bags)
    # for key, val in bags.items():
        # print(key + " contains " + str(val))
    bags_containing_color = []
    # go_through_bags(bags, "shiny gold", bags_containing_color)
    problem_2(bags, "shiny gold")
    print(COUNT)
    # print(problem_2(bags, "shiny gold", 0))
    # print(len(bags_containing_color))

    # print(check_questions(data))
    return

def parse_file(filepath):
    return_dict = {}
    with open(filepath) as f:
        for line in f:
            key_val = line.split(" bags contain ")
            key = key_val[0]
            if key_val[1] == "no other bags." or key_val[1] == "no other bags.\n":
                val = []
            elif key_val[1].find(", ") == -1:
                if key_val[1].find("bags.") == -1:
                    val = [key_val[1][2:-6]]
                else:
                    val = [key_val[1][2:-7]]
                    val = int(key_val[1][0]) *val
            else:
                vals = key_val[1].split(", ")
                val = []
                for i in vals:
                    bag_parsed = i.split(" ")
                    j = 0
                    while j < int(bag_parsed[0]):
                        val.append(bag_parsed[1] + " " + bag_parsed[2])
                        j += 1
                # print(val)
            return_dict[key] = val
    return return_dict

def go_through_bags(bag_dict, color, bags_containing_color):
    for key, val in bag_dict.items():
        if color in val:
            # print(color)
            if key not in bags_containing_color:
                # print(key)
                bags_containing_color.append(key)
                go_through_bags(bag_dict, key, bags_containing_color)
    return

def problem_2(bag_dict, color):
    # print(bag_dict)
    global COUNT
    list_bags = bag_dict[color]
    COUNT += 1
    # print(color)
    # print(count)
    for bag in list_bags:
        problem_2(bag_dict, bag)

                

    





if __name__ == "__main__":
    main()