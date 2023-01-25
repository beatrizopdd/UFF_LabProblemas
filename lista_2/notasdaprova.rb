nota = gets.chomp.to_i

if (86 <= nota and nota <= 100)
	puts "A"

elsif (61 <= nota and nota <= 85)
	puts "B"
	
elsif (36 <= nota and nota <= 60)
	puts "C"

elsif (1 <= nota and nota <= 35)
	puts "D"
	
elsif (nota == 0)
	puts "E"
	
end
