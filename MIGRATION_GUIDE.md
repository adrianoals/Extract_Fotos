# 🚀 Guia de Migração: OAuth 2.0 → Service Account

## 📋 **Resumo das Mudanças**

Este projeto foi migrado do **OAuth 2.0** para **Service Account** para melhorar a estabilidade e facilitar a automação.

## ✅ **Vantagens da Service Account**

- **Sem interação do usuário** (autenticação headless)
- **Sem problemas de redirect_uri**
- **Mais estável** para aplicações automatizadas
- **Permissões granulares** por pasta
- **Ideal para servidores** e automações

## 🔄 **O que Mudou**

### **1. Arquivo de Configuração (.env)**

**ANTES (OAuth 2.0):**
```bash
GOOGLE_CLIENT_ID=seu-client-id
GOOGLE_CLIENT_SECRET=seu-client-secret
GOOGLE_PROJECT_ID=seu-projeto-id
```

**AGORA (Service Account):**
```bash
GOOGLE_SERVICE_ACCOUNT_INFO={"type": "service_account", "project_id": "...", ...}
```

### **2. Autenticação**

**ANTES:** Fluxo OAuth 2.0 com navegador e tokens
**AGORA:** Autenticação direta via Service Account JSON

## 📝 **Como Configurar**

### **Passo 1: Obter Credenciais da Service Account**

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Selecione seu projeto
3. Vá em **APIs & Services** → **Credentials**
4. Clique em **Create Credentials** → **Service Account**
5. Preencha os dados e clique em **Create**
6. Clique na Service Account criada
7. Vá na aba **Keys**
8. Clique em **Add Key** → **Create new key** → **JSON**
9. Baixe o arquivo JSON

### **Passo 2: Configurar o .env**

1. Copie `env.example` para `.env`
2. Abra o arquivo JSON baixado
3. **Copie TODO o conteúdo** do JSON
4. Cole na variável `GOOGLE_SERVICE_ACCOUNT_INFO` no `.env`

**Exemplo:**
```bash
GOOGLE_SERVICE_ACCOUNT_INFO={"type": "service_account", "project_id": "meu-projeto", "private_key_id": "abc123", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n", "client_email": "service@projeto.iam.gserviceaccount.com", ...}
```

### **Passo 3: Configurar Permissões**

1. **No Google Drive:** Compartilhe as pastas com o email da Service Account
2. **No Google Cloud:** Verifique se as APIs estão habilitadas:
   - Google Drive API
   - Google Sheets API (se necessário)

## 🧪 **Testando a Configuração**

Execute o teste básico:
```bash
python src/google_drive.py
```

Se tudo estiver correto, você verá:
```
✅ Cliente Google Drive inicializado com sucesso!
✅ Conexão com Google Drive funcionando!
```

## ❌ **Problemas Comuns**

### **Erro: "JSON inválido"**
- Verifique se copiou o JSON completo
- Não quebre linhas no .env
- Use aspas duplas no JSON

### **Erro: "Permissão negada"**
- Verifique se a Service Account tem acesso às pastas
- Compartilhe as pastas com o email da Service Account

### **Erro: "APIs não habilitadas"**
- Vá no Google Cloud Console
- Habilite Google Drive API

## 🔒 **Segurança**

- **NUNCA** commite o arquivo `.env`
- **NUNCA** compartilhe suas credenciais
- Use `.gitignore` para proteger o `.env`
- A Service Account deve ter permissões mínimas necessárias

## 📚 **Arquivos Modificados**

- ✅ `src/google_drive.py` - Migrado para Service Account
- ✅ `src/main.py` - Atualizado para nova autenticação
- ✅ `env.example` - Novo formato de configuração
- ✅ `README.md` - Documentação atualizada
- ✅ `MIGRATION_GUIDE.md` - Este guia

## 🎯 **Próximos Passos**

1. ✅ Configure o `.env` com suas credenciais
2. ✅ Teste a conexão
3. ✅ Execute o programa principal
4. ✅ Processe suas pastas do Google Drive

---

**🎉 Parabéns! Sua migração está completa!**
