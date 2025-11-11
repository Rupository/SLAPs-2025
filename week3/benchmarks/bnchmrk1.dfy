// lucas numbers: 2, 1, 3, 4, 7, 11, 18, ...
// inspired by ICS and DM

method Lucas(n: int) returns (x : int)
    requires n >= 1
    ensures x == lucas(n)
{
    x := 2;
    var y := 1;
    var temp;
    var i := 1;

    while i < n
        invariant 1 <= i <= n
        invariant x == lucas(i)
        invariant y == lucas(i+1)
        
        decreases n - i
    {
        temp := y;
        y := y + x;
        x := temp;

        i := i+1;
    }
}

function lucas(n: int): int
    requires n >= 1
    decreases n
{
    if n == 1 then 2
    else if n == 2 then 1

    else lucas(n-2) + lucas(n-1)
}

// 