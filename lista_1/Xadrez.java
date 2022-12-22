package beecrowd_Java\lista_1;

import java.io.IOException;
import java.util.*;

public class Xadrez {
    
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);
        
        int linhas = input.nextInt();
        int colunas = input.nextInt();
        int cor = 0;
        
        if ((linhas + colunas) % 2 == 0) {
            cor = 1;
        } else if ((linhas + colunas) % 2 != 0) {
            cor = 0;
        }
        
        System.out.println(cor);

    }

}