from socket import *

def create_server():
   serversocket = socket(AF_INET, SOCK_STREAM)

   try:
      serversocket.bind(('localhost', 9000))
      serversocket.listen(5)
      while(True):
         client_socket, address = serversocket.accept()
         
         rd = client_socket.recv(5000).decode()
         pieces = rd.split("\n")
         if pieces : print(pieces[0])

         data = "HTTP/1.1 200 OK\r\n"
         data += "Content-Type: text/html; charset=utf-8\r\n"
         data += "\r\n"
         data += "<html><body>Hello World!!</body</html>\r\n\r\n"
         client_socket.sendall(data.encode())
         client_socket.shutdown(SHUT_WR)

   except KeyboardInterrupt:
      print("\nShutting down...\n")
   except Exception as exc:
      print("Error:\n")
      print(exc)

   serversocket.close()

print("Access http://localhost:9000")
create_server()

# we can run http://localhost:9000 in our browser to see this