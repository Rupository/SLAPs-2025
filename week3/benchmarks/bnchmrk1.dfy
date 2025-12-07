// triangular numbers - recurrence and closed form
// https://en.wikipedia.org/wiki/Triangular_number

method Triangular(n: int) returns (j: int)
    requires n > 0
    ensures j == (n*(n+1))/2
{
    var i := 0;
    j := 0;

    while i < n
        invariant 0 <= i <= n
        invariant j == (i*(i+1))/2
    {
        i := i + 1;
        j := j + i;
    }
}