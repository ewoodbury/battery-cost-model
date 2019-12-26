myDict = {
    "cell_id":0,
    "cell_name": "NMC111v1"
}

list_1 = list(myDict.values())

data = ', '.join([str(a) for a in list_1])
columns = ', '.join(myDict.keys())


print(data)