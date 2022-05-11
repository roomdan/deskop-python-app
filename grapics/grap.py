from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


class Grap_view():
    def __init__(self, grap_title: str, data: dict, destination_route) -> None:
        self.grap_title = grap_title
        self.data = data
        self.destination_route = destination_route

    def __gen_canvas_data(self):
        data = self.data
        group_data = list(data.values())
        group_names = list(data.keys())
        np.mean(group_data)

        # Define template desing and layout auto generate
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use('fivethirtyeight')

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(y=group_names, width=group_data)

        labels_field = ax.get_xticklabels()
        plt.setp(labels_field, rotation=45, horizontalalignment='right')

        ax.set(xlim=[-10000, 140000], xlabel='Score', ylabel='Students',
               title=self.grap_title)

        return (fig, ax)

    def show_graph(self, save_png: bool = False):
        fig, ax = self.__gen_canvas_data()

        if save_png:
            file_name = f'{self.grap_title.replace(" ", "_").lower()}_{datetime.now().date()}_{datetime.now().microsecond}'
            fig.savefig(f'{self.destination_route}/{file_name}.png', transparent=False,
                        dpi=80, bbox_inches="tight")
        else:
            plt.show()
        # print(plt.style.available) graph styles
        # # print(fig.canvas.get_supported_filetypes()) options for save figure

    def close_graph(self):
        plt.close()
