#if 0
cc -std=c99 -Wall -Werror $0 `sdl2-config --cflags --libs` -lGL -lGLU -lm || exit 1
exec ./a.out
#endif

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

#define INITIAL_WINDOW_WIDTH     1280
#define INITIAL_WINDOW_HEIGHT     720
#define INITIAL_VIEW_ROTATION       1.75
#define INITIAL_VIEW_HEIGHT         0.15
#define INITIAL_VIEW_DIST          70.0
#define ZSCALE                      0.5f
#define FENCE_HEIGHT               (0.25f * ZSCALE)
#define PATH_HEIGHT                (1.75f * ZSCALE)
#define MOUSE_ROTATE_SPEED          0.01
#define AMBIENT_LIGHT               0.375f
#define GRASS_SPECULAR_BRIGHTNESS  0.25f
#define GRASS_SPECULAR_EXP        32.0f
#define PATH_SPECULAR_BRIGHTNESS   1.0f
#define PATH_SPECULAR_EXP         64.0f
#define CENTER_HEIGHT_BIAS         1.0f

#include <SDL.h>
#include <GL/gl.h>
#include <GL/glu.h>

SDL_Window* win;
SDL_GLContext ctx;
char* grid;
int* dist;
int grid_width  = 0;
int grid_height = 0;
int startX, startY;
int endX, endY;
float centerX = 0.0f, centerY = 0.0f;
double view_dist   = INITIAL_VIEW_DIST;
double view_rotate = 3.141592653589793 * INITIAL_VIEW_ROTATION;
double view_height = 3.141592653589793 * INITIAL_VIEW_HEIGHT;

///////////////////////////////////////////////////////////////////////////////

#define D(x,y) dist[(y) * grid_width + (x)]
#define G(x,y) grid[(y) * grid_width + (x)]
#define MARK_BIT 0x40
#define HEIGHT(x,y)     (G(x,y) &  ~MARK_BIT)
#define MARKED(x,y)     (G(x,y) &   MARK_BIT)
#define MARK(x,y)   do { G(x,y) |=  MARK_BIT; } while (0)
#define UNMARK(x,y) do { G(x,y) &= ~MARK_BIT; } while (0)

bool find_marked(int *p_x, int *p_y) {
    const char* p = grid;
    for (int y = 0;  y < grid_height;  ++y) {
        for(int x = 0;  x < grid_width;  ++x) {
            if ((*p++) & MARK_BIT) {
                *p_x = x;
                *p_y = y;
                return true;
            }
        }
    }
    return false;
}

bool next_neighbor(int *p_x, int *p_y, int *p_n) {
    static const int dx[4] = { -1, +1, +1, -1 }; 
    static const int dy[4] = {  0, -1, +1, +1 };
    int x = *p_x, y = *p_y, n = *p_n;
    while (n < 4) {
        x += dx[n];
        y += dy[n];
        ++n;
        if ((x >= 0) && (y >= 0) && (x < grid_width) && (y < grid_height)) {
            *p_x = x;
            *p_y = y;
            *p_n = n;
            return true;
        }
    }
    return false;
}

///////////////////////////////////////////////////////////////////////////////

void draw_fence(int x0, int y0, int x1, int y1, float dz0, float dz1) {
    float z0 = ZSCALE * (float)G(x0, y0);
    float z1 = ZSCALE * (float)G(x1, y1);
    glNormal3f((float)(y1 - y0), (float)(x0 - x1), 0.0f);
    glVertex3f((float)x0, (float)y0, z0 + dz1);
    glVertex3f((float)x0, (float)y0, z0 + dz0);
    glVertex3f((float)x1, (float)y1, z1 + dz0);
    glVertex3f((float)x1, (float)y1, z1 + dz1);
    glNormal3f((float)(y0 - y1), (float)(x1 - x0), 0.0f);
    glVertex3f((float)x1, (float)y1, z1 + dz1);
    glVertex3f((float)x1, (float)y1, z1 + dz0);
    glVertex3f((float)x0, (float)y0, z0 + dz0);
    glVertex3f((float)x0, (float)y0, z0 + dz1);
}

void draw_triangle(
    float x0, float y0, float z0,
    float x1, float y1, float z1,
    float x2, float y2, float z2
) {
    glNormal3f((y1-y0) * (z2-z0) - (z1-z0) * (y2-y0),
               (z1-z0) * (x2-x0) - (x1-x0) * (z2-z0),
               (x1-x0) * (y2-y0) - (y1-y0) * (x2-x0));
    glVertex3f(x0, y0, z0);
    glVertex3f(x1, y1, z1);
    glVertex3f(x2, y2, z2);
}

