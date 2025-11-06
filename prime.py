def sum_naturals(n):
    total, k = 0, 1
    #我们需要循环加，so while
    while k<=n:
        total=total+k
        k=k+1
    return total
print(sum_naturals(2))

def sum_cubes(n):
    total,k = 0,1
    while k<=n:
        total,k = total + k*k*k,k+1
    return total
print(sum_cubes(2))

def pi_sum(n):
    total,k = 0,1
    while k <= n:
        total,k = total+8/((4*k-3)*(4*k-1)),k+1
    return total
print(pi_sum(2))


