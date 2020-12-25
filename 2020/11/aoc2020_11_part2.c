#if 0
gcc -std=c99 -Wall -Wextra -pedantic -Werror -O2 $0 || exit 1
exec ./a.out
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 128

struct seats {
    char s[MAXSIZE][MAXSIZE];
} p0, p1, *curr = &p0, *next = &p1;


char look(int x, int y, int dx, int dy) {
    char c;
    do {
        x += dx;
        y += dy;
        c = curr->s[y][x];
    } while (c == '.');
    return (c == '#');
}


int main(void) {
    curr->s[1][1] = 'X';

    FILE *f = fopen("input.txt", "r");
    if (!f) { return 1; }
    for (int y = 1;  !feof(f);  ++y) {
        if (!fgets(&next->s[y][1], MAXSIZE, f)) { break; }
    }
    fclose(f);

    do {
        struct seats *swaptmp = curr;
        curr = next;
        next = swaptmp;
    
        #if 0  // dump maze
            for (int y = 1;  y < MAXSIZE;  ++y) {
                int x;
                for (x = 0;  x < MAXSIZE;  ++x) {
                    if (curr->s[y][x+1] < 0x20) { break; }
                }
                if (!x) { break; }
                fwrite(&curr->s[y][1], 1, x, stdout);
                putchar('\n');
            }
            putchar('\n');
        #endif

        for (int y = 1;  y < MAXSIZE-1;  ++y) {
            for (int x = 1;  x < MAXSIZE-1;  ++x) {
                char c = curr->s[y][x];
                char n = (c < 0x20) ? 0 : (0
                       + look(x, y, -1, -1)
                       + look(x, y, -1,  0)
                       + look(x, y, -1, +1)
                       + look(x, y,  0, -1)
                       + look(x, y,  0, +1)
                       + look(x, y, +1, -1)
                       + look(x, y, +1,  0)
                       + look(x, y, +1, +1));
                next->s[y][x] = ((c == 'L') && (n == 0)) ? '#'
                              : ((c == '#') && (n >= 5)) ? 'L'
                              : c;
            }
        }
    } while (memcmp(&curr->s[0][0], &next->s[0][0], MAXSIZE * MAXSIZE));

    int count = 0;
    for (int y = 0;  y < MAXSIZE;  ++y) {
        for (int x = 0;  x < MAXSIZE;  ++x) {
            count += (curr->s[y][x] == '#');
        }
    }
    printf("%d\n", count);

    return 0;
}
