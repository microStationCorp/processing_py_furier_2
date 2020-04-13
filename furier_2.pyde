fX = []
fY = []

angle = 0
points = []

def setup():
    size(900, 800)
    background(51)
    stroke(255)

    # fY.extend(dft(val[1]))
    # fX.extend(dft(val[0]))
    # print(val[1])

def draw():
    pass
    # global angle, fY, points
    # background(51)
    # x1, y1 = epicycle(200, 450, fY, PI / 2)
    # x2, y2 = epicycle(450, 250, fX, 0)
    # line(x1, y1, x2, y1)
    # line(x2, y2, x2, y1)
    # points.insert(0, [x2, y1])
    # if len(points) > 400:
    #     points.pop()
    # for p in range(len(points)):
    #     point(points[p][0], points[p][1])
    # dt = 2 * PI / len(fY)
    # angle -= dt

def epicycle(x, y, f, rotation):
    for i in range(len(f)):
        freq = f[i]['freq']
        prevx = x
        prevy = y
        radious = f[i]['amp']
        phase = f[i]['phase']
        x += radious * cos(freq * angle + phase + rotation)
        y += radious * sin(freq * angle + phase + rotation)
        noFill()
        ellipse(prevx, prevy, radious * 2, radious * 2)
        line(prevx, prevy, x, y)
    return x, y

def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            phi = (2 * PI * k * n) / N
            re += x[n] * cos(phi)
            im -= x[n] * sin(phi)

        re = re / N
        im = im / N
        X.append({
            're': re,
            'im': im,
            'freq': k,
            'amp': sqrt(re * re + im * im),
            'phase': atan2(im, re)
        })
    return X
