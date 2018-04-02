
# coding: utf-8

# ### 1/5: STUDENT

# In[1]:


# STUDENT dataframe
import csv
import pandas as pd

with open('student.csv') as student_file:
    student = pd.read_csv(student_file, ',', None, header='infer');
#student_df = pd.DataFrame(student)


# In[2]:


# ==== Describing the data ===

# student.shape #(3, 2)
# len(student) # rows - 3
# student.describe()
student


# In[3]:


student['sid'].value_counts() # sid column


# In[4]:


student['name'].value_counts() # name column


# In[5]:


student['name'].nunique() # num unique values in column


# ### 2/5: TAKES

# In[6]:


with open('takes.csv') as takes_file:
    takes = pd.read_csv(takes_file, ',', None, header='infer');


# In[7]:


takes


# In[8]:


takes['sid'].nunique() # only 2


# In[9]:


takes.columns # column names


# In[10]:


takes.info() # general df info


# In[11]:


takes.dtypes # data types


# In[12]:


takes.count()


# ### 3/5: COURSE

# In[13]:


with open('course.csv') as course_file:
    course = pd.read_csv(course_file, ',', None, header='infer');


# In[14]:


course


# In[15]:


course.dtypes


# In[16]:


course.rank() # assigns rank to all values


# In[17]:


course.sort_values(by='cid') # now ranked in ascending order
# course['cid'] = course['cid'].astype(int) # type casting


# ### 4/5: PROFESSOR

# In[18]:


with open('professor.csv') as professor_file:
    professor = pd.read_csv(professor_file, ',', None, header='infer');


# In[19]:


professor


# ### 5/5: TEACHES

# In[20]:


with open('teaches.csv') as teaches_file:
    teaches = pd.read_csv(teaches_file, ',', None, header='infer');


# In[21]:


teaches


# # Import database

# In[22]:


import sqlite3
engine = sqlite3.connect('PRACTICE_DB')

# store dfs to database
student.to_sql(name='student', con=engine, if_exists = 'replace')
takes.to_sql(name='takes', con=engine, if_exists = 'replace')
course.to_sql(name='course', con=engine, if_exists = 'replace')
professor.to_sql(name='professor', con=engine, if_exists = 'replace')
teaches.to_sql(name='teaches', con=engine, if_exists = 'replace')


# In[23]:


# Now let’s connect to the database (as above), and then load back your DataFrames 
# from SQL, using the syntax:
student = pd.read_sql('select * from student', engine)
takes = pd.read_sql('select * from takes', engine)
course = pd.read_sql('select * from course', engine)
professor = pd.read_sql('select * from professor', engine)
teaches = pd.read_sql('select * from teaches', engine)


# In[24]:


student.info()
takes.info()
course.info()
professor.info()
teaches.info()


# In[25]:


import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# import sqlite3
# engine = sqlite3.connect('HW0_DB')
# dataframe = pd.read_sql('select * from name_df', engine)


# ## Queries

# In[26]:


student


# In[27]:


takes


# In[28]:


course


# In[29]:


professor


# In[30]:


teaches


# In[31]:


cur = engine.cursor()
query = "SELECT * FROM student, takes, course WHERE student.sid=takes.sid AND takes.cid=course.cid"
cur.execute(query)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
q1_df = DataFrame(get_data)
q1_df.columns = field_names


# In[32]:


q1_df


# In[33]:


cur = engine.cursor()
query = "SELECT * FROM course WHERE cid LIKE '5%'"
cur.execute(query)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
course_5xx_df = DataFrame(get_data)
course_5xx_df.columns = field_names


# In[34]:


course_5xx_df # leaves out 677 course


# In[35]:


cur = engine.cursor()
query = "WITH Bizz AS (SELECT sid AS student_id FROM student S WHERE S.name LIKE '%M_ya') SELECT T.expGrade FROM Bizz B INNER JOIN takes T ON B.student_id=T.sid WHERE T.cid='550-001';"
cur.execute(query)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
exp_grade_550_df = DataFrame(get_data)
exp_grade_550_df.columns = field_names


# In[36]:


exp_grade_550_df


# In[37]:


student


# In[38]:


takes


# ### Find the students with the best expected grades

# In[39]:


# inner query: SELECT DISTINCT expGrade FROM takes

cur = engine.cursor()
q = "SELECT DISTINCT expGrade FROM takes"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
exp_grade_550_INTERMEDIATE_df = DataFrame(get_data)
exp_grade_550_INTERMEDIATE_df.columns = field_names


# In[40]:


exp_grade_550_INTERMEDIATE_df


# In[41]:


# Find the students with the best expected grades

cur = engine.cursor()
q = "SELECT DISTINCT S.name FROM student S, takes T WHERE S.sid=T.sid AND T.expGrade >= (SELECT max(expGrade) FROM takes)"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
exp_grade_550_df = DataFrame(get_data)
exp_grade_550_df.columns = field_names

# SELECT S.name 
# FROM student S, takes T 
# WHERE S.sid=T.sid AND T.expGrade >= ANY 
#     (SELECT DISTINCT T.expGrade 
#      FROM takes T)


