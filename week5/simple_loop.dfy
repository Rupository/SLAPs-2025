// test cases from source repo
method Sum(n: int) returns (result: int)
  requires n >= 0
  ensures result == n * (n + 1) / 2
{
  var i := 0;
  var sum := 0;
  
  while (i <= n)
    invariant sum == i * (i - 1) / 2
    invariant 0 <= i <= n + 1
  {
    sum := sum + i;
    i := i + 1;
  }
  
  result := sum;
}