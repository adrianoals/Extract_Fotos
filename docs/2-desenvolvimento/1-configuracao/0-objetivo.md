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

#### **1.3 Configuração Google Drive API**
- Criar projeto no Google Cloud Console
- Habilitar Google Drive API
- Criar credenciais (Service Account ou OAuth2)
- Baixar arquivo de credenciais JSON
- Configurar permissões nas pastas do Drive

#### **1.4 Estrutura de Pastas do Projeto**
```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação (já temos)
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Variáveis de ambiente
└── README.md              # Instruções de uso
```

### **Por que `uv` é excelente:**
✅ **Muito mais rápido** que pip  
✅ **Resolução de dependências** inteligente  
✅ **Lock file** para versões exatas  
✅ **Compatível** com pip/requirements.txt  
✅ **Instalação paralela** de pacotes  
