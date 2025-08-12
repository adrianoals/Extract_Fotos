## **Criando o repositório:**

```bash
git init
git add .
git commit -m "Initial commit: Estrutura de documentação"
```

## **Conectando ao GitHub:**

```bash
# Crie um repositório no GitHub primeiro, depois:
git remote add origin https://github.com/seu-usuario/extract-fotos.git
git branch -M main
git push -u origin main
```

## **Agora vamos criar a estrutura de pastas:**

```bash
mkdir src
mkdir config
mkdir tests
```

## **Vamos criar os arquivos iniciais:**

### **1. requirements.txt (sem versões específicas):**
```txt
google-api-python-client
google-auth
pandas
openpyxl
click
python-dotenv
```

### **2. .env (arquivo de variáveis de ambiente):**
```env
GOOGLE_DRIVE_CREDENTIALS_FILE=credentials.json
GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here
```

### **3. .env.example (arquivo modelo):**
```env
# Copie este arquivo para .env e preencha com suas configurações
GOOGLE_DRIVE_CREDENTIALS_FILE=credentials.json
GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here

# Exemplo de configuração:
# GOOGLE_DRIVE_CREDENTIALS_FILE=meu-condominio-credentials.json
# GOOGLE_DRIVE_FOLDER_ID=1ABC123DEF456GHI789JKL
```

### **4. README.md básico:**
```markdown
# Extract Fotos

Sistema para extrair informações de nomes de arquivos de imagens do Google Drive e organizá-las em planilhas Excel.

## Instalação

1. Clone o repositório
2. Copie `.env.example` para `.env` e configure suas credenciais
3. Instale as dependências: `uv pip install -r requirements.txt`
4. Execute: `python src/main.py`

## Configuração

1. Copie o arquivo `.env.example` para `.env`
2. Edite o arquivo `.env` com suas configurações do Google Drive
3. Configure as credenciais do Google Drive API

## Estrutura do Projeto

```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Suas configurações (não versionado)
├── .env.example           # Modelo de configuração
└── README.md              # Este arquivo
```
```

## **Comandos para executar:**

```bash
# 1. Criar estrutura de pastas
mkdir src config tests

# 2. Criar arquivos
# (crie os arquivos requirements.txt, .env, .env.example e README.md)

# 3. Adicionar ao git (excluindo .env)
echo ".env" >> .gitignore
git add .
git commit -m "Estrutura inicial do projeto"
git push origin main
```