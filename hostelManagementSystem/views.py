# i have created this file -- omkar

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import HostelDataClass
from .models import HostelReviews


# Homepage rendering code
# ==================================================================================================================================
def homepage(request):
    return render(request, 'homepage.html')
    # return HttpResponse("<h1>Hello Home</h1>")


# ======================================================================================================================
# HOMEPAGE RENDERING DONE

# ADMIN LOGIN
# =======================================================================================================================
def adminlogin(request):
    return render(request, 'adminlogin.html')


# ========================================================================================================================
# ADMIN LOGIN Done

# GO TO ADMIN PAGE
# =======================================================================================================================
def adminpage(request):
    uname = request.GET.get('uname', 'User')
    params = {'uname': uname}
    return render(request, 'adminpage.html', params)


# =======================================================================================================================
# ADMIN PAGE RENDERED

# Admin CRUD OPERATIONS
# =========================================================================================================================================
# Does searcch query based on given inputs by admin
def showdata(request):
    inputhostelnum = request.GET.get('hnum', 'default')
    inputfloornum = request.GET.get('fnum', 'default')
    inputroomnum = request.GET.get('rnum', 'default')
    inputstudentroll = request.GET.get('sroll', 'default')
    inputstudentname = request.GET.get('sname', 'default')
    inputstudentdept = request.GET.get('sdept', 'default')

    # print(inputhostelnum, inputfloornum, inputroomnum,inputstudentroll,inputstudentname,inputstudentdept)

    # filtering out data on the basis of given inputs (when inputs are not empty)

    showall = HostelDataClass.objects.all()
    if inputhostelnum != '':
        showall = showall.filter(hoastelalloted__contains=inputhostelnum)
    if inputfloornum != '':
        showall = showall.filter(floorno=inputfloornum)
    if inputroomnum != '':
        showall = showall.filter(roomno=inputroomnum)

    if inputstudentroll != '':
        showall = showall.filter(rollnumber__contains=inputstudentroll)
    if inputstudentname != '':
        showall = showall.filter(studentname__contains=inputstudentname)
    if inputstudentdept != '':
        showall = showall.filter(department__contains=inputstudentdept)

    # showall = {'hostelnum': hostelnum, 'floornum': floornum,'roomnum':roomnum, 'Student_name': 'OmkarKadam', 'Student_branch': 'CSE', 'Student_rollnum':'22m2112'}
    return render(request, 'showdata.html', {"hosteldata": showall})


#  inserting the record based on hostel number, room number , floor number, name, branch and rollnumber
def insertdata(request):
    # checking on POST request if all inputs are provided by admin
    if request.method == 'POST':
        if request.POST.get('insertrollnumber') and \
                request.POST.get('insertstudentname') and \
                request.POST.get('insertdepartment') and \
                request.POST.get('inserthoastelalloted') and \
                request.POST.get('insertroomno') and \
                request.POST.get('insertfloorno'):

            inputhostelnum = request.POST.get('inserthoastelalloted')
            inputfloornum = request.POST.get('insertfloorno')
            inputroomnum = request.POST.get('insertroomno')
            inputstudentroll = request.POST.get('insertrollnumber')
            inputstudentname = request.POST.get('insertstudentname')
            inputstudentdept = request.POST.get('insertdepartment')

            # filtering out data on the basis of given inputs (when inputs are not empty)
            showall = HostelDataClass.objects.all()
            if inputhostelnum != '':
                showall = showall.filter(hoastelalloted__contains=inputhostelnum)
            if inputfloornum != '':
                showall = showall.filter(floorno=inputfloornum)
            if inputroomnum != '':
                showall = showall.filter(roomno=inputroomnum)

            if inputstudentroll != '':
                showall = showall.filter(rollnumber__contains=inputstudentroll)
            if inputstudentname != '':
                showall = showall.filter(studentname__contains=inputstudentname)
            if inputstudentdept != '':
                showall = showall.filter(department__contains=inputstudentdept)

            # temporary class object saverecord is created and all the inputs from user  stored into it
            saverecord = HostelDataClass()
            saverecord.rollnumber = request.POST.get('insertrollnumber')
            saverecord.studentname = request.POST.get('insertstudentname')
            saverecord.department = request.POST.get('insertdepartment')
            saverecord.hoastelalloted = request.POST.get('inserthoastelalloted')
            saverecord.roomno = request.POST.get('insertroomno')
            saverecord.floorno = request.POST.get('insertfloorno')
            # Checks it room already exists
            if HostelDataClass.objects.filter(roomno=saverecord.roomno).exists():
                if HostelDataClass.objects.filter(rollnumber=saverecord.rollnumber).exists():
                    messages.success(request, "Student " + saverecord.studentname + " cannot be added to Room " + str(
                        saverecord.roomno) + "\n----FAILED to ADD \n Room Already Occupied\n")
                else:
                    saverecord.save()
                    messages.success(request,
                                     "Student " + saverecord.studentname + " is added to Hostel " + saverecord.hoastelalloted + " Room " + str(
                                         saverecord.roomno) + " SUCCESSFULLY!!\n")
                    return render(request, 'showdata.html', {"hosteldata": showall})
            else:
                saverecord.save()
                messages.success(request, "New Room Created Room No. " + str(
                    saverecord.roomno) + "Student " + saverecord.studentname + " Added successfully")
                return render(request, 'showdata.html', {"hosteldata": showall})
    return render(request, 'showdata.html')


