import socket, random, requests

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Launching IPTOOLS Shell...\n\n")

while True:
    cmd = input("> ")
    if cmd.split(" ")[0] == "help":
        print("Commands:")
        print("send_byte : usage='send_byte <byteammt> <packets (* for inf)> <ip> <port>'")
        print("send_raw : usage='send_raw <raw_text> <ip> <port>'")
        print("web_request : usage='web_request <url> <requests (* for inf)>'")
    elif cmd.split(" ")[0] == "send_byte":
        if cmd.split(" ")[2] == "*":
            while True:
                byte = random.randbytes(int(cmd.split(" ")[1]))
                print(byte)
                sock.sendto(byte, (cmd.split(" ")[3], int(cmd.split(" ")[4])))
        else:
            for x in range(int(cmd.split(" ")[2])):
                byte = random.randbytes(int(cmd.split(" ")[1]))
                print(byte)
                sock.sendto(byte, (cmd.split(" ")[3], int(cmd.split(" ")[4])))
    elif cmd.split(" ")[0] == "send_raw":
        sock.sendto(bytes(cmd.split(" ")[1], "utf-8"), (cmd.split(" ")[2], int(cmd.split(" ")[3])))
    elif cmd.split(" ")[0] == "web_request":
        if cmd.split(" ")[2] == "*":
            while True:
                response = requests.get(cmd.split(" ")[1])
                print(response.status_code)
        else:
            for x in range(cmd.split(" ")[1]):
                response = requests.get(cmd.split(" ")[1])
                print(response.status_code)
    else:
        print("That command does not exist use 'help' for a list of valid commands.")