void draw_patch(int x0, int y0) {
    float za = ZSCALE * (float)G(x0,   y0);
    float zb = ZSCALE * (float)G(x0+1, y0);
    float zc = ZSCALE * (float)G(x0+1, y0+1);
    float zd = ZSCALE * (float)G(x0,   y0+1);
    float zz[4] = { za, zb, zc, zd };
    #define CE(a,b) do { if (zz[a] > zz[b]) { float t = zz[b]; zz[b] = zz[a]; zz[a] = t; } } while(0)
    CE(0,2); CE(1,3);
    CE(0,1); CE(2,3);
    float zm = 0.5f * (zz[1] + zz[2]);
    draw_triangle((float)x0,      (float)y0,      za,
    /* A->B */    (float)x0+1.0f, (float)y0,      zb,
                  (float)x0+0.5f, (float)y0+0.5f, zm);
    draw_triangle((float)x0+1.0f, (float)y0,      zb,
    /* B->C */    (float)x0+1.0f, (float)y0+1.0f, zc,
                  (float)x0+0.5f, (float)y0+0.5f, zm);
    draw_triangle((float)x0+1.0f, (float)y0+1.0f, zc,
    /* C->D */    (float)x0,      (float)y0+1.0f, zd,
                  (float)x0+0.5f, (float)y0+0.5f, zm);
    draw_triangle((float)x0,      (float)y0+1.0f, zd,
    /* D->A */    (float)x0,      (float)y0,      za,
                  (float)x0+0.5f, (float)y0+0.5f, zm);
}

void set_specular(float brightness, float shininess) {
    float rgba[4];
    rgba[0] = rgba[1] = rgba[2] = brightness;
    rgba[3] = 1.0f;
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgba);
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess);
}

///////////////////////////////////////////////////////////////////////////////

