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

### **2.2 Configuração Google Drive API**
- Criar projeto no Google Cloud Console
- Habilitar Google Drive API
- Criar credenciais (Service Account)
- Baixar arquivo `credentials.json`
- Configurar permissões nas pastas
- **URLs importantes:**
  - Google Cloud Console: https://console.cloud.google.com/
  - Google Drive API: https://developers.google.com/drive/api
  - Biblioteca Python: https://googleapis.dev/python/drive/latest/

### **2.3 Criação dos Primeiros Arquivos de Código**
```
src/
├── main.py              # Arquivo principal
├── google_drive.py      # Cliente Google Drive
├── parser.py            # Parser de nomes de arquivos
└── excel_generator.py   # Gerador de Excel
```

**Detalhamento dos arquivos:**
- `src/main.py` - Arquivo principal com CLI e fluxo de execução
- `src/google_drive.py` - Cliente Google Drive API para listar arquivos
- `src/parser.py` - Parser de nomes de arquivos usando regex
- `src/excel_generator.py` - Gerador de planilhas Excel organizadas

### **2.4 Testes Básicos**
- Testar conexão com Google Drive
- Testar parser de nomes
- Validar estrutura do projeto
