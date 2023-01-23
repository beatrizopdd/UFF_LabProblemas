idade = gets.chomp.to_i

ano = (idade / 365).to_i
mes = ((idade % 365) / 30).to_i
dia = ((idade % 365) % 30).to_i

puts "#{ano} ano(s)"
puts "#{mes} mes(es)"
puts "#{dia} dia(s)"
