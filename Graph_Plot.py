import matplotlib.pyplot as plt

def Plot(errors):
    x = errors
    y = []
    for i in range(0, len(x)):
        y.append(i)
    plt.plot(y, x, color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=3)
    plt.xlabel('No. of iterations')
    plt.ylabel('Error (In %)')
    # plt.ylim(0, 100)
    plt.title('Training Error Graph')
    plt.show()

