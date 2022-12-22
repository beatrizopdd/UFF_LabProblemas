package beecrowd_Java\lista_1;

import java.io.IOException;
import java.util.*;

public class Main {
    
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);
		
		int[] pinosMeta = new int[2];
        
		for (int i = 0; i < 2; i ++) {
			pinosMeta[i] = input.nextInt();
		}
		
		int qtdPinos = pinosMeta[0];
		int[] alturas = new int[qtdPinos];
        
		for (int k = 0; k < qtdPinos; k ++) {
			alturas[k] = input.nextInt();
		}
		
		int movimentos = 0;
		int meta = pinosMeta[1];
		
		while (alturas != []) {
      
			int diferenca = meta - alturas[0];

			alturas[0] = alturas[0] + dif
			  alturas[1] = alturas[1] + dif

			  if alturas[1] == meta:
					alturas.pop(1)
			  alturas.pop(0)

			  if dif < 0:
					dif *= -1
			  movi += dif
		print(movi)
		

	}

}