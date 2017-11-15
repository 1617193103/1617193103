#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
   '学生的基类'
   stuCount = 0
 
   def __init__(self,stu_no,name,stu_class,gender):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.gender = gender
      Student.stuCount += 1

   def study(self):
      print "Student can study"
 
   def getStuCount(self):
      print Student.stuCount
 
      
class MiddleStudent(Student):
   MiddlestuCount = 0
                     
   def __init__(self,stu_no,name,stu_class,gender):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.gender = gender
      Student.stuCount += 1
      MiddleStudent.MiddlestuCount += 1
   def Swim(self):
      print "Middle Student can swim"
 
   def Sing(self):
      print "Middle Student can sing"
 
 
class HighStudent(Student):
   HighstuCount = 0
   
   def __init__(self,stu_no,name,stu_class,gender):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.gender = gender
      Student.stuCount += 1
      HighStudent.HighstuCount += 1
      
   def English(self):
      print "High Student can english"
 
   def Chinese(self):
      print "High Student can chinese"
