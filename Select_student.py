from random import choice
list_student=open("alunos.txt","r")
n=list_student.read()
b=list(map(str,n.split("\n")))

def phrase_randon(list):
    print(choice(list))

def add_aluno(lista):
    insert=str(input("digite nome um aluno: "))
    file=open("alunos.txt","a")
    file.write("\n"+ insert)
    lista.append(insert)
    
  
def remove(lista):
    delete_name=str(input("digite um nome: "))
    with open("alunos.txt","w") as file:
        file.write("")
    lista.remove(delete_name)
    with open("alunos.txt","a") as file:
        for n in lista:
            file.write(n+"\n")


