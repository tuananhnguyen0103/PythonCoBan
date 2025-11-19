print("Giải bài toán 'Trăm trâu, trăm cỏ'")

for dung in range(0, 101):        # trâu đứng
    for nam in range(0, 101):     # trâu nằm
        for gia in range(0, 101): # trâu già
            if dung + nam + gia == 100 and (5 * dung + 3 * nam + gia / 3) == 100:
                print(f"Trâu đứng = {dung}, Trâu nằm = {nam}, Trâu già = {gia}")
