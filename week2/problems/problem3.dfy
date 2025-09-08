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
        invariant trivial_gcd(a,b,1,1) == trivial_gcd(x,y,1,1)
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


function min(a:int, b:int): int
{
    if a < b then a else b
}


// the following is a trivial implementation of gcd which is tail recursive
// (iterative, but dafny can verify via induction without needing invariants)

function trivial_gcd(a: int, b: int, gcd: int, k: int): int
  requires a >= 0 && b >= 0
  requires k > 0 && gcd > 0
  requires k <= min(a, b) + 1
  ensures trivial_gcd(a, b, gcd, k) > 0
  decreases min(a, b) - k + 1
{
  if k <= min(a, b) then
    if a % k == 0 && b % k == 0 then
      trivial_gcd(a, b, k, k+1)
    else
      trivial_gcd(a, b, gcd, k+1)
  else
    gcd
}

lemma 


