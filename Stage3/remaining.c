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
