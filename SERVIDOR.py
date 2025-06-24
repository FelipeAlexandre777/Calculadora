import socket

def calcular(operacao):
    try:
        resultado = eval(operacao)
        return str(resultado)
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    host = '10.90.36.116'
    porta = 5000
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(1)
    print("Servidor aguardando conexões...")
    
    while True:
        cliente, endereco = servidor.accept()
        print(f"Conexão recebida de {endereco}")
        
        operacao = cliente.recv(1024).decode('utf-8')

        if operacao.lower() == 'sair':
            print("Finalizando o servidor...")
            break
        
        resultado = calcular(operacao)
        
        cliente.send(resultado.encode('utf-8'))
        cliente.close()
    
    servidor.close()

