import json
jsondata="""[
         { "First Name" : "teacher1",
        "Last Name" : " last1",
        "Photo (Just a random url)" : "randomurl",
        "Department":"dep1" ,
        "Research Areas ":"r1 r2",
        "Contact Details ":"url2"
        },
         { "First Name":"teacher2",
        "Last Name":"last2",
        "Photo (Just a random url)":"url3",
        "Department" :"dep2",
        "Research Areas ":"r1 r3",
        "Contact Details ":"url4"
                 },
          {"First Name":"teacher3",
        "Last Name":"last3",
        "Photo (Just a random url)":"url5",
        "Department" :"dep2",
        "Research Areas ":"r3 r4",
        "Contact Details ":"url6"
                  }]"""
mydata=json.loads(jsondata)
print(mydata)
mydata2=json.dumps(mydata)