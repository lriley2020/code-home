"""
Sixth code@home homework task
"""
import sqlite3

conn = sqlite3.connect("exam_results.db")
menuagain = "yes"
conn.execute('''CREATE TABLE IF NOT EXISTS results
          (name           VARCHAR(50)     NOT NULL,
           score          INT             NOT NULL,
           grade          VARCHAR(1)      NOT NULL
            );''')
print("Welcome to the grade storage utility!")
while menuagain == "yes":
    entries = conn.execute("SELECT count(rowid) FROM results;")
    print(f"You currently have {entries.fetchone()[0]} results stored")
    print("Would you like to add, view or delete entries? (1/2/3)")
    operation = int(input("> "))

    if operation == 1:
        name = input("Name: ")
        score = int(input("Score: "))
        if score > 100:
            print("Oops - that's not a valid score!")
            break
        if not score > 100:
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "U"
        conn.execute(f"INSERT INTO results (name, score, grade) \
              VALUES ('{name.title()}', {score}, '{grade}')")
        conn.commit()
        print("Another operation?")
        menuagain = input("> ")

    if operation == 2:
        tablequery = conn.execute("SELECT rowid,name FROM results;")
        print("""# | name\n--------""")
        for row in tablequery:
            print(f"{row[0]} | {row[1]}")
        print("Which student id would you like to see data for?")
        queryid = input("> ")
        detail = conn.execute(f"SELECT * FROM results WHERE rowid = {queryid};")
        for row in detail:
            print(f"Name: {row[0]}\nScore: {row[1]}\nGrade: {row[2]}")

    if operation == 3:
        tablequery = conn.execute("SELECT rowid,name FROM results;")
        print("""# | name\n--------""")
        for row in tablequery:
            print(f"{row[0]} | {row[1]}")
        print("Which score would you like to delete? (id)")
        rmid = input("> ")
        conn.execute(f"DELETE FROM RESULTS WHERE rowid = {rmid};")
        print("Successfully deleted that row")

conn.close()
