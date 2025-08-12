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