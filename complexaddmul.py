class Complex ():
    def initcomplex(self):
        self.realpart = int(input("Enter the Real Part: "))
        self.imgpart = int(input("Enter the Imaginary Part: "))            
    def display(self):
        print(self.realpart,"+",self.imgpart,"i", sep="")
    def sum(self, c1, c2):
        self.realpart = c1.realpart + c2.realpart
        self.imgpart = c1.imgpart + c2.imgpart
    def mul(self, c1, c2):
        self.realpart = c1.realpart * c2.realpart
        self.imgpart = c1.imgpart * c2.imgpart
c1 = Complex()
c2 = Complex()
c3 = Complex()
print("Enter first complex number", end="")
c1.initcomplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initcomplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()
print("Multiplication of two complex numbers is ", end="")
c3.mul(c1,c2)
c3.display()