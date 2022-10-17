import requests
import mysql.connector
import json

##number loop for MySQL

theid = 2162
theidstring = str(theid)
##Connect to MySQL

def connect_it():
	mydb = mysql.connector.connect(
	host="51.159.113.75",
	port="25494",
	user="bbeyond",
	password="ajN}a-xBfgCXp5#4Ii$*K",
	database="rdb"
	)

	selectit = "SELECT d11880link FROM getter1 where id = "+str(theid)
	mycursor = mydb.cursor()
	mycursor.execute(selectit)

	myresult = mycursor.fetchall()
	print(mycursor.rowcount, "record(s) affected")

	for x in myresult:
		thelink = str(x)
		thelink2 = thelink.replace('(', '')
		thelink3 = thelink2.replace(',', '')
		thelink4 = thelink3.replace(')', '')
		thelink5 = thelink4.replace("'", "")
	return(thelink5)

#execute
connect_it()

########################################################

###ScrapingBee
def send_request():
	response = requests.get(
		url='https://app.scrapingbee.com/api/v1/',
		params={
			'api_key': '5G0U5CWV4MGEMMWXBLLHGR4ZN09N3HOTPTUEJCMC7U3KTDU6D7QOJVIM7JSCP1BTV19MOC91HTHGYH06',
			'url': connect_it(),
			'wait': '1000',
			'extract_rules': '{"email":{"selector":"#box-email-link > div.entry-detail-list__label","type":"item"},"webseite":{"selector":"#entry > div:nth-child(6) > div:nth-child(2) > div > div:nth-child(2) > a > div.entry-detail-list__label","type":"item"},"unternehmen":{"selector":"#entry > div:nth-child(2) > div.col-xs-10.col-sm-9 > h1","type":"item"},"branche":{"selector":"#entry > div:nth-child(4) > div > div > span > span > strong","type":"item"},"telefon":{"selector":"#entry > div:nth-child(6) > div:nth-child(1) > div > div:nth-child(1) > a > div.entry-detail-list__label","type":"item"},"adresse":{"selector":"#entry > div:nth-child(6) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span","type":"item"},"plz":{"selector":"#entry > div:nth-child(6) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span > span.js-postal-code","type":"item"},"ort":{"selector":"#entry > div:nth-child(6) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span > span.js-address-locality","type":"item"}}',
		},

	)
	#print('Response HTTP Status Code: ', response.status_code)
	#print('Response HTTP Response Body: ', response.content)
	thecontent = response.content
	contentget = json.loads(thecontent)

	websitevar = contentget["webseite"]
	mailvar = contentget["email"]
	unternehmen = contentget["unternehmen"]
	branche = contentget["branche"]
	telefon = contentget["telefon"]
	adresse = contentget["adresse"]
	plz = contentget["plz"]
	ort = contentget["ort"]



	if websitevar != "":
		print(websitevar)
		if mailvar == "":
			mailvar = "Keine E-Mail Adresse angegeben"
		print(mailvar)
		print(unternehmen)
		print(branche)
		print(telefon)
		print(adresse)
		print(plz)
		print(ort)
		def insert_it():
			mydb = mysql.connector.connect(
			host="51.159.113.75",
			port="25494",
			user="bbeyond",
			password="ajN}a-xBfgCXp5#4Ii$*K",
			database="rdb"
			)

			sql1 = "UPDATE getter1 SET website = "+'"'+str(websitevar)+'"'
			sql2 = sql1+", businessname = "+'"'+str(unternehmen)+'"'
			sql3 = sql2+", branche = "+'"'+str(branche)+'"'
			sql4 = sql3+", telefon = "+'"'+str(telefon)+'"'
			sql5 = sql4+", adresse = "+'"'+str(adresse)+'"'
			sql6 = sql5+", email = "+'"'+str(mailvar)+'"'
			sql7 = sql6+", plz = "+'"'+str(plz)+'"'
			sql8 = sql7+", ort = "+'"'+str(ort)+'"'
			sql9 = sql8+" WHERE ID = "+str(theid)

			sql = sql9

			mycursor = mydb.cursor()
			mycursor.execute(sql)

			mydb.commit()
			print(mycursor.rowcount, "record(s) affected")

		insert_it()
		return True
	return False

