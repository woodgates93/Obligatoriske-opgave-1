from socket import *
import json

servername = 'localhost'
serverport = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))


for _ in range(3):
    method = input('hvilken matematisk funktion? (Add/Random/Subtract):')
    num1 = int( input('dit første nummer'))
    num2 = int(input('dit andet nummer'))

    if method not in ["Add", "Random", "Subtract"]:
        print("Ugyldig metode")
        continue
    
    request = {"method": method, "Num1": num1, "Num2": num2}
    data = json.dumps(request).encode()


    clientSocket.send(data)

    response = clientSocket.recv(2048).decode()
    response_data = json.loads(response)

    if "error" in response_data:
        print(f'Fejl: {response_data["error"]}')
    elif "result" in response_data:
        print(f'Resulatet: {response_data["result"]}')
   

    
clientSocket.close()