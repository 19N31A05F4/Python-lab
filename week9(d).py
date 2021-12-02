class marks:
    sub1=int(input("Enter the marks of sub1:"))
    sub2=int(input("Enter the marks of sub2:"))
    sub3=int(input("Enter the marks of sub3:"))
    def result(self):
        if self.sub1>35:
            print("PASS")
        else:
            print("FAIL")
        if self.sub2>35:
            print("PASS")
        else:
            print("FAIL")
        if self.sub3>35:
            print("PASS")
        else:
            print("FAIL")
m=marks()
m.result()        
