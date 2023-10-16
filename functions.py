import psycopg2
import words


# function which read data from Postgre database
def read_from_database():
    polaczenie = psycopg2.connect(host="localhost", database="vocabulary", user="postgres", password="admin", port=5432)
    kursor = polaczenie.cursor()
    sql = "select * from words"
    kursor.execute(sql)
    kill_gui = 0
    for w in kursor:
        say = words.Words(w[0], w[1], w[2], kill_gui)
        kill_gui = say.flashcard()
    kursor.close()

