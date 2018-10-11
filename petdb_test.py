import petdb

#delete test
# ret = petdb.delete('하얀마음 백구')
# print('delete test:', ret)

# insert test
ret = petdb.insert({'name': '파트라슈', 'owner': '네로', 'species': 'dog', 'gender': 'f','birth': '1980-01-01'})
#print(ret)
print('insert test:', ret)


#update test
ret = petdb.update('파트라슈')
print('update test:', ret)


# fetchbyname test
result = petdb.fetchByName('하얀마음 백구')
print(result)

# fetchall test
petdb.fetchall()
