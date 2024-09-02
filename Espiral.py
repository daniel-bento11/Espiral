x = 1
num = 1
entradas = "entradas.txt"

def leituraArquivo(entradas):
    with open(entradas, 'r') as entradas:
        for linha in entradas:
            numeros = linha.split()
            if len(numeros) == 2:
                num = int(numeros[0])
                x = int(numeros[1])
                if x!=0 and num!=0:
                    buscarSpiral(x,num)
                else:
                    break
                                   
        
def createSpiral(num):
    mat = [[0 for x in range(num)] for x in range(num)]
    inicio = 0
    fim = num-1
    cont = num**2  

    while cont>=1:
        for i in range (inicio, fim+1):
            mat[i][fim] = cont
            cont -= 1
        for i in range(fim-1, inicio-1, -1):
            mat[fim][i] = cont
            cont -= 1
        for i in range(fim-1, inicio-1,-1):
            mat[i][inicio] = cont
            cont -= 1
        for i in range(inicio+1, fim):
            mat[inicio][i] = cont
            cont -= 1
        inicio += 1
        fim -= 1
    return mat

def buscarSpiral(x,num):
    mat = createSpiral(num)
    for i in range (len(mat)):
        if x in mat[i]:
            coluna = mat[i].index(x)+1
            linha = num-i
            print(f"Line = {linha} , column = {coluna}")
            createOutput(linha, coluna)
            
            
def createOutput(linha, coluna):
    saidas = open('saidas.txt','a')
    saidas.write(f"Line = {linha}, column = {coluna}.\n")


leituraArquivo(entradas)



