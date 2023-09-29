from random import choice
list_student=open("Student/alunos.txt")
n=list_student.read()
b=list(map(str,n.split("\n")))

def phrase_random(list):
    print(choice(list))

def add_aluno(lista):
    insert=str(input("digite nome um aluno: "))
    file=open("Student/alunos.txt","a")
    file.write("\n"+ insert)
    lista.append(insert)
    
  
def remove(lista):
    delete_name=str(input("remova um nome: "))
    with open("Student/alunos.txt","w") as file:
        file.write("")
    lista.remove(delete_name)
    with open("Student/alunos.txt","a") as file:
        for n in lista:
            file.write(n+"\n")


def main():
    while True:
        print("1.Random Choice\n2.Add Student\n3.Remove name in list")
        c= int(input("what do you want?: "))
        if c == 1:
            phrase_random(b)
        elif c == 2:
            add_aluno(b)
        elif c == 3:
            remove(b)
        break
main()