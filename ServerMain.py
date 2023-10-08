from socket import *
import threading
import json
import random

def handleOneClient(connectionSocket, address):
    print ('Adresse', addr)
    while True: 
        data = connectionSocket.recv(2048)
        if not data:
            break
        
        try:
            request = json.loads(data.decode())
            if "method" not in request:
                response = {"Error": "Missing 'method'" }
            else:
                method = request["method"]
                if method == "Random":
                    if "Num1" in request and "Num2" in request:
                        num1 = request["Num1"]
                        num2 = request["Num2"]
                        result = random.randint(num1, num2)
                        response = {"result": result}
                    else:
                        response =  {"error": "Missing 'Num1' or 'num2'"}
                elif method == "Add":
                    if "Num1" in request and "Num2" in request:
                        num1 = request["Num1"]
                        num2 = request["Num2"]
                        result = num1 + num2
                        response = {"result": result}
                    else:
                        response = {"error": "Missing 'Num1' or Num2'"}
                elif method =="Subtract":
                    if "Num1" in request and "Num2" in request:
                        num1 = request["Num1"]
                        num2 = request["Num2"]
                        result = num1 - num2
                        response = {"result": result}
                    else:
                        response = {"error": "Missing 'Num1' or 'Num2'"}
                else:
                    response = {"error": "Unkown method"}
        except json.JSONDecodeError:
            response = {"error": "Cant read JSON format"}
        
    
        connectionSocket.send(json.dumps(response).encode())
    connectionSocket.close()


serverport = 12345

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print ('the server is ready')

while 1:
    csock, addr = serverSocket.accept()
    threading.Thread(target=handleOneClient, args=(csock,addr)).start()