#  Updating the record based on hostel number, room number , floor number, name, branch and rollnumber
def updatedata(request):
    # checking on POST request if all inputs are provided by admin
    if request.POST.get('updaterollnumber') and \
            request.POST.get('updatestudentname') and \
            request.POST.get('updatedepartment') and \
            request.POST.get('updatehoastelalloted') and \
            request.POST.get('updateroomno') and \
            request.POST.get('updatefloorno'):
        inputhostelnum = request.POST.get('updatehoastelalloted')
        inputfloornum = request.POST.get('updatefloorno')
        inputroomnum = request.POST.get('updateroomno')
        inputstudentroll = request.POST.get('updaterollnumber')
        inputstudentname = request.POST.get('updatestudentname')
        inputstudentdept = request.POST.get('updatedepartment')

        # filtering out data on the basis of given inputs (when inputs are not empty)
        showall = HostelDataClass.objects.all()
        if inputhostelnum != '':
            showall = showall.filter(hoastelalloted__contains=inputhostelnum)
        if inputfloornum != '':
            showall = showall.filter(floorno=inputfloornum)
        if inputroomnum != '':
            showall = showall.filter(roomno=inputroomnum)

        if inputstudentroll != '':
            showall = showall.filter(rollnumber__contains=inputstudentroll)
        if inputstudentname != '':
            showall = showall.filter(studentname__contains=inputstudentname)
        if inputstudentdept != '':
            showall = showall.filter(department__contains=inputstudentdept)

        updaterollnumber = request.POST.get('updaterollnumber')
        updatestudentname = request.POST.get('updatestudentname')
        updatedepartment = request.POST.get('updatedepartment')
        updatehoastelalloted = request.POST.get('updatehoastelalloted')
        updateroomno = request.POST.get('updateroomno')
        updatefloorno = request.POST.get('updatefloorno')

        if HostelDataClass.objects.filter(roomno=updateroomno).exists():
            updaterecord = HostelDataClass.objects.get(roomno=updateroomno)
            updaterecord.rollnumber = updaterollnumber
            updaterecord.studentname = updatestudentname
            updaterecord.department = updatedepartment
            updaterecord.hoastelaloted = updatehoastelalloted
            updaterecord.roomno = updateroomno
            updaterecord.floorno = updatefloorno
            updaterecord.save()
            messages.success(request,
                             "Student " + updaterecord.studentname + " is Updated to Hostel " + updaterecord.hoastelalloted + " Room " + str(
                                 updaterecord.roomno) + " SUCCESSFULLY!!\n")
            return render(request, 'showdata.html', {"hosteldata": showall})
        else:
            messages.success(request,
                             "Student " + updatestudentname + " is cannot be Updated to Hostel " + updatehoastelalloted + " Room " + str(
                                 updateroomno) + " \n----- Failed to Update -----\n DOES NOT EXISTS TO UPDATE \n")
    return render(request, 'showdata.html')


