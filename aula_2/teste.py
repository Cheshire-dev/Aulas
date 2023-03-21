az = "abcdefghijklmnopqrstuvwxyz"
az_crip = "123456789abcfghijklmnopqrs"
mensagem_crip = ""
aux = 0

mensagem = input("Digite uma frase: ")

for i in range(0,len(mensagem)):
    
    if mensagem[i] == " ":
        mensagem_crip += "0"
    else:
        for a in range(0,len(az)):
            if(mensagem[i] == az[a]):
                aux = a
                break
        mensagem_crip += az_crip[aux]

print(mensagem_crip)