from survey import Anonymous as An
question ='What did u learn first to speak?'
survey = An(question)
 
survey.show_qn()
print("Enter q to quit")
while True:
	res = input("Language:")
	if res == 'q':
		break
	survey.store_res(res)
print("Thank u to everyone who participated in survey")
survey.show_result()
