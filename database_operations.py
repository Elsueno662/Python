import psycopg2

def insert_employee():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="office",
            user="postgres",
            password="postgres")

        cur = conn.cursor()
        sql = "INSERT INTO employee(name, address, contact, age) VALUES(%s,%s,%s,%s)"
        data_to_insert = ('Mark','Koteshwor','9841240367',23)
        cur.execute(sql, data_to_insert)
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_employee():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="office",
            user="postgres",
            password="postgres")

        cur = conn.cursor()
        sql = "UPDATE employee SET address=%s WHERE id=%s"
        data = ('Kamalpokhari', 1)
        cur.execute(sql, data)
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_employee():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="office",
            user="postgres",
            password="postgres")

        cur = conn.cursor()
        sql = "DELETE FROM employee WHERE id=%s"
        data = 2
        cur.execute(sql, [data])
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_rows():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="office",
            user="postgres",
            password="postgres")

        cur = conn.cursor()
        sql = "SELECT * FROM employee"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows


def bubble_sort():
    rows = get_rows()
    n = len(rows)
    for i in range(n-1):
        flag = True
        for j in range(0, n-i-1):
            if rows[j][4] > rows[j+1][4] :      #index 4 corresponds to the column age
                rows[j], rows[j+1] = rows[j+1], rows[j]
                flag = False
        if flag:
            break

    return rows


def binary_search(lis, value):
    l_lim = 0
    u_lim = len(lis) - 1
    mid = 0

    while l_lim <= u_lim:

        mid = (l_lim + u_lim) // 2

        if lis[mid][4] < value:
            l_lim = mid + 1

        elif lis[mid][4] > value:
            u_lim = mid - 1

        else:
            return mid

    return -1

sorted_rows = bubble_sort()
print("Employee records sorted age-wise:")
for r in sorted_rows:
    print(r)
print()
value = 21
result = binary_search(sorted_rows, value)  #value here refers to the age of the employee

if result != -1:
    print(f"Employee with age {value}:")
    print(f"id={sorted_rows[result][0]}, name={sorted_rows[result][1]}, address={sorted_rows[result][2]}, contact={sorted_rows[result][3]}, age={sorted_rows[result][4]}")
else:
    print("No such employee was found with the requested age value")