rodadas = gets.chomp.to_i

while (rodadas != 0)

	player1 = 0
	player2 = 0
	
	for r in 0...rodadas
		numero1, numero2 = gets.split.map(&:to_i)
		
		if (numero1 > numero2) 
			player1 += 1
		
		elsif (numero1 < numero2)
			player2 += 1
		
		end
	end
	
	puts "#{player1} #{player2}"
	rodadas = gets.chomp.to_i
	
end
