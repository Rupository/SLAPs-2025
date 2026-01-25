// Nonagonal numbers - recurrence and closed form
// https://oeis.org/A001106

method Nonagonal(n: int) returns (j: int)
    requires n > 0
    ensures j == n*(7*n - 5)/2
{
    var i := 0;
    j := 0;

    while (i < n) invariant true ==> i - n <= 0 && 7*i*i - 5*i - 2*j == 0 && -7*i*i - 11*i + 2*j <= 0 && -7*i*i + 2*j - 49*n + 26 <= 0
        //invariant i - n <= 0 
        //invariant j == i*(7*i - 5)/2
    {
        i := i + 1;
        j := j + 7*i - 6;
    }
}