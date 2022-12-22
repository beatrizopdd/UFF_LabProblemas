package beecrowd_Java\lista_1;

import java.io.IOException;

import java.util.*;



public class Main {
    
    

	public static void main(String[] args) throws IOException {
        
        		
		Scanner input = new Scanner(System.in);
        
        

		int teste = 1;
        
		int participantes = input.nextInt();
        
        

		while (participantes != 0) {
            
           

			List<Integer> entrada = new ArrayList<>();
        
            		
			for (int i = 0; i < participantes; i ++) {
            
				entrada.add(input.nextInt());
            
			}
            
            

			int ganhador = 1;
            
			for (int i = 0; i < participantes; i++) {
                							int pessoa = entrada.get(i);
                
				if (pessoa == ganhador) break;
                
				ganhador += 1;
            
			}
            
            
				
			System.out.println("Teste " + teste++);
            
			System.out.println(ganhador);
            
			System.out.println();
            
            		
	
			participantes = input.nextInt();
            
        
		}
    
	}

}