#include "header.h"
#include "stdio.h"

int main()
{
  double a, b, c;
  a = 1;
  b = 2;
  c = add_doubles(a, b);
  int d;
  d = (int)c;
  printf("%d.0\n", d);

   //scanf  ("%f", &c);

  classic();

}
