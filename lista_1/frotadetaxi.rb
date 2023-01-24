A, G, rendimentoA, rendimentoG = gets.split.map(&:to_f)

desempenhoA = rendimentoA / A
desempenhoG = rendimentoG / G

if desempenhoA > desempenhoG
	puts "A"
	
else 
	puts "G"
	
end
