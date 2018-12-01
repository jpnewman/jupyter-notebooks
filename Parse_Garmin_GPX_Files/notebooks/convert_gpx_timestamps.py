#!/usr/bin/env python3

"""Convert GPX Timestamps."""

import os
import re
import argparse

from glob import glob

# NOTE: etree and lxml don't work well with namespaces.


def parse_args():
    """Parse Args."""
    parser = argparse.ArgumentParser(description='Converts GPX Timestamps')
    parser.add_argument('input_path',
                        help='Input file path')
    parser.add_argument('--output_filetitle_suffix',
                        default='TimeFormatted',
                        help='Output file')
    args = parser.parse_args()

    return args


def patch_time(string):
    """Patch Time."""
    time_pattern = re.compile(
        r"<time>(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}).*?</time>")
    return time_pattern.sub(r"<time>\1Z</time>", string)


def process_file(input_file_path, output_filetitle_suffix):
    """Process File."""
    with open(input_file_path, 'r') as input_file:
        lines = []
        for line in input_file.readlines():
            lines += patch_time(line)

    root, ext =os.path.splitext(input_file_path)
    output_file_path = root + "_" + output_filetitle_suffix + ext
    print(output_file_path)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(''.join(lines))


def main():
    """Main."""
    args = parse_args()

    files = glob(args.input_path, recursive=True)
    files_filtered = [f for f in files if args.output_filetitle_suffix not in f]
    # print(files_filtered)

    for file in files_filtered:
        process_file(file, args.output_filetitle_suffix)


if __name__ == "__main__":
    main()
