# chat_user2.py
import os
from rsa_core import *

class ChatUser:
    def __init__(self, user_name):
        self.user_name = user_name
        ensure_directories()  
        self.load_or_generate_keys()
        self.load_other_user_public_key()
    
    def load_or_generate_keys(self):
        """Carrega chaves existentes ou gera novas"""
        if not os.path.exists("keys"):
            os.makedirs("keys")
            
        try:
            self.public_key = load_key_from_file(f"keys/{self.user_name}_public.txt")
            self.private_key = load_key_from_file(f"keys/{self.user_name}_private.txt")
            print(f"✅ Chaves de {self.user_name} carregadas!")
        except FileNotFoundError:
            print(f"🔑 Gerando novas chaves para {self.user_name}...")
            self.public_key, self.private_key = generate_rsa_keys(64)
            save_key_to_file(self.public_key, f"keys/{self.user_name}_public.txt")
            save_key_to_file(self.private_key, f"keys/{self.user_name}_private.txt")
            print(f"✅ Novas chaves geradas e salvas!")
    
    def load_other_user_public_key(self):
        """Carrega chave pública do outro usuário"""
        other_user = "user2" if self.user_name == "user1" else "user1"
        try:
            self.other_public_key = load_key_from_file(f"keys/{other_user}_public.txt")
            print(f"✅ Chave pública de {other_user} carregada!")
        except FileNotFoundError:
            print(f"⏳ Aguardando chave pública de {other_user}...")
            self.other_public_key = None
    
    def send_message(self, message):
        """Criptografa e envia mensagem"""
        if not self.other_public_key:
            print("❌ Erro: Chave pública do destinatário não disponível")
            print("   Execute o outro usuário primeiro para gerar as chaves")
            return
        
        try:
            encrypted = safe_encrypt_text(message, self.other_public_key)
            
            with open("shared_messages.txt", "a", encoding="utf-8") as f:
                f.write(f"{self.user_name}:{encrypted}\n")
            
            print(f"📤 Mensagem enviada: '{message}'")
            print(f"   🔐 Criptografada como: {encrypted}")
            
        except ValueError as e:
            print(f"❌ Erro: {e}")
            print("   Tente uma mensagem mais curta")
    
    def check_messages(self):
        """Verifica e descriptografa novas mensagens"""
        try:
            with open("shared_messages.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return []
        
        my_messages = []
        for line in lines:
            try:
                sender, encrypted = line.strip().split(":")
                if sender != self.user_name:  # Mensagens para mim
                    decrypted_text = safe_decrypt_text(int(encrypted), self.private_key)
                    my_messages.append(f"{sender}: {decrypted_text}")
            except (ValueError, IndexError):
                continue
        
        return my_messages

def main():
    print("🚀 Iniciando Chat - User2")
    user = ChatUser("user2")
    
    while True:
        print("\n" + "="*40)
        print("💬 CHAT USER2")
        print("="*40)
        print("1. 📤 Enviar mensagem")
        print("2. 📥 Ver mensagens recebidas")
        print("3. 🔄 Atualizar chaves do user1")
        print("4. 🚪 Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            message = input("Digite sua mensagem: ")
            if message.strip():
                user.send_message(message)
            else:
                print("❌ Mensagem vazia!")
                
        elif choice == "2":
            messages = user.check_messages()
            if messages:
                print("\n--- 📨 MENSAGENS RECEBIDAS ---")
                for i, msg in enumerate(messages, 1):
                    print(f"{i}. {msg}")
            else:
                print("📭 Nenhuma mensagem nova.")
                
        elif choice == "3":
            user.load_other_user_public_key()
            
        elif choice == "4":
            print("👋 Até logo!")
            break
            
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()