#  Deleting the record based on hostel number, room number , floor number
def deletedata(request):
    if request.POST.get('deletehoastelalloted') and \
            request.POST.get('deleteroomno') and \
            request.POST.get('deletefloorno'):

        inputhostelnum = request.POST.get('deletehoastelalloted')
        inputfloornum = request.POST.get('deletefloorno')
        inputroomnum = request.POST.get('deleteroomno')

        # filtering out data on the basis of given inputs (when inputs are not empty)
        showall = HostelDataClass.objects.all()
        if inputhostelnum != '':
            showall = showall.filter(hoastelalloted__contains=inputhostelnum)
        if inputfloornum != '':
            showall = showall.filter(floorno=inputfloornum)
        if inputroomnum != '':
            showall = showall.filter(roomno=inputroomnum)

        deletehoastelalloted = request.POST.get('deletehoastelalloted')
        deleteroomno = request.POST.get('deleteroomno')
        deletefloorno = request.POST.get('deletefloorno')
        if HostelDataClass.objects.filter(roomno=deleteroomno, hoastelalloted=deletehoastelalloted,
                                          floorno=deletefloorno).exists():
            deleterecord = HostelDataClass.objects.get(roomno=deleteroomno, hoastelalloted=deletehoastelalloted,
                                                       floorno=deletefloorno)
            messages.success(request,
                             "Student record " + deleterecord.studentname + " is deleted from Hostel " + deleterecord.hoastelalloted + " Room " + str(
                                 deleterecord.roomno) + " SUCCESSFULLY!!\n")
            deleterecord.delete()
            return render(request, 'showdata.html', {"hosteldata": showall})
        else:
            messages.success(request,
                             "Student record cannot be deleted from Hostel " + deletehoastelalloted + " Room " + str(
                                 deleteroomno) + " \n----- Failed to Delete---- \nDOES NOT EXISTS\n")
    return render(request, 'showdata.html')


# ===========================================================================================================================================================================
# ADMIN CRUD OPERATIONS ENDS

#  USER login
# ==============================================
def userlogin(request):
    return render(request, 'userlogin.html')


# ================================================
# USER LOGIN done

# GO TO USER PAGE
# =======================================================================================================================
def userpage(request):
    uname = request.GET.get('uname', 'User')
    params = {'uname': uname}
    return render(request, 'userpage.html', params)


# =======================================================================================================================
# USER PAGE RENDERED

# User preference Accepted or Rejected
# =======================================================================================================================
from django.db import transaction
from django.core.cache import cache

@transaction.atomic
def prefresult(request):
    if request.method == 'POST':
        # Check if all required entries are provided in the POST request
        if all(request.POST.get(key) for key in ['sroll', 'sname', 'sdept', 'hnum1', 'fnum1', 'rnum1', 'hnum2', 'fnum2', 'rnum2', 'hnum3', 'fnum3', 'rnum3']):
            # Temporary variables to store inputs
            rollnumber = request.POST.get('sroll')
            studentname = request.POST.get('sname')
            department = request.POST.get('sdept')
            allocated_room = None
            
            # Loop through the preferences and attempt to allocate the room
            for pref_num in range(1, 4):
                hnum = request.POST.get(f'hnum{pref_num}')
                rnum = request.POST.get(f'rnum{pref_num}')
                fnum = request.POST.get(f'fnum{pref_num}')
                
                # Attempt to allocate the room
                allocated_room = allocate_room(rollnumber, studentname, department, hnum, rnum, fnum)
                
                # If room allocation is successful, break the loop
                if allocated_room:
                    break
            
            # Check if room allocation was successful
            if allocated_room:
                messages.success(request, f"Student {studentname} allocated to Room {allocated_room.roomno}")
            else:
                messages.error(request, f"Failed to allocate room for Student {studentname}")
        
        else:
            messages.error(request, "Some entries are missing in the preferences. Please fill all fields.")
    
    return render(request, 'prefresult.html')

