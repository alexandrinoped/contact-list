import re  # Para validação de email

def validar_email(email):
  regex = r'\S+@\S+'
  if not re.match(regex, email):
    return False
  return True

def adicionar_contato(contatos, nome, telefone, email):
  favorito_resposta = input("Deseja adcicionar esse contato como favorito? (s/n): ").strip().lower()
  favorito = favorito_resposta == 's'

  novo_contato =  {
    "nome": nome, 
    "telefone": telefone, 
    "email": email, 
    "favorito": favorito 
    }
  contatos.append(novo_contato)
  status_favorito = "favorito" if favorito else "não favorito"
  print(f"\nO contato {nome} número de telefone {telefone} email {email} foi adicionado a sua agenda como {status_favorito}!")
  return

def lista_contatos(contatos):
  if len(contatos) <= 0:
    print("Lista de contatos vazia")
    return
  
  print("Sua lista de contatos:\n")
  for indice, novo_contato in enumerate(contatos, start=1):
    status = "🤍" if novo_contato["favorito"] else " "
    print(f"{indice}. {status} {novo_contato['nome']} {novo_contato['telefone']} {novo_contato['email']}")
  return
  
def editar_contato(contatos, indice_contato, novo_contato):
  indice_contato_atualizado = int(indice_contato) - 1

  if 0 <= indice_contato_atualizado < len(contatos):
    contato_atual = contatos[indice_contato_atualizado]
    contato_atual["nome"] = novo_contato["nome"]
    contato_atual["telefone"] = novo_contato["telefone"]
    contato_atual["email"] = novo_contato["email"]
    print(f"\nContato {indice_contato} atualizado com sucesso!")
  else:
    print("\nÍndice de contato inválido! Por favor, digite um número válido.")
  return

def marcar_desmarcar_favorito(contatos, indice_contato):
  indice_contato_favorito = int(indice_contato) - 1

  if indice_contato_favorito >= 0 and indice_contato_favorito < len(contatos):
    contatos[indice_contato_favorito]["favorito"] = not contatos[indice_contato_favorito]["favorito"]

    is_favorite_msg = "favoritado" if contatos[indice_contato_favorito]["favorito"] else "desfavoritado"

    print(f"Contato {indice_contato} foi {is_favorite_msg}")

def lista_contatos_favoritos(contatos):
  favoritos = [contato for contato in contatos if contato["favorito"]]

  if len(favoritos) == 0:
    print("Você não possui nenhum contato favorito!")
    return
  
  print("\nSua lista de contatos favoritos: ")
  for indice, contato in enumerate(favoritos, start=1):
    print(f"{indice}. {contato['nome']} {contato['telefone']} {contato['email']}")

def deletar_contato(contatos, indice_contato):
  indice_contato_deletado = int(indice_contato) - 1
  if 0 <= indice_contato_deletado < len(contatos): 
        contatos.pop(indice_contato_deletado)
        print(f"Contato {indice_contato} deletado!")
  else:
        print("Índice de contato inválido!")
  return

contatos = []
while True:
  print("\nSua Agenda de contatos:")
  print("1. Adicionar contato")
  print("2. Visualizar a lista de contatos")
  print("3. Editar um contato")
  print("4. Marcar/Desmarcar um contato como favorito")
  print("5. Visualizar lista de contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair da agenda")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome = input("Nome:")
    telefone = input("Telefone:")
    email = input("Email:")
    while not validar_email(email):
      email = input("Formato de email inválido. Tente novamente: ")
    adicionar_contato(contatos, nome, telefone, email)

  elif escolha == "2":
    lista_contatos(contatos)

  elif escolha == "3":
    lista_contatos(contatos)
    indice_contato = input("Digite o índice do contato que deseja atualizar: ")
    novo_contato = {
        "nome": input("Digite o novo nome: "),
        "telefone": input("Digite o novo telefone: "),
        "email": input("Digite o novo email: ")
    }
    editar_contato(contatos, indice_contato, novo_contato)  # Armazena a lista atualizada
    lista_contatos(contatos)  # Imprime a lista atualizada após a edição

  elif escolha == "4":
    lista_contatos(contatos)
    indice_contato = input("Informe o número do contato que deseja (des)favoritar: ")
    marcar_desmarcar_favorito(contatos, indice_contato)

  elif escolha == "5":
    lista_contatos_favoritos(contatos)

  elif escolha == "6":
    lista_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja deletar: ")
    deletar_contato(contatos, indice_contato)

  elif escolha == "7":
    break
print("Você saiu da agenda!")