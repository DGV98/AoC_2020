import sys
import os

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("%s is not a file", filepath)
        sys.exit()
    tickets = parse_file(filepath)
    solve(tickets)
    # print(binary_search(0, 127, "BFFFBBF"))
    return None

def find_max(tickets):
    max_seat_id = 0
    for seat in tickets:
        row = binary_search(0, 127, seat[0])
        col = binary_search(0, 7, seat[1])
        seat_id = row * 8 + col
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def parse_file(filepath):
    with open(filepath) as f:
        data = f.read().splitlines()
    # list_tuple_input = []
    # for i in data:
    #     position = (i[:7], i[7:])
    #     list_tuple_input.append(position)
    return data

def find_seat(tickets):
    list_seats = []
    for seat in tickets:
        row = binary_search(0, 127, seat[0])
        col = binary_search(0, 7, seat[1])
        seat_id = row * 8 + col
        list_seats.append(seat_id)
    list_seats.sort()
    for i in sorted(list_seats):
        if i+1 not in list_seats and i +2 in list_seats:
            print(i)
    return None
        

def solve(tickets):
    seats = []

    for ticket in tickets:
        seats.append(
            int(ticket.replace("F", "0")
                      .replace("B", "1")
                      .replace("L", "0")
                      .replace("R", "1"), 2)
        )

    print("Part 1", max(seats))

    mine = None
    for sid in range(127 * 8):
        if (sid - 1 in seats) and \
           (sid not in seats) and \
           (sid + 1 in seats):
            mine = sid

    print("Part 2", mine)

def binary_search(low, high, input):

    # Check base case
    if high >= low:

        mid = (high + low) // 2
        if high == low:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif input[0] == "F" or input[0] == "L":
            return binary_search(low, mid - 1, input[1:])

        # Else the element can only be present in right subarray
        else:
            return binary_search(mid + 1, high, input[1:])

    else:
        # Element is not present in the array
        return -1

if __name__ == "__main__":
    main()
