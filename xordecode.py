#!/usr/bin/env python

import sys
import os
import argparse

def xor_decrypt(data, key):
    result = bytearray()
    for i, byte in enumerate(data):
        result.append(byte ^ key)
    return bytes(result)

def ArgParse():
    parser = argparse.ArgumentParser(description=
    '''This script is XOR decrypter. Supports input from file or standard input.''',
    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), metavar='FILE', help='Original File (omit to read from standard input)', default=sys.stdin)
    parser.add_argument('-k', '--key', action='store', type=str, metavar='KEY', help='KEY (hexadecimal)')
    args = parser.parse_args()
    return args

def xorbf(data):
    for i in range(0,256):
        print("=== "+hex(i)+" ===")
        try:
            result = xor_decrypt(data, i)
            print(result.decode('latin-1', errors='ignore'))
        except:
            print("Error decrypting with key", hex(i))

def xorkey(data, key):
    try:
        result = xor_decrypt(data, int(key, 16))
        print(result.decode('latin-1', errors='ignore'))
    except:
        print("Error decrypting with key", key)

def main():
    args = ArgParse()
    
    # 標準入力またはファイルからデータを読み込み
    if args.infile == sys.stdin:
        # 標準入力の場合、バイナリデータとして読み込み
        try:
            data = sys.stdin.buffer.read()
        except AttributeError:
            # Python 2互換性のため
            data = sys.stdin.read()
    else:
        # ファイルの場合
        data = args.infile.read()
        if isinstance(data, str):
            data = data.encode('latin-1')
    
    if args.key == None:
        xorbf(data)
    else:
        xorkey(data, args.key)

if __name__ == "__main__":
    main()

