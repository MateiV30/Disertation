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
