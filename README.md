# Boas-vindas ao repositório do TING (Trybe is not Google)!

:warning: :brazil: | Nota: o material abaixo é propriedade exclusiva da Trybe, com uso restrito às pessoas estudantes vinculadas à instituição. | :us: Warn: the following content has all the legal rights reserved to Trybe. Its use is reserved to Trybe students. 

## Lista de Requisitos:

# Requisitos Obrigatórios

## Pacote `ting_file_management`

### 1 - Implemente uma fila para armazenar os arquivos que serão lidos.

- Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- A fila (Queue) deve ser uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila deve implementar os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila deverá ser exposto utilizando o método `__len__` que permitirá, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 1.1 - Será validado que o método `enqueue` deve adicionar um elemento à fila, modificando seu tamanho;

- 1.2 - Será validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho;

- 1.3 - Será validado que o método `search` deve retornar um valor da fila a partir de um índice válido e;

- 1.4 - Será validado que o método `search` deve lançar a exceção `IndexError` quando o índice for inválido.
</details>

### 2 - Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

- Caso o arquivo TXT não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

<details>
<summary><b>Exemplo simples de um arquivo txt a ser importado</b></summary>

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- 2.1 - Será validado que o método `txt_importer` deve retornar uma lista contendo as linhas do arquivo;

- 2.2 - Será validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo e;

- 2.3 - Será validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida a mensagem `Formato inválido` na `stderr`.
</details>

### 3 - Implemente uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o pré-processamento do conteúdo.

- A função irá receber como parâmetro a fila implementada no requisito 1 e o caminho do arquivo;

- A instância da fila recebida por parâmetro deve ser utilizada para registrar o processamento dos arquivos;

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, que tenham o mesmo caminho);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

<details>
<summary><b>Exemplo da estrutura de saída:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 3.1 - Será validado que ao executar a função `process` com um arquivo já existente na fila a execução deverá ignorá-lo e;

- 3.2 - Será validado que ao executar a função `process` com sucesso deverá mostrar dados via `stdout`.
</details>

### 4 - Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função irá receber como parâmetro a fila implementada no requisito 1.

- Caso não existam arquivos na fila, a função deve apenas emitir a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, deve ser emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 4.1 - Será validado que ao executar a função `remove` com sucesso deverá exibir mensagem correta via `stdout` e;

- 4.2 - Será validado que ao executar a função `remove` um arquivo inexistente deverá exibir a mensagem correta via `stdout`.
</details>

### 5 - Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.


- A função irá receber como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

<details>
<summary><b>Exemplo da estrutura de saída em caso de sucesso:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 5.1 - Será validado que ao executar a função `file_metadata` com sucesso deverá exibir a mensagem correta via `stdout` e;

- 5.2 - Será validado que ao executar a função `file_metadata` com posição inválida deverá exibir a mensagem correta via `stderr`.
</details>

## Pacote `ting_word_searches`

### 6 - Implemente uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

- A função irá receber como parâmetros a palavra a ser buscada e a fila implementada no requisito 1;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- A busca deve ser _case insensitive_ (não diferenciar maiúsculas e minúsculas);

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 2
    },
    {
      "linha": 7
    }
  ]
}]
````
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- 6.1 - Será validado que ao executar a função `exists_word` com sucesso deverá retornar a estrutura correta;

- 6.2 - Será validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia e;

- 6.3 - Será validado que ao executar a função `exists_word` a fila original não deverá ser alterada.
</details>
