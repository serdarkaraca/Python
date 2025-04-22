def not_sil(not_id):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notlar WHERE id = ?", (not_id,))
    conn.commit()
    conn.close()
