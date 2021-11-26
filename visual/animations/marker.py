import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.cla()
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5, 6]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.scatter(x[:frame], y[:frame])


def run():
    global fig
    simple_animation = animation.FuncAnimation(fig,
                                               animate,
                                               frames=10,
                                               interval=1000)
    plt.show()


run()
