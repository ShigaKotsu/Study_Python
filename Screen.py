from random import choice
import Student
import PySimpleGUI as sg

layout=[
    [sg.Text("Lista de alunos")],
    [sg.InputText(key="nome_aluno")],
    [sg.Button("adicione um aluno")],[sg.Button("remova um aluno")],[sg.Button("nome_aletatório"),sg.Button("lista")],
    [sg.Output(key="output",size=(10,10))]
]

janela=sg.Window("Lista TxT",layout)
lista=[]

while True:
    eventos,valores=janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "adicione um aluno":
        request = valores["nome_aluno"]
        insert = Student.add_aluno(request)
    if eventos == "lista":
        list_student=open("List_Student/alunos.txt")
        n=list_student.read()
        b=list(map(str,n.split("\n")))
        janela["output"].update("\n".join(b))
    if eventos == "nome_aletatório":
        janela["output"].update("\n"(choice(b)))
janela.close()