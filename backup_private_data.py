#!/usr/bin/env python3
"""
Generate an archive with private data (TASK files, inputs) of the entire
AoC directory structure.
"""
import argparse
import glob
import os
import sys
import zipfile

DefaultFileName = "aoc_private.zip"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile", metavar="ZIPFILE",
                        help="output file (default: " + DefaultFileName + " in base directory)")
    args = parser.parse_args()

    basedir = os.path.normpath(os.path.abspath(os.path.dirname(sys.argv[0])))
    outfile = os.path.normpath(os.path.abspath(args.outfile)) \
              if args.outfile else os.path.join(basedir, DefaultFileName)

    files = glob.glob("20*/*/TASK.md") + glob.glob("20*/*/input.txt")
    if not files:
        print("No files to backup, aborting.")
        sys.exit(1)

    print("output file:", outfile)
    try:
        z = zipfile.ZipFile(outfile, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
    except EnvironmentError as e:
        print("Can't create output file -", e)
        sys.exit(1)

    nfiles = 0
    usize = 0
    try:
        for f in sorted(files):
            print(f, end='\x1b[K\r')
            sys.stdout.flush()
            try:
                sz = os.path.getsize(f)
                z.write(f)
            except EnvironmentError as e:
                print(f, "- FAILED:", e)
            nfiles += 1
            usize += sz
    finally:
        z.close()

    csize = os.path.getsize(outfile)
    print(f"\x1b[K{nfiles} files, {usize/1e6:.1f} MB uncompressed, {csize/1e6:.1f} MB compressed")
