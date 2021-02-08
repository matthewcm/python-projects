import matplotlib.pyplot as plt
import numpy as np

X = np.array([
    [6, 3, 6, 5, 3, 3],
    [3, 6, 4, 6, 4, 5],
    [2, 3, 3, 2, 2, 5],
    [4, 3, 4, 6, 4, 6],
    [5, 4, 4, 4, 4, 6],
    [4, 4, 6, 6, 4, 6],
])  # sample 2D array
plt.imshow(X, cmap="gray", vmin=0, vmax=8)
plt.show()

X = np.array([
    [7, 2, 7, 5, 2, 2],
    [2, 7, 4, 7, 4, 5],
    [1, 2, 2, 1, 1, 5],
    [4, 2, 4, 7, 4, 7],
    [5, 4, 4, 4, 4, 7],
    [4, 4, 7, 7, 4, 7],
])  # sample 2D array
plt.imshow(X, cmap="gray", vmin=0, vmax=8)
plt.show()

figure_6 = {
    "0": 0,
    "1": 0,
    "2": 3,
    "3": 7,
    "4": 12,
    "5": 4,
    "6": 10,
}


def cumulative_freq_figure(figure=figure_6):
    cum_figure = {}
    c = 0
    for (index, value) in figure.items():
        c += value
        cum_figure[index] = c

    return cum_figure


def apply_histogram(figure, max_g=7, n=6, m=3):

    equalised_figure = {}
    for g in range(0, max_g):
        first_part = ((2 ** m) - 1) / (n ** 2)
        second_part = figure[str(g)]

        result = first_part * second_part

        print(str(g) + ': ' + str(result) + ' rounded to -> ' + str(round(result)))

        equalised_figure[str(g)] = round(result)

    print(equalised_figure)

    return equalised_figure
    # (figure[str(g)])


def app():
    print('ASSIGNMENT RESULTS')
    print('CUM FIGURE')
    cum_figure = cumulative_freq_figure(figure_6)

    print(cum_figure)

    print('EQUALISED')
    print(apply_histogram(cum_figure))


if __name__ == '__main__':
    app()
