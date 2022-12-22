package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);
		List<Integer> configuracao = new ArrayList<>();
		
		for (int i = 0; i < 2; i++) {
			configuracao.add(input.nextInt());
		}
		
		int saldo = configuracao.get(0);
		int rodadas = configuracao.get(1);
		int d = saldo;
		int e = saldo;
		int f = saldo;
		
		for (int k = 0; k < rodadas; k++) {
			
			String[] acoes = input.nextLine().split(" ");
			
			String acao  = acoes[0];
			String pessoa1 = acoes[1];
			String pessoa2 = "N";
			int reais = Integer.parseInt(acoes[2]);
			
			if (pessoa1 == "D") {
				
				if (acao == "C") {
					d -= reais;
					
				} else if (acao == "V") {
					d += reais;
					
				} else if (acao == "A") {
					reais = Integer.parseInt(acoes[3]);
					pessoa2 = acoes[2];
					d += reais;
					if (pessoa2 == "E") {
						e -= reais;
					} else if (pessoa2 == "F") {
						f -= reais;
					}
				}
				
			} else if (pessoa1 == "E") {
				
				if (acao == "C") {
					e -= reais;
					
				} else if (acao == "V") {
					e += reais;
					
				} else if (acao == "A") {
					reais = Integer.parseInt(acoes[3]);
					pessoa2 = acoes[2];
					e += reais;
					if (pessoa2 == "D") {
						d -= reais;
					} else if (pessoa2 == "F") {
						f -= reais;
					}
				}
				
			} else if (pessoa1 == "F") {
				
				if (acao == "C") {
					f -= reais;
					
				} else if (acao == "V") {
					f += reais;
					
				} else if (acao == "A") {
					reais = Integer.parseInt(acoes[3]);
					pessoa2 = acoes[2];
					f += reais;
					if (pessoa2 == "D") {
						d -= reais;
					} else if (pessoa2 == "E") {
						e -= reais;
					}
				}
				
			} 
			
			System.out.println(d + " " + e + " " + f);
		}

	}

}