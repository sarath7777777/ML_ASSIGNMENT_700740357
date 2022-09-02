It_companies = {'Facebook','Amazon', 'Google','Cognizant', 'Microsoft', 'Apple', 'Oracle'}
M = {19, 22, 24, 20, 25, 26}
N = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(It_companies))
It_companies.add('Wipro')
print(It_companies)
it_company = {'Zoho','Tech mahindra','Infosys'}
it_companies.update(it_company)
print(it_companies)
it_companies.remove('Zoho')
print(it_companies)
O = M.union(N)
print(O)
P = M.intersection(N)
print(P)
print(M.issubset(N))
print(M.isdisjoint(N))
Q = M.union(N)
print(E)
R = N.union(M)
print(R)
symm = M.symmetric_difference(N)
print(symm)
set_ages = set(age)
print(set_ages)
print(len(age))
print(len(set_ages))