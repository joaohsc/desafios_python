#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

#entrada do texto
txt = input("Informe um texto: ")

txt_reversed =""
# loop inverso do texto
for i in range(len(txt)-1, -1, -1):
    # concatenação dos caracteres invertidos
    txt_reversed += txt[i]

print(txt_reversed)