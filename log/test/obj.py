class proto(object):
    def __init__(self,x):
        self.x = x
    def get_x(self):
        return self.x


class ch(proto):
    def __init__(self,x,y):
        # proto.__init__(self,x)
        super(ch, self).__init__(x)
        self.y = y
    def get_y(self):
        return self.y
proto.z = 555
ch_instance = ch(11,22)
x = ch_instance.get_x()
y = ch_instance.get_y()

print x,y,proto.__dict__