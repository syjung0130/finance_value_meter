import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

# x축 값을 따로 지정하지 않으면 실숫값이 할당된다.
# plt.plot([1, 2, 3, 4])
# plt.show()
ax1.plot([1, 2, 3, 4])
ax1.set_xlabel('x')
ax1.set_ylabel('y=x')

x = range(0, 100)
y = [v*v for v in x]
# plt.plot(x, y)
# plt.show()
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_ylabel('y=x^2')


x = range(0, 100)
y = [v*v for v in x]
# ro를 마지막 인자로 넘기면 빨간 점이 그래프로 그려진다.
# plt.plot(x, y, 'ro')
# rx는 빨간색 x가 각 점마다 그려진다.
# plt.plot(x, y, 'rx')
# r-는 빨간색으로 직선이 그려진다.
# plt.plot(x, y, 'r-')
# plt.show()
ax3.plot(x, y, 'ro')
ax3.set_xlabel('x')
ax3.set_ylabel('y=x^2')

# 지원되는 색상
# b(blue), g(green), r(red), c(cyan), m(magenta)
# y(yellow), b(black), w(white)

# 점(마커) 도형
# o(원), v(역삼각형), ^(삼각형), 
# s(square, 네모), plus(플러스), .(point, 점)

plt.show()