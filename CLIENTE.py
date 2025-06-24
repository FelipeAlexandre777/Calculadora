import socket

host = '10.90.36.116'
porta = 5000

def enviar_operacao(host, porta, operacao):
    try:
        soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soquete.connect((host, porta))
        
        soquete.send(operacao.encode('utf-8'))

        resultado = soquete.recv(1024).decode('utf-8')
        
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro ao conectar com o servidor: {e}")
    finally:
        soquete.close()

if __name__ == "__main__":
    while True:
        operacao = input("Digite a operação (ou 'sair' para encerrar): ")
        
        if operacao.lower() == 'sair':
            break
        
        enviar_operacao(host, porta, operacao)


