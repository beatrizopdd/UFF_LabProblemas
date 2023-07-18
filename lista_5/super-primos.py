while True:
    try:
        numero = int(input()) # Recebe o número e já considera como não primo
        status = "Nada" 
        
        primoBase = (numero == 2) or (numero == 3) or (numero == 5) or (numero == 7) # Já trata os casos dos primos menores que 10
        if (primoBase == True):
            status = "Super"
        
        elif (numero >= 11): # Todos os números menores que 11 que não forem "primosBases" não são primos
        
            status = "Primo"
            
            for i in range(2, int(numero**0.5)+1): # Todo número é divisível por 1, vai de 2 até a raiz quadrada + 1
                if (numero % i == 0): # Para no momento que descobrir um divisor
                    status = "Nada"
                    break
                    
            if (status == "Primo"):
            
                status = "Super"
                numeroString = str(numero)
                    
                for i in numeroString:
                
                    digitoPrimo = (i == "2") or (i == "3") or (i == "5") or (i == "7") # Verifica se o dígito é primo
                    
                    if (digitoPrimo == False): # Para no primeiro dígito que não for primo
                        status = "Primo"
                        break
        
        print(status)
          
    except EOFError:
        break
