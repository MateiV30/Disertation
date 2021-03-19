
void drawAxes (void) {

// Draws X Y and Z axis lines, of length LEN

   float LEN= 1000000000000000.0;

   glLineWidth(2.0);

   glBegin(GL_LINES);
   glColor3f(1.0,0.0,0.0); // red
       glVertex3f(0.0, 0.0, 0.0);
       glVertex3f(LEN, 0.0, 0.0);

   glColor3f(0.0,1.0,0.0); // green
       glVertex3f(0.0, 0.0, 0.0);
       glVertex3f(0.0, LEN, 0.0);

   glColor3f(0.0,0.0,1.0); // blue
       glVertex3f(0.0, 0.0, 0.0);
       glVertex3f(0.0, 0.0, LEN);
   glEnd();

   glLineWidth(1.0);
}

/***********************************/
