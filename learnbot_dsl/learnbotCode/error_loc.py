import learnbot_dsl.learnbotCode.Parser as parser
from pyparsing import *
import re

error = ""
def locate(code):
	global error
	L = code.split("\n")
	#print ("code: ",code)
	#print (type(L))
	numbered_bt = {}
	for i in range(len(L)):
		if (i!=''):
			numbered_bt[i] = L[i]
		else:
			pass
	# LB_protocol = parser.IF
	# #print (numbered_bt)
	# try:
	# 	print("parseString: ",LB_protocol.parseString('if :\n\tn+=1\nend'))
	# except ParseException as pe:
	# 	print ('ERROR!')
	# 	error+=str(pe.line)+"\n"
	# 	error+=str(' ' * (pe.col - 1) + '^')+"\n"
	# 	error+="Expected USAGE of if block: if <condition>: \n<TABHERE> <content> \n"
	# 	error+=str(pe).partition("found")[1]+str(pe).partition("found")[2] 
	# print (error)

	LB_protocol = parser.BLOQUEFOR
	#print (numbered_bt)
	try:
		print("parseString: ",LB_protocol.parseString('for n:\n\tn+=1\nend'))
	except ParseException as pe:
		print ('ERROR!')
		error+=str(pe.line)+"\n"
		error+=str(' ' * (pe.col - 1) + '^')+"\n"
		#error+="Expected USAGE of if block: if <condition>: \n<TABHERE> <content> \n"
		error+=str(pe).partition("found")[1]+str(pe).partition("found")[2] 
	print (error)
	# tree = parser.__parserFromString(code)
	# print (tree)
	# if (bt==False):
	# 	error += "There is error"
	#print (error)
	return 
def print_error():
	return error

