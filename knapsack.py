import sys

# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return {
            "value": 0,
            "items": list()
        }
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else:
        knapsack1 = knapSack(W-wt[n-1], wt, val, n-1)
        knapsack2 = knapSack(W, wt, val, n-1)
        items = knapsack1['items']
        if val[n-1] + knapsack1['value'] > knapsack2['value']:
            items.append(n-1)
            return {
                "value": val[n-1] + knapsack1['value'],
                "items": items
            }

        else:
            return knapsack2

val = [60, 100, 130, 170] 
wt = [20, 20, 45, 35]
W = 50
n = len(val) 
print knapSack(W , wt , val , n)