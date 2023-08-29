import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# create an empty image in directory 'static/wisielec.jpg'
def empty_image():
    fig, ax = plt.subplots(facecolor='white')
    ax.axes.set_axis_off()
    plt.xlim(-1, 16)
    plt.ylim(-1, 22)
    plt.savefig(os.path.join('static', 'wisielec.jpg'))
    plt.close()


# coordinates needed to draw a hangman
x = [0, 3, 3, 6, 3, 3, 3, 12, 12, 12]
y = [0, 2, 2, 0, 2, 21, 21, 21, 21, 17]

x_8 = [12, 12, 12, 9, 12, 15]
y_8 = [14, 6, 6, 3, 6, 3]

x_11 = [12, 9, 12, 15]
y_11 = [10, 12, 10, 12]


# create an image of a hangman in directory 'static/wisielec.jpg'
# different picture depends on a value of trial
def draw_image(trial, h=y, v=x, h8=y_8, v8=x_8, h11=y_11, v11=x_11):
    fig, ax = plt.subplots(facecolor='white')
    ax.axes.set_axis_off()
    if 0 < trial < 6:
        a = v[:trial * 2]
        b = h[:trial * 2]
        ax.plot(a, b, linewidth=2.0, color='red')
    elif trial == 6:
        a = v + [None, 3, 7]
        b = h + [None, 17, 21]
        ax.plot(a, b, linewidth=2.0, color='red')
    elif trial == 7:
        a = v + [None, 3, 7]
        b = h + [None, 17, 21]
        drawing_uncolored_circle = plt.Circle((12, 15.5), 1.5, fill=False, linewidth=2.0, color='red')
        ax.plot(a, b, linewidth=2.0, color='red')
        ax.add_artist(drawing_uncolored_circle)
    elif 10 >= trial > 7:
        trial -= 7
        a = v + [None, 3, 7] + [None] + v8[0:trial * 2]
        b = h + [None, 17, 21] + [None] + h8[0:trial * 2]
        drawing_uncolored_circle = plt.Circle((12, 15.5), 1.5, fill=False, linewidth=2.0, color='red')
        ax.plot(a, b, linewidth=2.0, color='red')
        ax.add_artist(drawing_uncolored_circle)
    elif trial > 10:
        trial -= 10
        a = v + [None, 3, 7] + [None] + v8 + [None] + v11[:trial * 2]
        b = h + [None, 17, 21] + [None] + h8 + [None] + h11[:trial * 2]
        drawing_uncolored_circle = plt.Circle((12, 15.5), 1.5, fill=False, linewidth=2.0, color='red')
        ax.plot(a, b, linewidth=2.0, color='red')
        ax.add_artist(drawing_uncolored_circle)
    plt.xlim(-1, 16)
    plt.ylim(-1, 22)
    plt.savefig(os.path.join('static', 'wisielec.jpg'))
    plt.close()