#################################

def send_request_secondtry5():
	response = requests.get(
		url='https://app.scrapingbee.com/api/v1/',
		params={
			'api_key': '5G0U5CWV4MGEMMWXBLLHGR4ZN09N3HOTPTUEJCMC7U3KTDU6D7QOJVIM7JSCP1BTV19MOC91HTHGYH06',
			'url': connect_it(),
			'wait': '1000',
			'extract_rules': '{"email":{"selector":"#box-email-link > div.entry-detail-list__label","type":"item"},"webseite":{"selector":"#entry > div:nth-child(5) > div:nth-child(2) > div > div:nth-child(2) > a > div.entry-detail-list__label","type":"item"},"unternehmen":{"selector":"#entry > div:nth-child(1) > div.col-xs-10.col-sm-9 > h1","type":"item"},"branche":{"selector":"#entry > div:nth-child(3) > div > div > span > span > strong","type":"item"},"telefon":{"selector":"#entry > div:nth-child(5) > div:nth-child(1) > div > div:nth-child(1) > a > div.entry-detail-list__label","type":"item"},"adresse":{"selector":"#entry > div:nth-child(5) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span","type":"item"},"plz":{"selector":"#entry > div:nth-child(5) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span > span.js-postal-code","type":"item"},"ort":{"selector":"#entry > div:nth-child(5) > div:nth-child(1) > div > div:nth-child(3) > div > div.entry-detail-list__label > span > span.js-address-locality","type":"item"}}',
		},

	)
	#print('Response HTTP Status Code: ', response.status_code)
	#print('Response HTTP Response Body: ', response.content)
	thecontent = response.content
	contentget = json.loads(thecontent)

	websitevar = contentget["webseite"]
	mailvar = contentget["email"]
	unternehmen = contentget["unternehmen"]
	branche = contentget["branche"]
	telefon = contentget["telefon"]
	adresse = contentget["adresse"]
	plz = contentget["plz"]
	ort = contentget["ort"]


	if websitevar != "":
		print(websitevar)
		if mailvar == "":
			mailvar = "Keine E-Mail Adresse angegeben"
		print(mailvar)
		print(unternehmen)
		print(branche)
		print(telefon)
		print(adresse)
		print(plz)
		print(ort)
		def insert_it():
			mydb = mysql.connector.connect(
			host="51.159.113.75",
			port="25494",
			user="bbeyond",
			password="ajN}a-xBfgCXp5#4Ii$*K",
			database="rdb"
			)

			sql1 = "UPDATE getter1 SET website = "+'"'+str(websitevar)+'"'
			sql2 = sql1+", businessname = "+'"'+str(unternehmen)+'"'
			sql3 = sql2+", branche = "+'"'+str(branche)+'"'
			sql4 = sql3+", telefon = "+'"'+str(telefon)+'"'
			sql5 = sql4+", adresse = "+'"'+str(adresse)+'"'
			sql6 = sql5+", email = "+'"'+str(mailvar)+'"'
			sql7 = sql6+", plz = "+'"'+str(plz)+'"'
			sql8 = sql7+", ort = "+'"'+str(ort)+'"'
			sql9 = sql8+" WHERE ID = "+str(theid)

			sql = sql9

			mycursor = mydb.cursor()
			mycursor.execute(sql)

			mydb.commit()
			print(mycursor.rowcount, "record(s) affected")
		insert_it()
		return True
	print("Anderer Fehler!")
	return False


while theid <= 2200:
	if send_request():
		print("Sucess")
		theid += 1
	else:
		send_request_secondtry5()
		print("Second try successs")
		theid += 1
else:
	print("Done!!!!!")

########################################################
