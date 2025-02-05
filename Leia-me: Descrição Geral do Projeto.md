# Projeto de Importação de Dados de API com Informações de Estoque

Esse projeto visou a automação da importação de dados de uma API, com informações de Estoque real de uma empresa do setor de Varejo Calçadista.

Utilizando Python, foi realizado o acesso e leitura da API, sendo realizado o carregamento dos dados extraídos.

Desenvolvidas duas versões finais para disponibilização dos dados: 

1 - Grava em um arquivo xlsx (Excel)

2 - Grava em um banco de dados relacional (MySQL)

O objetivo é otimizar o processo de integração e garantir a eficiência no armazenamento e manipulação de informações.

A API possui uma estrutura onde, em sua URL podem ser informados critérios de data de inclusão e alteração dos itens, bem como valor de offset, ou seja, o ponto de paginação dos itens que se quer ler.

O desafio foi aplicar no código uma função que conseguisse selecionar determinada data, ler a primeira página com 1000 itens e, após isso, avançar para uma nova chamada, até que se leia todos os itens.

Por fim, processar todos os registros para uma planilha de Excel ou tabela de banco de dados, possibilitando tratamentos futuros utilizando outras ferramentas e SQL, isolando o processo de captura de dados da API.
