package beecrowd_Java\lista_1;

import java.io.IOException;
import java.util.*;



public class Main {
    
    

	public static void main(String[] args) throws IOException {
        
        

		Scanner input = new Scanner(System.in);
        
		List<Integer> coordenadas = new ArrayList<>();
        
        

		for (int i = 0; i < 4; i ++) {
            
			coordenadas.add(input.nextInt());
        
		}
        
        

		int xM = coordenadas.get(0);
        
		int yM = coordenadas.get(1);
        
		int xR = coordenadas.get(2);
        
		int yR = coordenadas.get(3);
        
        

		int xD = Math.abs(Math.abs(xM) - Math.abs(xR));
        
		int yD = Math.abs(Math.abs(yM) - Math.abs(yR));
        
        


		System.out.println(xD + yD);

    

	}

}