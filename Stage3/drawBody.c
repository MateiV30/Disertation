
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
