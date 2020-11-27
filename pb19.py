def diviseurs(n):
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    return lst

def somme_liste(n):
    s=0
    for i in diviseurs(n):
        s+=i
    return s

def est_abondant(n):
    return somme_liste(n)>n


abondants = []

for i in range(28123+1):
    if est_abondant(i):
        abondants.append(i)


k=len(abondants)

decomposables = set([])
for i in range(k):
    for j in range(i, k):
        l=abondants[i]+abondants[j]
        if l > 28123:
            break
        decomposables.add(abondants[i]+abondants[j])

somme_decomposables = 0
for i in decomposables:
    somme_decomposables += i
print ((28123*(28123+1))//2 - somme_decomposables)
