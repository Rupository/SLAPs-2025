// Problem 3: GCD Calculation
// Write loop invariant(s) for this method

method GCD(a: int, b: int) returns (gcd: int)
    requires a > 0 && b > 0
    ensures gcd > 0
    ensures a % gcd == 0 && b % gcd == 0
    ensures forall d :: d > 0 && a % d == 0 && b % d == 0 ==> d <= gcd
{
    var x := a;
    var y := b;
    
    
    while y > 0 // changed, since "decreases expression must be bounded below by 0 at end of loop iteration"

        invariant x >= 1
        invariant y >= 0
        invariant gcd_helper(a,b) == gcd_helper(x,y)
        // (see pg 19, CSUR14.pdf - this problem has been fully outlined)

        decreases y
    {
        var temp := y;
        y := x % y;
        x := temp;
    }
    
    gcd := x;
}

// inspired by the upcoming problems, i will use Helper Function(s)

function gcd_helper(a:int, b:int): int
    requires a >= 0 && b >= 0
    requires a + b > 0
    ensures gcd_helper(a,b) > 0
    ensures a % gcd_helper(a,b) == 0 && b % gcd_helper(a,b) == 0
    ensures forall d :: d > 0 && a % d == 0 && b % d == 0 ==> d <= gcd_helper(a,b)
    decreases b
{
    if b == 0 then a
    else gcd_helper(b, a % b)
}

