file_name = ["inouttime.txt", "leave_applications.txt", "room_info_boys.txt", "room_info_girls.txt",
             "student_info.txt", "room_info_others.txt", "visitor_info.txt"]

for x in file_name:
    fp = open(x,"x")
    fp.close()
