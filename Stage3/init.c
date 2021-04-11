
void init(void)
{
  /* Define background colour */
  glClearColor(0.0, 0.0, 0.0, 0.0);

  /* Set initial view parameters */
  eyex= 0; /* Set eyepoint at eye height within the scene */
  eyey= 0;
  eyez= 0;

  upx= 0.0;   /* Set up direction to the +Y axis  */
  upy= 1.0;
  upz= 0.0;

  lat= 0.0;   /* Look horizontally ...  */
  lon= 0.0;   /* ... along the +Z axis  */

  mlat= 0.0;  /* Zero mouse look angles */
  mlon= 0.0;

  current_view= TOP_VIEW;
  draw_labels= 1;
  draw_orbits= 1;