# In[42]:


exp_grade_550_df # DIDNT USE 'ANY' keyword -- WRONG


# ### Find the students who have taken subject that have (at any point) been taught by Prof. Marcus

# In[43]:


professor


# In[44]:


teaches


# In[45]:


# INNER QUERY: SELECT ta.cid FROM professor p, teaches ta WHERE p.fid=ta.fid AND p.name='Marcus'

cur = engine.cursor()
q = "SELECT ta.cid FROM professor p, teaches ta WHERE p.fid=ta.fid AND p.name='Marcus'"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
marcus_INTERMEDIATE_df = DataFrame(get_data)
marcus_INTERMEDIATE_df.columns = field_names


# In[46]:


marcus_INTERMEDIATE_df


# In[47]:


student


# In[48]:


takes


# In[49]:


# Find the students who have taken subject that have (at any point) been taught by Prof. Marcus
cur = engine.cursor()
q = "SELECT DISTINCT S.name, S.sid FROM student S, takes T WHERE T.sid=S.sid AND T.cid IN (SELECT ta.cid FROM professor p, teaches ta WHERE p.fid=ta.fid AND p.name='Marcus')"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
marcus_df = DataFrame(get_data)
marcus_df.columns = field_names


# In[50]:


marcus_df


# In[51]:


# from answer key

cur = engine.cursor()
q = "SELECT DISTINCT S.name FROM student S JOIN takes T ON T.sid=S.sid JOIN course C ON T.cid=C.cid WHERE C.name IN (SELECT C2.name FROM professor p JOIN teaches ta ON p.fid=ta.fid JOIN course C2 ON ta.cid=C2.cid WHERE p.name='Marcus')"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
marcus_df2 = DataFrame(get_data)
marcus_df2.columns = field_names


# In[52]:


marcus_df2


# ### Students who have taken subjects that have NEVER been taught by P. Marcus

# In[53]:


takes


# In[54]:


course


# In[55]:


student


# In[56]:


teaches


# In[57]:


professor


# In[58]:


# SELECT s.name FROM student s, takes t, course c WHERE s.sid=t.sid AND c.cid=t.cid AND c.name NOT IN (SELECT c2.name FROM p)

cur = engine.cursor()
q = "SELECT DISTINCT s.name FROM student s, takes t, course c WHERE s.sid=t.sid AND c.cid=t.cid AND c.name NOT IN (SELECT c2.name FROM professor p JOIN teaches ta ON p.fid=ta.fid JOIN course c2 ON ta.cid=c2.cid WHERE p.name='Marcus')"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
not_marcus_df = DataFrame(get_data)
not_marcus_df.columns = field_names


# In[59]:


not_marcus_df


# ### Find all students who have taken DB but not AI

# In[60]:


course


# In[61]:


student


# In[62]:


takes


# In[63]:


# inner query: SELECT * FROM takes T2, course C2 WHERE T2.cid=C2.cid AND C2.name='AI' AND T.sid=T2.sid
cur = engine.cursor()
q = "SELECT * FROM takes T, takes T2, course C2 WHERE T2.cid=C2.cid AND C2.name='AI' AND T.sid=T2.sid"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
db_not_ai_INTERMEDIATE_df = DataFrame(get_data)
db_not_ai_INTERMEDIATE_df.columns = field_names


# In[64]:


db_not_ai_INTERMEDIATE_df


# In[65]:


# inner query: SELECT * FROM takes T2, course C2 WHERE T2.cid=C2.cid AND C2.name='AI' AND T.sid=T2.sid
cur = engine.cursor()
q = "SELECT S.name, T.sid FROM takes T, course C, student S WHERE T.cid=C.cid AND S.sid=T.sid AND C.name='DB'"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
db_not_ai_INTERMEDIATE2_df = DataFrame(get_data)
db_not_ai_INTERMEDIATE2_df.columns = field_names


# In[66]:


# all students who took databases
db_not_ai_INTERMEDIATE2_df


# In[67]:


# Find all students who have taken DB but not AI
cur = engine.cursor()
q = "SELECT S.name, T.sid FROM takes T, course C, student S WHERE T.cid=C.cid AND S.sid=T.sid AND C.name='DB' AND NOT EXISTS (SELECT * FROM takes T2, course C2 WHERE T2.cid=C2.cid AND C2.name='AI' AND T.sid=T2.sid)"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
db_not_ai_df = DataFrame(get_data)
db_not_ai_df.columns = field_names


# In[68]:


# took databases - AI
db_not_ai_df


# ### Number of students in each course offering

# In[69]:


takes


# In[70]:


# SELECT COUNT (*) FROM takes t GROUP BY t.cid, t.sem

cur = engine.cursor()
q = "SELECT cid as Course, COUNT (*) AS Count FROM takes t GROUP BY t.cid, t.sem"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
cnt_students_df = DataFrame(get_data)
cnt_students_df.columns = field_names


# In[71]:


cnt_students_df


# ### Number of different grades expected for each course offering

# In[85]:


# SELECT COUNT(DISTINCT expGrade) FROM takes t GROUP BY t.cid, t.sem

