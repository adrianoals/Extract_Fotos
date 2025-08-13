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
3. Configure as permissões da Service Account para acessar as pastas compartilhadas

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
├── .env                    # Suas credenciais da Service Account (não versionado)
├── .env.example           # Modelo de configuração
└── README.md              # Este arquivo
```

## Vantagens da Service Account

✅ **Sem interação do usuário** (autenticação headless)  
✅ **Sem problemas de redirect_uri**  
✅ **Mais estável** para aplicações automatizadas  
✅ **Permissões granulares** por pasta  
✅ **Ideal para servidores** e automações