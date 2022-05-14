import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import csv

st.title("Dexcom Students System")
######### Global variables  ##########
names = ['Admin','Teacher']
usernames = ['admin','teacher']
passwords = ['123','456']

admin_csv = "admin_data.csv"
student_csv = "student_data.csv"
##################################
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')


if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('## Welcome *%s*' % (name))
    st.write("### What is Dataset you want?")
    select_item = st.radio("Please select Dataset",
                  ("Add Admin", "Add Teacher", "Add Student","Add Subject"))
#######################   add admin file 1,2  ###############################################
    if select_item == "Add Admin":      ### add admin
        file1 = open(admin_csv)
        df_admins = pd.DataFrame(file1)  
        file1.close()
        
        admin_id = st.sidebar.text_input("Admin ID")
        admin_name = st.sidebar.text_input("Admin Name")
        admin_phone = st.sidebar.text_input("Admin Phone Number")
        
        
        @st.cache(allow_output_mutation=True)
        def get_data_admin():
            return []
            
        
        df_admins = pd.DataFrame(get_data_admin())
        
        if st.sidebar.button("Add Admin"):
            get_data_admin().append({"Admin_ID": admin_id, 
                           "Admin_Name": admin_name, 
                           "Admin_Phone": admin_phone})
        st.write("## Show Admin Dataset")
        st.write(df_admins)
        st.write(df_admins.shape)
        
       #####convert df to csv and save it    ###
        def convert_df(df_admins):
            return df_admins.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_admins)
        #st.write(csv1)
        
        file2 = open(admin_csv)
        df_admins.to_csv (r'admin_data.csv', index = False, header=True)
        file2.close()
        
  ###################################### add teacher file 3,4 ###############################################
    elif select_item == "Add Teacher":  ### add teacher
        pass
  ################################## add student file 5,6#####################################################
    elif select_item == "Add Student":    ### add student
        file5 = open("student_data.csv")
        df_students = pd.DataFrame(file5)  
        file5.close()
        
        student_id = st.sidebar.text_input("Student ID")
        student_name = st.sidebar.text_input("Student Name")
        student_phone = st.sidebar.text_input("Student Phone Number")
        student_email = st.sidebar.text_input("Student Email")
        student_class_name = st.sidebar.text_input("Student Class Name")
        student_subject = st.sidebar.text_input("Student Subject")
        
        @st.cache(allow_output_mutation=True)
        def get_data_student():
            return []
            
        
        df_students = pd.DataFrame(get_data_student())
        
        if st.sidebar.button("Add Student"):
            get_data_student().append({"Student_ID": student_id, 
                           "Student_Name": student_name, 
                           "Student_Phone": student_phone,
                           "Student_Email": student_email,
                           "Student_Class_Name": student_class_name,
                           "Student_Subject": student_subject})
        st.write("## Show Student Dataset")
        st.write(df_students)
        st.write(df_students.shape)    
        
       #####convert df to csv and save it    ###
        def convert_df(df_students):
            return df_students.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_students)
        #st.write(csv1)
        
        file6 = open('student_data.csv')
        df_students.to_csv (r'student_data.csv', index = False, header=True)
        file6.close()
       
   ############################# add subjectfile 7,8#######################################################
    elif select_item == "Add Subject":      ### add subject
        pass

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
