#calculate highest marks and student for each subject
    #open file
    #gorup data by subject
    #calculate the highest value

#get the student with highest total marks and the marks he/she taken
    #open file
    #gorup data by student
    #calculate the total marks for each student
    #find highest marks

def get_max_for_subject(subject:str,subjectData:dict)->None:

    maxMarks=0
    studentName=''

    for student,marks in subjectData.items():
        if marks>maxMarks:
            maxMarks=marks
            studentName=student
    
    print("subject:",subject,", max marks:",maxMarks,", Student:",studentName)

def get_student_with_highest_marks(studentData:dict):
    
    maxMarks=0
    studentName=''

    for student,totalMarks in studentData.items():

        if totalMarks>maxMarks:
            maxMarks=totalMarks
            studentName=student

    print("Student with highest overall marks:",studentName," ,marks:",maxMarks)
    

def main():

    file = open('marks.txt','r')

    allEntries=file.readlines()
    file.close()

    if not allEntries:
        print("error has been occurred")
        exit()

    marksEntries = allEntries[1:] #remove header
    subjectMarks = {}   #key->subject value->{student,marks}
    studentMarks={}     #key->studentName value->totalMarks

    
    for entry in marksEntries:
        record = entry.split(',')    #seperate by comma and store to a list
        studentName=record[0].strip()
        subject=record[1].strip()
        marks=int(record[2].strip())

        #gorup data by subject
        if subject not in subjectMarks: #create new key for each subject that does not in the dictionary
            subjectMarks[subject]={}
        
        subjectMarks[subject][studentName]=marks

        #gorup data by student
        if studentName not in studentMarks:
            studentMarks[studentName]=0
        
        studentMarks[studentName]+=marks

    for subject,marks in subjectMarks.items():
        get_max_for_subject(subject,marks)
    
    #get the student with highest total marks and the marks he/she taken
    get_student_with_highest_marks(studentMarks)

if __name__ == '__main__':
    main()
    