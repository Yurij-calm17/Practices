import psycopg2

try:
    conn = psycopg2.connect(
        dbname="military_db",
        user="postgres",
        password="postgres123",  # або твій реальний пароль
        host="localhost",
        port="5432"
    )
    print("✅ З'єднання з PostgreSQL успішне!")
    conn.close()
except Exception as e:
    print("❌ Помилка з'єднання:"
