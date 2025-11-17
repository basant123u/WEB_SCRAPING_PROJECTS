import requests
from bs4 import BeautifulSoup
import pandas as pd
import pdfkit
from xhtml2pdf import pisa

names_final = []
price_final = []
ram_rom_final = []
battery_final = []
processor_final = []


for t in range(1,7):
    url = f"https://www.flipkart.com/search?q=samsung+smartphone+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={t}"


    r = requests.get(url)
    r_str = str(r.text)

    soup = BeautifulSoup(r_str, "html.parser")

    name = soup.find_all("div", class_ = "KzDlHZ")
    name_len = len(name)

    for i in range (name_len):
        a = name[i].text
        append_name = names_final.append(a)


    price = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")
    price_len = len(price)

    for i in range (price_len):
        a = price[i].text
        append_price = price_final.append(a)


    ram_rom = soup.find_all("ul", class_ = "G4BRas")

    ramrom_len = len(ram_rom)
    for i in range(ramrom_len):
        ramrom_text = ram_rom[i].text
        str_ramrom = str(ramrom_text)
        a = str_ramrom[0:21]
        append_ramrom = ram_rom_final.append(a)


    battery = soup.find_all("ul", class_ = "G4BRas")

    battery_len = len(battery)

    for i in range(battery_len):
        battery_txt = battery[i].text

        try:
            index1 = battery_txt.index("amera")
            index2 = battery_txt.index("Battery")
            f_index1 = index1 + 5
            f_index2 = index2 - 1
            a = battery_txt[f_index1:f_index2]
            append_battery = battery_final.append(a)
        except ValueError:
            append_ = battery_final.append("not listed")
            continue

    processor = soup.find_all("ul", class_ = "G4BRas")

    processor_len = len(processor)


    for i in range(processor_len):
        processor_txt = processor[i].text
        try:
            index1 = processor_txt.index("Battery")
            index2 = processor_txt.index("Processor")
            f_index1 = index1 + 7
            f_index2 = index2 + 9
            a = processor_txt[f_index1:f_index2]
            append = processor_final.append(a)

        except ValueError:
            append_ = processor_final.append("not listed in flipkart")
            continue



# print(len(names_final))
# print(len(price_final))
# print(len(ram_rom_final))
# print(len(battery_final))
# print(len(processor_final))

data = {"PRODUCT NAME(SAMSUNG)": names_final, "PRICE": price_final, "RAM | ROM": ram_rom_final, "BATTERY": battery_final, "PROCESSOR NAME": processor_final}

df = pd.DataFrame(data)

html_file = "under25k_mobs.html"
df.to_html(html_file)

with open("under25k_mobs.html") as f:
    html = f.read()

with open("under25k_mobs.pdf", "wb") as pdf:
    pisa.CreatePDF(html, pdf)

# pdfkit.from_file(html_file, "under25k_mob.pdf")



print("PDF created")