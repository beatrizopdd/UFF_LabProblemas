qtd = gets.chomp.to_i
secoes = gets.split.map(&:to_i)

tamanho = 0
metade = 0
indice_corte = 0

for s in secoes
	tamanho += s
end

tamanho /= 2

while (metade < tamanho)
	metade += secoes[indice_corte]
	indice_corte += 1
end
    
puts indice_corte
