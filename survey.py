class Anonymous:
	def __init__(self,question):
		self.question = question
		self.response=[]
	def show_qn(self):
		print(self.question)
	def store_res(self,new_res):
		self.response.append(new_res)
	def show_result(self):
		print("survey results:")
		for r in self.response:
			print(f'-{r}')
