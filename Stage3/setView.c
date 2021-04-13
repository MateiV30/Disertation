
void setView (void) {
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  switch (current_view) {
  case TOP_VIEW:
    gluLookAt(0.0, 550000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0 );
    break;
