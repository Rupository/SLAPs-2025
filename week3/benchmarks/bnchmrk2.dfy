// sum of positive odd numbers gives positive integer squares
// inspired by NCERT exercises on Induction

method square(n: int) returns (j: int)
    requires n > 0
    ensures j == n*n
{
    var i := 1;
    j := 1;

    while i < n
        invariant 1 <= i <= n
        invariant j == i*i
    {

        j := j + (2*i + 1);
        i := i + 1;
    }
}