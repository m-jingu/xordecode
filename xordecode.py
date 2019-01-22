#!/usr/bin/env python

import sys
import os
import argparse
from Crypto.Cipher import XOR

version = '%(prog)s 20160824'

def ArgParse():
    parser = argparse.ArgumentParser(description=
    '''This script is XOR decrypter.  ''',
    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), metavar='FILE', help='Original File', default=sys.stdin)
    parser.add_argument('-k', '--key', action='store', type=str, metavar='KEY', help='KEY')
    parser.add_argument('-v', '--version', action='version', version=version)
    args = parser.parse_args()
    return args

def xorbf(orgstr):
    for i in range(0,256):
        print("=== "+hex(i)+" ===")
        print(XOR.new(chr(i)).decrypt(orgstr))

def xorkey(orgstr, key):
    print(XOR.new(chr(int(key,16))).decrypt(orgstr))

if __name__ == "__main__":
    args = ArgParse()
    if args.key == None:
        xorbf(args.infile.read().rstrip())
    else:
        xorkey(args.infile.read().rstrip(), args.key)

