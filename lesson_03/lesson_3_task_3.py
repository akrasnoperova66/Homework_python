from address import Address
from mailing import Mailing

address1 = Address("123456", "Москва", "ул. Большая Московская", "д.15", "4")
address2 = Address("789012", "Санкт-Петербург", "ул. Сенная", "д.10", "6")
mail = Mailing(address1, address2, 450, "46273940574635241")

print(mail)

