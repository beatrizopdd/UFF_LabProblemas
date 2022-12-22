package beecrowd_Java\lista_1;

import java.io.IOException;

import java.util.*;



public class Main {
    
    

	public static void main(String[] args) throws IOException {


		Scanner input = new Scanner(System.in);
        
		List<Double> combustivel = new ArrayList<>();


		for (int i = 0; i < 4; i ++) {
            

			combustivel.add(input.nextDouble());
            
      		}
        
        

		double alcool = combustivel.get(0);
        
		double gasolina = combustivel.get(1);
        
		double rAlcool = combustivel.get(2);
        
		double rGasolina = combustivel.get(3);
        
        

		double razaoAlcool = rAlcool / alcool;
        
		double razaoGasolina = rGasolina / gasolina;
        
        

		char escolhido = 'G';
        
        

		if (razaoAlcool > razaoGasolina) {
            
			escolhido = 'A';
        
		} else if (razaoAlcool <= razaoGasolina) {
            
			escolhido = 'G';
        
		}
 
        
        
		System.out.println(escolhido);
    

	}



}