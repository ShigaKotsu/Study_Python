from random import choice
def list_random():
    list_student=open("Student/alunos.txt","r")
    n=list_student.read()
    b=list(map(str,n.split("\n")))
    print(choice(b))


def add_aluno():
    insert=str(input("coloque um aluno na lista"))
    file=open("Student/alunos.txt","a")
    file.write("\n"+ insert)

add_aluno()