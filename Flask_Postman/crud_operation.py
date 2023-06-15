from pymongo import MongoClient


'''
File contains mainly 4 operation

-Geting Data from database
    - get_all_data()
    - get_one_data(roll_no)
- Creating Data from database
    - insert_details(roll_no,name,age,class_,section)
-Update 
'''

class CRUD:
    def __init__(self):
        self.url = "mongodb://localhost:27017"
        self.client = MongoClient(self.url)
        self.db = self.client['Student']
        self.collection = self.db['Student_Details']

    def get_all_data(self):
        documents = list(self.collection.find())
        result = []
        for document in documents:
            document['_id'] = str(document['_id'])
            result.append(document)
        return result
    
    def get_one_data(self,roll_no):
        data=self.collection.find_one({"roll_no":roll_no})
        if data!=None:
            return data
        else:
            return "Not Present"
    def insert_details(self,roll_no,name,age,class_,section):
        data_to_insert={
            "name":name,"age":age,"class":class_,"sec":section,"roll_no":roll_no
        }
        self.collection.insert_one(data_to_insert)
        return self.collection
        
    def update_info(self, roll_no, name, age, class_, section):
        filter_ = {"roll_no": roll_no}
        new_values = {"$set": {
            "name": name,
            "age": age,
            "class": class_,
            "sec": section
        }}
        self.collection.update_one(filter_, new_values)

    def delete_info(self,roll_no):
        

        filter={"roll_no":roll_no}

        self.collection.delete_one(filter)

        return self.collection