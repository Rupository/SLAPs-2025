// Heptagonal numbers - recurrence and closed form
// https://oeis.org/A000566

method Heptagonal(n: int) returns (j: int)
    requires n > 0
    ensures j == n*(5*n - 3)/2
{
    var i := 0;
    j := 0;

    while (i < n) invariant true ==> -5*i*i + 2*j - 120*n + 105 <= 0 && 5*i*i - 3*i - 2*j == 0 && i - n <= 0 && -5*i*i + 2*j <= 0
        //invariant 0 <= i <= n
        //invariant j == i*(5*i - 3)/2
    {
        i := i + 1;
        j := j + 5*i - 4;
    }
}