from PIL import Image

N = 9
M = 6

width = 43 * M
height = 21 * M

mode = (
    (
        (1, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 1),
    ),
    (
        (0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
    ),
    (
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
    ),
    (
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
    ),
    (
        (0, 0, 0, 0, 1, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0),
    ),
    (
        (0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        (0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0),
        (0, 0, 1, 1, 0, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0),
    ),
)

#  定义的图像形状
target = {
    0: [],
    1: [],
    2: [12],
    3: [12,13],
    4: [5, 6, 9,12,14],
    5: [4, 7, 10,12,14,15],
    6: [4, 7, 10,12,14,16],
    7: [4, 7, 10,12,14,16,],
    8: [5, 8, 9,12,14,16],
    9: [12,14,16],
    10: [4, 5, 6, 7, 8, 9, 10,12,14,16],
    11: [7,12,14,16],
    12: [7,12,14,16],
    13: [7,12,14,16],
    14: [4, 5, 6, 7, 8, 9, 10,12,14,16],
    15: [12,14,18],
    16: [6, 7, 8, 9, 10,12,14,17,18],
    17: [5, 7,12,14,16,18],
    18: [4, 7,12,14,15,18],
    19: [5, 7,12,14,17],
    20: [6, 7, 8, 9, 10,12,15,16],
    21: [13,16],
    22: [4, 5, 6, 7, 8, 9, 10,12,15,16],
    23: [5,12,14,17],
    24: [6, 7,12,14,15,18],
    25: [5,12,14,16,18],
    26: [4, 5, 6, 7, 8, 9, 10,12,14,17,18],
    27: [12,14,18],
    28: [12,14,16],
    29: [4, 10,12,14,16],
    30: [4, 5, 6, 7, 8, 9, 10,12,14,16],
    31: [4, 10,12,14,16],
    32: [12,14,16],
    33: [12,14,16],
    34: [4, 5, 6, 7, 8, 9, 10,12,14,16],
    35: [4, 7,12,14,16],
    36: [4, 7,12,14,16],
    37: [4, 7,12,14,15],
    38: [5, 6, 8, 9, 10,12,14],
    39: [12,13],
    40: [12],
    41: [],
    42: [],
}


def put_white(img, x, y, mode_num):
    for i in range(0, M):
        for j in range(0, M):
            if mode[mode_num][i][j] == 0:
                img.putpixel((x + i, y + j), (255, 255, 255))
            elif mode[mode_num][i][j] == 1:
                img.putpixel((x + i, y + j), (0, 0, 0))


def put_white_re(img, x, y, mode_num):
    for i in range(0, N):
        for j in range(0, N):
            if mode[mode_num][i][j] == 1:
                img.putpixel((x + i, y + j), (255, 255, 255))
            elif mode[mode_num][i][j] == 0:
                img.putpixel((x + i, y + j), (0, 0, 0))


def combine(pic1, pic2, name):
    img1 = Image.open(pic1, "r")
    img2 = Image.open(pic2, "r")
    img3 = Image.new("RGB", (img1.size[0], img1.size[1]))
    pix1 = img1.load()
    pix2 = img2.load()
    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):
            if pix1[i, j][0] > 128 and pix2[i, j][0] >128:
                img3.putpixel((i, j), (255, 255, 255))
            else:
                img3.putpixel((i, j), (0, 0, 0))
    img3.save(name)
