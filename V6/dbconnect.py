#!/usr/bin/python

import mysql.connector as sql
from mysql.connector import Error

config = {
	"user": "root",
#	"password": "root",
#	"password": "checkout",
#	"host": "192.168.1.11",
	"unix_socket": "/tmp/mysql.sock",
	"database": "pong",
	"raise_on_warnings": True,
}

def connect():
	try:
		db = sql.connect(**config)
		if db.is_connected():
			print("Connection successful!")

			cursor = db.cursor()
			query = ("SELECT * FROM matches ORDER BY gameDate ASC")
			cursor.execute(query)
			rows = cursor.fetchall()

			for row in rows:
				return (row)

			return rows

	except Error as e:
		print (e)

	finally:
		db.close()

#if __name__ == "__main__":
#	connect()

#cursor = db.cursor()

#query = ("SELECT * FROM scores "
#	"ORDER BY playerScore")

#cursor.execute(query)
