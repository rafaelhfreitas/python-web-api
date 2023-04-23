# import socket


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("example.com", 80))

# # request
# # cmd = "GET http://example.com/index.html HTTP/1.0"
# cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()
# client.send(cmd)


# while True:
#     data = client.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end="")


# client.close()



# from urllib.request import urlopen

# result = urlopen("http://example.com/index.html")

# print(result.read())



# import requests

# result = requests.get("http://example.com/index.html")
# print(result.status_code)
# print(result.headers)
# print(result.content)



# import httpx

# print("httpx ---------------------------")
# result = httpx.get("http://example.com/index.html")
# print(result.status_code)
# print(result.headers)
# print(result.content)




import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))

# request
# cmd = "GET http://example.com/index.html HTTP/1.0"
cmd = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode()
client.send(cmd)


while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")


client.close()
