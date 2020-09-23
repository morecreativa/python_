import operator

trainDic, trainList={},[]

trainDic={
    'Thomas' : 'T',
    'Edward' : 'E',
    'What' : 'W',
}

trainList=sorted(trainDic.items(),key=operator.itemgetter(0))

# key is unique
# List use [] , Hashing Key & Dictionary use {}
print('Default= '+str(trainDic) + str(trainList))
print('keys  = ' + str(list(trainDic.keys())) +' '+ str(trainList))
print('tuple = '+  str(list(trainDic.items())) +' '+ str(trainList))
print('values= '+  str(list(trainDic.values())) +' '+ str(trainList))
print('Getter= '+  str((trainDic.get('Thomas'))) +' '+ str(trainList))

numList=[num+1 for num in range(1,6)]
print(numList)

foods=[]
sizds=[]

tupList=list(zip(foods,sizds))
dicT=dict(zip(foods,sizds))