#ifdef MACOS
  #include <GLUT/glut.h>
#else
  #include <GL/glut.h>
#endif

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_BODIES 25
#define TOP_VIEW 1
#define ECLIPTIC_VIEW 2
#define SHIP_VIEW 3
#define EARTH_VIEW 4
#define MOVIE_VIEW 5
#define FLY_VIEW 6
#define PI 3.141593
#define DEG_TO_RAD 0.01745329
#define ORBIT_POLY_SIDES 50
#define TIME_STEP 0.5   /* days per frame */

#define RUN_SPEED  500000
#define TURN_ANGLE 4.0
typedef struct {
  char    name[25];       /* name */
  GLfloat r,g,b;          /* colour */
  GLfloat orbital_radius; /* distance to parent body (km) */
  GLfloat orbital_tilt;   /* angle of orbit wrt ecliptic (deg) */
  GLfloat orbital_period; /* time taken to orbit (days) */
  GLfloat radius;         /* radius of body (km) */
  GLfloat axis_tilt;      /* tilt of axis wrt body's orbital plane (deg) */
  GLfloat rot_period;     /* body's period of rotation (days) */
  GLint   orbits_body;    /* identifier of parent body */
  GLfloat spin;           /* current spin value (deg) */
  GLfloat orbit;          /* current orbit value (deg) */
 } body;

body  bodies[MAX_BODIES];
int   numBodies, current_view, draw_orbits, draw_labels, draw_starfield;
float  date;
float x_earth, z_earth, x_movie, z_movie;
GLboolean draw_Axes = GL_TRUE;

GLdouble lat,     lon;              /* View angles (degrees)    */
GLdouble mlat,    mlon;             /* Mouse look offset angles */
GLfloat  eyex,    eyey,    eyez;    /* Eye point                */
GLfloat  centerx, centery, centerz; /* Look point               */
GLfloat  upx,     upy,     upz;     /* View up vector           */
GLint width= 900, height= 900;      /* size of window           */

/*****************************/
GLboolean have_Orbit = GL_FALSE;

/*****************************/

float myRand (void)
{
  /* return a random float in the range [0,1] */

  return (float) (rand()-rand()) / RAND_MAX * 2;
}

void calculate_lookpoint(void) { /* Given an eyepoint and latitude and longitude angles, will
     compute a look point one unit away */
  double dir_x, dir_y, dir_z;
  GLdouble newLat = lat + mlat;
  GLdouble newLon = lon + mlon;
  dir_x = cos(newLat*DEG_TO_RAD) * sin(newLon*DEG_TO_RAD);
  dir_y = sin(newLat*DEG_TO_RAD);
  dir_z = cos(newLat*DEG_TO_RAD) * cos(newLon*DEG_TO_RAD);
  centerx = eyex + dir_x*100;
  centery = eyey + dir_y*100;
  centerz = eyez + dir_z*100;

} // calculate_lookpoint()

