**Objetivo do Projeto:**
Criar um sistema que automatize a extração de informações de imagens armazenadas no Google Drive para organizá-las em uma planilha Excel.

**Como Funciona:**
1. **Fonte dos dados:** Imagens armazenadas em pastas específicas do Google Drive (cada pasta representa um condomínio diferente)

2. **Conteúdo das imagens:** Os nomes dos arquivos das imagens contêm legendas com informações sobre:
   - **Tipo 1:** `bloco-apartamento-leitura` (para condomínios com blocos)
   - **Tipo 2:** `apartamento-leitura` (para condomínios sem blocos)

3. **Processo desejado:**
   - Ler as imagens das pastas do Google Drive
   - Extrair as legendas das imagens, ou seja o nome dos arquivos
   - Organizar os dados em colunas no Excel:
     - Se for tipo 1: colunas para Bloco, Apartamento e Leitura
     - Se for tipo 2: colunas para Apartamento e Leitura

4. **Resultado final:** Uma planilha Excel organizada com os dados extraídos das legendas das imagens, facilitando a análise e gestão das informações dos condomínios.

**Exemplos Práticos:**

**Condomínio com Blocos (Tipo 1):**
- Nome do arquivo: `A-101-1234.jpg`
- Resultado no Excel: Bloco=A, Apartamento=101, Leitura=1234

**Condomínio sem Blocos (Tipo 2):**
- Nome do arquivo: `205-5678.png`
- Resultado no Excel: Apartamento=205, Leitura=5678

**Nota:** A "leitura" refere-se ao valor do medidor (água, gás, energia elétrica, etc.) capturado na imagem.
