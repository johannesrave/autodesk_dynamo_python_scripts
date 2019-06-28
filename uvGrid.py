# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
import Autodesk.DesignScript.Geometry as ds
import math

# The inputs to this node will be stored as a list in the IN variables.

IN = IN

#uvGrid = [["a1","b1","c1"],["a2","b2","c2"],["a3","b3","c3"],["a4","b4","c4"],["a5","b5","c5"]]

uvGrid = IN[0]

rot = 3

pts = []
arcs = []

#def diamondsByGrid(grid=[],u=int,v=int)

for u, col in enumerate(uvGrid):
    print("u is " + str(u))
    if (u + 1) % 2 == 0 and u < len(uvGrid) - 1:

        for v, pt in enumerate(col):
            print("v is " + str(v))
            if (v + 1) % 2 == 0 and v < len(col) - 1:
                pt = uvGrid[u][v]
                
                A = uvGrid[u][v+1]
                B = uvGrid[u+1][v]
                C = uvGrid[u][v-1]
                D = uvGrid[u-1][v]

                rotAxis = ds.Vector.Reverse(ds.Vector.XAxis())

                AB = ds.Vector.ByTwoPoints(A,B)
                rotAB = ds.Vector.Rotate(AB, rotAxis, rot)
                arcAB = ds.Arc.ByStartPointEndPointStartTangent(A, B, rotAB)
                
                CD = ds.Vector.ByTwoPoints(C,D)
                rotCD = ds.Vector.Rotate(CD, rotAxis, rot)
                arcCD = ds.Arc.ByStartPointEndPointStartTangent(C, D, rotCD)

                rotAxis = ds.Vector.XAxis()

                AD = ds.Vector.ByTwoPoints(A,D)
                rotAD = ds.Vector.Rotate(AD, rotAxis, rot)
                arcAD = ds.Arc.ByStartPointEndPointStartTangent(A, D, rotAD)
                
                CB = ds.Vector.ByTwoPoints(C,B)
                rotCB = ds.Vector.Rotate(CB, rotAxis, rot)
                arcCB = ds.Arc.ByStartPointEndPointStartTangent(C, B, rotCB)

                arcs.append([arcAB,arcAD,arcCB,arcCD])
    
    if (u) % 2 == 0 and 1 < u < len(uvGrid) - 1:

        for v, pt in enumerate(col):
            print("v is " + str(v))
            if (v) % 2 == 0 and 1 < v < len(col) - 1:
                pt = uvGrid[u][v]
                
                A = uvGrid[u][v+1]
                B = uvGrid[u+1][v]
                C = uvGrid[u][v-1]
                D = uvGrid[u-1][v]

                rotAxis = ds.Vector.Reverse(ds.Vector.XAxis())

                AB = ds.Vector.ByTwoPoints(A,B)
                rotAB = ds.Vector.Rotate(AB, rotAxis, rot)
                arcAB = ds.Arc.ByStartPointEndPointStartTangent(A, B, rotAB)
                
                CD = ds.Vector.ByTwoPoints(C,D)
                rotCD = ds.Vector.Rotate(CD, rotAxis, rot)
                arcCD = ds.Arc.ByStartPointEndPointStartTangent(C, D, rotCD)

                rotAxis = ds.Vector.XAxis()

                AD = ds.Vector.ByTwoPoints(A,D)
                rotAD = ds.Vector.Rotate(AD, rotAxis, rot)
                arcAD = ds.Arc.ByStartPointEndPointStartTangent(A, D, rotAD)
                
                CB = ds.Vector.ByTwoPoints(C,B)
                rotCB = ds.Vector.Rotate(CB, rotAxis, rot)
                arcCB = ds.Arc.ByStartPointEndPointStartTangent(C, B, rotCB)

                arcs.append([arcAB,arcAD,arcCB,arcCD])

print(pts)
                
OUT = arcs
