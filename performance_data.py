import pandas as pd
data = {"ID" : [1574,2258,3643,6464,9365,8476,4837,4738,2798,3180,1311,1622,4813,1437,1545,4516],
    "Name" :["Ali","Ahmad","Hamza","Ahad","Umer","Abubakar","Zahid","Uzair","Talha","Rehan","Mutahir","Abdul Rehman","Arsalan","Haris","Huzaifa","Ahad"],
    "Father Name" :["Ahad",None,"Ali","Rehan","Ali",None,"Hassan","Rafique","Amin",None,"Mubashir","Zia","Ali","Shaffiue","Zahid","Ahad"],
    "Joining_Date": ["2023-01-15","2024-03-10","2024-05-13","2025-5-14","2026-1-5","2023-01-15","2024-03-10","2024-05-13","2025-5-14","2026-1-5","2023-01-15","2024-03-10","2024-05-13","2025-5-14","2026-1-5","2024-05-13"],
    "Age" : [20,21,22,20,21,None,18,20,23,22,24,20,21,None,23,20],
    "Salary" : [50000,45000,25000,100000,75000,80000,95000,30000,20000,45000,50000,95000,70000,60000,40000,None],
    "Performance score" : [9,None,7,5,9,6,8,5,None,9,10,6,5,7,5,9],
    "College" : ["Science college","Punjab College","Superior College","Government College",None,"Science College","Unique College",None,"Superior College","Punjab College","Superior College","Government College","Punjab College","Science College","Science College","Science college"],
    "City" : ["Lahore","Lahore",None,"Multan","Karachi","Lahore",None,"Sodhiwal","Multan","Karachi","Lahore",None,"Sodhiwal","Multan","Karachi","Lahore"],
    "Role" : ["Employee","Employee","Manager","Accountant","Data scientist","AI Engineer","3D Motion Artist","Video Editor","Office Boy","ML Engineer","Data analyst","Boss","Programmer","Senior Manager","Distributor","Employe"],
    "Experience Months" : [19,26,None,5,32,9,21,16,None,25,28,19,15,12,9,19],
    "Shift" : ["Morning","Evening","Morning",None,"Morning","Evening","Morning","Evening","Morning","Evening",None,"Evening","Morning","Evening","Morning","Morning"],
    "Promotion": ["Yes","No","No","Yes","Yes","No","No","Yes","Yes","No","No","Yes","Yes","No","No","Yes"] 
    
}
df = pd.DataFrame(data)
print("Sample Data")
print(df)
print(df.describe())

df.to_csv("Performance.csv",index=False)