from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Veritabanı bağlantısı (Render'dan aldığın External Database URL'i buraya yaz)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://beyza:BUqh2YXOo1ihM0ZSISi3tIzENBUbj2Yy@dpg-d46s2249c44c738mtgv0-a.oregon-postgres.render.com/hello_cloud3_db_vwg4")

@app.route('/')
def index():
    try:
        # PostgreSQL bağlantısı
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Veritabanına başarıyla bağlandı!<br>PostgreSQL sürümü: {db_version}"
    except Exception as e:
        return f"Bağlantı hatası: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
