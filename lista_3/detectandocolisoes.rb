x1, y1, x2, y2 = gets.split.map(&:to_i)
bx1, by1, bx2, by2 = gets.split.map(&:to_i)

checagem = [0, 0]

if (x1 <= bx1 and bx1 <= x2) or (x1 <= bx2 and bx2 <= x2) or (bx1 <= x1 and x1 <= bx2) or (bx1 <= x2 and x2 <= bx2)
    checagem[0] = 1
end

if (y1 <= by1 and by1 <= y2) or (y1 <= by2 and by2 <= y2) or (by1 <= y1 and y1 <= by2) or (by1 <= y2 and y2 <= by2)
    checagem[1] = 1
end


if (checagem[0] + checagem[1] == 2)
    puts "1"
    
else
    puts "0"
    
end
