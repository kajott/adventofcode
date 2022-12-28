#if 0
cc -O3 $0 || exit 1
exec ./a.out
#endif

#include <stdbool.h>
#include <stdio.h>
#include <assert.h>

int main(void) {
    const struct dir {
        unsigned short nmask;
        unsigned char  gbit;
        char name;
        int addr_delta;
    } dirs[7] = {
        { 0x444, 0x10, 'N', -256 },
        { 0x111, 0x20, 'S', +256 },
        { 0x700, 0x40, 'W', -1   },
        { 0x007, 0x80, 'E', +1   },
        { 0x444, 0x10, 'N', -256 },  // (copy)
        { 0x111, 0x20, 'S', +256 },  // (copy)
        { 0x700, 0x40, 'W', -1   },  // (copy)
    };

    // central grid; each byte is an OR combination of:
    // - 0x01 = an elf is here
    // - 0x10 = an elf wants to move here in N direction (i.e. coming from S)
    // - 0x20 = an elf wants to move here in S direction (i.e. coming from N)
    // - 0x40 = an elf wants to move here in W direction (i.e. coming from E)
    // - 0x80 = an elf wants to move here in E direction (i.e. coming from W)
    static unsigned char G[256 * 256];
    #define Gxy(x,y) G[(x) + ((y) << 8)]

    int x = 85, y = 85, x0 = 85, y0 = 85, x1 = 85, y1 = 85, ticks = 0, firstdir = 0, elves = 0;
    bool moved;

    // read input file
    FILE *f = fopen("input.txt", "rb");
    assert(f);
    while (!feof(f)) {
        char c = getc(f);
        if (c == 10) {
            x = 85;  ++y;
        } else if (c == '#') {
            Gxy(x,y) |= 1;
            if (x > x1) x1 = x;
            if (y > y1) y1 = y;
            ++elves;
            ++x;
        } else {
            ++x;
        }
    }
    fclose(f);

    do {
        moved = false;

        // first half round: mark target locations in high bits
        for (y = y0;  y <= y1;  ++y) {
            unsigned char* p = &Gxy(x0-2, y);
            unsigned short nmask = 0;
            for (x = x0-2;  x <= x1;  ++x, ++p) {
                nmask = ((nmask & 0x77) << 4) | ((p[1-256] & 1) << 2) | ((p[1] & 1) << 1) | (p[1+256] & 1);
                if (!(p[0] & 1) || (nmask == 0x020)) continue;  // no object here, or no neighbors
                const struct dir* d = &dirs[firstdir];
                for (int subdir = 4;  subdir;  --subdir, ++d) {
                    if (!(nmask & d->nmask)) {
                        p[d->addr_delta] |= d->gbit;
                        break;
                    }
                }
            }
        }

        // second half round: resolve motion, clear high bits, update bounding box
        for (y = y0-1;  y <= (y1+1);  ++y) {
            unsigned char* p = &Gxy(x0-1, y);
            for (x = x0-1;  x <= (x1+1);  ++x, ++p) {
                switch (p[0] & 0xF0) {
                    case 0x10: p[0]  = 1;  p[+256] = 0;  ++moved;  if (y < y0) y0 = y; break;
                    case 0x20: p[0]  = 1;  p[-256] = 0;  ++moved;  if (y > y1) y1 = y; break;
                    case 0x40: p[0]  = 1;  p[+1]   = 0;  ++moved;  if (x < x0) x0 = x; break;
                    case 0x80: p[0]  = 1;  p[-1]   = 0;  ++moved;  if (x > x1) x1 = x; break;
                    default:   p[0] &= 1;  break;
                }
            }
        }
        ++ticks;
        if (ticks == 10) printf("%d\n", (y1-y0+1) * (x1-x0+1) - elves);
        firstdir = (firstdir + 1) & 3;
    } while (moved);
    printf("%d\n", ticks);

    return 0;
}
