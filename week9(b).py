class A:
	a=16
	b=23
	def mul(self):
		result=self.a*self.b
		print(result)
obj=A()
obj.mul()
print(obj.a)
print(obj.b)