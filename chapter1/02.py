police = "パトカー"
taxi = "タクシー"
print("".join(map("".join, zip(police,taxi))))

# other

res = []
for i in range(4):
    res.append(police[i])
    res.append(taxi[i])
print("".join(res))
