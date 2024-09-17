class Cor():
    def __init__(self,R,G,B):
        self._R = R
        self._G = G
        self._B = B

    def getColor(self):
        cor = (self._R/255,self._G/255,self._B/255)
        return cor