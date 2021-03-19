
void drawStarfield (void)
{
  srand(1);
  /* This is for you to complete. */
  int i;
  glBegin (GL_POINTS);
    for(i=0; i<1000; i++)
      {
        glColor3f(255.0, 255.0, 255.0);
        glVertex3f(myRand()*1000000000, myRand()*1000000000, myRand()*100000000);
      }
  glEnd ();
}
