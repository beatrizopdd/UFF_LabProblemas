package beecrowd_Java\lista_2;

import java.io.IOException;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		Scanner input = new Scanner(System.in);	
		List<String> operacao = new ArrayList<>();
	
		int limite = input.nextInt();
		
		for (int i = 0; i < 3; i++) {
		    operacao.add(input.next());
		}
		
		int numero1 = Integer.parseInt(operacao.get(0));
		int numero2 = Integer.parseInt(operacao.get(2));
		int resultado = 0;
		
		String sinalProvisorio = operacao.get(1);
		char sinal = sinalProvisorio.charAt(0);
		
        if (sinal == '+') {
			resultado = numero1 + numero2;
		} else if (sinal == '*') {
			resultado = numero1 * numero2;
		} 
		
		if (resultado > limite) {
			System.out.println("OVERFLOW");
		} else {
			System.out.println("OK");
		}
		
	}

}