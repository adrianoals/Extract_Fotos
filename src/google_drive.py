"""
Google Drive Client para Extract Fotos
Responsável por conectar e listar arquivos do Google Drive
"""

import os
from typing import List, Dict, Optional
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle

# Escopos necessários para acessar o Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

class GoogleDriveClient:
    """Cliente para interagir com a API do Google Drive"""
    
    def __init__(self):
        """Inicializa o cliente Google Drive"""
        self.creds = None
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Autentica com o Google Drive usando OAuth 2.0"""
        # Verifica se já existe um token salvo
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        
        # Se não há credenciais válidas, faz o fluxo de autenticação
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                # Carrega credenciais do arquivo .env
                client_id = os.getenv('GOOGLE_CLIENT_ID')
                client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
                
                if not client_id or not client_secret:
                    raise ValueError("GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET devem estar configurados no .env")
                
                # Executa fluxo de autenticação OAuth 2.0
                flow = InstalledAppFlow.from_client_config({
                    'installed': {
                        'client_id': client_id,
                        'client_secret': client_secret,
                        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
                        'token_uri': 'https://oauth2.googleapis.com/token',
                        'scopes': SCOPES
                    }
                }, SCOPES)
                
                self.creds = flow.run_local_server(port=0)
            
            # Salva as credenciais para a próxima execução
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        
        # Cria o serviço do Google Drive
        self.service = build('drive', 'v3', credentials=self.creds)
    
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
    print("🧪 Testando Google Drive Client...")
    
    # Carrega variáveis de ambiente
    from dotenv import load_dotenv
    load_dotenv()
    
    try:
        client = GoogleDriveClient()
        print("✅ Cliente Google Drive inicializado com sucesso!")
        
        # Teste com um folder ID de exemplo
        test_folder_id = "test_folder_id"
        print(f"📁 Testando listagem de arquivos na pasta: {test_folder_id}")
        
        files = client.list_files_in_folder(test_folder_id)
        print(f"📊 Arquivos encontrados: {len(files)}")
        
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
