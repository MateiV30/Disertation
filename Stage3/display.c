
void display(void)
{
  int i;

  glClear(GL_COLOR_BUFFER_BIT);

  /* set the camera */
  setView();

  if (draw_Axes) drawAxes();

  for (i= 0; i < numBodies; i++)
  {
    glPushMatrix();
      drawBody (i);
    glPopMatrix();
  }

/*****************************/
