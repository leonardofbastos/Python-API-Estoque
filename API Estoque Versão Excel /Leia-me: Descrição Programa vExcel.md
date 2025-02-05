# *Resumo sobre o programa vExcel: api_estoque_excel.py*

1. Descrição do código
2. Conclusão
   
---

***1. Descrição do código:***
   
- São importadas as bibliotecas e módulos necessários:

  ![image](https://github.com/user-attachments/assets/0bbf8230-c2d8-441b-9205-bf1b437d5db5)

- Criada uma função chamada "Estoque". Nela, definidos algumas variáveis de data e diretório, por exemplo:

  ![image](https://github.com/user-attachments/assets/7daa76d7-9077-42f4-b09a-7ae44f90c1fb)

- Realizada requisição do tipo GET com a API:
  
  ![image](https://github.com/user-attachments/assets/76009b87-049d-4b19-8896-d1371c143194)

- Criada uma variável relevante chamada "produtos". Nesta, são gravados os dados da API convertidos em DataFrame através do Pandas:

  ![image](https://github.com/user-attachments/assets/4d28d69e-531c-489b-9280-d9a6c13617da)

- Removidas algumas colunas irrelevantes para o processo. Alimentada a variável "todos_produtos" com os dados em lista. Atualiza o offset com +1000 para depois realizar nova chamada:

  ![image](https://github.com/user-attachments/assets/7e8695c0-59fb-43ee-b40c-e90f4406aba3)

- Realizado um if usando "todos_produtos", no qual é criado o caminho do arquivo e através do method to_excel do Pandas, é gerado arquivo em formato xlsx, a partir dos dados do DataFrame:

  ![image](https://github.com/user-attachments/assets/4df176c7-02ea-4da4-a773-a5f64effbd18)

- Por fim, é executada validação de erros e finalizada a função Estoque:

  ![image](https://github.com/user-attachments/assets/4d41d83b-41fb-4412-a39c-5ccb8a1e472b)

---

***2. Conclusão:***

- Exemplo do retorno apresentado na interface, com as etapas executadas pelo programa:

  ![image](https://github.com/user-attachments/assets/4941bbf4-c507-41ae-900f-6fb1b9fe7249)

- Exemplo de arquivo gerado (o mesmo encontra-se no pasta "Arquivos Gerados" deste repositório):

  ![image](https://github.com/user-attachments/assets/db823a78-e95b-494a-aa7d-cf590dfcab58)

- Vídeo do processo:

   https://github.com/user-attachments/assets/1bc23305-21ab-4342-9c3f-64934f9006b5


