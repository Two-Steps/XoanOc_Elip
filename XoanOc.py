import turtle

t = turtle.Turtle()
kc = int(input('Nhap vao gia tri: '))
start_pos = t.pos()
r = 1
while r < kc:
    t.lt(18)
    t.fd(r)
    r += 1
    # get current position
    now_pos = t.pos()
    dis = t.distance(start_pos,now_pos)
    if dis >= kc:
        break

turtle.done()
