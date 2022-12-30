from django.http import HttpResponse
from django.shortcuts import render
import json
import functools
import random
from shamirapp.util import *

PRIME = 2 ** 31 - 1
RINT_FUNC = functools.partial(random.SystemRandom().randint, 0)


# shamir密钥分享页面
def index(request):
    return render(request, "../templates/index.html")


# 生成传统门限密钥API
def generate(request):
    def value_at(poly, x, p):
        value = 0
        for i in range(len(poly)):
            value += poly[i] * x ** i
        return value % p

    def make_random_shares(t, n, p=PRIME):
        if t > n:
            raise ValueError("门限不能大于密钥总数!")
        poly = [RINT_FUNC(p - 1) for i in range(t)]
        points = [(i, value_at(poly, i, p)) for i in range(1, n + 1)]
        return poly[0], points

    if request.method == 'POST':
        t = request.POST.get('t')
        n = request.POST.get('n')
        if len(t) == 0 or len(n) == 0:
            resp = {
                'code': 422,
                'msg': "t与n数值未定义"
            }
        elif int(t) <= 0 or int(n) <= 0:
            resp = {
                'code': 422,
                'msg': "t与n不能小于0!"
            }
        elif t > n:
            resp = {
                'code': 422,
                'msg': "门限不能大于密钥总数!"
            }
        else:
            secret, points = make_random_shares(int(t), int(n), PRIME)
            resp = {
                'code': 200,
                'secret': secret,
                'points': points
            }
        return HttpResponse(json.dumps(resp))


def decrypt(request):
    def egcd(a, b):
        if b == 0:
            return a, 1, 0
        r, x, y = egcd(b, a % b)
        return r, y, x - a // b * y

    def lagrange_interpolate(selected_points, p):
        s = 0
        for i in range(len(selected_points)):
            up = 1
            down = 1
            for j in range(len(selected_points)):
                if i != j:
                    up *= -selected_points[j][0]
                    down *= selected_points[i][0] - selected_points[j][0]
            item = (up * egcd(down, p)[1]) % p
            s += item * selected_points[i][1]
        return s % p

    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        points = data.get('points')
        for point in points:
            point[1] = int(point[1])
        secret = lagrange_interpolate(points, PRIME)
        resp = {
            'code': 200,
            "decrypted_secret": secret
        }
        return HttpResponse(json.dumps(resp))


def vcs(request):
    img = []
    for i in range(0, N):
        img.append(Image.new("RGB", (width, height)))
    for i in range(0, width // M):
        #  全为白色
        if len(target[i]) == 0:
            for j in range(0, height // M):
                for k in range(0, N):
                    put_white(img[k], i * M, j * M, random.randint(0, N - 1))
            continue

        s = 0
        for j in range(0, height // M):
            if s < len(target[i]) and j == target[i][s]:  # 是目标块
                r = random.randint(0, N - 1)
                for k in range(0, N):
                    put_white(img[k], i * M, j * M, (k + r) % N)
                s = s + 1
            else:  # 不是目标块
                for k in range(0, N):
                    put_white(img[k], i * M, j * M, random.randint(0, N - 1))

    for i in range(0, N):
        img[i].save("static/images/pic" + str(i + 1) + ".jpg")

    combine("static/images/pic1.jpg", "static/images/pic2.jpg", "static/images/secret_x2.jpg")
    for i in range(2, N):
        combine("static/images/pic" + str(i + 1) + ".jpg", "static/images/secret_x" + str(i) + ".jpg", "static/images/secret_x" + str(i + 1) + ".jpg")
    resp = {
        'code': 200,
    }
    return HttpResponse(json.dumps(resp))