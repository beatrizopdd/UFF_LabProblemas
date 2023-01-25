tentativas = gets.chomp.to_i
danos = 0

for i in 0...tentativas
	latas, copos = gets.split.map(&:to_i)
	
	if (latas > copos)
		danos += copos
	
	end
end

puts danos

