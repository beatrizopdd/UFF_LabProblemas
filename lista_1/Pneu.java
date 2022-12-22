package beecrowd_Java\lista_1;
import java.io.IOException;
import java.util.*;

public class Pneu {
    
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);
        
        int pDesejada = input.nextInt();
        int pLida = input.nextInt();
        int diferenca = pDesejada - pLida;
        
        System.out.println(diferenca);

    }

}