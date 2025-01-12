import colorsys

ID = [21, 10, 10, 78]
# ID = [21, 30, 14, 14]
# ID = [23, 34, 10, 33]
converted_ID = list(map(lambda x: round(x / 255, 3), ID))
# ID = converted_ID

points = [(-6, 40),
          (-24, 40),
          (-35, 40),
          (-43, 40),
          (-35, 24),
          (3, 24),
          (-4, 7),
          (-14, 7)
          ]

vertex_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

point_vertex_map = [
    ("G", "D"),  # (fROM, TO)
    ("H", "D"),
    ("H", "E"),
    ("E", "F"),
    ("F", "E"),
    ("B", "C"),
    ("A", "B"),
    ("A", "F")
]

# index 0 =A .... H
vertices_points = [
    (0, 0),
    (-10, 18),
    (22, 35),
    (-14, 55),
    (-45, 50),
    (-33, 17),
    (-3, 35),
    (-27, 33)

]

vertices_color = [(ID[0], ID[1], ID[2]),
                  (ID[0], ID[1], ID[3]),
                  (ID[0], ID[2], ID[1]),
                  (ID[0], ID[2], ID[3]),
                  (ID[0], ID[3], ID[1]),
                  (ID[0], ID[3], ID[2]),
                  (ID[1], ID[0], ID[2]),
                  (ID[3], ID[1], ID[2]),
                  ]

# empty list for points color (tuple) in rgb
rgb_points_color = []


def exec(loop_index, point, v_from, v_to, ):

    print(f"P_{i} = {point}")
    vertex_from = vertices_points[vertex_map[v_from]]
    vertex_to = vertices_points[vertex_map[v_to]]
    print(f"vertex {v_from}, {vertex_from} ---> to vertex {v_to}, {vertex_to}")

    v_from_i = vertex_map[v_from]  # converted into index
    v_to_i = vertex_map[v_to]  # converted into index

    # print(vertex_from, vertex_to)
    dx = vertex_to[0] - vertex_from[0]
    dy = vertex_to[1] - vertex_from[1]
    print(f"dx = {vertex_to[0]} - ({vertex_from[0]}) = {dx},\ndy = {vertex_to[1]} - ({vertex_from[1]}) = {dy}")
    D_ft = 0
    D_fp = 0
    if (dx > dy):

        D_ft = dx
        D_fp = point[0] - vertex_from[0]

        print("Here, dy > dx, ")

    else:
        D_ft = dy
        D_fp = point[1] - vertex_from[1]
        print("Here, dx < dy, ")

    print(f"Hence, D_{v_from}{v_to} = {D_ft},")
    print(f"D_{v_from}p{loop_index} = {D_fp}")

    print(f"Color P_{i} = Color_{v_from} + (Color_{v_to} - Color_{v_from}) * D_{v_from}p{loop_index}/D_{v_from}{v_to}")

    diff_color = tuple(a - b for a, b in zip(vertices_color[v_to_i], vertices_color[v_from_i]))
    print(f"Color P_{i} = {vertices_color[v_from_i]} + {diff_color} * {D_fp}/{D_ft}")
    # print(f"Color F - color T = {diff_color}")
    
    color_of_point = tuple(
        vertices_color[v_from_i][i] +
        round((vertices_color[v_to_i][i] -
              vertices_color[v_from_i][i]) * (D_fp / D_ft))
        for i in range(len(vertices_color[v_from_i]))
    )

    return (color_of_point)


# exec(points[0], "G", "D")


def rgb_to_hsv(rgb, isNormalized=False):
    # rgb as tuple
    r, g, b = rgb

    print(f"RGB : ({r:.2f}, {g:.2f}, {b:.2f})")
    # if not normalized--:
    if (not isNormalized):
        # Normalize RGB values to [0, 1]
        r, g, b = r / 255, g / 255, b / 255
    r = round(r, 3)
    g = round(g, 3)
    b = round(b, 3)
    print(f"Normalized Color: ({r:.2f}, {g:.2f}, {b:.2f})")

    # Calculate the maximum and minimum values
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    print(f"cmax = {cmax}, cmin = {cmin}, delta = {delta}")

    # # Calculate Hue
    if delta == 0:
        h = 0  # Undefined hue
    elif cmax == r:
        h = ( ((g - b) / delta) + 0)
    elif cmax == g:
        h = ( ((b - r) / delta) + 2) 
    elif cmax == b:
        h = ( ((r - g) / delta) + 4) 
    h = (60*h) % 360


    # Calculate Saturation
    if cmax == 0:
        s = 0
    else:
        s = delta / cmax

    # Calculate Value
    v = cmax

    h_builtin, s_builtin, v_builtin = colorsys.rgb_to_hsv(r,g,b)

    # print("Custom Function HSV: ", (h, s, v))
    print(f"Built-in Function HSV: ({h_builtin*360:.2f} deg, {s_builtin:.2f}, {v_builtin:.2f})")

    return (h, s, v)


# print(f"HSV: ({h:.2f}, {s:.2f}, {v:.2f})")


for i in range(8):
    v_from = point_vertex_map[i][0]
    v_to = point_vertex_map[i][1]
    print(f"For point P{i}: From vertex {v_from}, to vertex {v_to}")

    color = exec(i, points[i], v_from, v_to)
    print(f"Color P_{i} = {color}")
    # store this somewhere for later use:
    rgb_points_color.append(color)

    # normalized_color = tuple(value / 255 for value in color)
    # print(f"Normalized Color (0-1), {normalized_color}")
    print("---------****---------")

for i in range(8): 
        print(f"-------------- P{i}(HSV) ------------ ")
        h, s, v = rgb_to_hsv(rgb_points_color[i], isNormalized=False)
        print(f"HSV: ({h:.2f} deg, {s:.2f}, {v:.2f})")


print(rgb_points_color)