import pymysql
from config import host, password, user, db
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Connected successfully')
    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS orders;')
        cursor.execute('DROP TABLE IF EXISTS sales;')
        creat_sales = ("""CREATE TABLE IF NOT EXISTS sales
        (id INT PRIMARY KEY AUTO_INCREMENT,
        order_date DATE NOT NULL,
        count_product INT DEFAULT 0);""")
        creat_order = ("""CREATE TABLE IF NOT EXISTS orders
        (id INT PRIMARY KEY AUTO_INCREMENT,
        employee_id VARCHAR(10) NOT NULL,
        amount TIME DEFAULT '00:00:00',
        order_status VARCHAR(10) NOT NULL);""")
        cursor.execute(creat_order)
        cursor.execute(creat_sales)
        print('Tables created successfully')
        insert_sales = ("""INSERT sales(order_date, count_product)
        VALUES
        ('2022.01.01', 156),
        ('2022.01.02', 180),
        ('2022.01.03', 21),
        ('2022.01.04', 124),
        ('2022.01.05', 341);""")
        insert_order = ("""INSERT orders(employee_id, amount, order_status)
        VALUES
        ('e03',15.00, 'OPEN'),
        ('e01',25.50, 'OPEN'),
        ('e05',100.70, 'CLOSED'),
        ('e02',22.18, 'OPEN'),
        ('e04',9.50, 'CANCELLED');;""")
        cursor.execute(insert_sales)
        cursor.execute(insert_order)
        print('Insert successfully')
        connection.commit()
        select_sal = """SELECT id,
        CASE
            WHEN count_product < 100
            THEN 'Маленький заказ'
            WHEN count_product < 301
            THEN 'Средний заказ'
            ELSE 'Большой заказ'
        END AS 'Тип заказа'
        FROM sales;"""
        cursor.execute(select_sal)
        rows = cursor.fetchall()
        for row in rows:
            print(row['id'])
            print(row['Тип заказа'])
            print(row)
        select_order = """SELECT id,
        CASE
            WHEN order_status = 'OPEN'
                THEN 'Order is in open state'
            WHEN order_status =  'CLOSED'
                THEN 'Order is closed'
            ELSE  'Order is cancelled'
        END AS full_order_status
        FROM orders;"""
        cursor.execute(select_order)
        rows = cursor.fetchall()
        for row in rows:
            print(row['id'])
            print(row['full_order_status'])
            print(row)
    finally:
        connection.close()
except Exception as ex:
    print(ex)
    print('Disconnected')