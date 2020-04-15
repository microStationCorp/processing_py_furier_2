fX = []
fY = []
val = []
valX = []
valY = []
angle = 0
points = []

def setup():
    size(900, 800)
    background(51)
    stroke(255)
    
    for i in range(0,11,1):
        val.append([75-i*.5,50-i])
    for i in range(0,11,1):
        val.append([70-i*.5,40+i])
    for i in range(0,11,1):
        val.append([65+i,50])
    for i in range(0, 41, 1):
        val.append([i + 50, 0])
    for i in range(0, 51, 1):
        val.append([90 + i, i * 2])
    for i in range(0, 41, 1):
        val.append([140 - i, 100])
    for i in range(0,41,1):
        val.append([100-i*.5,100-i])
    for i in range(0,21,1):
        val.append([80-i,60])
    for i in range(0, 41, 1):
        val.append([60 - i * .5, i+60])
    for i in range(0, 41, 1):
        val.append([40 - i, 100])
    for i in range(0, 101, 1):
        val.append([i * .5, 100 - i])
    for i in range(0, len(val), 1):
        valX.append(val[i][0])
        valY.append(val[i][1])
    fY.extend(dft(valY))
    fX.extend(dft(valX))
    print('start',valX[len(valX) - 1], valY[len(valY) - 1])
    print('end',valX[0], valY[0])
    
def draw():
    # pass
    global angle, fY, points
    background(51)
    x1, y1 = epicycle(200, 450, fY, PI / 2)
    x2, y2 = epicycle(450, 250, fX, 0)
    stroke(0,255,255)
    line(x1, y1, x2, y1)
    line(x2, y2, x2, y1)
    points.insert(0, [x2, y1])
    if len(points) > 500:
        points.pop()
    for p in range(len(points)):
        stroke(255,100,200)
        point(points[p][0], points[p][1])
    dt = 2 * PI / len(fY)
    angle -= dt

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
        stroke(255,100)
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
