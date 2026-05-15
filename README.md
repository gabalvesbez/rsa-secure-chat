# RSA Cryptography Engine & P2P Study 🔐
Este projeto foi desenvolvido durante o meu período de Erasmus na University of Debrecen, na unidade curricular de Criptografia. O objetivo foi implementar e otimizar o algoritmo RSA utilizando Python.

## Diferenciais de Engenharia
Ao contrário de implementações simples, este projeto foca na eficiência computacional:

Otimização com CRT (Chinese Remainder Theorem): Implementei a desencriptação utilizando o Teorema do Resto Chinês, o que reduziu o custo computacional e tornou o processamento 4x mais rápido.

Geração de Chaves Seguras: Lógica para tratamento de grandes números primos e verificação de coprimalidade.

Base para Sistemas P2P: O motor foi desenhado para ser integrado em sistemas de comunicação Peer-to-Peer seguros.

## Tecnologias e Conceitos
Linguagem: Python 3.x

Conceitos: Aritmética Modular, Teoria dos Números, Complexidade de Algoritmos.

## Como Usar
(Chat P2P)O sistema simula uma comunicação Peer-to-Peer utilizando o sistema de ficheiros para troca de mensagens cifradas.
Siga estes passos para testar a comunicação entre dois utilizadores:  
Preparar o Ambiente:
```Bash
git clone https://github.com/gabalvesbez/RSA-Encrypted-Chat.git
cd RSA-Encrypted-Chat
```
Iniciar o Utilizador 1:
Abra um terminal e execute:   
```Bash
python chat_user1.py
```
O sistema gerará automaticamente o par de chaves RSA e criará a pasta keys/.
Iniciar o Utilizador 2:
Abra um segundo terminal (ao lado do primeiro) e execute:   
```Bash
python chat_user2.py
```
## Fluxo de Mensagens:
### No User 1, escolha a opção 1 para enviar uma mensagem.   
### No User 2, escolha a opção 3 para atualizar a chave pública do User 1 e depois a opção 2 para ler a mensagem recebida.
### Observação técnica: Pode abrir o ficheiro shared_messages.txt para ver como a mensagem é armazenada de forma ilegível (cifrada) antes de ser processada pelo destinatário.   
