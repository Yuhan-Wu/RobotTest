from RobotCharTest.BodyPart import Body_Part
class Body(Body_Part):
    def __init__(self,path="square1.png",position=(300,300)):
        super(Body,self).__init__(path=path,position=position)
        self.damage=1
        pass
    pass