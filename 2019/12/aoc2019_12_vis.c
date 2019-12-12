#if 0  // self-compiling code
gcc -std=c99 -Wall -Wextra -pedantic -Wno-missing-field-initializers -Werror -g -O2 $0 -lglut -lGLU -lGL -lm || exit 1
exec ./a.out
#endif

// n-body trajectory visualization modeled after AoC 2019 day 12
// - uses old-school OpenGL 1.0 and GLUT
// - rotate view by clicking and dragging with the mouse
// - zoom in/out with the mouse wheel
// - press 1,2,3,...,9,0 to select speed and trail length
// - press space to pause

#include <stdio.h>
#include <math.h>

#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/freeglut.h>

#define NBODY  4

typedef struct _body {
    int p[3];  // position
    int v[3];  // velocity
} body_t;

body_t bodies[NBODY] = {
#if 0  // first example from puzzle description
       // (the one that repeats at t=2772)
    {{  -1,   0,   2 }},
    {{   2, -10,  -7 }},
    {{   4,  -8,   8 }},
    {{   3,   5,  -1 }},
#endif
#if 1  // second example from puzzle description
    {{  -8, -10,   0 }},
    {{   5,   5,  10 }},
    {{   2,  -7,   3 }},
    {{   9,  -8,  -3 }},
#endif
};

#define START_PAUSED  0
#define WIDE_LINES    0

const float bodyColors[NBODY][3] = {
    { 1.00f, 0.00f, 0.00f },
    { 0.25f, 0.75f, 0.00f },
    { 0.00f, 0.50f, 1.00f },
    { 1.00f, 0.75f, 0.00f },
};

double t = 0.0;
double speed = START_PAUSED ? 0.0 : 32.0;

double camDist = 100.0;
double camAngle = 0.75;
double camHeight = 0.375;

double radius = 1.0;
double trailLength = 96.0;

#define MAX_TRAIL_LENGTH  256

#if MAX_TRAIL_LENGTH & (MAX_TRAIL_LENGTH - 1)
    #error MAX_TRAIL_LENGTH must be a power of two
#endif
static int trail[NBODY][MAX_TRAIL_LENGTH][3];
static int trailIndex = 0;
#define TM(x) ((x) & (MAX_TRAIL_LENGTH - 1))

static int screenWidth, screenHeight;


void onInit(void) {
    glEnable(GL_NORMALIZE);
    glEnable(GL_COLOR_MATERIAL);

    glClearColor(0.0625f, 0.0625f, 0.0625f, 0.0f);
    glLineWidth(1.0 + WIDE_LINES);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glEnable(GL_LIGHT0);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (GLfloat[4]){0.25f, 0.25, 0.25f, 1.0f});
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (GLfloat[4]){1.0f, 1.0f, 1.0f, 1.0f});
    glLightfv(GL_LIGHT0, GL_SPECULAR, (GLfloat[4]){1.0f, 1.0f, 1.0f, 1.0f});
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (GLfloat[4]){1.0f, 1.0f, 1.0f, 1.0f});
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 64.0f);

    for (int n = 0;  n < NBODY;  ++n) {
        for (int c = 0;  c < 3;  ++c) {
            trail[n][0][c] = bodies[n].p[c];
        }
    }
}

static void drawText(int x, int y, const char *str) {
    glRasterPos2i(x, y);
    while (*str) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *str++);
    }
}

