disciplinas = ["Algoritmos","Segurança","Desenv. Web"]
turma = []



def cadastro_aluno(nome, matricula, idade):


    aluno = {
        "nome":nome,
        "matricula":matricula,
        "idade":idade,
        "notas":[[],[],[],]



    }

    turma.append(aluno)

def encontra_aluno(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def inicializa_notas(matricula):
    aluno = encontra_aluno(matricula)
    for notas_disciplinas in aluno["notas"]:
        for item_nota in range(0,5):
            notas_disciplinas.append(0)

def valida_nota(nota):
    if nota < 0 or nota > 10 :
        return False 
    return True 


def insere_notas(matricula, cod_disc):
    aluno = encontra_aluno(matricula)
    for nota in range(0,5):
        mensagem = "Informe a nota " + str(nota + 1) + ":"
        nota_temporaria = float(input(mensagem))
        while not valida_nota (nota_temporaria):
            nota_temporaria = float(input(mensagem))
            aluno["notas"][cod_disc][nota] = nota_temporaria
                                          
                                        
                                          

        aluno["notas"][cod_disc][nota] = float(input("Informe a nota:"))
          

def gera_relatorio_desempenho(matricula):
    aluno = encontra_aluno(matricula)
    cont_disciplina = 0 #contador utilizado para acessar o nome das diciplinas na lista disciplinas
    for notas_disciplina in aluno["notas"]: #percorre as linhas da matriz de notas (cada linha á uma disciplina)
        media = 0
        for nota in notas_disciplina: #percorre as notas de cada disciplina
            media += nota #média é atualizada somando-se cada nota da disciplina (mé dia é variável acumuladora)
        media /= len(notas_disciplina) #média é atualizada dividindo su valor pela quantidade de notas por disciplina (x /= y é equivalente a x = x/y)
        print(disciplinas[cont_disciplina] + ": ", + media) #exibe a média de cada disciplina
        cont_disciplina += 1


def consulta_informacoes_aluno(matricula):
    aluno = encontra_aluno(matricula)
    print("Nome: ", aluno["nome"])
    cont_disciplina = 0 #contador utilizado para acessar o nome das diciplinas na lista disciplinas
    for notas_disciplina in aluno["notas"]: #percorre as linhas da matriz de notas (cada linha á uma disciplina)
        print(disciplinas[cont_disciplina] + ": ", notas_disciplina) #exibe a lista de notas de cada disciplina
        cont_disciplina += 1




cadastro_aluno("carlos",123,19)
inicializa_notas(123)
cadastro_aluno("guilherme",124,25)
inicializa_notas(124)
insere_notas(124, 0)
print(encontra_aluno(124))
consulta_informacoes_aluno(123)
gera_relatorio_desempenho(123)
print(turma)
for aluno in turma:
    print(aluno)



                   
    
