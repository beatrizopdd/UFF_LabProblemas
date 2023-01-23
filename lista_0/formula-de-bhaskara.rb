a, b, c = gets.split.map(&:to_f)
delta = b ** 2 - 4 * a * c

if (delta < 0 or a == 0.0)
	puts "Impossivel calcular"
   
else
	raio1 = (delta ** 0.5 - b) / (2 * a)
    raio2 = (-delta ** 0.5 - b) / (2 * a)
    
    puts "R1 = %.5f" % raio1
    puts "R2 = %.5f" % raio2
    
end
