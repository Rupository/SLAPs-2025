method Sum(n: int) returns (s: int)
    requires n >= 0
    ensures s == n * (n - 1) / 2
{
    var i := 0;
    s := 0;
    
    while (i < n)
        invariant 0 <= i <= n
        invariant s == i * (i - 1) / 2
        decreases n - i
    {
        s := s + i;
        i := i + 1;
    }
}