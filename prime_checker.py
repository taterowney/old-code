from num_archive import get_primes
print('loading...')
P=list(get_primes())
print('done')

ans=True

print('processing...')
for val in P:
    prod=1
    for elem in P:
        prod*=elem
        if elem>=val:
            break
    if prod>99990:
        break
#    if not(prod+1 in P and prod-1 in P):
    if not(prod+1 in P):
        ans=False
        print(prod+1)

print()
print(ans)
