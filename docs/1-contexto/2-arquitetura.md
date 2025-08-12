## **Arquitetura Corrigida:**

### **1. Componentes Principais:**
- **Autenticação Google Drive API** - Para acessar as pastas
- **Leitor de Nomes de Arquivos** - Para listar os nomes das imagens
- **Parser de Nomes** - Para extrair informações dos nomes dos arquivos
- **Gerador de Excel** - Para criar a planilha organizada
- **Interface de Usuário** - Para configurar condomínios e executar o processo

### **2. Fluxo de Dados:**
```
Google Drive → Listar Nomes dos Arquivos → Parser de Nomes → Excel
```

### **3. Diagrama do Fluxo:**
```
┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────┐    ┌─────────────┐
│   Google Drive  │───▶│  Listar Nomes dos    │───▶│  Parser de      │───▶│   Excel     │
│                 │    │     Arquivos         │    │     Nomes       │    │             │
└─────────────────┘    └──────────────────────┘    └─────────────────┘    └─────────────┘
         │                       │                          │
         ▼                       ▼                          ▼
   Autenticação           Extrair nomes              Extrair dados
   via API                das imagens                (bloco, apt, leitura)
```

### **4. Tecnologias Sugeridas:**
- **Backend:** Python (com bibliotecas como `google-api-python-client`, `pandas`, `openpyxl`)
- **Google Drive API:** Para listar arquivos e pastas
- **Processamento:** Regex para extrair informações dos nomes dos arquivos
- **Excel:** Para organizar os dados extraídos

### **5. Configuração por Condomínio:**
- Arquivo de configuração para definir:
  - ID da pasta do Google Drive
  - Tipo de formato (com ou sem bloco)
  - Padrões de regex para extrair bloco, apartamento e leitura dos nomes

### **6. Detalhamento dos Componentes:**

**Autenticação Google Drive API:**
- Gerencia credenciais e permissões de acesso
- Conecta-se às pastas específicas de cada condomínio

**Leitor de Nomes de Arquivos:**
- Navega pelas pastas do Google Drive
- Lista todos os arquivos de imagem encontrados
- Filtra por extensões de imagem (.jpg, .png, .jpeg, etc.)

**Parser de Nomes:**
- Aplica expressões regulares para extrair informações
- Identifica automaticamente o tipo de formato (com ou sem bloco)
- Valida e limpa os dados extraídos

**Gerador de Excel:**
- Cria planilhas com colunas organizadas
- Aplica formatação e validação de dados
- Permite exportação em diferentes formatos

**Interface de Usuário:**
- Configuração de condomínios e pastas
- Execução do processo de extração
- Visualização dos resultados e logs