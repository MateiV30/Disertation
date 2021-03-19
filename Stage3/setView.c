
void setView (void) {
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  switch (current_view) {
  case TOP_VIEW:
    /* This is for you to complete. */
    gluLookAt(0.0, 550000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0 );
    break;
  case ECLIPTIC_VIEW:
    /* This is for you to complete. */
    gluLookAt(0.0, 0.0, 550000000.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case SHIP_VIEW:
    /* This is for you to complete. */
    gluLookAt(154366378, 56345439, 105365820, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case EARTH_VIEW:
    /* This is for you to complete. */
    x_earth = bodies[3].orbital_radius * sin((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component
    z_earth = bodies[3].orbital_radius * cos((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component
    gluLookAt(x_earth*1.1, 10000000, z_earth*1.1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case MOVIE_VIEW:
    /* This is for you to complete. */
    x_movie = bodies[3].orbital_radius * sinf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the x component
    z_movie = bodies[3].orbital_radius * cosf((bodies[3].orbit+90) * DEG_TO_RAD);//calculate the y component
    gluLookAt(x_movie+bodies[3].orbital_radius, bodies[3].orbital_radius, z_movie+bodies[3].orbital_radius, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 );
    break;
  case FLY_VIEW:
    calculate_lookpoint(); /* Compute the centre of interest   */
    gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz);
    break;

  }
  glutPostRedisplay();
}
