import sys
import argparse
from csv import reader

# parses the price file into a map
def parse_file(f_name, price):
    item_map = {}

    with open(f_name, "r") as f:
        price_reader = reader(f)
        for row in price_reader:
            # if the price is equal to or higher than our desired amount, we ignore it
            if int(row[1]) < price:
                item_map[row[0]] = int(row[1])

    return item_map


def find_pair(imap, amt):
    best = 0
    item1, item2 = None, None

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

def main():
    # parse input
    parser = argparse.ArgumentParser()
    parser.add_argument("price_file", help="Path to text file containing our prices")
    parser.add_argument("price", help="The price we are trying to get close to", type=int)
    args = parser.parse_args()

    price = args.price
    # generate item map
    item_map = parse_file(args.price_file, price)
    # find a pair that most closely satisfies target price (if one exists)
    find_pair(item_map, price)


if __name__ == "__main__":
    main()