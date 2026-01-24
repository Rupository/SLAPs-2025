// try putting your own file for the tool!

method Sum(n: int) returns (s: int)
    requires n >= 0
    ensures s == n * (n - 1) / 2
{
    var i := 0;
    s := 0;
    
    while (i < n) 
    {
        s := s + i;
        i := i + 1;
    }
}