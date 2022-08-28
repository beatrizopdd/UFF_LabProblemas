package beecrowd_Java\lista_1;

import java.io.IOException;
import java.util.*;

public class Main {
    
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);
		
		String mensagem = input.next();
		String crib = input.next();

		copiam = []
		for i in mensagem:
			copiam.append(i)
		copiac = []
		for j in criterio:
			copiac.append(j)

		ok = 0
		tamanho = len(copiac)
		while len(copiam) >= tamanho:
			fatia = copiam[0:tamanho]
			Ih = 0
			for k in range(tamanho):
				if fatia[k] == copiac[k]:
					Ih += 1
					break
			if Ih == 0:
				ok += 1
			copiam.pop(0)
			
		print(ok)



	}

}