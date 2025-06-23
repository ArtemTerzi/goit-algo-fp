import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    plt.plot([x, x_end], [y, y_end], color='brown', linewidth=1)

    delta = np.pi / 4 

    draw_tree(x_end, y_end, angle - delta, length * 0.7, depth - 1)
    draw_tree(x_end, y_end, angle + delta, length * 0.7, depth - 1)

def main():
    level = int(input("Enter recursion level: "))
    plt.figure(figsize=(10, 10))
    draw_tree(x=0, y=0, angle=np.pi/2, length=100, depth=level)
    plt.axis("off")
    plt.gca().set_aspect('equal')
    plt.show()

if __name__ == "__main__":
    main()
