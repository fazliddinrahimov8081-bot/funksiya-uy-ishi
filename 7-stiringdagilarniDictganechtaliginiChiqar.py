harf = 'w3resource'
natija ={}
for belgi in harf:
    if belgi in natija:
        natija[belgi]+=1
    else:
        natija[belgi]=1
print(natija)