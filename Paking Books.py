import math
n = int(input())
for x in range(n):
    inp = input().split()
    shelf_x = int(inp[0])
    shelf_has_books_y = int(inp[1])
    cardbox_z = int(inp[2])
    box_need = math.ceil(shelf_has_books_y / cardbox_z)
    total_box_needed = shelf_x * box_need
    print(total_box_needed)
