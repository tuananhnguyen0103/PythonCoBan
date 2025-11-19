while True:
    age = int(input("Bạn bao nhiêu tuổi? "))

    if age < 0:
        break

    if age < 18:
        print("Tuổi dưới 18")
    elif age >= 18 and age <= 25:
        print("Tuổi từ 18 đến 25")
    else:
        print("Tuổi trên 25")