def allocate_room(rollnumber, studentname, department, hnum, rnum, fnum):
    lock_key = f"room_lock_{rnum}"
    
    # Acquire lock for the room
    with cache.lock(lock_key):
        # Check if the room exists and is available
        if HostelDataClass.objects.filter(roomno=rnum).exists():
            room = HostelDataClass.objects.get(roomno=rnum)
            
            # Check if the room is vacant
            if not room.rollnumber:
                # Allocate the room to the student
                room.rollnumber = rollnumber
                room.studentname = studentname
                room.department = department
                room.save()
                return room
            
            else:
                return None
        else:
            return None


# ========================================================================================================================
# Preference Allocation Done


# Enter / Show reviews by student
# =========================================================================================================================================
def reviewpage(request):
    return render(request, "insertreview.html")


def searchreview(request):
    showall = HostelReviews.objects.all()
    inputsname = request.GET.get('sname', 'default')
    inputsroll = request.GET.get('sroll', 'default')
    inputhnum = request.GET.get('hnum', 'default')
    # print(inputsname)
    # filtering out data on the basis of given inputs (when inputs are not empty)

    if inputsname != '':
        showall = showall.Q(student__user__username__icontains=inputsname)
    if inputsroll != '':
        showall = showall.Q(student__roll_number__icontains=inputsroll)
    if inputhnum != '':
        showall = showall.Q(hostel__name__icontains=inputhnum)
    return render(request, 'showreview.html', {"hosteldata": showall})


def insertreview(request):
    # on  POST checking if all inputs given
    if request.method == 'POST':
        if request.POST.get('snamei') and \
                request.POST.get('srolli') and \
                request.POST.get('hnumi') and \
                request.POST.get('review'):
            showall = HostelReviews.objects.all()
            inputsname = request.POST.get('snamei')
            inputsroll = request.POST.get('srolli')
            inputhnum = request.POST.get('hnumi')
            inputreview = request.POST.get('review')
            # print(inputsname)
            # filtering out data on the basis of given inputs (when inputs are not empty)
            if inputsname != '':
                showall = showall.filter(studentname__contains=inputsname)
            if inputsroll != '':
                showall = showall.filter(rollnumber__contains=inputsroll)
            if inputhnum != '':
                showall = showall.filter(hostelnum__contains=inputhnum)
            # new data object with given inputs created.. to be inserted
            saverecord = HostelReviews()
            saverecord.studentname = request.POST.get('snamei')
            saverecord.rollnumber = request.POST.get('srolli')
            saverecord.hostelnum = request.POST.get('hnumi')
            saverecord.review = request.POST.get('review')
            # if same rollnumber already given review, then update his previous review else insert new entry
            if HostelReviews.objects.filter(rollnumber=inputsroll).exists():
                updaterecord = HostelReviews.objects.get(rollnumber=inputsroll)
                updaterecord.review = inputreview
                updaterecord.save()
                messages.success(request, "Updated Previous review of student " + request.POST.get(
                    'snamei') + " Roll No." + request.POST.get('srolli'))
            else:
                saverecord.save()
                messages.success(request, "New Record Inserted Successfully ")
            return render(request, 'showreview.html', {"hosteldata": showall})
        else:
            messages.success(request, "Please Enter Review details in all fields ")
    return render(request, 'showreview.html')


# =========================================================================================================================================
# Reviews end

# STATISTICS RENDERING
# ========================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt


