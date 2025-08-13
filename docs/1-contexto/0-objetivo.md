## **Etapa 1: Configuração do Ambiente de Desenvolvimento**

### **O que será feito:**

#### **1.1 Instalação e Configuração do Python**
- Verificar versão do Python (recomendo 3.13)
- Configurar ambiente virtual com `uv`
- Criar estrutura de pastas do projeto

#### **1.2 Dependências Principais (requirements.txt)**
- **Google Drive API:** `google-api-python-client`, `google-auth`
- **Processamento de dados:** `pandas`, `openpyxl`
- **Regex e parsing:** `re` (built-in), `typing`
- **CLI:** `click` ou `argparse` (built-in)
- **Logging:** `logging` (built-in)

#### **1.3 Configuração Google Drive API (Service Account)**
- **Usar projeto existente** no Google Cloud Console
- **Google Drive API** já habilitada ✅
- **Google Sheets API** já habilitada ✅
- **Service Account** configurado para autenticação ✅
- **Credenciais da Service Account** no arquivo .env
- **Folder ID será inserido** via terminal (mais flexível)

#### **1.4 Estrutura de Pastas do Projeto**
```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação (já temos)
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Credenciais da Service Account
└── README.md              # Instruções de uso
```

### **Por que `uv` é excelente:**
✅ **Muito mais rápido** que pip  
✅ **Resolução de dependências** inteligente  
✅ **Lock file** para versões exatas  
✅ **Compatível** com pip/requirements.txt  
✅ **Instalação paralela** de pacotes  

### **Configuração Service Account:**
✅ **Service Account criado** no Google Console  
✅ **APIs já habilitadas** (Drive + Sheets)  
✅ **Credenciais configuradas** no arquivo .env  
✅ **Permissões configuradas** para acessar pastas compartilhadas  
✅ **Pronto para desenvolvimento** 🚀

### **Vantagens da Service Account vs OAuth 2.0:**
✅ **Sem interação do usuário** (headless)  
✅ **Sem problemas de redirect_uri**  
✅ **Mais estável** para aplicações automatizadas  
✅ **Permissões granulares** por pasta  
✅ **Ideal para servidores** e automações
