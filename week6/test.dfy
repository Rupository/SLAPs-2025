method Sum(n: int) returns (s: int)
    requires n >= 0
    ensures s == n * (n - 1) / 2
{
    var i := 0;
    s := 0;
    
    while (i < n)
        invariant i - n  <= 0
        invariant -i*i + i + 2*s == 0
    {
        s := s + i;
        i := i + 1;
    }
}