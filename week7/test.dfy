method Compute(n: int) returns (x: int)
  requires n >= 0
  ensures x >= n
{
  var i := 0;
  x := 0;

  while (i < n) 
  
  invariant i < 10 ==> i - x == 0 && -x <= 0 && i - n <= 0 && i - 12 <= 0 
  invariant !(i < 10) && i < 20 ==> -2*i + x == 0 && -n <= 0 && -i - x - 1 <= 0 
  invariant !(i < 10) && !(i < 20) ==> i - n - 1 <= 0 && -3*i + x == 0 && -15*i - x <= 0 && -16*i - 8*n + 5*x <= 0
  
  
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