student_info1 = {
    "Name": "Kisho",
    "Age" : "24",
    "Address" : "CTC",
}
student_info2 = {
    "Name": "Mimo",
    "Age" : "25",
    "Address" : {
       "Home Address" : "DKL",
        "Office Address" : "BBS"
    }
}

student_list = [student_info1, student_info2]
print(student_list)

print(student_list[0])
print(student_list[0]["Name"])
#print(student_list[1]["Address"]["Home Address"])

