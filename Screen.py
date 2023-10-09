from random import choice
import Student
import PySimpleGUI as sg

layout=[
    [sg.Text("Lista de alunos")],
    [sg.InputText(key="nome_aluno")],
    [sg.Button("adicione um aluno"),sg.Button("remove"),sg.Button("nome_aletatório"),sg.Button("lista")],
    [sg.Output(key="output",size=(10,10))]
]

janela=sg.Window("Lista TxT",layout)
lista=[]

while True:
    eventos,valores=janela.read()
    if eventos == sg.WIN_CLOSED:
        break

    if eventos == "lista":
        list_student=open("Study_Python/alunos.txt")
        leitura_texto=list_student.read()
        name = list(map(str,leitura_texto.split("\n")))
        janela["output"].update("\n".join(name))

    if eventos == "nome_aletatório":
        janela["output"].update((choice(name)))
        
    if eventos == "adicione um aluno":
        request = valores["nome_aluno"]
        if request:
            Student.add_aluno(lista,request,janela)
    if eventos == 'remove':
        remover = valores["nome_aluno"]
        if request in name:
            Student.remove(name,remover,janela)
janela.close()