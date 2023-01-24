convidados = gets.chomp.to_i
teste = 1

while (convidados != 0)
	lista = gets.split.map(&:to_i)
	
	for i in 0...convidados do
		if (lista[i] == i+1)
			puts "Teste #{teste}"
			puts i+1
			puts
    end
  end

	convidados = gets.chomp.to_i
	teste += 1

end
