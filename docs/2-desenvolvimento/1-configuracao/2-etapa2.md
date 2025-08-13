## ** Próximas Ações (Etapa 2):**

### **2.1 Instalação do `uv` e Dependências**

```bash
# Instalar uv (se não tiver) 
# No windows, abra seu PowerShell e cole o seguinte comando:
irm https://astral.sh/uv/install.ps1 | iex

# Criar ambiente virtual e instalar dependências
uv venv
uv pip install -r requirements.txt
```

### **2.2 Configuração Google Drive API (Service Account)** ✅ **CONCLUÍDA!**
- ✅ **Projeto existente** no Google Cloud Console
- ✅ **Google Drive API** já habilitada
- ✅ **Google Sheets API** já habilitada
- ✅ **Service Account** criado e configurado
- ✅ **Arquivo credentials.json** baixado com credenciais
- ✅ **Permissões configuradas** para acessar pastas compartilhadas
- ✅ **Folder ID será inserido** via terminal (mais flexível)

**URLs importantes (para referência):**
- Google Cloud Console: https://console.cloud.google.com/
- Google Drive API: https://developers.google.com/drive/api
- Biblioteca Python: https://googleapis.dev/python/drive/latest/

### **2.3 Criação dos Primeiros Arquivos de Código**
```
src/
├── main.py              # Arquivo principal com CLI interativo
├── google_drive.py      # Cliente Google Drive
├── parser.py            # Parser de nomes de arquivos
└── excel_generator.py   # Gerador de Excel
```

**Detalhamento dos arquivos:**
- `src/main.py` - **CLI interativo** com menu para tipo de condomínio e input do Folder ID
- `src/google_drive.py` - Cliente Google Drive API para listar arquivos
- `src/parser.py` - Parser de nomes de arquivos usando regex
- `src/excel_generator.py` - Gerador de planilhas Excel organizadas

### **2.4 Interface CLI Planejada**
```
=== EXTRACT FOTOS ===
Escolha o tipo de condomínio:
1. COM blocos (bloco-apartamento-leitura)
2. SEM blocos (apartamento-leitura)

Digite o Folder ID da pasta do Google Drive: [input do usuário]
```

### **2.5 Testes Básicos**
- Testar conexão com Google Drive via Service Account
- Testar parser de nomes
- Validar estrutura do projeto
- Testar interface CLI

### **2.6 Status Atual** 🚀
- ✅ **Estrutura do projeto** criada
- ✅ **Dependências** definidas
- ✅ **Configuração Service Account** completa
- ✅ **Arquivo credentials.json** configurado com credenciais
- ✅ **Permissões configuradas** para acessar pastas compartilhadas
- ✅ **Folder ID dinâmico** via terminal (mais flexível)
- ✅ **Pronto para desenvolvimento** do código!

**Próximo passo:** Implementar os arquivos de código em `src/` com interface CLI interativa usando Service Account
