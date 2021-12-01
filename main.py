import csv
from datetime import datetime
import ps5_bot

date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
headers = ["Ps5 Edition", "Date", "is Ps5 Available?"]
ps5 = ps5_bot.Ps5()

with open("ps5_availability.csv", "a") as file:
    write = csv.writer(file)
    # write.writerow(headers)  # Uncomment this line only the first you run this code

    write.writerow(["PS5通常版 Rakuten", date, ps5.is_available])
    write.writerow(["PS5デジタル版 Rakuten", date, ps5.is_available_2])
    write.writerow(["PS5通常版 ratchet and clank Amazon", date, ps5.is_available_3])
    write.writerow(["PS5通常版 Tales-ARISE Amazon", date, ps5.is_available_4])
    write.writerow(["PS5通常版 Spider-Man Amazon", date, ps5.is_available_5])
    write.writerow(["PS5通常版 Demon-Souls Amazon", date, ps5.is_available_6])
    write.writerow(["PS5通常版 Original Amazon", date, ps5.is_available_7])
    write.writerow(["PS5通常版 Original 2 Amazon", date, ps5.is_available_8])
    write.writerow(["PS5通常版 Original 3 Amazon", date, ps5.is_available_9])
    write.writerow(["PS5通常版 ratchet and clank bag Amazon", date, ps5.is_available_10])
    write.writerow(["PS5通常版 Rakuten New", date, ps5.is_available_11])
    write.writerow(["PS5デジタル版 Rakuten New", date, ps5.is_available_12])
