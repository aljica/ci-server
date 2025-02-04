import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to a SQLite database

    Parameters:
    db_file (str): Database file

    Returns:
    conn (Connection): Connection to a SQLite database
   """    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """Create the build_history table

    Parameters:
    conn (Connection): Connection to a SQLite database
    create_table_sql (str): String representative of SQL query

    Returns:
    None
   """    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_commit(conn, commit):
    """Create a new task

    Parameters:
    conn (Connection): Connection to a SQLite database
    
    Return:
    last_row (str): String representative of integer ID of last row modified
   """    
    sql = ''' INSERT INTO history(commit_id,build_date,build_logs,url)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, commit)
    conn.commit()

    last_row = cur.lastrowid
    return last_row


def select_commit(conn, id):
    """Select commit by ID

    Parameters:
    conn (Connection): Connection to a SQLite database
    id (str): Commit ID (sha-hash)
    
    Return:
    build_details (dict): Dictionary containing commit info, including commit_id, build_date, build_logs and url
   """  
    cur = conn.cursor()
    cur.execute("SELECT * FROM history WHERE commit_id=?", (id,))

    row = cur.fetchone()
    if row is None:
        return {}
    build_details = {
        "commit_id": row[0],
        "build_date": row[1],
        "build_logs": row[2],
        "url": row[3]
    }
    return build_details


def select_all(conn):
    """Select all commits from history

    Parameters:
    conn (Connection): Connection to a SQLite database
    
    Return:
    rows (list): List containing all historical commits
   """ 
    cur = conn.cursor()
    cur.execute("SELECT * FROM history")

    rows = cur.fetchall()
    return rows

sql_create_build_history_table = """CREATE TABLE IF NOT EXISTS history (
                                    commit_id text PRIMARY KEY,
                                    build_date text NOT NULL,
                                    build_logs text NOT NULL,
                                    url text NOT NULL
                                );"""

# Initialize db connection and table.
def init():
    conn = create_connection(r"commit_history")
    if conn is not None:
        create_table(conn, sql_create_build_history_table)
    else:
        print("Error! cannot create the database connection.")

