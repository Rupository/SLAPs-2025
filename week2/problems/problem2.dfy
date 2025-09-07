// Problem 2: Integer Division (Quotient & Remainder)
// Write loop invariant(s) for this method

method IntegerDivision(dividend: int, divisor: int) returns (quotient: int, remainder: int)
    requires divisor > 0
    requires dividend >= 0 // NEEDED TO BE ADDED - the method would fail if we keep
    // negative integers as dividends, there is no handling for negative quotients!

    ensures dividend == divisor * quotient + remainder
    ensures 0 <= remainder < divisor
    
{
    quotient := 0;
    remainder := dividend;
    
    while remainder >= divisor
        
        invariant dividend == divisor * quotient + remainder
        // we must generalise this postcondition (CSUR14.pdf) to arrive at a statement
        // which remains true at initialization, throughout ({I} S {B} => {I}) the loop body
        // and on termination (I AND NOT B => Q).

        // we start by attempting to generalise the postcondition: dividend == divisor * quotient + remainder
        // we realise that we don't need to generalise this further as this holds by default. we are utilising
        // the fact that division of positive integers is repeated subtraction till the smallest possible +ve 
        // remainder is reached. 

        invariant 0 <= remainder
        // postcondition: 0 <= remainder < divisor

        // genaralising, we note that it is possible for the remainder to exceed the divisor
        // at stages (for example, if remainder = dividend >= divisor)

        // thus, remainder < divisor cannot hold for our generalisation and we drop it.

        // note that 0 <= remainder always holds.
        // [INIT]: remainder = dividend >= 0
        // [MAIN]: As per the Loop Condition, remainder >= divisor (> 0). So remainder > 0 --> remainder >= 0
        // [TERM]: In the final iteration of the loop, we start with remainder >= divisor. on computing
        // remainder := remainder - divisor, we will have 0 <= remainder < divisor (as the loop condition
        // will no longer be met after the final iteration). Thus, remainder >= 0

        // we also arrive at our postcondition via termination.

    {
        quotient := quotient + 1;
        remainder := remainder - divisor;
    }
}
