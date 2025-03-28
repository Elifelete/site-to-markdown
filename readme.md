# Conversor HTML para Markdown

Esta aplicação é uma API desenvolvida com o framework **FastAPI** que converte páginas HTML de URLs fornecidas em arquivos Markdown. A API é protegida por autenticação Bearer Token para garantir a segurança do endpoint.

## Estrutura do Código

### Dependências

As principais bibliotecas utilizadas são:

- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **Pydantic**: Para validação de dados.
- **Requests**: Para realizar requisições HTTP.
- **Docling**: Para conversão de documentos HTML para Markdown.
- **Python-dotenv**: Para carregar variáveis de ambiente do arquivo .env.

### Arquivo .env

O arquivo .env contém o token de autenticação necessário para acessar o endpoint:

    API_TOKEN="seu_token_aqui"

### Endpoints

#### POST `/convert`

- **Descrição**: Converte uma página HTML de uma URL fornecida em Markdown.
- **Autenticação**: Requer um Bearer Token válido.
- **Payload:**

```JSON
{
  "url": "https://exemplo.com"
}
```

- **Resposta**:

- Sucesso

```JSON
{
  "markdown": "conteúdo_em_markdown"
}
```

- Erros:
  - `401 Unauthorized`: Token inválido ou não fornecido.
  - `400 Bad Request`: Erro ao buscar a URL.
  - `500 Internal Server Error`: Erro na conversão de HTML para Markdown.

### Segurança

A autenticação é implementada com o middleware HTTPBearer. O token fornecido no cabeçalho da requisição é comparado com o valor armazenado na variável de ambiente API_TOKEN.

### Fluxo de Conversão

1.  O cliente envia uma URL no corpo da requisição.
2.  A aplicação faz uma requisição HTTP para buscar o conteúdo HTML da URL.
3.  O conteúdo HTML é convertido para Markdown utilizando a biblioteca docling.
4.  O resultado é retornado no formato JSON.

### Execução

Para rodar a aplicação, execute o seguinte comando:

```shell
uvicorn main:app --host 0.0.0.0 --port  8000
```

A aplicação estará disponível em `http://localhost:8000`.

## Requisitos

As dependências necessárias estão listadas no arquivo requirements.txt:

```
os
dotenv
docling
fastapi
pydantic
requests
io
uvicorn
```

Instale-as com:

```shell
pip install -r requirements.txt
```

## Observações

- Certifique-se de configurar corretamente o arquivo .env com o token de autenticação.
- A aplicação utiliza a biblioteca [docling](https://github.com/docling-project/docling) para conversão de HTML para Markdown. Certifique-se de que ela está instalada e funcionando corretamente.
