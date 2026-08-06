import socket

import time 

def verificar_site(host, porta=80, timeout=3):
    """
    Tenta estabelecer uma conexão TCP com o host informado.
    Retorna Status (True/False) e Latência em milissegundos (ms).
    """
    # Cria o socket IPv4 (AF_INET) usando o protocolo TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout) # Tempo limite de espera antes de considerar OFFLINE
    
    inicio = time.time()
    try:
        # Tenta conectar ao host na porta especificada
        s.connect((host, porta))
        
        # Calcula o tempo gasto e converte para milissegundos
        tempo_resposta = (time.time() - inicio) * 1000 
        s.close()
        return True, tempo_resposta
        
    except (socket.timeout, socket.error):
        s.close()
        return False, 0
    


# Lista de alvos para diagnóstico (pode alterar/adicionar conforme desejar)
alvos = [
    "google.com",
    "github.com",
    "1.1.1.1",
    "site-inexistente-teste-1234.com"
]

# Execução e exibição dos resultados
print("=" * 45)
print("   INICIANDO VERIFICAÇÃO DE DISPONIBILIDADE   ")
print("=" * 45)

for alvo in alvos:
    status, latencia = verificar_site(alvo)
    
    if status:
        print(f"[ONLINE]  {alvo:<32} | Latência: {latencia:.2f} ms")
    else:
        print(f"[OFFLINE] {alvo:<32} | Não respondeu")

print("=" * 45)
