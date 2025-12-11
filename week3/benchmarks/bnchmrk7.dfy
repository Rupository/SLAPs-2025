// heptagonal pyramidal numbers - as running sum of heagonal numbers
// https://oeis.org/A002413
// https://en.wikipedia.org/wiki/Pyramidal_number

method HeptagonalPyramidal(n: int) returns (j: int)
  requires n > 0
  ensures j == n*(n+1)*(5*n - 2)/6
{
  var i := 0;
  var k := 0;
  j := 0;

  while (i < n)
    invariant 0 <= i <= n
    invariant j == i*(i+1)*(5*i - 2)/6
    invariant k == i*(5*i - 3)/2

    // helper invariant
    invariant i*(5*i - 3) % 2 == 0 
  {
    i := i + 1;
    k := k + 5*i - 4;
    j := j + k; 
  }
}