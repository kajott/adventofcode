#if 0
c++ -std=c++11 -Wall -Wextra -pedantic -Werror -O3 $0 || exit 1
exec ./a.out
#endif

#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>

#include <vector>
#include <functional>
#include <unordered_map>
#include <algorithm>

struct Blueprint {
    uint8_t requirements[4][4];
    uint8_t maxRobots[4];
    int id;
    explicit Blueprint(const uint8_t *nums, int numCount) {
        assert(numCount == 7);
        for (int i = 0;  i < 4;  ++i)
            for (int j = 0;  j < 4;  ++j)
                requirements[i][j] = 0;
        id = nums[0];
        requirements[0][0] = nums[1];
        requirements[1][0] = nums[2];
        requirements[2][0] = nums[3];
        requirements[2][1] = nums[4];
        requirements[3][0] = nums[5];
        requirements[3][2] = nums[6];
        for (int i = 0;  i < 3;  ++i) {
            maxRobots[i] = requirements[0][i];
            for (int j = 1;  j < 4;  ++j)
                maxRobots[i] = std::max(maxRobots[i], requirements[j][i]);
        }
        maxRobots[3] = 99;
    }
    void dump() const {
        printf("BP #%d:", id);
        for (int i = 0;  i < 4;  ++i) {
            for (int j = 0;  j < 4;  ++j) printf(" %d", requirements[i][j]);
            printf(" |");
        }
        for (int j = 0;  j < 4;  ++j) printf(" %d", maxRobots[j]);
        printf("\n");
    }
};


struct State {
    uint32_t packedWord;
    union {
        uint8_t materials[4];
        uint32_t secondWord;
    } u;
    inline int robots(const int index) const { return (packedWord >> (6 * index)) & 63; }
    inline void setRobots(const int index, int value) { const int shift = 6 * index; packedWord = (packedWord & (~(63 << shift))) | (value << shift); }
    inline int material(const int index) const { return int(u.materials[index]); }
    inline void setMaterial(const int index, int value) { u.materials[index] = (value > 255) ? 255 : uint8_t(value); }
    inline int time() const { return packedWord >> 24; }
    inline void setTime(int value) { packedWord = (packedWord & 0xFFFFFFu) | ((value > 0) ? (value << 24) : 0); }
    State(int time) { u.secondWord = 0; packedWord = 1u | uint32_t(time << 24); }
    void dump() const {
        printf("[t=%d]", time());
        for (int i = 0;  i < 4;  ++i) printf(" %d", robots(i));
        printf(" robots +");
        for (int i = 0;  i < 4;  ++i) printf(" %d", u.materials[i]);
        printf(" materials\n");
    }
    inline bool operator== (const State& other) const { return (packedWord == other.packedWord) && (u.secondWord == other.u.secondWord); }
};

template<> struct std::hash<State> {
    std::size_t operator() (const State& s) const noexcept {
        return (s.packedWord * 31337) ^ s.u.secondWord ^ (s.u.secondWord >> 17);
    }
};


struct DFSCache {
    int best;
    std::unordered_map<State,int> lookup;
    inline DFSCache() : best(0) {}
    inline ~DFSCache() {
        //printf("      -> cache size: %lu\n", (unsigned long)lookup.size());
    }
};
int DFSmain(const Blueprint& bp, DFSCache& cache, const State& state) {
    int time = state.time();
    if (!time) return state.material(3);
//state.dump();

    const auto it = cache.lookup.find(state);
    if (it != cache.lookup.end()) { return it->second; }

    int best = state.material(3) + state.robots(3) * time;
    if ((best + ((time * time + time + 1) >> 1)) <= cache.best) {
        cache.lookup.emplace(state, 0);
        return 0;
    }

    for (int rt = 3;  rt >= 0;  --rt) {
        if (state.robots(rt) >= bp.maxRobots[rt])
            continue;  // don't mine more resources than we can possibly spend on robots
        int timeReq = 1;
        for (int i = 0;  i < 4;  ++i) {
            int missing = bp.requirements[rt][i] - state.material(i);
            int rate = state.robots(i);
            int t = rate ? ((missing + rate - 1) / rate) : ((missing > 0) ? 999 : 0);
            timeReq = std::max(timeReq, t + 1);
        }
        if (timeReq > time) continue;
        State derived(time - timeReq);
        for (int i = 0;  i < 4;  ++i) {
            int rate = state.robots(i);
            derived.setRobots(i, rate + ((i == rt) ? 1 : 0));
            derived.setMaterial(i, state.material(i) + timeReq * rate - bp.requirements[rt][i]);
        }
        best = std::max(best, DFSmain(bp, cache, derived));
//printf(" `-> "); derived.dump();
    }

    if (best > cache.best) cache.best = best;
    cache.lookup.emplace(state, best);
    return best;
}
int runDFS(const Blueprint& bp, int time) {
    State initial(time);
    DFSCache cache;
    return DFSmain(bp, cache, initial);
}


int main() {
    FILE *f = fopen("input.txt", "rb");

    std::vector<Blueprint> blueprints;
    uint8_t nums[8] = {0,};
    int numIdx = 0;
    while (!feof(f)) {
        char c = fgetc(f);
        if (isdigit(c)) {
            nums[numIdx] = (nums[numIdx] * 10) + c - '0';
        } else if (c == '\n') {
            blueprints.emplace_back(nums, numIdx);
            numIdx = 0;
            nums[0] = 0;
        } else if (nums[numIdx] && (numIdx < 7)) {
            nums[++numIdx] = 0;
        }
    }

    // part 1
#if 1
    int sum = 0;
    for (const auto& bp : blueprints) {
        //printf("    - BP %d ", bp.id);
        int res = runDFS(bp, 24);
        //printf("=> %d\n", res);
        sum += bp.id * res;
    }
    printf("%d\n", sum);
#endif

    // part 2
#if 1
    int prod = 1;
    for (int i = 0;  (i < 3) && (i < int(blueprints.size()));  ++i) {
        const auto& bp = blueprints[i];
        //printf("    - BP %d ", bp.id);
        int res = runDFS(bp, 32);
        //printf("=> %d\n", res);
        prod *= res;
    }
    printf("%d\n", prod);
#endif

    return 0;
}
