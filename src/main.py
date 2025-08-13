"""
Arquivo principal do Extract Fotos
Interface CLI interativa e orquestração de todos os componentes
"""

import os
import sys
from dotenv import load_dotenv
from typing import List, Dict

# Importa os módulos locais
from google_drive import GoogleDriveClient
from parser import FileNameParser, parse_file_list
from excel_generator import generate_excel_report

def print_banner():
    """Exibe o banner do programa"""
    print("=" * 60)
    print("           🏢 EXTRACT FOTOS 🏢")
    print("    Sistema de Extração de Dados de Condomínios")
    print("=" * 60)
    print()

def print_menu():
    """Exibe o menu de opções"""
    print("📋 Escolha o tipo de condomínio:")
    print("   1. COM blocos (formato: bloco-apartamento-leitura)")
    print("   2. SEM blocos (formato: apartamento-leitura)")
    print("   3. Sair")
    print()

def get_user_choice() -> int:
    """Obtém a escolha do usuário"""
    while True:
        try:
            choice = input("🔢 Digite sua opção (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("❌ Opção inválida! Digite 1, 2 ou 3.")
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            sys.exit(0)
        except Exception:
            print("❌ Erro na entrada. Tente novamente.")

def get_folder_id() -> str:
    """Obtém o Folder ID do usuário"""
    print("\n📁 Configuração da pasta do Google Drive")
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

def process_files(folder_id: str, condominio_type: int) -> bool:
    """
    Processa os arquivos da pasta do Google Drive
    
    Args:
        folder_id: ID da pasta no Google Drive
        condominio_type: Tipo de condomínio (1=com blocos, 2=sem blocos)
        
    Returns:
        True se sucesso, False caso contrário
    """
    try:
        print(f"\n🚀 Iniciando processamento...")
        print(f"   📁 Pasta: {folder_id}")
        print(f"   🏢 Tipo: {'COM blocos' if condominio_type == 1 else 'SEM blocos'}")
        print()
        
        # 1. Conecta ao Google Drive
        print("🔐 Conectando ao Google Drive...")
        drive_client = GoogleDriveClient()
        print("✅ Conectado com sucesso!")
        
        # 2. Lista arquivos da pasta
        print("📋 Listando arquivos da pasta...")
        files = drive_client.list_files_in_folder(folder_id)
        
        if not files:
            print("❌ Nenhum arquivo de imagem encontrado na pasta!")
            return False
        
        print(f"✅ Encontrados {len(files)} arquivos de imagem")
        
        # 3. Extrai nomes dos arquivos
        print("📝 Extraindo nomes dos arquivos...")
        filenames = [file['name'] for file in files]
        
        # 4. Processa nomes dos arquivos
        print("🔍 Processando nomes dos arquivos...")
        parser = FileNameParser()
        files_info, stats = parse_file_list(filenames)
        
        # 5. Exibe estatísticas
        print("\n📊 Estatísticas do processamento:")
        print(f"   📁 Total de arquivos: {stats['total_files']}")
        print(f"   ✅ Arquivos válidos: {stats['valid_files']}")
        print(f"   ❌ Arquivos inválidos: {stats['invalid_files']}")
        print(f"   🏢 COM blocos: {stats['with_blocks']}")
        print(f"   🏠 SEM blocos: {stats['without_blocks']}")
        print(f"   📈 Taxa de sucesso: {stats['success_rate']:.1f}%")
        
        # 6. Verifica se há arquivos válidos
        if stats['valid_files'] == 0:
            print("\n❌ Nenhum arquivo válido encontrado!")
            print("   Verifique se os nomes seguem o padrão esperado.")
            return False
        
        # 7. Gera relatório Excel
        print("\n📊 Gerando relatório Excel...")
        timestamp = f"{'com_blocos' if condominio_type == 1 else 'sem_blocos'}_{len(files_info)}_arquivos"
        output_file = generate_excel_report(files_info, f"extract_fotos_{timestamp}.xlsx")
        
        print(f"✅ Relatório gerado com sucesso: {output_file}")
        
        # 8. Exibe resumo final
        print("\n🎉 Processamento concluído com sucesso!")
        print(f"   📊 Arquivos processados: {stats['valid_files']}")
        print(f"   📁 Relatório salvo: {output_file}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erro durante o processamento: {e}")
        print("   Verifique suas credenciais e tente novamente.")
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
            print("   Configure o arquivo .env com o conteúdo JSON da sua Service Account")
            return
        
        # Exibe banner
        print_banner()
        
        while True:
            # Exibe menu
            print_menu()
            
            # Obtém escolha do usuário
            choice = get_user_choice()
            
            if choice == 3:
                print("\n👋 Obrigado por usar o Extract Fotos!")
                break
            
            # Obtém Folder ID
            folder_id = get_folder_id()
            
            # Processa arquivos
            success = process_files(folder_id, choice)
            
            if success:
                # Pergunta se quer processar outra pasta
                print("\n🔄 Deseja processar outra pasta?")
                another = input("   Digite 's' para sim ou qualquer tecla para sair: ").strip().lower()
                if another not in ['s', 'sim', 'y', 'yes']:
                    print("\n👋 Obrigado por usar o Extract Fotos!")
                    break
            else:
                # Em caso de erro, pergunta se quer tentar novamente
                print("\n🔄 Deseja tentar novamente?")
                retry = input("   Digite 's' para sim ou qualquer tecla para sair: ").strip().lower()
                if retry not in ['s', 'sim', 'y', 'yes']:
                    print("\n👋 Obrigado por usar o Extract Fotos!")
                    break
            
            print("\n" + "=" * 60 + "\n")
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("   Entre em contato com o suporte técnico.")

if __name__ == "__main__":
    main()