int main(void) {
    int res = SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS);
    assert(res == 0);

    {   // load grid
        FILE *f = fopen("input.txt", "rb");
        assert(f);
        fseek(f, 0, SEEK_END);
        int size = (int)ftell(f);
        fseek(f, 0, SEEK_SET);
        grid = malloc(size + 1);
        assert(grid);
        res = (int) fread(grid, 1, size, f);
        assert(res == size);
        grid[size] = '\0';
        fclose(f);
    }

    {   // "compact" grid and find start/end positions
        const char* p_in = grid;
        char* p_out = grid;
        int x = 0, y = 0;
        float w, wsum = 0.0f;
        char c;
        while ((c = *p_in++)) {
            if  (c == 'S') { startX = x; startY = y; c = 'a'; }
            if  (c == 'E') {   endX = x;   endY = y; c = 'z'; }
            if ((c >= 'a') && (c <= 'z')) {
                c -= 'a';
                *p_out++ = c;
                ++x;
                w = c + CENTER_HEIGHT_BIAS;
                centerX += x * w;
                centerY += y * w;
                wsum += w;
            } else if (c == '\n') {
                if (grid_width) { assert(x == grid_width); }
                else { grid_width = x; }
                x = 0;  ++y;
            }
        }
        assert((x == 0) || (x == grid_width)); 
        grid_height = y + (x ? 1 : 0);
        centerX /= wsum;
        centerY /= wsum;
    }
    printf("loaded grid: %dx%d cells, start @ %d,%d, end @ %d,%d\n", grid_width, grid_height, startX, startY, endX, endY);

    {   // solve the grid
        dist = calloc(grid_width * grid_height, sizeof(int));
        assert(dist);
        MARK(startX, startY);
        D(startX, startY) = 1;
        int x, y, n;
        while (find_marked(&x, &y)) {
            UNMARK(x, y);
            int max_height = G(x,y) + 1;
            int next_dist = D(x,y) + 1;
            n = 0;
            while (next_neighbor(&x, &y, &n)) {
                if ((HEIGHT(x,y) <= max_height) && (!D(x,y) || (D(x,y) > next_dist))) {
                    D(x,y) = next_dist;
                    MARK(x,y);
                }
            }
        }
    }
    printf("%d steps to reach the goal (part 1 solution)\n", D(endX, endY) - 1);

    win = SDL_CreateWindow(
        "AoC Hill Climbing Visualization",
        SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
        INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT,
        SDL_WINDOW_RESIZABLE | SDL_WINDOW_OPENGL);
    assert(win);

    SDL_GL_SetAttribute(SDL_GL_RED_SIZE,      8);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE,    8);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE,     8);
    SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE,    8);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE,   24);
    SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE,  8);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER,  1);
    ctx = SDL_GL_CreateContext(win);
    assert(ctx);

    glClearColor(0.843f, 0.918f, 0.976f, 0.0f);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_CULL_FACE);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_NORMALIZE);
    static const float zero[4] = { 0.0f, 0.0f, 0.0f, 1.0f };
    static const float  amb[4] = { AMBIENT_LIGHT, AMBIENT_LIGHT, AMBIENT_LIGHT, 1.0f };
    static const float  one[4] = { 1.0f, 1.0f, 1.0f, 1.0f };
    glLightfv(GL_LIGHT0, GL_AMBIENT, zero);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, one);
    glLightfv(GL_LIGHT0, GL_SPECULAR, one);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, amb);
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);

    bool active = true;
    bool resize = true;
    bool moving = false;
    int move_start_x = 0, move_start_y = 0;
    double move_ref_x = 0, move_ref_y = 0;
    while (active) {
        SDL_Event ev;
        bool redraw = true;
        while (active && SDL_PollEvent(&ev)) {
            switch (ev.type) {
                case SDL_WINDOWEVENT:
                    switch (ev.window.event) {
                        case SDL_WINDOWEVENT_RESIZED:
                        case SDL_WINDOWEVENT_SIZE_CHANGED:
                            resize = true;
                            break;
                        case SDL_WINDOWEVENT_EXPOSED:
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
                        default:
                            break;
                    }
                    break;
                case SDL_MOUSEBUTTONDOWN:
                    if (ev.button.button == SDL_BUTTON_LEFT) {
                        moving = true;
                        move_start_x = ev.button.x;
                        move_start_y = ev.button.y;
                        move_ref_x = view_rotate;
                        move_ref_y = view_height;
                    }
                    break;
                case SDL_MOUSEBUTTONUP:
                    if (ev.button.button == SDL_BUTTON_LEFT) {
                        moving = false;
                    }
                    break;
                case SDL_MOUSEMOTION:
                    if (moving) {
                        view_rotate = move_ref_x - (ev.motion.x - move_start_x) * MOUSE_ROTATE_SPEED;
                        view_height = move_ref_y - (ev.motion.y - move_start_y) * MOUSE_ROTATE_SPEED;
                        if (view_height < 0.00) { view_height = 0.00; }
                        if (view_height > 1.57) { view_height = 1.57; }
                        redraw = true;
                    }
                    break;
                case SDL_QUIT:
                    active = false;
                    break;
                default:
                    break;
            }
        }
        if (!active) { break; }

        if (resize) {
            int w = 1, h = 1;
            SDL_GL_GetDrawableSize(win, &w, &h);
            glViewport(0, 0, w, h);
            glMatrixMode(GL_PROJECTION);
            glLoadIdentity();
            gluPerspective(45, (double)w / (double) h, 0.1, 1000.0);
            glMatrixMode(GL_MODELVIEW);
            redraw = true;
            resize = false;
        }

        if (redraw) {
            int x0,y0,x,y;
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            glLoadIdentity();
            gluLookAt(
                view_dist * cos(view_rotate) * cos(view_height),
                view_dist * sin(view_rotate) * cos(view_height),
                view_dist *                    sin(view_height),
                0.0, 0.0, 0.0,  0.0, 0.0, 1000.0);
            glTranslatef(-centerX, -centerY, 0.0f);
            static const float light_pos[4] = { 1.0f, -2.0f, 1.0f, 0.0f };
            glLightfv(GL_LIGHT0, GL_POSITION, light_pos);

            set_specular(GRASS_SPECULAR_BRIGHTNESS, GRASS_SPECULAR_EXP);
            glColor3ub(48,96,32);
            glBegin(GL_TRIANGLES);
            for (y = 1;  y < grid_height;  ++y) {
                for (x = 1;  x < grid_width;  ++x) {
                    draw_patch(x-1, y-1);
                }
            }
            glEnd();

            glColor3ub(16,16,16);
            glBegin(GL_QUADS);
            for (y = 0;  y < grid_height;  ++y) {
                for (x = 0;  x < grid_width;  ++x) {
                    if (x) draw_fence(x,y, x-1,y, 0.0f, FENCE_HEIGHT);
                    if (y) draw_fence(x,y, x,y-1, 0.0f, FENCE_HEIGHT);
                }
            }
            glEnd();

            set_specular(PATH_SPECULAR_BRIGHTNESS, PATH_SPECULAR_EXP);
            glColor3ub(255,215,0);
            glBegin(GL_QUADS);
            x = x0 = endX;  y = y0 = endY;
            for (;;) {
                int n = 0, d = D(x,y) - 1;
                if (!d) break;  // start reached
                do {
                    bool valid = next_neighbor(&x, &y, &n);
                    assert(valid);
                } while (D(x,y) != d);
                draw_fence(x0,y0, x,y, FENCE_HEIGHT, PATH_HEIGHT);
                x0 = x;  y0 = y;
            }
            glEnd();

            SDL_GL_SwapWindow(win);
        }
        SDL_WaitEvent(NULL);
    }

    free(dist);
    free(grid);
    SDL_GL_DeleteContext(ctx);
    SDL_DestroyWindow(win);
    SDL_Quit();
    return 0;
}
