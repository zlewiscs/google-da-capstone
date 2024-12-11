import matplotlib.pyplot as plt


def plot_data(data, title):
    """
    Plot the data    :param data:  to plot
    :param data:
    :param title: the title of the plot
    :return: None
    """
    f = plt.figure()
    plt.plot(data)
    plt.title(title)
    plt.show()

    f.savefig("/home/lewiscs/PycharmProjects/google-da-capstone/data/" + title + ".pdf", bbox_inches='tight')
