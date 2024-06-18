from bs4 import BeautifulSoup
with open("samplexml.xml","r") as f:
    data = f.read()
Bs_data = BeautifulSoup(data, "xml")
b_names = Bs_data.find_all("name")
print(b_names)
b_waffle = Bs_data.find("food").find("name")
b_price = Bs_data.find("food").find("price")

print(b_waffle)
print(b_price)
