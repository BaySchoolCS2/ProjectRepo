import pymongo

print('This tool DELETES THE WHOLE DATABASE!  Use this tool ONLY IN LOCAL TESTING!')
Uin = raw_input('Are you sure you want to delete the WHOLE database [Y/n]')
Uin = Uin.lower()
if Uin == 'y':
	pymongo.MongoClient().drop_database('project')
