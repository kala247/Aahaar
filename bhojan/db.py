import MySQLdb
import json
import datetime

dbconn=MySQLdb.connect(
    database="bhojan", user="root", password="", host="localhost")
query = "select * from bhojan_partymenu;"
with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(query)
    data = cursor.fetchall()
    data =list(data)
jsondata=json.dumps(data,indent=4,default=str)
# print(data)
categorytypes ="select distinct category from bhojan_partymenu;"
with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(categorytypes)
    categorydata = cursor.fetchall()
category_list=[]
for i in range(0,len(categorydata)):
    category_list.append(categorydata[i]['category'])

# l = {'category':[]}
# cat_list =[]
def p_menu(l):
    # l = {'category':[]}
    cat_list =[]
    for item in range(0,len(category_list)):
        for i in range(len(data)):
            if category_list[item] == data[i]['category'] :
                cat_list.append(data[i])
        l['category'].append({category_list[item]:cat_list})
        cat_list= []
    print( json.dumps(l,indent=4, default=str) )
l = {'category':[]}
p_menu(l)

# k = json.dumps(l,indent=4, default=str)
# print(k["category"])
 
# with open('category.json', 'w') as json_file:
#     def myconverter(o):
#         if isinstance(o, datetime.datetime):
#             return o.__str__()
#     json.dump(l, json_file,default=myconverter)
    