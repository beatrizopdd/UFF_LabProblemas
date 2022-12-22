package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);		
		List<Integer> cartas = new ArrayList<>();
		
		for (int i = 0; i < 2; i++) {
			cartas.add(input.nextInt());
		}
		
		int cartaA = cartas.get(0);
		int cartaB = cartas.get(1);
		int coringa = 0;
		
		if (cartaA >= cartaB) {
			coringa = cartaA;
		} else if (cartaA < cartaB) {
			coringa = cartaB;
		}
		
		System.out.println(coringa);
		
	}

}