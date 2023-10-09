


def add_aluno(lista,insert,saida):
    lista.append(insert)
    file=open("Study_Python/alunos.txt","a")
    file.write("\n"+ insert)
    saida["output"].update("\n".join(lista))
def remove(lista,delete_name,saida):
    lista.remove(delete_name)
    with open("Study_Python/alunos.txt","w") as file:
        file.write("")
        saida["output"].update("\n".join(lista))