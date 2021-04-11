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
