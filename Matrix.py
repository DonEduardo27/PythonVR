import math
 
class Vector4(object):
 
        Array = []
 
        def __init__(self, a,b,c,d):
                self.Array = [a,b,c,d]
 
        def euclidean_distance(self,point):
                a = (self.Array[0] - point.Array[0])
                b = (self.Array[1] - point.Array[1])
                c = (self.Array[2] - point.Array[2])
                d = (self.Array[3] - point.Array[3])
                return math.sqrt((a**2) + (b**2) + (c**2) + (d**2))#not sure


        def printVec(self):
                print("|" +str(self.Array[0])+ "|")
                print("|" +str(self.Array[1])+ "|")
                print("|" +str(self.Array[2])+ "|")
                print("|" +str(self.Array[3])+ "|")
                print(" ") 

class TMatrix:
 
        Array = []
 
        def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
                self.Array = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
 
        def transpose(self):
                transArray = []
 
                transArray[0] = self.Array[0]
                transArray[1] = self.Array[4]
                transArray[2] = self.Array[8]
                transArray[3] = self.Array[12]
                transArray[4] = self.Array[1]
                transArray[5] = self.Array[5]
                transArray[6] = self.Array[9]
                transArray[7] = self.Array[13]
                transArray[8] = self.Array[2]
                transArray[9] = self.Array[6]
                transArray[10] = self.Array[10]
                transArray[11] = self.Array[14]
                transArray[12] = self.Array[3]
                transArray[13] = self.Array[7]
                transArray[14] = self.Array[11]
                transArray[15] = self.Array[15]
 
                self.Array = transArray
 
        def mult(self, other_matrix):
                returnArray = []
                for x in range(0,4):
                    for y in range(0,4):
                        returnArray.append(0)
                        for z in range(0,4):
                            returnArray[x*4+y] = (returnArray[x*4+y] + (self.Array[x*4 + z] * other_matrix.Array[z*4 +y]))
                self.Array = returnArray
 
        def mult_vec(self, vector):
                returnArray = []
                for x in range(0,4):
                    returnArray.append(0)
                    for y in range (0,4):
                        returnArray[x] = returnArray[x] + (self.Array[4*x + y] * vector.Array[x])
                return Vector4(returnArray[0],returnArray[1],returnArray[2],returnArray[3])

        def printMat(self):
                print("|"  +str(self.Array[0])+ ", " +str(self.Array[1])+ ", " +str(self.Array[2])+ ", " +str(self.Array[3])+"|")
                print("|" +str(self.Array[4])+ ", " +str(self.Array[5])+ ", " +str(self.Array[6])+ ", " +str(self.Array[7])+"|")
                print("|" +str(self.Array[8])+ ", " +str(self.Array[9])+ ", " +str(self.Array[10]) + ", "+ str(self.Array[11])+"|")
                print("|" +str(self.Array[12])+ ", " +str(self.Array[13])+ ", " +str(self.Array[14])+ ", " +str(self.Array[15])+"|")
                print(" ")


def make_trans_mat(x,y,z):
        return TMatrix (0,0,0,x,0,0,0,y,0,0,0,z,0,0,0,1)

def make_rot_mat(phi,axis):
        if(axis == "x"):
            return TMatrix (1,0,0,0,math.cos(phi),-math.sin(phi),0,0,math.sin(phi),math.cos(phi),0,0,0,0,0,1)
        if(axis == "y"):
            return TMatrix (math.cos(phi),0,math.sin(phi),0, 0,1,0,0, -math.sin(phi),0,math.cos(phi),0, 0,0,0,1)
        if(axis == "z"):
            return TMatrix (math.cos(phi),-math.sin(phi),0,0 ,math.sin(phi),math.cos(phi),0,0, 0,0,1,0,0,0,0,1)

def make_scale_mat(x,y,z):
        return TMatrix(x,0,0,0, 0,y,0,0, 0,0,z,0, 0,0,0,1)


def MatTest():
    A = TMatrix(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    print("A:")
    A.printMat()

    B = TMatrix(1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16)
    print("B:")
    B.printMat()

    A.mult(B)
    print("A*B:")
    A.printMat()

    make_trans_mat(1,2,3).printMat()
    make_rot_mat(45,'x').printMat()
    make_rot_mat(90,'y').printMat()
    make_rot_mat(120,'z').printMat()
    make_scale_mat(1,2,3).printMat()

    vA = Vector4(2,4,6,2)
    print("Vector A:")
    vA.printVec()  

    vB = Vector4(0,0,0,1)
    print("Vector B:")
    vB.printVec()
    print("Distance A B:")
    print(vB.euclidean_distance(vA))

    vE = Vector4(1,2,3,1)
    Vres = A.mult_vec(vE)
    Vres.printVec()
MatTest()

