
void drawOrbit (int n)
{
    if(draw_orbits)
    {
      int i;
      glBegin(GL_LINE_LOOP);
        for(i = 0; i < ORBIT_POLY_SIDES; i++)
        {
          float theta = 2.0f * 3.1415926f * (float)i / (float)ORBIT_POLY_SIDES;//get the current angle
          //float theta = 90-((ORBIT_POLY_SIDES-2)*180 / 2*ORBIT_POLY_SIDES);

          float x = bodies[n].orbital_radius * sinf(theta);//calculate the x component
          float z = bodies[n].orbital_radius * cosf(theta);//calculate the y component

          glVertex3f(x, 0, z);//output vertex
        }
        glColor3f(bodies[n].r, bodies[n].g, bodies[n].b);
        glEnd();
    }
}

/*****************************/
