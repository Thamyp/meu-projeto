
while True:
    user= input("Digite seu nome de usuário: ")
    senha= input("Digite sua senha: ")

    if len(user) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres!")
        continue
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres!")
        continue 
    print("Cadastro realizado com sucesso!")
    break
