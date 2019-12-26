import json
import mysql.connector

def connect_to_sql():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Batteryatmosphere150!",
        database="battery_cost")
    return connection


def insert_to_sql(table, columns_list, data_list):
    '''Uploads selected data to specified columns in specified table.

    Inputs:
    table: str, name of the desired table in the database \n
    columns_list: python list of column names \n
    data_list: python list of data to be inserted, can be mixed type (int, double, str)
    '''

    connection = connect_to_sql()
    try:
        #Preprocess data to have proper format for SQL query:
        columns = "(" + ", ".join(columns_list) + ")"
        data = "('" + "', '".join([str(a) for a in data_list]) + "')"

        #Making query
        insert_query = f"INSERT INTO {table} {columns} VALUES {data}"
        print(insert_query)
        #Running query:
        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        print(cursor.rowcount,f"Record inserted successfully into {table} table")
        cursor.close()

    except mysql.connector.Error as error:
        print(f"Failed to insert record into {table} table {error}")

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")


def cellinput_to_sql(json_path):
    '''Uploads cell parameter input data from json file to mysql database.

    Input: .json file with the same fields as nmc111.json
    Ouput: none
    '''
    # Importing the data from cell input json
    with open(json_path) as cellInput_json:
        cellInput = json.load(cellInput_json)

    insert_to_sql('cell_input',
                  list(cellInput.keys()),
                  list(cellInput.values()))


# cellinput_to_sql(r'.\cell_inputs\nmc111.json')


def priceinput_to_sql(json_path):
    '''Uploads price input data from json file to mysql database.

    Input: .json file with the same fields as price_0.json
    Ouput: none
    '''
    # Importing the data from price input json
    with open(json_path) as priceInput_json:
        priceInput = json.load(priceInput_json)

    print("json file opened successfully")
    # print(", ".join(cellInput.keys()))

    insert_to_sql('price_input',
                  list(priceInput.keys()),
                  list(priceInput.values()))