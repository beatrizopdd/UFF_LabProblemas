package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);
		
		int quebrados = 0;
		int qtdBandejas = input.nextInt();
		int latas = 0;
		int copos = 0;
		
		for (int i = 0; i < qtdBandejas; i++) {
			
			List<Integer> bandeja = new ArrayList<>();
			
			for (int k = 0; k < 2; k++) {
				bandeja.add(input.nextInt());
			}
			
			latas = bandeja.get(0);
			copos = bandeja.get(1);
				
			if (latas > copos) quebrados += copos;
		
		}
		
		System.out.println(quebrados);
		
	}

}
