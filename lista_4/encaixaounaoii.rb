teste = gets.chomp.to_i

for t in 0...teste
	A, B = gets.split.map(&:to_s)
	copiaA = A.slice(A.length - B.length, B.length)
	
	if (copiaA == B)
		puts "encaixa"
	else
		puts "nao encaixa"
	end
	
end
