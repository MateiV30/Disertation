

void drawString (void *font, float x, float y, char *str)
{ /* Displays the string "str" at (x,y,0), using font "font" */

  /* This is for you to complete. */

}

/*****************************/

int j;

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

void keyboard(unsigned char key, int x, int y)
{
  double Dx, Dz;
  switch(key)
  {
    case 27:  /* Escape key */
      exit(0);
    case 97:
      if(draw_Axes)
          draw_Axes = GL_FALSE;
      else draw_Axes = GL_TRUE;
      break;
    case 44: //Comma
      Dx = sin((lon+90)*DEG_TO_RAD) * RUN_SPEED;
      Dz = cos((lon+90)*DEG_TO_RAD) * RUN_SPEED;
      eyex = eyex + Dx;
      eyez = eyez + Dz;
      break;
    case 46: //Full-stop
      Dx = sin((lon-90)*DEG_TO_RAD) * RUN_SPEED;
      Dz = cos((lon-90)*DEG_TO_RAD) * RUN_SPEED;
      eyex = eyex + Dx;
      eyez = eyez + Dz;
      break;
    }
  glutPostRedisplay();
}

void cursor_keys(int key, int x, int y)
{
  float Dx, Dy, Dz;
  Dx = sin(lon*DEG_TO_RAD) * RUN_SPEED;
  Dy = sin(lat*DEG_TO_RAD) * RUN_SPEED;
  Dz = cos(lon*DEG_TO_RAD) * RUN_SPEED;
  switch (key)
   {
    case GLUT_KEY_LEFT:
	   lon = lon + TURN_ANGLE; break;
    case GLUT_KEY_RIGHT:
	   lon = lon - TURN_ANGLE; break;
    case GLUT_KEY_PAGE_UP:
	   if(lat + TURN_ANGLE < 90)
	    {
        lat = lat + TURN_ANGLE;
        break;
      }
      else
      {
        lat = 89;
        break;
      }
    case GLUT_KEY_PAGE_DOWN:
	   if(lat - TURN_ANGLE > -90)
	    {
        lat = lat - TURN_ANGLE;
        break;
      }
      else
      {
        lat = -89;
        break;
      }
    case GLUT_KEY_HOME:
	   lat = 0;
     mlat = 0;
     eyex = 0;
     eyey = 0;
     eyez = 0;
     break;

    case GLUT_KEY_UP:
      eyex = eyex + Dx;
      eyey = eyey + Dy;
      eyez = eyez + Dz;
      break;
    case GLUT_KEY_DOWN:
      eyex = eyex - Dx;
      eyey = eyey - Dy;
      eyez = eyez - Dz;
      break;

    case 27: exit(0); // '27' is ASCII code for the escape key
    }

    glutPostRedisplay(); // tell GLUT that a call to glutDisplayFunc() is needed
      /* To be completed */
} // cursor_keys()

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
  glutKeyboardFunc (keyboard);
  glutSpecialFunc (cursor_keys);
  glutPassiveMotionFunc (mouse_motion);
  glutIdleFunc (animate);
  readSystem();
  glutMainLoop();
  return 0;
}
