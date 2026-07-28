# verificador-ativos-rede

# 🌐 Verificador de Disponibilidade de Ativos de Rede (Pinger TCP)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)


Um utilitário simples e eficiente desenvolvido em Python para diagnóstico automatizado e medição de latência de ativos de rede via conexões TCP. 

O projeto foi construído utilizando apenas a **biblioteca padrão do Python**, com o objetivo de demonstrar a aplicação prática de conceitos da **Camada de Transporte** e manipulação de **sockets**.

---

## 🚀 Funcionalidades

- **Teste de Conectividade TCP:** Validação de disponibilidade de domínios ou endereços IP na porta HTTP (80) ou personalizada.
- **Medição de Latência:** Cálculo do tempo de resposta da conexão em milissegundos ($ms$).
- **Tratamento de Exceções:** Manipulação de *timeouts* e erros de socket para evitar falhas durante a varredura.
- **Feedback Visual no Terminal:** Exibição clara e formatada do status de cada alvo (`ONLINE` / `OFFLINE`).

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3
- **Módulos Nativos:** `socket` (comunicação de rede) e `time` (medição de desempenho)
- **Redes & Segurança:**
  - Modelo OSI / TCP/IP (Camada de Transporte)
  - Conexões via Sockets TCP (`AF_INET`, `SOCK_STREAM`)
  - Tratamento de *Timeouts* e exceções de rede

---

## 💻 Como Executar o Projeto

### Pré-requisitos
Ter o **Python 3.x** instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
   cd NOME-DO-REPOSITORIO
