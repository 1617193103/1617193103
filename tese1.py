Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1 = {'si':1617193103}
>>> dict1
{'si': 1617193103}
>>> dict1['si']
1617193103
>>> dict1['si']=678
>>> dict1['si']
678
>>> del dict1['si']
>>> dict1
{}
>>> users = {
    'A':{
    'first':'si',
    'last':'bo',
    'location':'hs',
    },
    'B':{
    'first':'du',
    'last':'shuang',
    'location':'hs',    
    },
}
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'si', 'location': 'hs', 'first': 'bo'}
userid£ºB
userinfo:{'last': 'du', 'location': 'hs', 'first': 'shuang'}
SyntaxError: invalid syntax
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'bo', 'location': 'hs', 'first': 'si'}
userid£ºB
userinfo:{'last': 'shuang', 'location': 'hs', 'first': 'du'}
SyntaxError: invalid syntax
>>> for username, userinfo in users.items():
	print("suerid:"+ username)
	print("suerinfo:"+ str(userinfo))

	
suerid:A
suerinfo:{'last': 'bo', 'location': 'hs', 'first': 'si'}
suerid:B
suerinfo:{'last': 'shuang', 'location': 'hs', 'first': 'du'}
>>> dict = {'Name':'Zara','Age':7}
>>> print "Vlaue:%s"% dict.keys()
Vlaue:['Age', 'Name']
>>> print"Key:%s"% dict.keys()
Key:['Age', 'Name']
>>> for key in dict.key():
	print key

	

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for key in dict.key():
AttributeError: 'dict' object has no attribute 'key'
>>> for key in dict.keys
SyntaxError: invalid syntax
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
