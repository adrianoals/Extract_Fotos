"""
Google Drive Client para Extract Fotos
Responsável por conectar e listar arquivos do Google Drive usando Service Account
"""

import os
import json
from typing import List, Dict, Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Escopos necessários para acessar o Google Drive
# 'drive.readonly' = só leitura
# 'drive' = leitura + escrita + modificação
SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleDriveClient:
    """Cliente para interagir com a API do Google Drive usando Service Account"""
    
    def __init__(self):
        """Inicializa o cliente Google Drive com Service Account"""
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Autentica com o Google Drive usando Service Account"""
        try:
            # Obtém as credenciais do arquivo .env
            service_account_info = os.getenv('GOOGLE_SERVICE_ACCOUNT_INFO')
            
            if not service_account_info:
                raise ValueError(
                    "GOOGLE_SERVICE_ACCOUNT_INFO deve estar configurado no .env\n"
                    "Cole o conteúdo JSON da sua Service Account nesta variável"
                )
            
            try:
                # Converte a string JSON para dicionário
                credentials_dict = json.loads(service_account_info)
            except json.JSONDecodeError:
                raise ValueError(
                    "GOOGLE_SERVICE_ACCOUNT_INFO deve conter JSON válido\n"
                    "Verifique se o JSON foi copiado corretamente"
                )
            
            # Cria credenciais da Service Account
            credentials = service_account.Credentials.from_service_account_info(
                credentials_dict, 
                scopes=SCOPES
            )
            
            # Cria o serviço do Google Drive
            self.service = build('drive', 'v3', credentials=credentials)
            
            print("✅ Autenticação com Service Account realizada com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro na autenticação: {e}")
            raise
    
    def list_files_in_folder(self, folder_id: str) -> List[Dict]:
        """
        Lista todos os arquivos de imagem em uma pasta específica
        
        Args:
            folder_id: ID da pasta no Google Drive
            
        Returns:
            Lista de arquivos com informações (id, name, mimeType)
        """
        try:
            # Tipos MIME de imagens suportadas
            image_mime_types = [
                'image/jpeg',
                'image/jpg', 
                'image/png',
                'image/gif',
                'image/bmp',
                'image/webp'
            ]
            
            # Query para buscar apenas arquivos de imagem na pasta
            query = f"'{folder_id}' in parents and trashed=false and ({' or '.join([f'mimeType=\'{mime}\'' for mime in image_mime_types])})"
            
            results = []
            page_token = None
            
            while True:
                response = self.service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType, size)',
                    pageToken=page_token
                ).execute()
                
                files = response.get('files', [])
                results.extend(files)
                
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break
            
            print(f"✅ Encontrados {len(results)} arquivos de imagem na pasta")
            return results
            
        except HttpError as error:
            print(f"❌ Erro ao listar arquivos: {error}")
            return []
    
    def get_file_info(self, file_id: str) -> Optional[Dict]:
        """
        Obtém informações detalhadas de um arquivo específico
        
        Args:
            file_id: ID do arquivo no Google Drive
            
        Returns:
            Dicionário com informações do arquivo ou None se erro
        """
        try:
            file = self.service.files().get(
                fileId=file_id,
                fields='id, name, mimeType, size, createdTime, modifiedTime'
            ).execute()
            
            return file
            
        except HttpError as error:
            print(f"❌ Erro ao obter informações do arquivo {file_id}: {error}")
            return None
    
    def test_connection(self) -> bool:
        """
        Testa a conexão com o Google Drive
        
        Returns:
            True se conectado com sucesso, False caso contrário
        """
        try:
            # Tenta listar arquivos (limite 1 para teste rápido)
            response = self.service.files().list(
                pageSize=1,
                fields='files(id, name)'
            ).execute()
            
            print("✅ Conexão com Google Drive testada com sucesso!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao testar conexão: {e}")
            return False

# Função de conveniência para uso direto
def get_files_from_folder(folder_id: str) -> List[Dict]:
    """
    Função simples para obter arquivos de uma pasta
    
    Args:
        folder_id: ID da pasta no Google Drive
        
    Returns:
        Lista de arquivos encontrados
    """
    client = GoogleDriveClient()
    return client.list_files_in_folder(folder_id)

if __name__ == "__main__":
    # Teste básico da classe
    print("🧪 Testando Google Drive Client com Service Account...")
    
    # Carrega variáveis de ambiente
    from dotenv import load_dotenv
    load_dotenv()
    
    try:
        client = GoogleDriveClient()
        print("✅ Cliente Google Drive inicializado com sucesso!")
        
        # Testa conexão
        if client.test_connection():
            print("✅ Conexão com Google Drive funcionando!")
        else:
            print("❌ Problema na conexão com Google Drive")
        
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
        print("\n💡 Verifique:")
        print("   1. Se o arquivo .env está configurado corretamente")
        print("   2. Se GOOGLE_SERVICE_ACCOUNT_INFO contém JSON válido")
        print("   3. Se as APIs do Google Drive estão habilitadas")
        print("   4. Se a Service Account tem permissões adequadas")
