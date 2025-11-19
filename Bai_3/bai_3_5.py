print("Giải bài toán 'Vừa gà vừa chó'")

print("Vừa gà vừa chó, bó lại cho tròn, 36 con 100 chân chẵn!")

found = False

for ga in range(0, 37):
    cho = 36 - ga
    if 2 * ga + 4 * cho == 100:
        print(f"Số gà = {ga}, số chó = {cho}")
        found = True
        break

if not found:
    print("Không có nghiệm phù hợp!")
