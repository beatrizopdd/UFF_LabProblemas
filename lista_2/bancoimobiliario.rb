quantia, operacoes = gets.split.map(&:to_i)

D = quantia
E = quantia
F = quantia

for p in 0...operacoes
	
	operacao = gets.split.map(&:to_s)
	valor = operacao[-1].to_i
    
    if (operacao[0] == "C")
    	if (operacao[1] == "D")
    		D -= valor
    		
    	elsif (operacao[1] == "E")
    		E -= valor
    		
    	elsif (operacao[1] == "F")
    		F -= valor
    
    	end
    	
    elsif (operacao[0] == "V")
		if (operacao[1] == "D")
    		D += valor
    		
    	elsif (operacao[1] == "E")
    		E += valor
    		
    	elsif (operacao[1] == "F")
    		F += valor
    
    	end
    
    elsif (operacao[0] == "A")
    	if (operacao[1] == "D")
    		D += valor
    		if (operacao[2] == "E")
    			E -= valor
    	
			elsif (operacao[2] == "F")
				F -= valor
			
			end
    		
    	elsif (operacao[1] == "E")
    		E += valor
    		if (operacao[2] == "F")
    			F -= valor
    	
			elsif (operacao[2] == "D")
				D -= valor
			
			end
    		
    	elsif (operacao[1] == "F")
    		F += valor
    		if (operacao[2] == "D")
    			D -= valor
    	
			elsif (operacao[2] == "E")
				E -= valor
			
			end
    		
    	end
    
    end 
    
end
                
puts "#{D} #{E} #{F}"
