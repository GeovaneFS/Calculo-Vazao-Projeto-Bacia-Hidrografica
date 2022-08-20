'''Geovane Fernandes - o Código abaixo visa o calculo da vazão de projeto para uma bacia hidrografica
    sendo este calculo necessário para obtenção de outorgas para uso da água e ou dispensa de outorgas
    as equações utilizadas abaixo segundo literatura e utilizadas para bacias hidrograficas pequenas com áreas de ate
    2 km² e tempo de concentração menor que 1 hora.
    
    a equação utilizada na função intensidade de precipitação, serve apenas para o municipio de Lavras - MG, onde as constantes
    foram encontradas apos analise de dados historicos de chuva compreendidos entre 1914 e 1991.'''

# def tempo de concentração chuva Kirpich
def tempo (cursoagua, variacaoaltura):
    '''Calculo tempo de concentração usando equação de Kirpich'''
    Tempo_Concentracao = 57*(((cursoagua**3)/(variacaoaltura))**0.385)
    return Tempo_Concentracao

# def intensidade de precipitação
def intensidade (TR, TC):
    '''Calculo intensidade de precipitação'''
    Intensidade = ((842.702*(TR**0.179))/(10.39+TC)**0.736)
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
    UsodeArea = int (input ('Qual o uso e ocupação da área? 1 - Florestas, 2 - Pastagens, 3 - Terras Cultivadas: '))

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
Area_Bacia = float(input('Digite a area da bacia em km²: '))
print ('\n')
Comprimento_Curso = float(input('Digite o comprimento do curso dágua em km: '))
print ('\n')
Cota_Maxima = float(input('Digite a cota maxima da Bacia Hidrografica em m: '))
print ('\n')
Cota_Controle = float(input('Digite a conta do ponto de controle: '))
print ('\n')
Tempo_Retorno = int (input('Digite o tempo de retorno em anos: '))
print ('\n')

# Contas basicas
DESNIVEL = Cota_Maxima - Cota_Controle
DECLIVIDADE = DESNIVEL/(Comprimento_Curso*1000)
# Chamada das funções
COEFICIENTE = coeficienterunoff(DECLIVIDADE)
TEMPO_CONCENTRACAO = tempo(Comprimento_Curso, DESNIVEL)
INTENSIDADE = intensidade(Tempo_Retorno, TEMPO_CONCENTRACAO)
VAZAO_Q = vazao(COEFICIENTE, INTENSIDADE, Area_Bacia)

# Resultados
print ('O tempo de concentracao da chuva e:' ,round(TEMPO_CONCENTRACAO,2),'minutos \n')
print ('A intensidade de precipitação e:', round(INTENSIDADE,2),'mm/h \n')
print('Vazao de projeto: ',round (VAZAO_Q,2), 'm³/s')