def plot_floor_branches():
    datafile = "data.csv"
    data_db = HostelDataClass.objects.all()
    M = []

    for row in data_db:
        tmplist = []
        tmplist.append(row.rollnumber)
        tmplist.append(row.studentname)
        tmplist.append(row.department)
        tmplist.append(row.hoastelalloted)
        tmplist.append(row.roomno)
        tmplist.append(row.floorno)
        M.append(tmplist)

    NULL_M = [row for row in M if row[0] == None]
    data_M = [row for row in M if row[0] != None]

    floors = {}
    dept = {}

    for row in data_M:
        if row[-1] not in floors:
            floors[row[-1]] = 1
        else:
            floors[row[-1]] += 1

    for row in data_M:
        if row[-1] not in dept:
            dept[row[2]] = 1
        else:
            dept[row[2]] += 1

    floors = sorted(list(floors.keys()))
    dept = sorted(list(dept.keys()))
    data = {}
    for key in dept:
        data[key] = {}
        for key_1 in floors:
            data[key][key_1] = 0

    for row in data_M:
        data[row[2]][row[-1]] += 1

    data_1 = []
    for key in data:
        temp = [key]
        temp = temp + list(data[key].values())
        data_1.append(temp)

    df = pd.DataFrame(data_1, columns=['branch'] + floors)
    print(df)
    ax1 = df.plot(x='branch', y=floors, kind='bar', stacked=True, title='#students per branch per floor', figsize=(20, 10))

    # ax1 = df.plot(x='branch' , y=['1','2','3','4','5','6','7'] , kind='bar', stacked=True,
    # title='#students per branch per floor' , figsize=(20, 10), fontsize=10)
    ax1.set_xlabel('Streams', fontdict={'fontsize': 24})
    ax1.set_ylabel('number of students', fontdict={'fontsize': 24})
    plt.savefig("hostelManagementSystem/static/statistics/output2.png", bbox_inches='tight')


def plot_students_per_floor():
    data_db = HostelDataClass.objects.all()
    M = []
    for row in data_db:
        tmplist = []
        tmplist.append(row.rollnumber)
        tmplist.append(row.studentname)
        tmplist.append(row.department)
        tmplist.append(row.hoastelalloted)
        tmplist.append(row.roomno)
        tmplist.append(row.floorno)
        M.append(tmplist)

    floors = {}
    NULL_M = [row for row in M if row[0] == None]
    data_M = [row for row in M if row[0] != None]
    for row in data_M:
        print(row)
    for row in data_M:
        if row[-1] not in floors:
            floors[row[-1]] = 1
        else:
            floors[row[-1]] += 1
    X = floors.keys()
    Y = floors.values()
    fig = plt.figure(figsize=(20, 10))
    plt.bar(X, Y)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Floor number", fontsize=20)
    plt.ylabel("Number of students", fontsize=20)
    plt.title("Students per floor", fontsize=20)
    plt.savefig("hostelManagementSystem/static/statistics/output1.png", bbox_inches='tight')


def hostel_Branch_dist():
    depart = {}

    data_db = HostelDataClass.objects.all()
    M = []
    for row in data_db:
        tmplist = []
        tmplist.append(row.rollnumber)
        tmplist.append(row.studentname)
        tmplist.append(row.department)
        tmplist.append(row.hoastelalloted)
        tmplist.append(row.roomno)
        tmplist.append(row.floorno)
        M.append(tmplist)

    NULL_M = [row for row in M if row[0] == None]
    data_M = [row for row in M if row[0] != None]

    for row in data_M:
        if row[2] not in depart:
            depart[row[2]] = 1
        else:
            depart[row[2]] += 1
    print(depart)
    depart_keys = [i.split()[0] for i in list(depart.keys())]
    labels = depart_keys
    values = list(depart.values())
    fig = plt.figure(figsize=(12, 8))
    plt.pie(values, labels=values, counterclock=False, shadow=True)
    plt.title('Branch distribution')
    plt.legend(labels, loc='center')
    # plt.show()
    plt.savefig("hostelManagementSystem/static/statistics/output3.png", bbox_inches='tight')


def showstat(request):
    # Creating output1.png plot 1
    plot_students_per_floor()
    # Creating output2.png plot 2
    plot_floor_branches()
    # Creating output3.png plot 3
    hostel_Branch_dist()

    data = HostelDataClass.objects.all()
    M = []
    for row in data:
        tmplist = []
        tmplist.append(row.rollnumber)
        tmplist.append(row.studentname)
        tmplist.append(row.department)
        tmplist.append(row.hoastelalloted)
        tmplist.append(row.roomno)
        tmplist.append(row.floorno)
        M.append(tmplist)
    # for row in M:
        # print(row)

    return render(request, 'showstat.html')
# ========================================================================================================================
# STATISTICS RENDERING FINISHED
