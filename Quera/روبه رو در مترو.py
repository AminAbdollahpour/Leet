data_lin1_list = input().split()
data_lin2_list = input().split()
ans = 0
for i in range(0, 8):
    if data_lin1_list[i] == '1':
        if data_lin2_list[i] == '1':
            ans += 1
print(str(ans))
