x1, y1 = gets.split.map(&:to_f)
x2, y2 = gets.split.map(&:to_f)

distancia = ((x2 - x1) ** 2  + (y2 - y1) ** 2) ** 0.5

puts "%.4f" % distancia
