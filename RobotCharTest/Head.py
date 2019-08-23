from RobotCharTest.BodyPart import Body_Part
class Head(Body_Part):
    def __init__(self,path="square1.png",position=(300,300)):
        super(Head,self).__init__(path=path,position=position)
        self.damage=2
        pass
