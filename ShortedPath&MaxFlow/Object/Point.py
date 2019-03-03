class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, Id, X, Y):
        """ Create a new point at the origin """
        self.id = Id;
        self.x = X
        self.y = Y
    def __str__(self):
      return (self.id, self.x, self.y)