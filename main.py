# -*- coding: utf-8 -*-
import nfc
import binascii
import sqlite3

dbname = "nfclogger.db"
db = sqlite3.connect(dbname)

def on_connect(tag):
	print "Touch!"
	idm = binascii.hexlify(tag.idm)

	c = db.cursor();
	sql = 'insert into log (idm, date) values (?,?)'
	sqlvar = (idm, `

def on_release(tag):
	print "Release!"

def main():
	with nfc.ContactlessFrontend('usb') as clf:
		clf.connect(rdwr={'on-connect': on_connect, 'on-release': on_release})


if __name__ == '__main__':
	main()
