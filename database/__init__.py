import pymongo
 
client = pymongo.MongoClient('mongodb+srv://smartpet:smartpet@cluster0.jwnow.mongodb.net/?ssl=true&authSource=admin')
db = client["smartpet"]

