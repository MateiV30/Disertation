
void readSystem(void)
{
  /* reads in the description of the solar system */

  int i;
  printf("How many planets do you want? ");
  scanf("%d", &numBodies);
  printf("\n");
  for (i= 0; i < numBodies; i++)
  {
  	printf("How is this planet named? ");
    scanf("%s", &bodies[i].name);
    printf("Input the color of %s in rgb format divided by spaces: ", bodies[i].name);
    scanf("%f %f %f", &bodies[i].r, &bodies[i].g, &bodies[i].b);
    printf("Input the orbital radius of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].orbital_radius);
    printf("Input the orbital tilt of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].orbital_tilt);
    printf("Input the orbital period of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].orbital_period);
    printf("Input the radius of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].radius);
    printf("Input the axis tilt of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].axis_tilt);
    printf("Input the rotation period of %s: ", bodies[i].name);
    scanf("%f", &bodies[i].rot_period);
    printf("Which body does %s orbit? In array number: ", bodies[i].name);
    scanf("%d", &bodies[i].orbits_body);

    /* Initialise the body's state */
    bodies[i].spin= 0.0;
    bodies[i].orbit= myRand() * 360.0; /* Start each body's orbit at a
                                          random angle */
    bodies[i].radius*= 1000.0; /* Magnify the radii to make them visible */

    printf("Input for %s terminated!! \n\n", bodies[i].name);
  }
  printf("Input terminated, enjoy the animation!\n");
}

/*****************************/
