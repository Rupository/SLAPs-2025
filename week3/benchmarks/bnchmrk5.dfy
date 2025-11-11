// Permutation
// Inspired by ICS, Factorial example in week 1

method Permutation(n: int, k:int) returns (j:int)
    requires n >= 0
    requires 0 <= k <= n
    ensures j == permutation(n,k)
{
    var i := 0;
    j := 1;

    while i < k
        invariant 0 <= i <= k
        invariant j == permutation(n,i)
        decreases k-i
    {
        j := j*(n-i);
        i := i+1;
    }
}

function permutation(n:int, k:int) : int
    requires n >= 0
    requires 0 <= k <= n
{
    if k == 0 then 1
    else (permutation(n,k-1))*(n-k+1)
}