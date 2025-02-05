# Resumo sobre o programa vExcel: api_estoque_excel.py

- São importadas as bibliotecas necessárias
  ![image](https://github.com/user-attachments/assets/0bbf8230-c2d8-441b-9205-bf1b437d5db5)

- Criada uma função chamada "Estoque"
- Nela, definidos algumas variáveis de data e diretório, por exemplo
- Realizada requisição do tipo GET com a API
- Criada uma variável relevante chamada "produtos"
- Nesta, são gravados os dados da API convertidos em DataFrame através do Pandas
- Removidas algumas colunas irrelevantes para o processo
- Alimentada a variável "todos_produtos" com os dados em lista
- Atualiza o offset com +1000 para depois realizar nova chamada
- Por fim, é realizado um if usando "todos_produtos", no qual é criado o caminho do arquivo e através do method to_excel do Pandas, é gerado arquivo em formato xlsx, a partir dos dados do DataFrame
