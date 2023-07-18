risada = gets.chomp.to_s.chars
vogais = ['a','e','i','o','u']

for r in risada
	if r not in vogais
		risada.delete(r)
	end
end

re = risada
rd = risada.reverse

if (re == rd)
      print('S')
else:
      print('N')
