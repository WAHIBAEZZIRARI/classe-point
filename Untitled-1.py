class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self,a):
        self.x=a 

    def set_y(self, b):
        self.y=b

    def deplace(self,dx,dy):
        self.set_x(self.get_x()+dx)
        self.set_y(self.get_y()+dy)
       

    def affiche(self):
        print("x=",self.get_x())
        print("y=",self.get_y())


    def saisir(self):
        print("donner les coordonnées")
        self.x = int(input ("x = "))
        self.y = int(input ("y = "))
      

    def distance (self,p):
        x1=(self.get_x()-p.get_x())*(self.get_x()-p.get_x());
        x2=(self.get_y()-p.get_y())*(self.get_y()-p.get_y());
        d=(x1+x2)
        return d


    def milieu(self, p):
        p1 = Point();
        p1.x=(self.get_x()+p.get_x())/2
        p1.y=(self.get_y()+p.get_y())/2
        return p1

p = Point(1,1)
x = Point(5,5)
c = Point()
p.affiche()
p.deplace(5,5)
p.affiche();
print("la distance px est: ",p.distance(x));
c=p.milieu(x)
print("le milieu de [px] est: (",c.get_x(),",",c.get_y(),")")
        
    