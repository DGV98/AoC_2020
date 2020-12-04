import sys
import os

list_slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File %s is not correct", filepath)
        sys.exit()
    tree_map = data_to_matrix(filepath)
    # print(tree_map)
    product = 1
    for slope in list_slopes:
        tree_count = count_trees(slope, tree_map)
        product *= tree_count
    print(product)
    return None
    
def count_trees(slope, tree_map):
    position = {"posX": 0, "posY": 0}
    tree_count = 0
    x = slope[0]
    y = slope[1]
    length_pattern = len(tree_map[0])
    while position["posY"] < len(tree_map):
        coord = (position["posX"], position["posY"])
        if tree_map[coord[1]][coord[0]] == "#":
            tree_count += 1
        if position["posX"] + x >= length_pattern:
            position["posX"] = position["posX"] + x - length_pattern
        else:
            position["posX"] += x
        position["posY"] += y
    return tree_count

def data_to_matrix(filepath):
    matrix = []
    with open(filepath) as f:
        data = f.readlines()
    for i in data:
        inner_list = [char for char in i]
        if inner_list[-1] == "\n":
            inner_list.pop(-1)
        matrix.append(inner_list)
    return matrix
    
if __name__ == "__main__":
    main()