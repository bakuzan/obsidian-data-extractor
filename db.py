import sqlite3
import os


def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row  # Make query results dict rather than tuple
    except IOError as e:
        print(e)

    return conn

# Fetch queries
def fetch_file_data(conn, file):
    """
    Query rows in the Files table for file
    :param conn: the Connection object
    :return: None
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Files WHERE Location = ? AND Name = ?", (file["Location"],file["Name"],))
    return cur.fetchone()

# Mutations
def create_file(conn, file):
    """
    Create a new file into the files table
    :param conn:
    :param file:
    :return: file id
    """
    sql = '''
        INSERT INTO Files(Location, Name, WordCount) 
        VALUES(:Location, :Name, :WordCount)
    '''
    cur = conn.cursor()
    cur.execute(sql, file)
    conn.commit()
    return cur.lastrowid

def update_file(conn, update):
    """
    Update a file in the files table
    :param conn:
    :param update:
    :return: file id
    """
    sql = '''
        UPDATE Files
           SET WordCount = :WordCount
         WHERE Id = :FileId
    '''
    cur = conn.cursor()
    cur.execute(sql, update)
    conn.commit()
    return cur.lastrowid

# Action
def add_or_update_file_data(file):
    database = os.getenv("DATABASE_PATH")
    conn = create_connection(database)

    with conn:
        # Check if file already exists
        existing_record = fetch_file_data(conn, file)
        
        if existing_record:
            update = {}
            update["FileId"] = existing_record["Id"]
            update["WordCount"] = file["WordCount"]
            file_id = update_file(conn, update)
            print(f"File({file_id}) already exists in database, updating...")
        else:
            # Create file entry as it doesn't exist
            file_id = create_file(conn, file)
            print(f"File({file_id}) added to database.")