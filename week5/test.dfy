// test cases from source repo
method Sum(n: int) returns (result: int, test:int)
  requires n >= 0
  ensures result == n * (n + 1) / 2
{
  var i := 0;
  var sum := 0;
  
  while (i <= n)
    invariant 0 <= i <= n + 1
    invariant sum == i * (i - 1) / 2
  {
    sum := sum + i;
    i := i + 1;
  }
  
  result := sum;
  test := sum;
}


method Factorial(n: int) returns (result: int)
  requires n >= 0
  ensures result >= 1
{
  result := 1;
  
  for i := 1 to n+1 // needs to be n+1
    //invariant 1 <= i <= n + 1
    //invariant result >= 1
  {
    result := result * i;
  }
}

// my yayful benchmarks