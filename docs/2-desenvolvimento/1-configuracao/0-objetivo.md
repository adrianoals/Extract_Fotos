## **Etapa 1: Configuração do Ambiente de Desenvolvimento**

### **O que será feito:**

#### **1.1 Instalação e Configuração do Python**
- Verificar versão do Python (recomendo 3.13)
- Configurar ambiente virtual com `uv`
- Criar estrutura de pastas do projeto

#### **1.2 Dependências Principais (requirements.txt)**
- **Google Drive API:** `google-api-python-client`, `google-auth`, `google-auth-oauthlib`
- **Processamento de dados:** `pandas`, `openpyxl`
- **Regex e parsing:** `re` (built-in), `typing`
- **CLI:** `click` ou `argparse` (built-in)
- **Logging:** `logging` (built-in)

#### **1.3 Configuração Google Drive API**
- **Usar projeto existente** no Google Cloud Console
- **Google Drive API** já habilitada ✅
- **Google Sheets API** já habilitada ✅
- **Credenciais OAuth 2.0** já configuradas ✅
- **Configurar credenciais** no arquivo .env
- **Folder ID será inserido** via terminal (mais flexível)

#### **1.4 Estrutura de Pastas do Projeto**
```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação (já temos)
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Credenciais OAuth 2.0 (fixas)
└── README.md              # Instruções de uso
```

### **Por que `uv` é excelente:**
✅ **Muito mais rápido** que pip  
✅ **Resolução de dependências** inteligente  
✅ **Lock file** para versões exatas  
✅ **Compatível** com pip/requirements.txt  
✅ **Instalação paralela** de pacotes  

### **Configuração OAuth 2.0:**
✅ **Credenciais já configuradas** no Google Console  
✅ **APIs já habilitadas** (Drive + Sheets)  
✅ **Arquivo .env** configurado com client_id e client_secret  
✅ **Folder ID dinâmico** via terminal (mais flexível)  
✅ **Pronto para desenvolvimento** 🚀
