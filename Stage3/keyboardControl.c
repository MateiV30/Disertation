
/************************************************/

void keyboard(unsigned char key, int x, int y)
{
  double Dx, Dz;
  switch(key)
  {
    case 27:  /* Escape key */
      exit(0);
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
