import sqlite3

con = sqlite3.connect('application.db')

cur = con.cursor()

# Create table
cur.execute(
    'CREATE TABLE blogs (id text not null primary key, date text, title text, content text, public integer)'
    )

# Inser a few rows of data
cur.execute("INSERT INTO blogs VALUES ('blog1', '2023-03-07', 'My first blog', 'Content of blog1', 1)")
cur.execute("INSERT INTO blogs VALUES ('blog2', '2023-03-08', 'My second blog', 'Content of blog2', 1)")
cur.execute("INSERT INTO blogs VALUES ('blog3', '2023-03-09', 'Secret blog', 'This is secret', 0)")


# Save (commit) the changes
con.commit()


# Wecan also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
