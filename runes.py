#! /usr/bin/env python3

"""
Show the codepoint, name and UTF-8 bytes
of each unicode character in command line arguments or standard input.
"""

import argparse
import sys
import unicodedata


NO_NAME = '(none)'


def describe(ch):
    return '{0!r} U+{1:04X}  {2}  [{3}]'.format(ch, ord(ch),
            unicodedata.name(ch, NO_NAME),
            ' '.join('{:02x}'.format(b) for b in ch.encode('utf-8')))


def gen_chars_from_str_list(str_list):
    for string in str_list:
        for char in string:
            yield char


def gen_chars_from_text_io(text_io):
    while True:
        char = text_io.read(1)
        if not char:
            return
        yield char


def main():
    if len(sys.argv) > 1:
        gen = gen_chars_from_str_list(sys.argv[1:])
    else:
        gen = gen_chars_from_text_io(sys.stdin)

    for char in gen:
        print(describe(char))


if __name__ == '__main__':
    main()
