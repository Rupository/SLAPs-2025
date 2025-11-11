// P(n) : 1 × 1! + 2 × 2! + 3 × 3! + ... + n × n! = (n + 1)! – 1, 
// Inspired by Induction exercies in NCERT

method weird_sum(n: int) returns (j: int)
    requires n > 0
    ensures j == Factorial(n+1) - 1
{
    var i := 1;
    j := 0;

    while i < n+1
        invariant 1 <= i <= n+1
        invariant j == Factorial(i) - 1
        decreases n+1-i
    {
        var i' := 0;
        var fact_i := 1;

        while i' < i
            invariant 0 <= i' <= i
            invariant fact_i == Factorial(i')
            decreases i-i'
        {
            i' := i' + 1;
            fact_i := fact_i * i';
        }
        j := j + i * fact_i;
        
        i := i + 1;
    }
}

function Factorial(n: int): int
    requires n >= 0
    decreases n
{
    if n == 0 then 1 else n * Factorial(n - 1)
}
