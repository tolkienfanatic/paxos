import argparse
from csv import reader

# parses the price file into a map
# first implementation
def parse_file(f_name, price):
    item_map = {}

    with open(f_name, "r") as f:
        price_reader = reader(f)
        for row in price_reader:
            # if the price is equal to or higher than our desired amount, we ignore it
            # assume an item won't have a price of 0
            if int(row[1]) < price:
                item_map[row[0]] = int(row[1])

    return item_map

# parses the price file into a map
# second implementation
def parse_file2(f_name, price):
    item_map = {}
    price_list = []

    with open(f_name, "r") as f:
        price_reader = reader(f)
        for row in price_reader:
            item_price = int(row[1])
            # handle duplicate prices
            if item_price < price:
                # Price is in the map already, append the new item
                if item_price in item_map:
                    item_map[item_price] = item_map[item_price] + [row[0]]
                # This is a new price
                else:
                    item_map[item_price] = [row[0]]
                price_list.append(item_price)

    return item_map, price_list

# find a pair of items that equal the goal amount or are the closest to it
# first implementation - O(n^2), where n = number of items
def find_pair(imap, amt):
    best = 0
    item1, item2 = None, None

    # bad runtime!
    for k, v in imap.iteritems():
        for k2, v2 in imap.iteritems():
            # if we find a new best, we store the relevant information
            if best < v + v2 <= amt and k != k2:
                best = v + v2
                item1, item2 = k, k2

    # we have found no suitable pairs
    if item1 is None and item2 is None:
        print "Not possible"
    # output our best pair
    else:
        print "{} {}, {} {}".format(item1, imap[item1], item2, imap[item2])

# find a pair of items that equal the goal amount or are the closest to it
# second implementation O(n), where n = number of items
def find_pair2(imap, p_lst, amt):
    # first pointer
    p1 = 0
    # second pointer
    p2 = len(p_lst)-1
    best = 0
    num1, num2 = None, None
    # if we have less than two items, we can't possibly have a pair
    if len(p_lst) < 2:
        print "Not possible"

    # Worst case we stop when the pointers meet
    while p1 < p2:
        # We have found two items that exactly match our amount, break out of the loop
        if p_lst[p1] + p_lst[p2] == amt:
            num1, num2 = p_lst[p1], p_lst[p2]
            break
        # We have found two items that sum to more than our price target, we decrement the second pointer
        elif p_lst[p1] + p_lst[p2] > amt:
            # decrement second pointer
            p2 -= 1
        # We have found two items that beat our previous best, we store the new best, as well as the item prices
        # We increment our first pointer to see if we can get closer to the price target
        elif best < p_lst[p1] + p_lst[p2] < amt:
            best = p_lst[p1] + p_lst[p2]
            num1, num2 = p_lst[p1], p_lst[p2]
            # increment our first pointer
            p1 += 1
        # We have found two items that are less than the price target but not better than our previous best
        # Increment the first pointer
        elif best > p_lst[p1] + p_lst[p2] < amt:
            # increment our first pointer
            p1 += 1

    # we have found no suitable pairs
    if num1 is None and num2 is None:
        print "Not possible"

    # output our best pair (the first case is necessary if prices are duplicated)
    elif num1 == num2:
        print "{} {}, {} {}".format(imap[num1][0], num1, imap[num2][1], num2)
    else:
        print "{} {}, {} {}".format(imap[num1][0], num1, imap[num2][0], num2)


def main():
    # parse input
    parser = argparse.ArgumentParser()
    parser.add_argument("price_file", help="Path to text file containing our prices")
    parser.add_argument("price", help="The price we are trying to get close to", type=int)
    args = parser.parse_args()

    price = args.price
    # generate item map
    item_map, price_list = parse_file2(args.price_file, price)
    # find a pair that most closely satisfies target price (if one exists)
    find_pair2(item_map, price_list, price)


if __name__ == "__main__":
    main()