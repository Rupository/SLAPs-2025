// try putting your own file for the tool!// Nonagonal numbers - recurrence and closed form
// https://oeis.org/A001106

method Nonagonal(n: int) returns (j: int)
    requires n > 0
    ensures j == n*(7*n - 5)/2
{
    var i := 0;
    j := 0;

    while (i < n) 
        invariant i - n <= 0 
        invariant j == i*(7*i - 5)/2
    {
        i := i + 1;
        j := j + 7*i - 6;
    }
}