limite = gets.chomp.to_i
num1, operador, num2 = gets.split.map(&:to_s)

if (operador == "+")
    resultado = num1.to_i + num2.to_i
    
elsif (operador == "*")
    resultado = num1.to_i * num2.to_i

end

if (resultado <= limite)
    puts "OK"
    
else
    puts "OVERFLOW"
    
end
