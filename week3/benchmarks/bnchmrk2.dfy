// pentagonal numbers - recurrence and closed form
// https://en.wikipedia.org/wiki/Pentagonal_number

method Pentagonal(n: int) returns (j: int)
    requires n > 0
    ensures j == (3*n*n - n)/2
{
    var i := 1;
    j := 1;

    while (i < n)
        invariant 1 <= i <= n
        invariant j == (3*i*i - i)/2
    {
        i := i + 1;
        j := j + 3*i - 2;
    }
}