void setView (void) {
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  switch (current_view) {
  case TOP_VIEW:
    /* This is for you to complete. */
    gluLookAt(0.0, 550000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0 );
    break;
  case ECLIPTIC_VIEW:
    /* This is for you to complete. */
    gluLookAt(0.0, 0.0, 550000000.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case SHIP_VIEW:
    /* This is for you to complete. */
    gluLookAt(154366378, 56345439, 105365820, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case EARTH_VIEW:
    /* This is for you to complete. */
    x_earth = bodies[3].orbital_radius * sin((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component
    z_earth = bodies[3].orbital_radius * cos((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component
    gluLookAt(x_earth*1.1, 10000000, z_earth*1.1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case MOVIE_VIEW:
    /* This is for you to complete. */
    x_movie = bodies[3].orbital_radius * sinf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component
    z_movie = bodies[3].orbital_radius * cosf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component
    gluLookAt(x_movie+bodies[3].orbital_radius, bodies[3].orbital_radius, z_movie+bodies[3].orbital_radius, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case FLY_VIEW:
    calculate_lookpoint(); /* Compute the centre of interest   */
    gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz);
    break;

  }
  glutPostRedisplay();
}

void init(void)
{
  /* Define background colour */
  glClearColor(0.0, 0.0, 0.0, 0.0);

  /* Set initial view parameters */
  eyex= 0; /* Set eyepoint at eye height within the scene */
  eyey= 0;
  eyez= 0;

  upx= 0.0;   /* Set up direction to the +Y axis  */
  upy= 1.0;
  upz= 0.0;

  lat= 0.0;   /* Look horizontally ...  */
  lon= 0.0;   /* ... along the +Z axis  */

  mlat= 0.0;  /* Zero mouse look angles */
  mlon= 0.0;

  current_view= TOP_VIEW;
  draw_labels= 1;
  draw_orbits= 1;
  glutAddMenuEntry ("", 999);
  glutAddMenuEntry ("Quit", 10);
  glutAttachMenu (GLUT_RIGHT_BUTTON);
}
void drawOrbit (int n) {}
void drawBody(int n)
{
 /* Draws body "n" */
  if(n == 0)
  {
    glBegin(GL_LINES);
      glColor3f(5.0,5.0,5.0);
      glVertex3f(bodies[n].axis_tilt, -bodies[n].radius*2, 0.0);
      glVertex3f(bodies[n].axis_tilt, bodies[n].radius*2, 0.0);
    glEnd();

    glColor3f(bodies[n].r, bodies[n].g, bodies[n].b);

    glRotatef(bodies[n].axis_tilt, 1.0, 0.0, 0.0);
    glRotatef(bodies[n].spin, 0.0, 1.0, 0.0);
    glRotatef(90, 1, 0, 0);

    glutWireSphere(bodies[n].radius, 30, 30);
  }
  else if(bodies[n].orbits_body == 0)
  {
    glColor3f(bodies[n].r, bodies[n].g, bodies[n].b);

    glRotatef(bodies[n].orbital_tilt, 1.0, 0.0, 0.0);
    glRotatef(bodies[n].orbit, 0, 1, 0);
    if(have_Orbit) drawOrbit(n);
    glTranslatef(bodies[n].orbital_radius, 0, 0);// + bodies[n].orbit);
    glRotatef(bodies[n].axis_tilt, 1.0, 0.0, 0.0);
    glRotatef(bodies[n].spin, 0.0, 1.0, 0.0);

    glBegin(GL_LINES);
      //glColor3f(5.0,5.0,5.0);
      glVertex3f(bodies[n].axis_tilt, -bodies[n].radius*2, 0.0);
      glVertex3f(-bodies[n].axis_tilt, bodies[n].radius*2, 0.0);
    glEnd();

    glRotatef(90, 1, 0, 0);

    glutWireSphere(bodies[n].radius, 15, 15);
  }
  else
  {
    glColor3f(bodies[n].r, bodies[n].g, bodies[n].b);

    glRotatef(bodies[bodies[n].orbits_body].orbital_tilt, 1.0, 0.0, 0.0);
    glRotatef(bodies[bodies[n].orbits_body].orbit, 0, 1, 0);
    glTranslatef(bodies[bodies[n].orbits_body].orbital_radius, 0, 0);// + bodies[n].orbit);
    glRotatef(bodies[bodies[n].orbits_body].axis_tilt, 1.0, 0.0, 0.0);
    glRotatef(bodies[n].orbit, 0.0, 1.0, 0.0);
    if(have_Orbit) drawOrbit(n);
    glTranslatef(bodies[n].orbital_radius, 0, 0);
    glRotatef(bodies[n].axis_tilt, 0.0, 1.0, 0.0);
    glRotatef(bodies[n].spin, 0.0, 1.0, 0.0);

    glBegin(GL_LINES);
      //glColor3f(5.0,5.0,5.0);
      glVertex3f(bodies[n].axis_tilt, -bodies[n].radius*2, 0.0);
      glVertex3f(-bodies[n].axis_tilt, bodies[n].radius*2, 0.0);
    glEnd();

    glRotatef(90, 1, 0, 0);

    glutWireSphere(bodies[n].radius, 10, 10);

  }

}

/*****************************/

void display(void)
{
  int i;

  glClear(GL_COLOR_BUFFER_BIT);

  /* set the camera */
  setView();

  for (i= 0; i < numBodies; i++)
  {
    glPushMatrix();
      drawBody (i);
    glPopMatrix();
  }
  glutSwapBuffers();
}
void readSystem(void)
{
  /* reads in the description of the solar system */

  FILE *f;
  int i;

  f= fopen("sys", "r");
  if (f == NULL) {
     printf("Program couldn't open the specifications file 'sys'\n");
     printf("Please create the file\n");
     exit(0);
  }
  fscanf(f, "%d", &numBodies);
  for (i= 0; i < numBodies; i++)
  {
    fscanf(f, "%s %f %f %f %f %f %f %f %f %f %d",
      bodies[i].name,
      &bodies[i].r, &bodies[i].g, &bodies[i].b,
      &bodies[i].orbital_radius,
      &bodies[i].orbital_tilt,
      &bodies[i].orbital_period,
      &bodies[i].radius,
      &bodies[i].axis_tilt,
      &bodies[i].rot_period,
      &bodies[i].orbits_body);

    /* Initialise the body's state */
    bodies[i].spin= 0.0;
    bodies[i].orbit= myRand() * 360.0; /* Start each body's orbit at a
                                          random angle */
    bodies[i].radius*= 1000.0; /* Magnify the radii to make them visible */
  }
  fclose(f);
}

/*****************************/
/*****************************/

void animate(void)
{
  int i;

    date+= TIME_STEP;

    for (i= 0; i < numBodies; i++)  {
      bodies[i].spin += 360.0 * TIME_STEP / bodies[i].rot_period;
      bodies[i].orbit += 360.0 * TIME_STEP / bodies[i].orbital_period;
      glutPostRedisplay();
    }
}


void drawString (void *font, float x, float y, char *str)
{ /* Displays the string "str" at (x,y,0), using font "font" */

  /* This is for you to complete. */

}

/*****************************/

void drawLabel(int n){ /* Draws the name of body "n" */}

/*****************************/

void reshape(int w, int h)
{
  glViewport(0, 0, (GLsizei) w, (GLsizei) h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective (48.0, (GLfloat)w/(GLfloat)h,  10000.0, 800000000.0);
  glMatrixMode (GL_MODELVIEW);
  width= w;   /* Record the new width and height */
  height= h;
}

/*****************************/
void mouse_motion(int x, int y) {

  /* To be completed */
  mlon = -100*x/width + 50;
  mlat = -100*y/height + 50;

} // mouse_motion()
/*****************************/

int main(int argc, char** argv)
{
  glutInit (&argc, argv);
  glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
  glutCreateWindow ("Solar system");
  // glutFullScreen();
  glutInitWindowSize (width, height);
  init();
  glutDisplayFunc (display);
  glutReshapeFunc (reshape);
  glutPassiveMotionFunc (mouse_motion);
  readSystem();
  glutIdleFunc (animate);
  glutMainLoop();
  return 0;
}