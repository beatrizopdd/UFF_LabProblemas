package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);
		
		int nota = input.nextInt();
		char letra = 'N';
		
		if (nota == 0) {
			letra = 'E';
		} else if (nota >= 1 && nota <= 35 ) {
			letra = 'D';
		} else if (nota >= 36 && nota <= 60 ) {
			letra = 'C';
		} else if (nota >= 61 && nota <= 85 ) {
			letra = 'B';
		} else if (nota >= 86 && nota <= 100 ) {
			letra = 'A';
		}
		
		System.out.println(letra);

	}

}