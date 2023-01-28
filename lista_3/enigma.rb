mensagem = gets.chomp.chars
criterio = gets.chomp.chars

possivel = 0
tamanho = criterio.length

while (mensagem.length >= criterio.length)

    particao = mensagem.slice(0, tamanho)
    
    indice = 0
    while (particao[indice] != criterio[indice] and indice < tamanho)
    	indice += 1
    end
    
    if (indice == tamanho)
    	possivel += 1
    end
    
    mensagem.delete_at(0)
 
end 
   
puts possivel
