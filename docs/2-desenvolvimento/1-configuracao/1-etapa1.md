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
google-auth-oauthlib  # Para OAuth 2.0
google-auth-httplib2  # Para requisições HTTP
```

### **2. .env (arquivo de variáveis de ambiente - OAuth 2.0):**
```env
# Credenciais Google OAuth 2.0 (fixas)
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_PROJECT_ID=your_project_id_here

# NOTA: Folder ID será inserido via terminal (mais flexível)
```

### **3. .env.example (arquivo modelo):**
```env
# Copie este arquivo para .env e preencha com suas credenciais
# Credenciais Google OAuth 2.0 (fixas)
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_PROJECT_ID=your_project_id_here

# NOTA: Folder ID será inserido via terminal para cada execução
# Isso permite usar diferentes pastas sem editar o arquivo

# Exemplo de configuração (substitua pelos seus valores reais):
# GOOGLE_CLIENT_ID=seu_client_id_aqui
# GOOGLE_CLIENT_SECRET=seu_client_secret_aqui
# GOOGLE_PROJECT_ID=seu_project_id_aqui
```

### **4. README.md básico:**
```markdown
# Extract Fotos

Sistema para extrair informações de nomes de arquivos de imagens do Google Drive e organizá-las em planilhas Excel.

## Instalação

1. Clone o repositório
2. Copie `.env.example` para `.env` e configure suas credenciais OAuth 2.0
3. Instale as dependências: `uv pip install -r requirements.txt`
4. Execute: `python src/main.py`

## Configuração

1. Copie o arquivo `.env.example` para `.env`
2. Edite o arquivo `.env` com suas credenciais OAuth 2.0 do Google Drive
3. **Folder ID será inserido via terminal** (mais flexível para diferentes condomínios)

## Como usar

1. Execute o programa: `python src/main.py`
2. Escolha o tipo de condomínio (com ou sem blocos)
3. Digite o Folder ID da pasta do Google Drive
4. O programa processará os arquivos e gerará o Excel

## Estrutura do Projeto

```
Extract_Fotos/
├── src/                    # Código fonte
├── config/                 # Arquivos de configuração
├── docs/                   # Documentação
├── tests/                  # Testes
├── requirements.txt        # Dependências
├── .env                    # Suas credenciais OAuth 2.0 (fixas)
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
git commit -m "Estrutura inicial do projeto com OAuth 2.0"
git push origin main
```