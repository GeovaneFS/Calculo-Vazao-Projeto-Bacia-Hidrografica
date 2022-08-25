'''
Geovane Fernandes - o Código abaixo visa o calculo da vazão de projeto para uma bacia hidrografica
sendo este calculo necessário para obtenção de outorgas para uso da água e ou dispensa de outorgas
as equações utilizadas abaixo segundo literatura são utilizadas para bacias hidrograficas pequenas com áreas de até
2 km² tempo de retorno de 2 a 100 anos e tempo de concentração de 5 a 1440 minutos.    
'''

import json

#ler o arquivo json
with open('RelacaoIDF.json') as arquivo:
    data = json.load(arquivo)

def tempo (cursoagua, variacaoaltura):
    '''Calculo tempo de concentração usando equação de Kirpich'''
    Tempo_Concentracao = 57*(((cursoagua**3)/(variacaoaltura))**0.385)
          
    return Tempo_Concentracao

# def intensidade de precipitação
def intensidade (TR, TC, Nome_Municipio):
    '''Determinando intensidade de precipitação'''
    for i in data:
        if i['cidade'] == Nome_Municipio.upper():
            k = float (i['k'])
            a = float (i['m'])
            b = float (i['t'])
            c = float (i['n'])

    Intensidade = ((k*(TR**a))/(b+TC)**c)
    return Intensidade

# def vazao de projeto
def vazao (coeficiente, I, area):
    '''Calculo vazao de projeto'''
    Vazao_Projeto = (coeficiente*I*area)/3.6
    return Vazao_Projeto

# def tabela coeficiente de runoff (C)
def coeficienterunoff (Declividade):
    '''Determinando Coeficiente'''
    D = Declividade*100 #Convertendo para porcentagem
    
    TipoSolo = int (input ('Qual o tipo de Solo da área? 1 - Solo Arenoso, 2 - Solo Franco, 3 - Solo Argiloso: '))
    while TipoSolo != 1 and TipoSolo != 2 and TipoSolo != 3:
        TipoSolo = int (input ('Digite um valor válido:\n' + '1 - Solo Arenoso\n' + '2 - Solo Franco\n' + '3 - Solo Argiloso: '))
        
    UsodeArea = int (input ('Qual o uso e ocupação da área? 1 - Florestas, 2 - Pastagens, 3 - Terras Cultivadas: '))    
    while UsodeArea != 1 and UsodeArea != 2 and UsodeArea != 3:
        UsodeArea = int (input ('Digite um valor válido:\n' + '1 - Florestas\n' + '2 - Pastagens\n' + '3 - Terras Cultivadas: '))

    if D >= 0 and D <= 5:
        if TipoSolo == 1:
            if UsodeArea == 1:
                C = 0.10
            elif UsodeArea == 2:
                C = 0.10
            elif UsodeArea == 3:
                C = 0.30
        elif TipoSolo == 2:
            if UsodeArea == 1:
                C = 0.30
            elif UsodeArea == 2:
                C = 0.30
            elif UsodeArea == 3:
                C = 0.50
        elif TipoSolo == 3:
            if UsodeArea == 1:
                C = 0.40
            elif UsodeArea == 2:
                C = 0.40
            elif UsodeArea == 3:
                C = 0.60
    elif D > 5 and D <= 10:
        if TipoSolo == 1:
            if UsodeArea == 1:
                C = 0.25
            elif UsodeArea == 2:
                C = 0.15
            elif UsodeArea == 3:
                C = 0.40
        elif TipoSolo == 2:
            if UsodeArea == 1:
                C = 0.35
            elif UsodeArea == 2:
                C = 0.35
            elif UsodeArea == 3:
                C = 0.60
        elif TipoSolo == 3:
            if UsodeArea == 1:
                C = 0.50
            elif UsodeArea == 2:
                C = 0.55
            elif UsodeArea == 3:
                C = 0.70
    elif D > 10 and D <= 30:
        if TipoSolo == 1:
            if UsodeArea == 1:
                C = 0.30
            elif UsodeArea == 2:
                C = 0.20
            elif UsodeArea == 3:
                C = 0.50
        elif TipoSolo == 2:
            if UsodeArea == 1:
                C = 0.50
            elif UsodeArea == 2:
                C = 0.40
            elif UsodeArea == 3:
                C = 0.70
        elif TipoSolo == 3:
            if UsodeArea == 1:
                C = 0.60
            elif UsodeArea == 2:
                C = 0.60
            elif UsodeArea == 3:
                C = 0.80
    return C

# Dados de entrada (obtidos apos delimitação da área)
Nome_Municipio = input ('Digite o nome do municipio: ')

#importar cidades do arquivo json para uma lista e fazer a busca pelo nome do municipio
for i in data:
    #se municipio for igual ao nome do municipio
    if i['cidade'] == Nome_Municipio.upper():
        Area_Bacia = float(input('Digite a area da bacia em km²: '))
        Comprimento_Curso = float(input('Digite o comprimento do curso dágua em km: '))
        Cota_Maxima = float(input('Digite a cota maxima da Bacia Hidrografica em m: '))
        Cota_Controle = float(input('Digite a conta do ponto de controle: '))
        Tempo_Retorno = int (input('Digite o tempo de retorno em anos: '))
        print ('\n')
        # Contas basicas
        DESNIVEL = Cota_Maxima - Cota_Controle
        DECLIVIDADE = DESNIVEL/(Comprimento_Curso*1000)
        # Chamada das funções
        TEMPO_CONCENTRACAO = tempo(Comprimento_Curso, DESNIVEL)
        INTENSIDADE = intensidade(Tempo_Retorno, TEMPO_CONCENTRACAO, Nome_Municipio)
        COEFICIENTE = coeficienterunoff(DECLIVIDADE)
        VAZAO_Q = vazao(COEFICIENTE, INTENSIDADE, Area_Bacia)
        # Resultados
        print ('\nTempo de concentracao da chuva e:' ,round(TEMPO_CONCENTRACAO,2),'minutos \n')
        print ('A intensidade de precipitação e:', round(INTENSIDADE,2),'mm/h \n')
        print('Vazao de projeto: ',round (VAZAO_Q,2), 'm³/s')
        print ('\n')
        break
    if i == data[-1]: #se a posição for igual ao ultimo elemento da lista
        print ('Municipio nao encontrado')
        break
