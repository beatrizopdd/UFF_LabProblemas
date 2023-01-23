def super_primo(num, status):

        
        

        

        else:
                return status
        
        
def primo(num):

        
	

while True:

        try:
                status = "Nada"
                primos = ["1", "2", "3", "5", "7"]
                digitos_primos = 0
                
                numero = int(input())

                if (numero >= 2):
                        for n in range(2, int(num ** 0.5)):
						    if (num % n == 0):
						            status = "Nada"
						            break

						status = "Primo"

                if (status == "Primo"):
                		for n in str(numero):
						    if (n in primos):
						            digitos_primos += 1

						if (digitos_primos == len(str(numero))):
								status = "Super"

                print(status)

        except EOFError:
                break
