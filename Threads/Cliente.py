import socket

def iniciar_cliente():
    host = "127.0.0.1"  # ou IP do servidor
    porta = 12345

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    print(cliente.recv(1024).decode())  # Mensagem inicial

    while True:
        msg = input("Você: ")
        cliente.send(msg.encode())
        resposta = cliente.recv(1024).decode()
        print("Servidor:", resposta)

        if msg.lower() == "sair":
            break

    cliente.close()

iniciar_cliente()
