import pymongo

myclient = pymongo.MongoClient("mongodb://admin:DEPxfa35911@node9142-advweb-04.app.ruk-com.cloud:11164")
mydb = myclient["PorPlai"]
mycol = mydb["user"]

for x in mycol.find():
  print(x)