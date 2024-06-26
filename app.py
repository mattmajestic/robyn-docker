from robyn import Robyn
import sqlite3

app = Robyn(__file__)


@app.get("/")
def index():
    # your db name
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE test(column_1, column_2)")
    res = cur.execute("SELECT name FROM sqlite_master")
    th = res.fetchone()
    table_name = th[0]
    return f"Welcome to Robyn, This is a rust based Python package utilzing the effciency of Rust with simplicity of Python.  Here is an example fo the SQLtable create by default in this framework  {table_name}"


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
