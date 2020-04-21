def equalSubSetSumPartition(s):
    n = len(s)
    tot = sum(s)
    
    if tot%2:
        return []
    
    tgt = tot//2
    
    p = [[() for _ in range(tgt+1)] for _ in range(n)]
    dp = [[False for _ in range(tgt+1)] for _ in range(n)]
    dp[0][0] = True
    
    for i in range(1,n):
        for j in range(tgt+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-s[i]]
            if dp[i-1][j] :
                p[i][j] = (i-1,j)
            if dp[i-1][j-s[i]]:
                p[i][j] = (i-1,j-s[i])
             
    print(p)
    return dp[n-1][tgt]
       
inp = [9,1,5,2,5]
print (equalSubSetSumPartition(inp))
