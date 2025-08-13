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
google-auth-httplib2  # Para requisições HTTP
python-dotenv          # Para carregar variáveis de ambiente
```

### **2. .env (arquivo de variáveis de ambiente - Service Account):**
```env
# Credenciais da Service Account do Google Cloud Console
GOOGLE_SERVICE_ACCOUNT_TYPE=service_account
GOOGLE_PROJECT_ID=seu-projeto-id
GOOGLE_PRIVATE_KEY_ID=sua-private-key-id
GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
GOOGLE_CLIENT_EMAIL=sua-service-account@seu-projeto.iam.gserviceaccount.com
GOOGLE_CLIENT_ID=seu-client-id
GOOGLE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
GOOGLE_TOKEN_URI=https://oauth2.googleapis.com/token
GOOGLE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
GOOGLE_CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/sua-service-account%40seu-projeto.iam.gserviceaccount.com

# NOTA: Folder ID será inserido via terminal (mais flexível)
```

### **3. .env.example (arquivo modelo):**
```env
# Copie este arquivo para .env e preencha com suas credenciais
# Credenciais da Service Account do Google Cloud Console
GOOGLE_SERVICE_ACCOUNT_TYPE=service_account
GOOGLE_PROJECT_ID=seu-projeto-id
GOOGLE_PRIVATE_KEY_ID=sua-private-key-id
GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
GOOGLE_CLIENT_EMAIL=sua-service-account@seu-projeto.iam.gserviceaccount.com
GOOGLE_CLIENT_ID=seu-client-id
GOOGLE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
GOOGLE_TOKEN_URI=https://oauth2.googleapis.com/token
GOOGLE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
GOOGLE_CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/sua-service-account%40seu-projeto.iam.gserviceaccount.com

# NOTA: Folder ID será inserido via terminal para cada execução
# Isso permite usar diferentes pastas sem editar o arquivo

# Exemplo de configuração (substitua pelos seus valores reais):
# GOOGLE_PROJECT_ID=seu-projeto-id-aqui
# GOOGLE_CLIENT_EMAIL=sua-service-account@seu-projeto.iam.gserviceaccount.com
# GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
```

### **4. README.md básico:**
```markdown
# Extract Fotos

Sistema para extrair informações de nomes de arquivos de imagens do Google Drive e organizá-las em planilhas Excel.

## Instalação

1. Clone o repositório
2. Copie `.env.example` para `.env` e configure suas credenciais da Service Account
3. Instale as dependências: `uv pip install -r requirements.txt`
4. Execute: `python src/main.py`

## Configuração

1. Copie o arquivo `.env.example` para `.env`
2. Edite o arquivo `.env` com suas credenciais da Service Account do Google Drive
3. **Folder ID será inserido via terminal** (mais flexível para diferentes condomínios)

## Como usar

1. Execute o programa: `python src/main.py`
2. Escolha o tipo de condomínio (com ou sem blocos)
3. Digite o Folder ID da pasta do Google Drive
4. O programa processará os arquivos automaticamente e gerará o Excel

## Estrutura do Projeto

```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Suas credenciais da Service Account
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
git commit -m "Estrutura inicial do projeto com Service Account"
git push origin main
```