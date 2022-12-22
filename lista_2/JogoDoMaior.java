package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String[] arg) throws IOException {
		
		Scanner input = new Scanner(System.in);
		int rodadas = input.nextInt();
		
		while (rodadas != 0) {
			
			int jogador1 = 0;
			int jogador2 = 0;
			
			for (int i = 0; i < rodadas; i++) {
				
				List<Integer> numeros = new ArrayList<>();
				
				for (int k = 0; k < 2; k++){
					numeros.add(input.nextInt());
				}
				
				int a = numeros.get(0);
				int b = numeros.get(1);
				
				if (a > b) {
					jogador1 += 1;
				} else if (b > a) {
					jogador2 += 1;
				}		
			}
			
			System.out.println(jogador1 + " " + jogador2);
			
			rodadas = input.nextInt();
			
		}
		
	}

}