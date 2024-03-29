class Rectangle:
    area=0
    perimeter=0
    diagonal=0
    st=""
    picture=""
    inside=0
    
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,width):
        self.width=width
  
    def set_height(self,height):
        self.height=height

    def get_area(self):
        self.area=self.width*self.height
        return self.area

    def get_perimeter(self):
        self.perimeter=(2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal=((self.width ** 2 + self.height ** 2) ** .5)
        return self.diagonal

    def get_picture(self):
        if self.width>50 or self.height>50:
            self.picture="Too big for picture."
        else:
            for i in range (self.height):
                for i in range (self.width):
                    self.picture+="*"
                self.picture+="\n"
        return self.picture
    
    def get_amount_inside(self,shape):
        self.inside=int(self.width/shape.width)*int(self.height/shape.height)
        return self.inside
        
    def __str__(self):
        self.st="Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
        return self.st

class Square(Rectangle):

    def __init__(self,side):
        self.width=side
        self.height=side
    
    def set_side(self,side):
        self.width=side
        self.height=side
    
    def __str__(self):
        self.st="Square(side="+str(self.width)+")"
        return self.st


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))