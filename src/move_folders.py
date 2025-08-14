"""
Move Folders - Programa para mover pastas no Google Drive
Usa a Service Account configurada para operações rápidas
"""

import os
from dotenv import load_dotenv
from google_drive import GoogleDriveClient

def print_banner():
    """Exibe o banner do programa"""
    print("=" * 60)
    print("           📁 MOVE FOLDERS 📁")
    print("    Sistema de Movimentação de Pastas no Google Drive")
    print("=" * 60)
    print()

def get_folder_info(prompt: str) -> str:
    """Obtém informações de uma pasta"""
    print(f"\n{prompt}")
    print("   Para encontrar o Folder ID:")
    print("   1. Abra a pasta no Google Drive")
    print("   2. A URL será: https://drive.google.com/drive/folders/FOLDER_ID")
    print("   3. Copie o FOLDER_ID da URL")
    print()
    
    while True:
        folder_id = input("🔑 Digite o Folder ID da pasta: ").strip()
        
        if not folder_id:
            print("❌ Folder ID não pode estar vazio!")
            continue
        
        if len(folder_id) < 10:
            print("❌ Folder ID parece muito curto. Verifique novamente.")
            continue
        
        # Confirma com o usuário
        confirm = input(f"✅ Confirmar Folder ID '{folder_id}'? (s/n): ").strip().lower()
        if confirm in ['s', 'sim', 'y', 'yes']:
            return folder_id
        else:
            print("🔄 Digite o Folder ID novamente.")

def move_folder(source_folder_id: str, destination_folder_id: str) -> bool:
    """
    Move uma pasta para outro local
    
    Args:
        source_folder_id: ID da pasta origem
        destination_folder_id: ID da pasta destino
        
    Returns:
        True se sucesso, False caso contrário
    """
    try:
        print(f"\n🚀 Iniciando movimentação...")
        print(f"   📁 Origem: {source_folder_id}")
        print(f"   📁 Destino: {destination_folder_id}")
        print()
        
        # 1. Conecta ao Google Drive
        print("🔐 Conectando ao Google Drive...")
        drive_client = GoogleDriveClient()
        print("✅ Conectado com sucesso!")
        
        # 2. Obtém informações da pasta origem
        print("📋 Obtendo informações da pasta origem...")
        source_folder = drive_client.service.files().get(
            fileId=source_folder_id,
            fields='id, name, parents'
        ).execute()
        
        print(f"✅ Pasta origem: '{source_folder['name']}'")
        
        # 3. Obtém informações da pasta destino
        print("📋 Obtendo informações da pasta destino...")
        destination_folder = drive_client.service.files().get(
            fileId=destination_folder_id,
            fields='id, name'
        ).execute()
        
        print(f"✅ Pasta destino: '{destination_folder['name']}'")
        
        # 4. Move a pasta
        print("🔄 Movendo pasta...")
        
        # Remove da pasta atual e adiciona na nova
        previous_parents = ",".join(source_folder.get('parents', []))
        
        result = drive_client.service.files().update(
            fileId=source_folder_id,
            addParents=destination_folder_id,
            removeParents=previous_parents,
            fields='id, name, parents'
        ).execute()
        
        print(f"✅ Pasta '{result['name']}' movida com sucesso!")
        print(f"   📍 Nova localização: '{destination_folder['name']}'")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erro durante a movimentação: {e}")
        print("   Verifique:")
        print("   1. Se ambas as pastas estão compartilhadas com a Service Account")
        print("   2. Se a Service Account tem permissão de 'Editor'")
        print("   3. Se os Folder IDs estão corretos")
        return False

def main():
    """Função principal do programa"""
    try:
        # Carrega variáveis de ambiente
        load_dotenv()
        
        # Verifica se as credenciais da Service Account estão configuradas
        required_vars = ['GOOGLE_SERVICE_ACCOUNT_INFO']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            print("❌ Configuração incompleta!")
            print(f"   Variáveis faltando: {', '.join(missing_vars)}")
            print("   Configure o arquivo .env com suas credenciais da Service Account")
            return
        
        # Exibe banner
        print_banner()
        
        print("⚠️  IMPORTANTE: Antes de usar este programa:")
        print("   1. Compartilhe a pasta ORIGEM com a Service Account (permissão: Editor)")
        print("   2. Compartilhe a pasta DESTINO com a Service Account (permissão: Editor)")
        print("   3. A Service Account deve ter permissão de 'Editor' em ambas as pastas")
        print()
        
        # Obtém Folder IDs
        source_folder_id = get_folder_info("📁 CONFIGURAÇÃO DA PASTA ORIGEM")
        destination_folder_id = get_folder_info("📁 CONFIGURAÇÃO DA PASTA DESTINO")
        
        # Confirma a operação
        print(f"\n⚠️  CONFIRMAÇÃO FINAL:")
        print(f"   Você está prestes a mover a pasta '{source_folder_id}'")
        print(f"   para dentro da pasta '{destination_folder_id}'")
        print()
        
        confirm = input("🔒 Digite 'CONFIRMO' para prosseguir: ").strip()
        if confirm != "CONFIRMO":
            print("❌ Operação cancelada pelo usuário.")
            return
        
        # Executa a movimentação
        success = move_folder(source_folder_id, destination_folder_id)
        
        if success:
            print("\n🎉 Movimentação concluída com sucesso!")
            print("   A pasta foi movida para o novo local.")
        else:
            print("\n❌ Movimentação falhou!")
            print("   Verifique as permissões e tente novamente.")
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("   Entre em contato com o suporte técnico.")

if __name__ == "__main__":
    main()
