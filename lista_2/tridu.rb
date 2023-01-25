carta1, carta2 = gets.split.map(&:to_i)

if (carta1 >= carta2)
	puts carta1

elsif (carta1 < carta2)
	puts carta2

end
