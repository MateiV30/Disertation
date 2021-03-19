
float myRand (void)
{
  /* return a random float in the range [0,1] */

  return (float) (rand()-rand()) / RAND_MAX * 2;
}
