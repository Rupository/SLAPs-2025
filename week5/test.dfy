method StressTest(n: int) returns (x: int)
    requires n > 0
{
    var i := 0;
    x := 1;
    
    while (i < n && i <= n) 
        invariant 0 <= i <= n
    {
        // Path 1: Direct hit
        if (i % 3 == 0) {
            var bonus := 10; // DECLARATION inside path
            x := x + bonus;
        } 
        else {
            // Nested branching
            if (i % 3 == 1) {
                 // Path 2: Multiplier
                 x := x * 2;
            } else {
                 // Path 3: Penalty
                 x := x - 1;
            }
        }
        
        // Common update for ALL paths
        i := i + 1;
    }
}