cur = engine.cursor()
q = "SELECT cid AS Course, COUNT(DISTINCT expGrade) AS Count FROM takes t GROUP BY t.cid, t.sem"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
cnt_grades_df = DataFrame(get_data)
cnt_grades_df.columns = field_names


# In[73]:


cnt_grades_df


# ### Number of distinct students taking AI courses

# In[74]:


takes


# In[75]:


course


# In[76]:


# SELECT COUNT(DISTINCT *) FROM takes t JOIN course c ON t.cid=c.cid WHERE c.name='AI'

cur = engine.cursor()
q = "SELECT COUNT(*) FROM takes t JOIN course c ON t.cid=c.cid WHERE c.name='AI'"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
ai_df = DataFrame(get_data)
ai_df.columns = field_names


# In[77]:


ai_df


# ### For each subject taught by at LEAST two professors, list the minimum expected grade

# In[78]:


takes


# In[82]:


course


# In[84]:


# cur = engine.cursor()
# q = "SELECT name, MIN(t.expGrade) FROM takes t JOIN course c on t.cid=c.cid JOIN teaches ta ON c.cid=ta.cid GROUP BY name HAVING count(DISTINCT ta.fid)>=2"
# cur.execute(q)
# field_names = [i[0] for i in cur.description]
# # print(field_names)
# get_data = [xx for xx in cur]
# cur.close()
# # engine.close()
# min_exp_grd_df = DataFrame(get_data)
# min_exp_grd_df.columns = field_names


# In[ ]:


# min_exp_grd_df # not working


# ### Aggregation with table expressions

# In[87]:


# WITH ClassSize AS (
#     SELECT c.cid AS id, c.name as subj, COUNTS(s.sid) AS size
#     FROM student s INNER JOIN takes t ON s.sid=t.sid
#         INNER JOIN course c ON t.cid=c.cid
#     GROUP BY c.cid, c.name
#     )
# SELECT subj, AVG(size)
# FROM ClassSize CS
# GROUP BY subj;

cur = engine.cursor()
q = "WITH ClassSize AS (SELECT c.cid AS id, c.name as subj, COUNT(s.sid) AS size FROM student s INNER JOIN takes t ON s.sid=t.sid INNER JOIN course c ON t.cid=c.cid GROUP BY c.cid, c.name) SELECT subj, AVG(size) FROM ClassSize CS GROUP BY subj;"
cur.execute(q)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
class_size_df = DataFrame(get_data)
class_size_df.columns = field_names


# In[88]:


class_size_df


# # Creating a table

# In[48]:


# creating table
c = engine.cursor()
create_table_sql = "CREATE TABLE employee (LastName character, DepartmentID number);"
c.execute(create_table_sql)
c.close()


# In[51]:


# inserting values in table
cursor = engine.cursor() 
insert_cmd = "INSERT INTO employee (LastName, DepartmentID) VALUES ('Rafferty', 31), ('Jones', 33), ('Steinberg', 33), ('Robinson', 34), ('Smith', 34), ('John', null);"
number_of_rows = cursor.execute(insert_cmd)
engine.commit()
cursor.close()


# In[52]:


employee = pd.read_sql('select * from employee', engine)
employee


# In[53]:


# creating table
c = engine.cursor()
create_table_sql = "CREATE TABLE department (DepartmentID number, DepartmentName character);"
c.execute(create_table_sql)
c.close()


# In[54]:


# inserting values in table
cursor = engine.cursor() 
insert_cmd = "INSERT INTO department (DepartmentID, DepartmentName) VALUES (31, 'Sales'), (33, 'Engineering'), (34, 'Clerical'), (35, 'Marketing');"
number_of_rows = cursor.execute(insert_cmd)
engine.commit()
cursor.close()


# In[55]:


department = pd.read_sql('select * from department', engine)
department


# In[57]:


# Joins

cur = engine.cursor()
query = "SELECT * FROM employee emp NATURAL JOIN department dept WHERE emp.DepartmentID=dept.DepartmentID"
cur.execute(query)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
emp_nat_join_df = DataFrame(get_data)
emp_nat_join_df.columns = field_names


# In[58]:


emp_nat_join_df # avoids repeats


# In[61]:


cur = engine.cursor()
query = "SELECT * FROM employee emp LEFT OUTER JOIN department dept ON emp.DepartmentID=dept.DepartmentID"
cur.execute(query)
field_names = [i[0] for i in cur.description]
get_data = [xx for xx in cur]
cur.close()
# engine.close()
emp_L_outer_join_df = DataFrame(get_data)
emp_L_outer_join_df.columns = field_names


# In[62]:


emp_L_outer_join_df


# In[63]:


# cur = engine.cursor()
# query = "SELECT * FROM employee emp RIGHT OUTER JOIN department dept ON emp.DepartmentID=dept.DepartmentID"
# cur.execute(query)
# field_names = [i[0] for i in cur.description]
# get_data = [xx for xx in cur]
# cur.close()
# # engine.close()
# emp_R_outer_join_df = DataFrame(get_data)
# emp_R_outer_join_df.columns = field_names

