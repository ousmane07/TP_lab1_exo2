import math


def calc_distance(point1, point2):
    #Exercice: calcul de distance entre 2 points


    # Soient x1, x2, x3 = point1 et x2, y2, z2 = point2

    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calculons la distance entre les 2 points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    #On retourne la distance
    return distance


# on s'est basé sur cet exemple
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = list(map(calc_distance, points1, points2))

#On affiche la distance
print(distances)
