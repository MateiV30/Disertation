
void calculate_lookpoint(void) { /* Given an eyepoint and latitude and longitude angles, will
     compute a look point one unit away */
  double dir_x, dir_y, dir_z;
  GLdouble newLat = lat + mlat;
  GLdouble newLon = lon + mlon;
  dir_x = cos(newLat*DEG_TO_RAD) * sin(newLon*DEG_TO_RAD);
  dir_y = sin(newLat*DEG_TO_RAD);
  dir_z = cos(newLat*DEG_TO_RAD) * cos(newLon*DEG_TO_RAD);
  centerx = eyex + dir_x*100;
  centery = eyey + dir_y*100;
  centerz = eyez + dir_z*100;

} // calculate_lookpoint()
