"""
Parser de nomes de arquivos para Extract Fotos
Responsável por extrair informações dos nomes dos arquivos de imagem
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class CondominioType(Enum):
    """Tipos de condomínio suportados"""
    COM_BLOCOS = "com_blocos"
    SEM_BLOCOS = "sem_blocos"

@dataclass
class FileInfo:
    """Informações extraídas de um arquivo"""
    filename: str
    condominio_type: CondominioType
    bloco: Optional[str] = None
    apartamento: Optional[str] = None
    leitura: Optional[str] = None
    is_valid: bool = False
    error_message: Optional[str] = None

class FileNameParser:
    """Parser para nomes de arquivos de imagem"""
    
    def __init__(self):
        """Inicializa o parser com padrões regex"""
        # Padrão para condomínio COM blocos: bloco-apartamento-leitura
        self.pattern_with_blocks = re.compile(
            r'^([A-Za-z0-9]+)-(\d+)-(\d+)(?:\.\w+)?$'
        )
        
        # Padrão para condomínio SEM blocos: apartamento-leitura
        self.pattern_without_blocks = re.compile(
            r'^(\d+)-(\d+)(?:\.\w+)?$'
        )
    
    def parse_filename(self, filename: str) -> FileInfo:
        """
        Extrai informações de um nome de arquivo
        
        Args:
            filename: Nome do arquivo a ser analisado
            
        Returns:
            FileInfo com as informações extraídas
        """
        # Remove extensão do arquivo para análise
        name_without_ext = re.sub(r'\.\w+$', '', filename)
        
        # Tenta primeiro o padrão COM blocos
        match = self.pattern_with_blocks.match(name_without_ext)
        if match:
            bloco, apartamento, leitura = match.groups()
            return FileInfo(
                filename=filename,
                condominio_type=CondominioType.COM_BLOCOS,
                bloco=bloco,
                apartamento=apartamento,
                leitura=leitura,
                is_valid=True
            )
        
        # Tenta o padrão SEM blocos
        match = self.pattern_without_blocks.match(name_without_ext)
        if match:
            apartamento, leitura = match.groups()
            return FileInfo(
                filename=filename,
                condominio_type=CondominioType.SEM_BLOCOS,
                apartamento=apartamento,
                leitura=leitura,
                is_valid=True
            )
        
        # Se não encontrou padrão válido
        return FileInfo(
            filename=filename,
            condominio_type=CondominioType.COM_BLOCOS,  # Default
            is_valid=False,
            error_message="Nome do arquivo não segue os padrões esperados"
        )
    
    def parse_multiple_files(self, filenames: List[str]) -> List[FileInfo]:
        """
        Processa múltiplos nomes de arquivo
        
        Args:
            filenames: Lista de nomes de arquivos
            
        Returns:
            Lista de FileInfo processados
        """
        results = []
        for filename in filenames:
            file_info = self.parse_filename(filename)
            results.append(file_info)
        
        return results
    
    def get_statistics(self, files_info: List[FileInfo]) -> Dict:
        """
        Gera estatísticas dos arquivos processados
        
        Args:
            files_info: Lista de FileInfo processados
            
        Returns:
            Dicionário com estatísticas
        """
        total_files = len(files_info)
        valid_files = sum(1 for f in files_info if f.is_valid)
        invalid_files = total_files - valid_files
        
        # Conta tipos de condomínio
        with_blocks = sum(1 for f in files_info if f.condominio_type == CondominioType.COM_BLOCOS and f.is_valid)
        without_blocks = sum(1 for f in files_info if f.condominio_type == CondominioType.SEM_BLOCOS and f.is_valid)
        
        # Arquivos com erro
        error_files = [f for f in files_info if not f.is_valid]
        
        return {
            'total_files': total_files,
            'valid_files': valid_files,
            'invalid_files': invalid_files,
            'with_blocks': with_blocks,
            'without_blocks': without_blocks,
            'error_files': error_files,
            'success_rate': (valid_files / total_files * 100) if total_files > 0 else 0
        }
    
    def validate_data(self, file_info: FileInfo) -> bool:
        """
        Valida os dados extraídos
        
        Args:
            file_info: FileInfo a ser validado
            
        Returns:
            True se válido, False caso contrário
        """
        if not file_info.is_valid:
            return False
        
        # Validações específicas
        if file_info.condominio_type == CondominioType.COM_BLOCOS:
            if not file_info.bloco or not file_info.apartamento or not file_info.leitura:
                return False
            
            # Valida bloco (deve ser alfanumérico)
            if not re.match(r'^[A-Za-z0-9]+$', file_info.bloco):
                return False
            
            # Valida apartamento (deve ser número)
            if not re.match(r'^\d+$', file_info.apartamento):
                return False
            
            # Valida leitura (deve ser número)
            if not re.match(r'^\d+$', file_info.leitura):
                return False
        
        elif file_info.condominio_type == CondominioType.SEM_BLOCOS:
            if not file_info.apartamento or not file_info.leitura:
                return False
            
            # Valida apartamento (deve ser número)
            if not re.match(r'^\d+$', file_info.apartamento):
                return False
            
            # Valida leitura (deve ser número)
            if not re.match(r'^\d+$', file_info.leitura):
                return False
        
        return True

# Função de conveniência para uso direto
def parse_file_list(filenames: List[str]) -> Tuple[List[FileInfo], Dict]:
    """
    Função simples para processar uma lista de nomes de arquivos
    
    Args:
        filenames: Lista de nomes de arquivos
        
    Returns:
        Tupla com (lista de FileInfo, estatísticas)
    """
    parser = FileNameParser()
    files_info = parser.parse_multiple_files(filenames)
    stats = parser.get_statistics(files_info)
    
    return files_info, stats

if __name__ == "__main__":
    # Teste básico da classe
    print("🧪 Testando File Name Parser...")
    
    # Exemplos de teste
    test_files = [
        "A-101-1234.jpg",      # COM blocos
        "B-205-5678.png",      # COM blocos
        "101-1234.jpg",        # SEM blocos
        "205-5678.png",        # SEM blocos
        "invalid-name.txt",    # Inválido
        "A101-1234.jpg",       # Inválido (sem hífen)
    ]
    
    try:
        parser = FileNameParser()
        files_info, stats = parse_file_list(test_files)
        
        print(f"📊 Estatísticas:")
        print(f"   Total de arquivos: {stats['total_files']}")
        print(f"   Arquivos válidos: {stats['valid_files']}")
        print(f"   Arquivos inválidos: {stats['invalid_files']}")
        print(f"   COM blocos: {stats['with_blocks']}")
        print(f"   SEM blocos: {stats['without_blocks']}")
        print(f"   Taxa de sucesso: {stats['success_rate']:.1f}%")
        
        print(f"\n📁 Detalhes dos arquivos:")
        for file_info in files_info:
            status = "✅" if file_info.is_valid else "❌"
            if file_info.is_valid:
                if file_info.condominio_type == CondominioType.COM_BLOCOS:
                    print(f"   {status} {file_info.filename} -> Bloco: {file_info.bloco}, Apt: {file_info.apartamento}, Leitura: {file_info.leitura}")
                else:
                    print(f"   {status} {file_info.filename} -> Apt: {file_info.apartamento}, Leitura: {file_info.leitura}")
            else:
                print(f"   {status} {file_info.filename} -> {file_info.error_message}")
        
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
