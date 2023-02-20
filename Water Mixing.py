n = int(input())
for x in range(n):
    inp = input().split()
    initial_temp = int(inp[0])
    final_temp = int(inp[1])
    hot_water = int(inp[2])
    cold_water = int(inp[3])
    tem_rise_hot = final_temp - initial_temp
    tem_fall_cold = initial_temp - final_temp
    if (tem_rise_hot and tem_fall_cold) == 0:
        print("YES")
    elif cold_water < tem_fall_cold:
        print("NO")
    elif hot_water < tem_rise_hot:
        print("NO")
    else:
        print("YES")


