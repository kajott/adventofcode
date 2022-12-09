# 2022, Day 7: No Space Left On Device

You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

    $ system-update --please --pretty-please-with-sugar-on-top
    Error: No space left on device
    

Perhaps you can delete some files to make space for the update?

## Part 1

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
    

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called `/`. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with `$` are _commands you executed_, very much like some modern computers:

*   `cd` means _change directory_. This changes which directory is the current directory, but the specific result depends on the argument:
    *   `cd x` moves _in_ one level: it looks in the current directory for the directory named `x` and makes it the current directory.
    *   `cd ..` moves _out_ one level: it finds the directory that contains the current directory, then makes that directory the current directory.
    *   `cd /` switches the current directory to the outermost directory, `/`.
*   `ls` means _list_. It prints out all of the files and directories immediately contained by the current directory:
    *   `123 abc` means that the current directory contains a file named `abc` with size `123`.
    *   `dir xyz` means that the current directory contains a directory named `xyz`.

Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

    - / (dir)
      - a (dir)
        - e (dir)
          - i (file, size=584)
        - f (file, size=29116)
        - g (file, size=2557)
        - h.lst (file, size=62596)
      - b.txt (file, size=14848514)
      - c.dat (file, size=8504156)
      - d (dir)
        - j (file, size=4060174)
        - d.log (file, size=8033020)
        - d.ext (file, size=5626152)
        - k (file, size=7214296)
    

Here, there are four directories: `/` (the outermost directory), `a` and `d` (which are in `/`), and `e` (which is in `a`). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the _total size_ of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

*   The total size of directory `e` is _584_ because it contains a single file `i` of size 584 and no other directories.
*   The directory `a` has total size _94853_ because it contains files `f` (size 29116), `g` (size 2557), and `h.lst` (size 62596), plus file `i` indirectly (`a` contains `e` which contains `i`).
*   Directory `d` has total size _24933642_.
*   As the outermost directory, `/` contains every file. Its total size is _48381165_, the sum of the size of every file.

To begin, find all of the directories with a total size of _at most 100000_, then calculate the sum of their total sizes. In the example above, these directories are `a` and `e`; the sum of their total sizes is _`95437`_ (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. _What is the sum of the total sizes of those directories?_

Your puzzle answer was `1077191`.

## Part 2

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is _`70000000`_. To run the update, you need unused space of at least _`30000000`_. You need to find a directory you can delete that will _free up enough space_ to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is `48381165`; this means that the size of the _unused_ space must currently be `21618835`, which isn't quite the `30000000` required by the update. Therefore, the update still requires a directory with total size of at least `8381165` to be deleted before it can run.

To achieve this, you have the following options:

*   Delete directory `e`, which would increase unused space by `584`.
*   Delete directory `a`, which would increase unused space by `94853`.
*   Delete directory `d`, which would increase unused space by `24933642`.
*   Delete directory `/`, which would increase unused space by `48381165`.

Directories `e` and `a` are both too small; deleting them would not free up enough space. However, directories `d` and `/` are both big enough! Between these, choose the _smallest_: `d`, increasing unused space by _`24933642`_.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. _What is the total size of that directory?_

Your puzzle answer was `5649896`.

## Solution Notes

This task is not a complicated one at all, but the devil's in the details and there are various ways to introduce subtle bugs.

What definitely helps is that the input is constructed in a non-malicious way; specifically, there's exactly one `cd /` at the beginning of the file (which means that it can be ignored completely, and `ls` is called exactly *once* for each directory. This means that a separate data structure that keeps track of "visited" directories is not necessary; we can just add all file sizes we encounter to their parent directories right during parsing.

I combined the solutions for both parts into a single file, because only the final `print` statement would be different between the individual parts' solutions.

* Parts 1+2, Python: 261 bytes, <100 ms
