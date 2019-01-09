#if 0
cc -Wall -Wno-unused-result -g -O9 -march=native $0 || exit 1
exec ./a.out $*
#endif

#define EXTRA_OBJECTS 4
#include "aoc2016_11_part1.c"
