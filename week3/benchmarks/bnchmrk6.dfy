// pentagonal pyramidal numbers - as running sum of pentagonal numbers
// https://oeis.org/A002411
// https://en.wikipedia.org/wiki/Pyramidal_number

method PentagonalPyramidal(n: int) returns (j: int)
  requires n > 0
  ensures j == (n*n*(n+1))/2
{
  var i := 0;
  var k := 0;
  j := 0;

  while (i < n)
    invariant 0 <= i <= n
    invariant j == (i*i*(i+1))/2
    invariant k == (3*i*i - i)/2

    // helper invariant
    invariant (3*i*i - i) % 2 == 0 
  {
    i := i + 1;
    k := k +  3*i - 2;
    j := j + k; 
  }
}