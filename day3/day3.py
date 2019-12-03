def wire_processing(wire):
    matrix = [(0,0)]
    for i in wire:
        if 'U' in i:
            state = matrix[-1]
            move = int(i.split('U')[1])
            new_state = (state[0],state[1]+move)
            matrix.append(new_state)
        elif 'D' in i:
            state = matrix[-1]
            move = int(i.split('D')[1])
            new_state = (state[0],state[1]-move)
            matrix.append(new_state)
        elif 'R' in i:
            state = matrix[-1]
            move = int(i.split('R')[1])
            new_state = (state[0]+move,state[1])
            matrix.append(new_state)
        elif 'L'in i:
            state = matrix[-1]
            move = int(i.split('L')[1])
            new_state = (state[0]-move,state[1])
            matrix.append(new_state)

    return matrix


def manhattan_distance(x,y):
    res = abs(x)+abs(y)
    return res


def find_intersections(mat1, mat2):
    intersection_list = []
    for i in range(len(mat1)-1):
        refX1 = mat1[i][0]
        refX2 = mat1[i+1][0]
        refY1 = mat1[i][1]
        refY2 = mat1[i+1][1]
        for j in range(len(mat2)-1):
            x1 = mat2[j][0]
            x2 = mat2[j+1][0]
            y1 = mat2[j][1]
            y2 = mat2[j+1][1]
            if (x1 > refX1 and x2 < refX2) or (x1 < refX1 and x2 > refX2):
                if (y1 < refY1 and y2 > refY2) or (y1 > refY1 and y2 < refY2):
                    if x1 == x2:
                        intX = x1
                        intY = refY1
                    elif y1 == y2:
                        intX = refX2
                        intY = y1

                    intersection_list.append((intX,intY))

    return intersection_list


def get_steps(matrix, intersection):
    steps = 0
    xi = intersection[0]
    yi = intersection[1]

    for i in range(len(matrix)-1):

        if (xi == matrix[i][0] == matrix[i+1][0]) and ((yi < matrix[i][1] and yi > matrix[i+1][1]) or (yi > matrix[i][1] and yi < matrix[i+1][1])):
            steps = steps + abs(matrix[i][0]-intersection[0]) + abs(matrix[i][1]-intersection[1])
            break

        elif (intersection[1] == matrix[i][1] == matrix[i+1][1]) and ((xi < matrix[i][0] and xi > matrix[i+1][0]) or (xi > matrix[i][0] and xi < matrix[i+1][0])):
            steps = steps + abs(matrix[i][0] - intersection[0]) + abs(matrix[i][1] - intersection[1])
            break

        else:
            steps = steps + abs(matrix[i][0]-matrix[i+1][0]) + abs(matrix[i][1]-matrix[i+1][1])


    return steps


if __name__ == "__main__":
    f = open("../inputs/day3.txt", "r")

    wire1 = f.readline().split(',')
    wire2 = f.readline().split(',')

    # Processing both wires to obtain a matrix with the points of each wire
    matrix1 = wire_processing(wire1)
    matrix2 = wire_processing(wire2)

    # Finding all existing intersections
    intersections = find_intersections(matrix1, matrix2)

    # Retrieve intersection with the shortest Manhattan dist. from the starting point (PART 1)
    mindist = 9999999999999999999999999999999999
    for intersection in intersections:
        dist = manhattan_distance(intersection[0], intersection[1])
        mindist = min(mindist, dist)
    print('The Manhattan distance to the closest intersection is: ', mindist)

    # Retrieve the intersection reachable with the shortest num. of steps (PART 2)
    minsteps = 9999999999999999999999999999999999
    for intersection in intersections:
        steps1 = get_steps(matrix1, intersection)
        steps2 = get_steps(matrix2, intersection)
        steps = steps1+steps2
        minsteps = min(minsteps, steps)

    print('The num. of steps to the closest intersection is: ', minsteps)
