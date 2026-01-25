method Compute(n: int) returns (x: int)
  requires n >= 0
  ensures x >= n
{
  var i := 0;
  x := 0;

  while (i < n)
  {
    if (i < 10) {
      x := x + 1;
    } 
    else {
      if (i < 20) {
        x := x + 2;
      }
      else {
        x := x + 3;
      }
    }
    
    i := i + 1;
  }
}