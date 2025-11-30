#if 0  // self-compiling code
gcc -std=c99 -Wall -Wextra -pedantic -Werror -g -O4 -march=native $0 || exit 1
exec ./a.out
#endif

// warning: no error checking and memory cleaning here.

#define MAX_MOLECULE_SIZE 512
#define MAX_REACTIONS 64

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>


struct reaction {
    char from[8];
    char to[16];
    int from_len, to_len;
} reactions[MAX_REACTIONS];


int compare_reactions(const void* _a, const void* _b) {
    const struct reaction *a = _a;
    const struct reaction *b = _b;
    int res = (b->to_len - b->from_len) - (a->to_len - a->from_len);
    if (res) { return res; }
    res = b->to_len - a->to_len;
    if (res) { return res; }
    res = strcmp(a->from, b->from);
    if (res) { return res; }
    return strcmp(a->to, b->to);
}


int reduce_molecule(const char* molecule, int depth) {
    // printf("[%d] %s\n", depth, molecule);  // debug output
    if (!strcmp(molecule, "e")) {  // Heureka!
        printf("Solution found at depth %d.\n\nReactions:\n[0] %s\n", depth, molecule);
        return depth;
    }
    char buffer[MAX_MOLECULE_SIZE];
    for (struct reaction *r = reactions;  r->from_len;  ++r) {
        const char *pos = molecule;
        while ((pos = strstr(pos, r->to))) {
            int i_pos = (int) (pos - molecule);
            memcpy(buffer, molecule, i_pos);
            strcpy(&buffer[i_pos], r->from);
            strcpy(&buffer[i_pos + r->from_len], &molecule[i_pos + r->to_len]);
            int res = reduce_molecule(buffer, depth + 1);
            if (res) {
                printf("using %s => %s\n[%d] %s\n", r->from, r->to, res - depth, molecule);
                return res;
            }
            pos++;
        }
    }
    return 0;
}


int main(void) {
    char molecule[MAX_MOLECULE_SIZE] = "";

    // load input
    FILE *f = fopen("input.txt", "r");
    assert(f);
    static char line[MAX_MOLECULE_SIZE];
    struct reaction *r = reactions;
    while (fgets(line, MAX_MOLECULE_SIZE, f)) {
        // strip trailing whitespace
        char *pos = &line[strlen(line)];
        while ((pos != line) && isspace(pos[-1])) { *(--pos) = '\0'; }
        if (!*line) {
            continue;  // empty line
        }
        
        // split into "from => to" parts
        char *sep = strstr(line, " => ");
        if (sep) {
            *sep = '\0';
            assert(r != &reactions[MAX_REACTIONS]);
            strcpy(r->from, line);
            strcpy(r->to, sep + 4);
            r->from_len = strlen(r->from);
            r->to_len = strlen(r->to);
            ++r;
        }
        else {
            // no reaction -> this is likely the molecule name!
            strcpy(molecule, line);
        }
    }
    fclose(f);

    // sort reactions so that those with maximum length savings come first
    qsort(reactions, r - reactions, sizeof(struct reaction), compare_reactions);

    // dump input again (to see that it has been correctly loaded)
    printf("Possible reactions (sorted):\n");
    for (struct reaction *r = reactions;  r->from_len;  ++r) {
        printf("  - %s => %s\n", r->from, r->to);
    }

    printf("\nSearching for molecule: %s\n\n", molecule);
    return !reduce_molecule(molecule, 0);
}
