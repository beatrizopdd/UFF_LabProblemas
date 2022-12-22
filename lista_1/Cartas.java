package beecrowd_Java\lista_1;

import java.io.IOException;

import java.util.*;



public class Cartas {
  
  
	public static void main(String[] args) throws IOException {
        
   	    
		Scanner input = new Scanner(System.in);
        
		List<Integer> sequencia = new ArrayList<>();
   
     
        
		for (int i = 0; i < 5; i ++) {
            
			sequencia.add(input.nextInt());
            
        
		}

       	 
        
		int a = sequencia.get(0);
        
		int b = sequencia.get(1);
        
		int c = sequencia.get(2);
        
		int d = sequencia.get(3);
        
		int e = sequencia.get(4);
   
     
   	     
		char ordem;
       
	 
        
		if (a <= b && b <= c && c <= d && d <= e) {
            
			ordem = 'C';
        
		} else if (e <= d && d <= c && c <= b && b <= a) {
            
			ordem = 'D';
        
		} else {
            
			ordem = 'N';
        
		}
       
 
        
		System.out.println(ordem);
    

	}




}