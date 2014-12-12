diction = {'name': 'chris', 'city': 'seattle', 'cake': 'chocolate'}
print(diction) 
diction.pop('cake')
print(diction)
diction['fruit'] = 'mango'
print(diction)
print(diction.keys())
print(diction.values())
print('cake' in diction.keys())
print('mango' in diction.values())

num = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
hexi = (0,1,2,3,4,5,6,7,8,9,'A','B', 'C','D','E','F')
for i,j in zip(num, hexi):
    combo = {(i,j)}
    print(combo)
#print(num)
#print(hexi)