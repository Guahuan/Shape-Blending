from Struct import *


def SignAngle(PointA: Point, PointB: Point, PointC: Point):
    VectorAB = Vector(PointB.x - PointA.x, PointB.y - PointA.y)
    VectorBC = Vector(PointC.x - PointB.x, PointC.y - PointB.y)
    return VectorAB.angle_signed(VectorBC)


def EdgeLength(PointA: Point, PointB: Point):
    VectorAB = Vector(PointA.x - PointB.x, PointA.y - PointB.y)
    return VectorAB.norm()


def Polygon2Turtle(polygon: Polygon):
    theta = []
    L = []
    for i in range(0, len(polygon.points)):
        if i == 0:
            theta.append(SignAngle(Point(
                polygon.points[0].x - 1, polygon.points[0].y), polygon.points[0], polygon.points[1]))
            L.append(EdgeLength(polygon.points[i], polygon.points[i + 1]))
        elif i == len(polygon.points) - 1:
            theta.append(SignAngle(
                polygon.points[i - 1], polygon.points[i], polygon.points[0]))
            L.append(EdgeLength(polygon.points[i], polygon.points[0]))
        else:
            theta.append(SignAngle(
                polygon.points[i - 1], polygon.points[i], polygon.points[i + 1]))
            L.append(EdgeLength(polygon.points[i], polygon.points[i + 1]))
    return Turtle(polygon.points[0], theta, L)


def Turtle2Polygon(turtle: Turtle):
    points = []
    points.append(turtle.p_0)
    alpha = turtle.theta[0]
    for i in range(1, len(turtle.L)):
        points.append(Point(points[i - 1].x + turtle.L[i - 1] * math.cos(alpha),
                            points[i - 1].y + turtle.L[i - 1] * math.sin(alpha)))
        alpha += turtle.theta[i]
    return Polygon(points)
