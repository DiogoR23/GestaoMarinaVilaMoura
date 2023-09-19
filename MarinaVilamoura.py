#Gestão da marina de vilamoura
from os import system
from datetime import date
import json
Todos=[{"01": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Portugal", "Número de Passageiros": "3", "Data de Entrada": "19/07/2022", "Data de Saída": "29/11/2022"}}, {"02": {"Nome do Proprietário": "Lucas", "Nome do Capitão": "Diogo", "País de Origem": "Holanda", "Número de Passageiros": "7", "Data de Entrada": "21/11/2022", "Data de Saída": "27/03/2023"}}, {"03": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "19", "Data de Entrada": "19/09/2022", "Data de Saída": "29/06/2023"}}, {"04": {"Nome do Proprietário": "Ricardo", "Nome do Capitão": "Lucas", "País de Origem": "Japão", "Número de Passageiros": "27", "Data de Entrada": "21/10/2022", "Data de Saída": "21/10/2023"}}, {"05": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "10", "Data de Entrada": "27/09/2022", "Data de Saída": "29/01/2023"}}, {"06": {"Nome do Proprietário": "Ricardo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "30", "Data de Entrada": "30/09/2022", "Data de Saída": "29/03/2023"}}, {"07": {"Nome do Proprietário": "Lucas", "Nome do Capitão": "Diogo", "País de Origem": "Suíça", "Número de Passageiros": "15", "Data de Entrada": "05/06/2022", "Data de Saída": "11/11/2022"}}]
CategoriaA=[{"01": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Portugal", "Número de Passageiros": "3", "Data de Entrada": "19/07/2022", "Data de Saída": "29/11/2022"}}]
CategoriaB=[{"02": {"Nome do Proprietário": "Lucas", "Nome do Capitão": "Diogo", "País de Origem": "Holanda", "Número de Passageiros": "7", "Data de Entrada": "21/11/2022", "Data de Saída": "27/03/2023"}}]
CategoriaC=[{"05": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "10", "Data de Entrada": "27/09/2022", "Data de Saída": "29/01/2023"}}]
CategoriaD=[{"07": {"Nome do Proprietário": "Lucas", "Nome do Capitão": "Diogo", "País de Origem": "Suíça", "Número de Passageiros": "15", "Data de Entrada": "05/06/2022", "Data de Saída": "11/11/2022"}}]
CategoriaE=[{"03": {"Nome do Proprietário": "Diogo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "19", "Data de Entrada": "19/09/2022", "Data de Saída": "29/06/2023"}}]
CategoriaF=[{"04": {"Nome do Proprietário": "Ricardo", "Nome do Capitão": "Lucas", "País de Origem": "Japão", "Número de Passageiros": "27", "Data de Entrada": "21/10/2022", "Data de Saída": "21/10/2023"}}]
CategoriaG=[{"06": {"Nome do Proprietário": "Ricardo", "Nome do Capitão": "Lucas", "País de Origem": "Alemanha", "Número de Passageiros": "30", "Data de Entrada": "30/09/2022", "Data de Saída": "29/03/2023"}}]
chave= "Marina2022"
chave2= "Marina2023"
opcao=-1
#Função para o Menu
def menu():
    system("cls")
    print("1- Opções Avançadas")
    print("2- Inserir novo Barco")
    print("3- Procurar")
    print("4- Remover Barco do Sistema")
    print("5- Prolongar a Estadia")
    print("6- Pesquisar embarcações Com a mesma Data de Saída")
    print("7- Aceder aos ganhos totais da empresa")
    print("0- Sair")

#Função para Inserir Barcos 
def inserir():
    x= int(input("Insira o tamanho: "))
    m1= input("Matricula: ")
    a1= input("Nome do Proprietário: ")
    b1= input("Nome do Capitão: ")
    c1= input("País de Origem: ")
    d1= int(input("Número de Passageiros a bordo: "))
    e1= str(input("Introduza a data de entrada(dd/mm/aaaa): "))
    f1= str(input("Introduza a data de saída (dd/mm/aaaa): "))
    if 0<=x<7.99:
        z1=len(CategoriaA)
        if z1>=40:
            print("Lugares indisponiveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaA.append(barco)
        Todos.append(barco)
    elif 8<=x<9.99:
        z2=len(CategoriaB)
        if z2>=32:
            print("Indisponivel")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaB.append(barco)
        Todos.append(barco)
    elif 10<=x<11.99:
        z3=len(CategoriaC)
        if z3>=35:
            print("Lugares indisponíveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaC.append(barco)
        Todos.append(barco)
    elif 12<=x<14.99:
        z4= len(CategoriaD)
        if z4>=30:
            print("Lugares indisponíveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaD.append(barco)
        Todos.append(barco)
    elif 15<=x<17.99:
        z5= len(CategoriaE)
        if z5>= 25:
            print("Lugares indisponíveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaE.append(barco)
        Todos.append(barco)
    elif 18<=x<19.99:
        z6= len(CategoriaF)
        if z6>= 17:
            print("Lugares indisponíveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaF.append(barco)
        Todos.append(barco)
    elif x>=20:
        z7= len(CategoriaG)
        if z7>= 7:
            print("Lugares indisponíveis!")
            return
        barco={}
        v_m1=  {"Nome do Proprietário": a1, "Nome do Capitão": b1, "País de Origem": c1, "Número de Passageiros": d1, "Data de Entrada": e1, "Data de Saída": f1}
        barco[m1]= v_m1 
        CategoriaG.append(barco)
        Todos.append(barco)

#Função para Aceder ás Opções Avançadas
def opcoesavancadas():
    #Listar Barcos
    print("Categoria A: ", CategoriaA)
    print("Categoria B: ", CategoriaB)
    print("Categoria C: ", CategoriaC)
    print("Categoria D: ", CategoriaD)
    print("Categoria E: ", CategoriaE)
    print("Categoria F: ", CategoriaF)
    print("Categoria G: ", CategoriaG)
    #Nº de vagas
    Na= 40-len(CategoriaA)
    print("Nº de lugares vagos para a Categoria A: ", Na)
    Nb= 32-len(CategoriaB)
    print("Nº de lugares vagos para a Categoria B: ", Nb)
    Nc= 35-len(CategoriaC)
    print("Nº de lugares vagos para a Categoria C: ", Nc)
    Nd= 30-len(CategoriaD)
    print("Nº de lugares vagos para a Categoria D: ", Nd)
    Ne= 25-len(CategoriaE)
    print("Nº de lugares vagos para a Categoria E: ", Ne)
    Nf= 17-len(CategoriaF)
    print("Nº de lugares vagos para a Categoria F: ", Nf)
    Ng= 7-len(CategoriaG)
    print("Nº de lugares vagos para a Categoria G: ", Ng)
 
#Função para Procurar Barco no Sistema
def procurar():
    encontrado = False
    num= input("Insira a Matrícula do Barco que pretende procurar: ")
    for boat in Todos:
        if num in boat.keys():
            print(boat)
            encontrado=True
    if encontrado==False:
        print("Barco não encontrado, clique enter!")

#Função para Remover Barco do Sistema   
def eliminar():
    mat= input("Insira a Matrícula que deseja remover do Sistema: ")
    for boat in Todos: 
        if mat in boat.keys():
            for iate in boat.values():
                da= iate["Data de Entrada"].split("/")
                dia1= int(da[0])
                mes1= int(da[1])
                ano1= int(da[2])
                data1= date(ano1, mes1, dia1)

                l1= date.today()
                dias= l1-data1
                z= dias.days

                if z>=30:
                    sda= ((z*10.40)*0.9)
                    print("Preço após estadia longa: {:.2f}€".format(sda))
                else:
                    pr= z*10.40 
                    print("O preço Total a pagar é de: {:.2f}€".format(pr))
            boat.pop(mat, None)
            print("Barco removido com sucesso.")
        else:
            print("Matrícula não encontrada!")

#Função para Pedir Prolongamento da Estadia
def prolongamento():
    matricula= input("Introduza a Matrícula: ")
    for barco in Todos:
        if matricula in barco.keys():
            for boat in barco.values():
                ds1= input("Introduza uma nova Data de Saída (dd/mm/aaaa): ")
                
                dat= boat["Data de Saída"].split("/")
                diat= int(dat[0])
                mest= int(dat[1])
                anot= int(dat[2])
                Antiga_Saída= date(anot, mest, diat)
                
                dat1= ds1.split("/")
                diat1= int(dat1[0])
                mest1= int(dat1[1])
                anot1= int(dat1[2])
                Nova_Saída= date(anot1, mest1, diat1)
                
                if Nova_Saída>Antiga_Saída:
                    boat["Data de Saída"]= ds1
                    print("A data foi atualizada com sucesso!")
                else:
                    print("Operação não autorizada!")
                    print("Insira uma nova Data de Saída superior á antiga!")
        else:
            print("Matricula não encontrada")

#Função para Pesquisar Embarcações com a mesma Data de Saída  
def procurardata():
    pds= str(input("Introduza a Data de Saída que deseja procurar: "))
    data_saida=[]
    for bot in Todos:
        for lm in bot.values():
                if pds==lm["Data de Saída"]:
                    data_saida.append(bot)
                else:
                    print("Data que pretende não existe!")
        print(data_saida)
        data_saida.clear()

#Função para Acessar ao Saldo da Empresa
def saldoempresa():
    for barco in Todos:
        for boat in barco.values():
            data= boat["Data de Entrada"].split("/")
            dia= int(data[0])
            mes= int(data[1])
            ano= int(data[2])
            data_entrada= date(ano, mes, dia)
            datas= boat["Data de Saída"].split("/")
            dias= int(datas[0])
            mess= int(datas[1])
            anos= int(datas[2])
            data_saída= date(anos, mess, dias)  
            dias= data_saída-data_entrada
            z= dias.days

            #Desconto e Saldo de cada Categoria
        prA=0
        prA1=0
        prB=0
        prB1=0
        prC=0
        prC1=0
        prD=0
        prD1=0
        prE=0
        prE1=0
        prF=0
        prF1=0
        prG=0
        prG1=0
        Saldo=0

        if barco in CategoriaA:
            if z>=30:
                prA= float((z*10.40)*0.90)
                print("Totais da Categoria A: {:.2f}€".format(prA))
            else:
                prA1= float(z*10.40)
                print("Totais da Categoria A (sem descontos): {:.2f}€".format(prA1))
        if barco in CategoriaB:
            if z>=30:
                prB= float((z*15.50)*0.90)
                print("Totais da Categoria B: {:.2f}€".format(prB))
            else:
                prB1= float(z*15.50)
                print("Totais da Categoria B (sem descontos): {:.2f}€".format(prB1))
        if barco in CategoriaC:
            if z>=30:
                prC= float((z*19.50)*0.90)
                print("Totais da Categoria C: {:.2f}€".format(prC))
            else:
                prC1= float(z*19.50)
                print("Totais da Categoria C (sem descontos): {:.2f}€".format(prC1))
        if barco in CategoriaD:
            if z>=30:
                prD= float((z*25.60)*0.90)
                print("Totais da Categoria D: {:.2f}€".format(prD))
            else:
                prD1= float(z*25.60)
                print("Totais da Categoria D (sem descontos): {:.2f}€".format(prD1))
        if barco in CategoriaE:
            if z>=30:
                prE= float((z*50.50)*0.90)
                print("Totais da Categoria E: {:.2f}€".format(prE))
            else:
                prE1= float(z*50.50)
                print("Totais da  Categoria E (sem descontos): {:.2f}€".format(prE1))
        if barco in CategoriaF:
            if z>=30:
                prF= float((z*62.80)*0.90)
                print("Totais da Categoria F: {:.2f}€".format(prF))
            else:
                prF1= float(z*62.80)
                print("Totais da Categoria F (sem descontos): {:.2f}€".format(prF1))
        if barco in CategoriaG:
            if z>=30:
                prG= float((z*80.00)*0.90)
                print("Totais da Categoria G: {:.2f}€".format(prG))
            else:
                prG1= float(z*80.00)
                print("Totais da Categoria G (sem descontos): {:.2f}€".format(prG1))

#Programa
while opcao!=0:
    menu()
    opcao= int(input("Insira a opção: "))
    if opcao==1:
        ch= input("Introduza a palavra-passe: ")
        if ch==chave:
            opcoesavancadas()
            input()
        else:
            print("Palavra-Passe incorreta!")
            input("Carregue no enter para continuar!")
    elif opcao==2:
        inserir()
        input()
    elif opcao==3:
        procurar()
        input()
    elif opcao==4:
        eliminar()
        input()
    elif opcao==5:
        prolongamento()
        input()
    elif opcao==6:
        procurardata()
        input()
    elif opcao==7:
        ch1= input("Introduza a palavra-passe: ")
        if ch1==chave2:
            saldoempresa()
            input()
        else:
            print("Palavra-Passe incorreta!")
            input("Carregue no enter para continuar!")

filename= 'barcos.json'
with open(filename, 'w') as file_object:
    json.dump(Todos, file_object)
    json.dump(CategoriaA, file_object)
    json.dump(CategoriaB, file_object)
    json.dump(CategoriaC, file_object)
    json.dump(CategoriaD, file_object)
    json.dump(CategoriaE, file_object)
    json.dump(CategoriaF, file_object)
    json.dump(CategoriaG, file_object)