def rotate(self, x):
    y = x.parent
     
    if x == y.left:
        self.relink(y,x.right,True)
        self.relink(x,y,False)
    else:
        self.relink(y,x.left,False)
        self.relink(x,y,True)