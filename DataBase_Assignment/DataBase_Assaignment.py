import sqlite3

# Use variable conn to create a database file using the sql3.connect command
conn = sqlite3.connect('files.db')

with  conn:
    # Make cur equal to the cursor command on conn
    cur = conn.cursor()
    # Use the .execute command to create two columns
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_names TEXT)")
    # Commit the changes made to the database
    conn.commit()

conn = sqlite3.connect('files.db')

# Creating a miltituple of files
files_tuple = ('information.docx','Hello.txt','myImage.png', \
               'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Loop through each object in the files tuple to find the names that end in .txt
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple
        # (x,) will denote a one-element tuple for each name ending in .txt
            cur.execute("INSERT INTO tbl_files (col_names) VALUES (?)",  (x,))
            print(x)
conn.close()
