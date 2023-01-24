L = gets.chomp.to_i
C = gets.chomp.to_i
H = L + C

if (H % 2 == 0)
  puts "1"
  
elsif (H % 2 != 0)
  puts "0"
  
end
