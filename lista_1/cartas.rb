cartas = gets.split.map(&:to_i)

if ((cartas[0] < cartas[1]) and (cartas[1] < cartas[2]) and (cartas[2] < cartas[3]) and (cartas[3] < cartas[4]))
	puts "C"

elsif ((cartas[0] > cartas[1]) and (cartas[1] > cartas[2]) and (cartas[2] > cartas[3]) and (cartas[3] > cartas[4]))
	puts "D"
	
else
	puts "N"

end
