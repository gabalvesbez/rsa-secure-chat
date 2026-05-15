RSA Cryptography Engine & P2P Study 🔐
Este projeto foi desenvolvido durante o meu período de Erasmus na University of Debrecen, na unidade curricular de Criptografia. O objetivo foi implementar e otimizar o algoritmo RSA utilizando Python.

🚀 Diferenciais de Engenharia
Ao contrário de implementações simples, este projeto foca na eficiência computacional:

Otimização com CRT (Chinese Remainder Theorem): Implementei a desencriptação utilizando o Teorema do Resto Chinês, o que reduziu o custo computacional e tornou o processamento 4x mais rápido.

Geração de Chaves Seguras: Lógica para tratamento de grandes números primos e verificação de coprimalidade.

Base para Sistemas P2P: O motor foi desenhado para ser integrado em sistemas de comunicação Peer-to-Peer seguros.

🛠️ Tecnologias e Conceitos
Linguagem: Python 3.x

Conceitos: Aritmética Modular, Teoria dos Números, Complexidade de Algoritmos.

📦 Como Executar
Bash
python RSA.py
```bash
# Terminal 1 - User1
python src/chat_user1.py

# Terminal 2 - User2  
python src/chat_user2.py
