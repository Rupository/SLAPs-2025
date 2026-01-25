// [AI DISCLOSURE] - Generated test case for disjunctive invariant synthesis
method ComputeWeightedSum(limit: int) returns (total: int)
  requires limit >= 0
  ensures total >= limit
{
  var i := 0;
  total := 0;

  while (i < limit)
    invariant 0 <= i <= limit
    invariant total >= i 
  {
    if i < 10 {
      total := total + 1;
    } 
    else if i < 20 {
      total := total + 2;
    }
    else {
      total := total + 3;
    }
    
    i := i + 1;
  }
}