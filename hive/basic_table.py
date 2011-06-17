#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse

def parse_option():
    p = optparse.OptionParser(usage="basic_table_py [-n|--number-of-rows=NUM]")
    p.add_option("-n", "--number-of-rows",help="the number of rows you want to generate. 10 by default")
    (opts, _) = p.parse_args()
    return opts

def main():
    options = parse_option()

    number_of_rows = 10;
    if options.number_of_rows:
        number_of_rows = int(options.number_of_rows)

    for i in xrange(number_of_rows):
        print "%d%sstr%d" % (i, chr(1), i)

if __name__ == '__main__':
    main()
