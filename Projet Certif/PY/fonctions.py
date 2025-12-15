import sqlite3

def fetch_lessons_by_id(select,id) :
    """
    id => value to search for
    select => column to search in (e.g., 'lesson' or 'user')
    """
    conn = sqlite3.connect("node/BDD/BDD.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT file_path FROM Lessons WHERE id_{select} = {id}")
    donnees = [x[0] for x in cursor.fetchall()]
    conn.close()
    return donnees

def fetch_lessons_all() :
    conn = sqlite3.connect("node/BDD/BDD.db")
    cursor = conn.cursor()
    cursor.execute("SELECT file_path FROM Lessons")
    donnees = [x[0] for x in cursor.fetchall()]
    conn.close()
    return donnees

for p in fetch_lessons_by_id('user',1) :
    print(p)
# print(fetch_lessons_by_id('user',1))
# print(fetch_lessons_by_id('lesson',2))