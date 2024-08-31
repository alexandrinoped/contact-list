# Agenda de Contatos 📒

Este é um projeto de agenda de contatos desenvolvido em Python, que permite gerenciar contatos diretamente no terminal. O projeto inclui funcionalidades para adicionar, visualizar, editar, marcar/desmarcar como favorito e deletar contatos.
## Funcionalidades
1. **Adicionar Contato**
   
   Adiciona um novo contato à lista de contatos. O usuário pode inserir o nome, telefone e email do contato. Além disso, existe a opção de marcar o contato como favorito no momento da adição.
   ```python
        def adicionar_contato(contatos, nome, telefone, email):
   ```
2. **Validar Email**
   
  Utiliza expressões regulares para validar o formato do email inserido pelo usuário, garantindo que o email seja válido.
  ```python
        import re  # Para validação de email

        def validar_email(email):
   ```
3. **Listar Contatos**
   
  Exibe todos os contatos cadastrados, mostrando o nome, telefone, email, e se o contato está marcado como favorito.
  ```python
        def lista_contatos(contatos):
  ```
4. **Editar Contato**
   
Permite que o usuário edite as informações de um contato existente na lista, incluindo nome, telefone e email.
```python
      def editar_contato(contatos, indice_contato, novo_contato):
```
5. **Marcar/Desmarcar Contato como Favorito**
   
Permite ao usuário marcar ou desmarcar um contato existente como favorito.
```python
      def marcar_desmarcar_favorito(contatos, indice_contato):
```
6. **Listar Contatos Favoritos**
   
Exibe apenas os contatos que foram marcados como favoritos.
```python
      def lista_contatos_favoritos(contatos):
```
7. **Deletar Contato**
   
Permite ao usuário remover um contato da lista de contatos.
```python
      def deletar_contato(contatos, indice_contato):
```
## Como Usar
1. **Iniciar a Agenda:** Ao executar o programa, o usuário verá um menu de opções no terminal.
2. **Escolher uma Opção:** O usuário deve escolher uma das opções apresentadas (adicionar, listar, editar, favoritar, visualizar favoritos, deletar, sair).
3. **Interagir com o Programa:** Dependendo da opção escolhida, o usuário poderá adicionar novos contatos, visualizar todos os contatos ou apenas os favoritos, editar informações, marcar ou desmarcar favoritos, ou deletar contatos.
4. **Sair da Agenda:** Ao escolher a opção "7", o programa será encerrado.
   
## Regras da Aplicação
* A aplicação é iniciada mostrando um menu de opções e solicita que o usuário escolha uma delas para continuar.
* Ao adicionar um contato, o usuário deve fornecer um nome, telefone, e um email válido.
* Contatos podem ser marcados como favoritos, facilitando sua visualização na lista de favoritos.
* Todos os contatos e suas alterações são exibidos no terminal, proporcionando uma experiência de usuário interativa e amigável.

## Exemplo de Uso
```shell
      Sua Agenda de contatos:
      1. Adicionar contato
      2. Visualizar a lista de contatos
      3. Editar um contato
      4. Marcar/Desmarcar um contato como favorito
      5. Visualizar lista de contatos favoritos
      6. Deletar um contato
      7. Sair da agenda
      Digite a sua escolha: 1
      Nome: João
      Telefone: 123456789
      Email: joao@example.com
      Deseja adicionar esse contato como favorito? (s/n): s

```

## Conclusão
Este projeto oferece uma interface simples para gerenciar contatos diretamente pelo terminal, utilizando Python. Ele é ideal para quem deseja aprender mais sobre manipulação de listas, dicionários, controle de fluxo, e manipulação de entrada e saída no Python.
