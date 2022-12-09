#if 0
cc -std=c99 -Wall -Werror $0 `sdl2-config --cflags --libs` || exit 1
exec ./a.out
#endif

// rope simulation as in AoC 2022, day 9
// - use mouse to pull rope
// - cursor keys left/right = adjust rope length
// - cursor keys up/down = zoom in/out

#define MAX_ROPE_LENGTH       1000
#define INITIAL_GRID_SIZE       10
#define INITIAL_ROPE_LENGTH     20
#define INITIAL_WINDOW_WIDTH  1024
#define INITIAL_WINDOW_HEIGHT  768

#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>

#include <SDL.h>

typedef struct _knot {
    int x, y;
} Knot;

SDL_Window *win;
SDL_Renderer *render;
int grid_size = INITIAL_GRID_SIZE;
int rope_length = INITIAL_ROPE_LENGTH;
Knot rope[MAX_ROPE_LENGTH];

static inline Uint8 clip_color(int x) {
    return (x < 0) ? 0u : (x > 255) ? 255u : (Uint8)x;
}

///////////////////////////////////////////////////////////////////////////////

void move_rope(int x, int y) {
    rope[0].x = x;
    rope[0].y = y;
    for (int k = 1;  k < MAX_ROPE_LENGTH;  ++k) {
        int dx = rope[k-1].x - rope[k].x;
        int dy = rope[k-1].y - rope[k].y;
        if ((abs(dx) > 1) || (abs(dy) > 1)) {
            rope[k].x += (dx > 0) ? 1 : (dx < 0) ? (-1) : 0;
            rope[k].y += (dy > 0) ? 1 : (dy < 0) ? (-1) : 0;
        }
    }
}

void move_to_pixel(int x, int y) {
    int  nx = x / grid_size, ny = y / grid_size;
    int  ox = rope[0].x,     oy = rope[0].y;
    int adx = abs(ox - nx), ady = abs(oy - ny);
    int delta = (adx > ady) ? adx : ady;
    if (delta <= 1) {
        move_rope(nx, ny);
        return;
    }
    // larger delta -> interpolate coordinates
    for (int t = 1;  t <= delta;  ++t) {
        move_rope((ox * (delta - t) + nx * t + (delta >> 1)) / delta,
                  (oy * (delta - t) + ny * t + (delta >> 1)) / delta);
    }
}

///////////////////////////////////////////////////////////////////////////////

int main(void) {
    int res = SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS);
    assert(res == 0);

    win = SDL_CreateWindow(
        "AoC Rope Simulation",
        SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
        INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT,
        SDL_WINDOW_RESIZABLE);
    assert(win);

    render = SDL_CreateRenderer(win, -1, SDL_RENDERER_PRESENTVSYNC);
    assert(render);

    bool active = true;
    while (active) {
        SDL_Event ev;
        bool redraw = true;
        while (SDL_PollEvent(&ev)) {
            switch (ev.type) {
                case SDL_WINDOWEVENT:
                    switch (ev.window.event) {
                        case SDL_WINDOWEVENT_EXPOSED:
                        case SDL_WINDOWEVENT_RESIZED:
                        case SDL_WINDOWEVENT_SIZE_CHANGED:
                            redraw = true;
                            break;
                        default:
                            break;
                    }
                    break;
                case SDL_KEYDOWN:
                    switch (ev.key.keysym.sym) {
                        case SDLK_q:
                        case SDLK_ESCAPE:
                            active = false;
                            break;
                        case SDLK_LEFT:
                            if (rope_length > 1) {
                                rope_length--;
                                redraw = true;
                            }
                            break;
                        case SDLK_RIGHT:
                            if (rope_length < MAX_ROPE_LENGTH) {
                                rope_length++;
                                redraw = true;
                            }
                            break;
                        case SDLK_UP:
                            grid_size++;
                            redraw = true;
                            break;
                        case SDLK_DOWN:
                            if (grid_size > 1) {
                                grid_size--;
                                redraw = true;
                            }
                            break;
                        default:
                            break;
                    }
                    break;
                case SDL_MOUSEMOTION:
                    move_to_pixel(ev.motion.x, ev.motion.y);
                    redraw = true;
                    break;
                case SDL_QUIT:
                    active = false;
                    break;
                default:
                    break;
            }
        }

        if (redraw) {
            SDL_SetRenderDrawColor(render, 0, 0, 0, 255);
            SDL_RenderClear(render);
            for (int k = rope_length - 1;  k >= 0;  --k) {
                SDL_Rect r;
                r.x = rope[k].x * grid_size;
                r.y = rope[k].y * grid_size;
                r.w = r.h = grid_size;
                int color = 768 - (k * 768 / rope_length);
                if (color > 0) {
                    SDL_SetRenderDrawColor(render, clip_color(color), clip_color(color - 256), clip_color(color - 512), 255u);
                    SDL_RenderFillRect(render, &r);
                }
            }
            SDL_RenderPresent(render);
        }

        SDL_WaitEvent(NULL);
    }

    SDL_DestroyRenderer(render);
    SDL_DestroyWindow(win);
    SDL_Quit();
    return 0;
}
