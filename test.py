mycursor = mydb.cursor()

clients = {}
endpoint = ""

headers = {'Content-type':'application/json', 
            'Accept':'application/json',}
raw_dump_clients = requests.get(endpoint, headers=headers).json()
for i in range(0,len(raw_dump_clients["items"])):
    client_key = raw_dump_clients["items"][i]["values"][0]
    print(client_key)
    sql = "INSERT INTO clients (id, client_name) VALUES (%s, %s)"
    val = (None, client_key)
    mycursor.execute(sql, val)
    mydb.commit()
    clients[client_key] = 0
