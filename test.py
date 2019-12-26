cellInput = {
    "cell_id":0,
    "cell_name": "NMC111v1"
}

list_columns = list(cellInput.keys())
list_data = list(cellInput.values())

columns = "(" + ", ".join(list_columns) + ")"

data = "('" + "', '".join([str(a) for a in list_data]) + "')"



print(list_columns)
print(list_data)

print(columns)
print(data)