Xm,Ym,Xr,Yr = gets.split.map(&:to_i)

diferencaX = (Xr).abs - (Xm).abs
diferencaY = (Yr).abs - (Ym).abs
distancia = (diferencaX).abs + (diferencaY).abs

puts distancia
