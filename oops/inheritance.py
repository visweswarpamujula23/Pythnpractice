#...........single inheritance................
 '''
class Base_class:
class derived_class(Base_class):  #Child class
    c=20
    d=200
    def show(self):
        print("Derived class")
bobject=Base_class()
print(bobject.a,bobject.b)
bobject.display()

dobject = derived_class()
print(dobject.c,dobject.d)
dobject.display()
'''


#..........muti level inheritance...........

class Grand_parent:
    def gpdisplay(self):
        print("Grand parent")
class parent(Grand_parent):
    def parentdisplay(self):
        print("parent display")
class child(parent):
    def childdisplay(self):
        print("child display")

c=child()
c.childdisplay()
c.parentdisplay()
c.gpdisplay()





