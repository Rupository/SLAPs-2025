// tetrahedral numbers - as running sum of triangular numbers
// https://en.wikipedia.org/wiki/Tetrahedral_number
// https://en.wikipedia.org/wiki/Pyramidal_number

method Tetrahedral(n: int) returns (j: int)
  requires n > 0
  ensures j == (n*(n+1)*(n+2))/6
{
  var i := 0;
  var k := 0;
  j := 0;

  while (i < n)
    invariant 0 <= i <= n
    invariant j == (i*(i+1)*(i+2))/6
    invariant k == (i*(i+1))/2 

    // helper invariant: teaches dafny arithmetic
    // enterprise LLMs were not able to zero-shot this (as of 2025-12-07)
    invariant (i*(i+1)) % 2 == 0 
  {
    i := i + 1;
    k := k + i;
    j := j + k; 
  }
}