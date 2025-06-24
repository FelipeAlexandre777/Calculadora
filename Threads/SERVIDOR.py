import socket
import threading

def lidar_com_cliente(conexao, endereco):
    print(f"[NOVA CONEXÃO] {endereco} conectado.")
    conexao.send("Conexão estabelecida. Digite 'sair' para encerrar.".encode())

    while True:
        try:
            msg = conexao.recv(1024).decode()
            if msg.lower() == "sair":
                conexao.send("Conexão encerrada.".encode())
                break
            print(f"[{endereco}] {msg}")
            conexao.send(f"Servidor ecoou: {msg}".encode())
        except:
            break

    conexao.close()
    print(f"[DESCONECTADO] {endereco} desconectado.")

def iniciar_servidor():
    host = "127.0.0.1"  # localhost
    porta = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"[SERVIDOR ATIVO] Aguardando conexões na porta {porta}...")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")

iniciar_servidor()
