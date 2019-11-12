import sqlite3
from flask import request, flash

if __name__ == '__main__':
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    c.execute("CREATE TABLE mood (date TEXT, rating INTEGER)")
    c.execute("CREATE TABLE journal (date TEXT, response TEXT)")
    c.execute("CREATE TABLE moodNotes (date TEXT, note TEXT)")
    db.commit()
    db.close()

#adding entries to database
def addMood(date, rating){
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    vals = [date, rating]
    c.execute("INSERT INTO mood VALUES(?, ?)", vals)
    db.close()
}

def addJournal(date, response){
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    vals = [date, response]
    c.execute("INSERT INTO journal VALUES(?, ?)", vals)
    db.close()
}

def addMoodNotes(date, note){
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    c.execute("INSERT INTO moodNotes VALUES(?, ?)", vals)
    db.close()

}

# retrieve entries
def getJournal():
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    x = c.execute("SELECT date, response FROM journal")
    journal = []
    for row in x:
        journal.append(row)
    db.close()
    return journal

def getMoods():
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    x = c.execute("SELECT date, rating FROM mood")
    moodOvertime = []
    for row in x:
        moodOvertime.append(row)
    db.close()
    return moodOvertime

def getMoodNote(date):
    db = sqlite3.connect("data/moodTrack.db")
    c = db.cursor()
    x = c.execute("SELECT note FROM moodNotes WHERE date= ?", [date])
    db.close()
    return x
