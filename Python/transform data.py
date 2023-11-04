import pandas as pd

st = {}
product_name = []
count_and_price = []
count = []
price = []
total_price = []
order_date = ''



with open('D:/Mail_read_files/email_body.txt', 'r', encoding='utf-8') as f:
    line = f.readline()  # считываем первую строку
    while line != '':  # пока не конец файла
        if 'Приход' in line:
            for i in range(3):
                line = f.readline()
            order_date = line.strip()
        if 'product-name' in line:
            line = f.readline()
            product_name.append(line.strip())
            for i in range(5):
                line = f.readline()
            count.append(func.parsing_quantity_and_price_per_one(line.strip())[0])
            price.append(round(func.parsing_quantity_and_price_per_one(line.strip())[1], 2))
            count_and_price.append(line.strip())
            for i in range(8):
                line = f.readline()
            total_price.append(line.strip())
        line = f.readline()  # читаем новую строку

# with open('D:/Mail_read_files/email_body.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()  # считываем первую строку
#     while line != '':  # пока не конец файла
#         if 'Приход' in line:
#             for i in range(3):
#                 line = f.readline()
#             order_date = line.strip()
#         if 'product-name' in line:
#             line = f.readline()
#             product_name.append(line.strip())
#             for i in range(5):
#                 line = f.readline()
#             count.append(func.parsing_quantity_and_price_per_one(line.strip())[0])
#             price.append(round(func.parsing_quantity_and_price_per_one(line.strip())[1], 2))
#             count_and_price.append(line.strip())
#             for i in range(8):
#                 line = f.readline()
#             total_price.append(line.strip())
#         line = f.readline()  # читаем новую строку

st.setdefault('product_name', product_name)
st.setdefault('count', count)
st.setdefault('price', price)
st.setdefault('total_price', total_price)

df = pd.DataFrame(st)

# Трансформация - необходимо распарсить поле count_and_price. поле total_price сделать int

# df['total_price'] = df['total_price'].astype(float)

# print(df['total_price'].dtype)