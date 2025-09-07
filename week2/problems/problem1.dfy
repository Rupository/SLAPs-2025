// Problem 1: Simple Loop with Two Variables
// Write loop invariant(s) for this method

method loop(n: int) returns (j: int)
    requires n >= 0
    ensures j == 2 * n // Postcondition
{
    // Precondtion P
    var i := 0;
    j := 0;
    
    while i < n // Loop Condition (B)

        invariant 0 <= i <= n
        // invariant to ensure that Loop Condition is met, and for Termination
        // at the end of the loop, (i <= n) AND (i >= n) := (i = n) => Q (Postcondition) 

        invariant j == 2*i
        // we want to arrive at the postcondition j = 2*n 

        // we must generalise this postcondition (CSUR14.pdf) to arrive at a statement
        // which remains true at initialization, throughout ({I} S {B} => {I}) the loop body
        // and on termination (I AND NOT B => Q).

        // observe that j = 2*n is equivalent to saying
        // j = 2*i where i = n

        // inductively, we can show that j =  2*i holds for all iterations of the loop
        // (Base Case) i = 0, j = 0 (set at P, j = 0 = 2*0 = 2*i)

        // (Inductive Hypothesis and Induction Step) Suppose j = 2i at some iteration k in the loop. 
        // From S, on the (k+1)th iteration,
        // i := i+1

        // j := j+2 = 2i+2 = 2(i+1)
        // But i := i+1

        // So j = 2i

        decreases n - i
    {
        // Loop Body S
        i := i + 1;
        j := j + 2;
    }
}
