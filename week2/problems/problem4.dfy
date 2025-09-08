// Problem 4: Fast Power (Exponentiation by Squaring)
// Write loop invariant(s) for this method

method FastPower(base: int, exp: int) returns (result: int)
    requires exp >= 0
    ensures result == Power(base, exp)
{
    var x := base;
    var n := exp;
    result := 1;
    
    while n > 0
        // TODO: Write loop invariant(s)
        invariant n >= 0

        invariant Power(base, exp) == Power(x, n) * result
        // i think this invariant should be correct, it's not getting verified (checked with Smayan) - dafny keeps 
        // saying that it is not maintained. after including the lemma (see later), it is working.

        // i used a couple of examples as dry runs and noticed the pattern to arrive at this invariant which holds at
        // initialization, maintainance and termination. nothing clever...
        
        decreases n
    {
        PowerEven(x, n/2);
        // including this lemma is super necessary. it helps in the verification of the invariant during maintanance.
        // why? at the start of the loop dafny checks that if Power(base, exp) == Power(x, n) * result
        // (contd. at end of loop body)
        
        if n % 2 == 1 {
            result := result * x;
        }
 
        x := x * x;
        n := n / 2;

        // as per the variable updates above, to check maintanance, dafny now checks if Power(base, exp) == Power(x*x, n/2) * result
        // the implicit assumption here is that Power(x,n) == Power(x*x, n/2). We know this to be true as per the law of
        // exponents, but dafny is unable to unfold the recursion of the Power() function to verify this property.
        
        // including the lemma in the loop body helps dafny utilise the property when verifying invariant maintanance.
    }
}

// Helper function
function Power(base: int, exp: int): int
    requires exp >= 0
{
    if exp == 0 then 1 else base * Power(base, exp - 1)
}


// [AI Disclosure] AI assistance was needed to figue this out
lemma PowerEven(x: int, n: int)
    requires n >= 0
    ensures Power(x, 2 * n) == Power(x * x, n)
{
    if n == 0 { // base case, 1 == 1
    } else {
        PowerEven(x, n - 1); // inductive hypothesis, induction step done implictly by dafny
    }
}
