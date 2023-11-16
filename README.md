# ponderadaETL

# Projeto ClimaFlask - ETL para Dados Climáticos

## Visão Geral

O Projeto ClimaFlask é uma aplicação em Flask que oferece uma API para acessar informações climáticas de diferentes cidades. Além disso, ele inclui um processo de ETL (Extração, Transformação e Carregamento) para calcular dados climáticos ponderados e armazená-los em um banco de dados SQLite.

## Estrutura do Projeto

A estrutura do projeto é organizada em três partes principais:

- **app.py**: Este arquivo contém a implementação da API com definições de rotas e lógica de acesso aos dados climáticos.
- **test_app.py**: Um arquivo de testes unitários que garante o funcionamento adequado das funcionalidades principais do projeto.
- **dados_climaticos.db**: Um banco de dados SQLite utilizado para armazenar os dados climáticos ponderados.

## Funcionalidades

### API de Clima

A API ClimaFlask oferece as seguintes rotas:

- **/clima**: Rota principal da API que retorna informações sobre as funcionalidades disponíveis.
- **/clima/dados**: Rota que fornece dados climáticos ponderados armazenados no banco de dados.
- **/clima/etl**: Rota de exemplo que sinaliza a execução do processo ETL.

### Testes

O arquivo `test_app.py` contém testes unitários para assegurar o correto funcionamento das funcionalidades do projeto.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado em seu ambiente.

### Instalação de Dependências

Instale as dependências necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

Siga as instruções abaixo para executar o projeto:

1. Clone este repositório para o seu ambiente de desenvolvimento.

2. Navegue até o diretório do projeto:

```bash
cd ClimaFlask
```

### Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. Inicie o aplicativo Flask:

```bash
python app.py
```

### Executando o Projeto

Para visualizar a mensagem de boas-vindas e obter os dados climáticos ponderados, siga os passos abaixo:

1. Abra um navegador e acesse http://127.0.0.1:5000/ para visualizar a mensagem de boas-vindas.

2. Para obter os dados climáticos ponderados, acesse http://127.0.0.1:5000/clima/dados.

### Testes

Para executar os testes unitários, utilize o seguinte comando:

```bash
pytest test_app.py
```

### Observações

- O Projeto ClimaFlask utiliza Flask para criar uma API simples e o SQLite para armazenar os dados climáticos ponderados.
- Certifique-se de ter uma conexão à internet ao acessar a rota /clima/dados, pois ela consome dados da API OpenWeather.
