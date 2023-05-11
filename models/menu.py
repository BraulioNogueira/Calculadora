from controller.adicao  import adicao
from controller.subtracao import subtracao
from controller.multiplicacao import multiplicacao
from controller.divisao import divisao

def menu ():
    var = 'sim'
    while var == 'sim':
        operacao =input('Qual operação deseja saber (adicao,subtracao,multiplicacao,divisao) >>> ')
        if  operacao == 'divisao' :
            n1 = int(input('Digite um numero >>>'))
            n2 = int(input('Digite um numero >>>'))


            divisao(n1, n2)  

        elif  operacao == 'adicao':
            n1 = int(input('Digite um numero >>>'))
            n2 = int(input('Digite um numero >>>'))

            adicao(n1,n2)

        elif operacao == 'multiplicacao':
            n1 = int(input('Digite um numero >>>'))
            n2 = int(input('Digite um numero >>>'))

            multiplicacao(n1,n2)

        elif operacao == 'subtracao':
            n1 = int(input('Digite um numero >>>'))
            n2 = int(input('Digite um numero >>>'))

            subtracao(n1,n2)
            
        var = input('Deseja continuar >>>')   
                 

      