void onDraw(void) {
    while (t > trailIndex) {
        trailIndex++;
        for (int a = 0;  a < NBODY;  ++a) {
            for (int b = 0;  b < NBODY;  ++b) {
                for (int c = 0;  c < 3;  ++c) {
                    int pa = bodies[a].p[c];
                    int pb = bodies[b].p[c];
                    bodies[a].v[c] += (pa < pb) - (pa > pb);
                }
            }
        }
        for (int n = 0;  n < NBODY;  ++n) {
            for (int c = 0;  c < 3;  ++c) {
                trail[n][TM(trailIndex)][c] =
                    (bodies[n].p[c] += bodies[n].v[c]);
            }
        }
    }

    static GLUquadricObj* quadric = NULL;
    if (!quadric) {
        quadric = gluNewQuadric();
    }

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (double)screenWidth / (double)screenHeight, 1.0, 1024.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(
        camDist * cos(camHeight) * sin(camAngle),
        camDist * cos(camHeight) * cos(camAngle),
        camDist * sin(camHeight),
        0.0, 0.0, 0.0,
        0.0, 0.0, 1.0
    );
    glLightfv(GL_LIGHT0, GL_POSITION, (GLfloat[4]){1024.0f, -1024.0f, 2048.0f, 1.0f});

    glDisable(GL_DEPTH_TEST);
    glBegin(GL_LINES);
    #define A 96
    #define B 64
    glColor4ub(0, 0, 0, 255);  glVertex3i(-1024, 0, 0);
    glColor4ub(A, B, B, 255);  glVertex3i(0, 0, 0); glVertex3i(0, 0, 0);
    glColor4ub(0, 0, 0, 255);  glVertex3i( 1024, 0, 0);
    glColor4ub(0, 0, 0, 255);  glVertex3i(0, -1024, 0);
    glColor4ub(B, A, B, 255);  glVertex3i(0, 0, 0); glVertex3i(0, 0, 0);
    glColor4ub(0, 0, 0, 255);  glVertex3i(0,  1024, 0);
    glColor4ub(0, 0, 0, 255);  glVertex3i(0, 0, -1024);
    glColor4ub(B, B, A, 255);  glVertex3i(0, 0, 0); glVertex3i(0, 0, 0);
    glColor4ub(0, 0, 0, 255);  glVertex3i(0, 0,  1024);
    glEnd();
    glEnable(GL_DEPTH_TEST);

#if 0
    glEnable(GL_LIGHTING);
    glColor4ub(255, 255, 240, 255);
    glRotated(90.0, 1.0, 0.0, 0.0);
    glutSolidTeapot(20.0);
    glDisable(GL_LIGHTING);
#endif

    float tFrac = (float)(trailIndex - t);
    float alphaScale = (float) (1.0 / (trailLength - 1.0));
    for (int n = 0;  n < NBODY;  ++n) {
        float pos[3];
        const float *col = &bodyColors[n][0];
        for (int c = 0;  c < 3;  ++c) {
            float a = (float)trail[n][TM(trailIndex)][c];
            float b = (float)trail[n][TM(trailIndex - 1)][c];
            pos[c] = a + tFrac * (b - a);
        }
        glColor4f(col[0], col[1], col[2], 1.0f);

        glEnable(GL_LIGHTING);
        glPushMatrix();
        glTranslatef(pos[0], pos[1], pos[2]);
        gluSphere(quadric, radius, 16, 8);
        glPopMatrix();
        glDisable(GL_LIGHTING);

        glEnable(GL_BLEND);
        glBegin(GL_LINE_STRIP);
        glVertex3fv(pos);
        for (int i = 1;  (i <= trailIndex) && (i < MAX_TRAIL_LENGTH);  ++i) {
            float trailPos = i - tFrac;
            float alpha = 1.0f - trailPos * alphaScale;
            if (alpha < 0.0f) { alpha = 0.0f; }
            alpha *= alpha * alpha;
            glColor4f(col[0], col[1], col[2], alpha);
            glVertex3iv(&trail[n][TM(trailIndex - i)][0]);
            if (trailPos > (float)trailLength) { break; }
        }
        glEnd();
        glDisable(GL_BLEND);
    }

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, screenWidth, screenHeight, 0, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glColor4ub(255, 255, 255, 255);

    char s[40];
    sprintf(s, "speed: %.0f/s", speed);
    drawText(10, 20, s);
    sprintf(s, "t=%.2f", t);
    drawText(10, 40, s);

    glutSwapBuffers();
}

void onIdle(void) {
    static double tLast = -1.0;
    double tNow = glutGet(GLUT_ELAPSED_TIME) * 0.001;
    if (tLast >= 0.0) {
        t += (tNow - tLast) * speed;
    }
    tLast = tNow;
    glutPostRedisplay();
}

void onResize(int w, int h) {
    glViewport(0, 0, w, h);
    screenWidth = w;
    screenHeight = h;
}

void onKey(unsigned char c, int x, int y) {
    (void)x,(void)y;
    switch (c) {
        case 'q':
            glutLeaveMainLoop();
            break;
        case ' ': {
            static double pausedSpeed = 0.0;
            if (speed > 0.0) {
                pausedSpeed = speed;
                speed = 0.0;
            } else {
                speed = pausedSpeed;
            }
            break; }
        default:
            if ((c >= '0') && (c <= '9')) {
                int digit = c - '0';
                if (!digit) { digit = 10; }
                speed = exp2(digit - 3);
                trailLength = speed * 3.0 + 2.0;
            }
            break;
    }
}

static int m_x0, m_y0;
static double m_a0, m_h0;

void onMouseWheel(int wheel, int direction, int x, int y) {
    (void)wheel, (void)x, (void)y;
    camDist += direction * 10.0;
    if (camDist < 1.0) { camDist = 1.0; }
}

void onMouseClick(int button, int state, int x, int y) {
    if (state != GLUT_DOWN) { return; }
    switch (button) {
        case GLUT_LEFT_BUTTON:
            m_x0 = x;  m_a0 = camAngle;
            m_y0 = y;  m_h0 = camHeight;
            break;
        case 3: onMouseWheel(0, -1, x, y); break;
        case 4: onMouseWheel(0, +1, x, y); break;
        default:
            break;
    }
}

void onMouseMove(int x, int y) {
    camAngle  = m_a0 + (x - m_x0) * 0.01;
    camHeight = m_h0 + (y - m_y0) * 0.01;
    if (camHeight < -1.5) { camHeight = -1.5; }
    if (camHeight >  1.5) { camHeight =  1.5; }
}


int main(int argc, char* argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA);
    glutInitWindowSize(1280, 720);
    glutCreateWindow("AoC 2019 day 12");
    glutReshapeFunc(onResize);
    glutDisplayFunc(onDraw);
    glutIdleFunc(onIdle);
    glutKeyboardFunc(onKey);
    glutMouseFunc(onMouseClick);
    glutMotionFunc(onMouseMove);
    glutMouseWheelFunc(onMouseWheel);
    onInit();
    glutMainLoop();
    return 0;
}
