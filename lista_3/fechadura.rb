pinos, meta = gets.split.map(&:to_i)
alturas = gets.split.map(&:to_i)

movimento = 0

while (alturas != [])
      
      	diferenca = meta - alturas[0]
      
      	alturas[0] += diferenca
      	alturas[1] += diferenca

      	if (alturas[1] == meta)
       		alturas.delete_at(1)
      	end 
      
		alturas.delete_at(0)
		movimento += diferenca.abs
		
end    
      
puts movimento
