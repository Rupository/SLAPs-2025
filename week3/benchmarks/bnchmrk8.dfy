// nonagonal pyramidal numbers - as running sum of nonagonal numbers
// https://oeis.org/A007584

method NonagonalPyramidal(n: int) returns (j: int)
  requires n > 0
  ensures j == n*(n+1)*(7*n-4)/6
{
  var i := 0;
  var k := 0;
  j := 0;

  while i < n
    invariant 0 <= i <= n
    invariant j == i*(i+1)*(7*i-4)/6
    invariant k == i*(7*i-5)/2

    // helper invariant
    invariant i*(7*i-5) % 2 == 0 
  {
    i := i + 1;
    k := k + 7*i - 6;
    j := j + k;
  }
}