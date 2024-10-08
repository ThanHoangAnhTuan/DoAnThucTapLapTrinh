import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Task 1: them truong input cho nguoi dung nhap (MINH)
# - title
# - vd: dinh_1, dinh_2, weight (option)
# Task 2: them popup chon type_graph voi type_weight cho nguoi dung chon (AN)
# Task 3: parse input tu truong input (KHOI)

class GraphApp:
    # ham __init__ duoc chay dau tien
    def __init__(self, master):
        self.error_label = None
        self.entry_edges = None
        self.entry_vertices = None
        self.master = master
        self.master.title("Graph Management")

        # full man hinh
        self.master.state('zoomed')

        # khong cho chinh sua kich thuoc
        self.master.resizable(False, False)

        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack(pady=10)

        self.button_random = tk.Button(self.master, text="Random graph",
                                       command=self.create_popup)
        # padding
        self.button_random.pack(pady=10)

        self.button_draw = tk.Button(self.master, text="Draw graph",
                                     command=self.draw_graph)
        self.button_draw.pack(pady=10)

        self.popup = None
        self.G = nx.Graph()  # do thi vo huong
        self.DG = nx.DiGraph()  # do thi co huong

    def create_popup(self):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Enter number of vertices and edges")
        popup_width, popup_height = 300, 300
        self.popup.resizable(False, False)

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_x = int(screen_width / 2 - popup_width / 2)
        center_y = int(screen_height / 2 - popup_height / 2)
        self.popup.geometry(
            f"{popup_width}x{popup_height}+{center_x}+{center_y}")

        tk.Label(self.popup, text="Number of vertices:").pack(pady=10)
        self.entry_vertices = tk.Entry(self.popup, width=30)
        self.entry_vertices.pack(pady=5)

        tk.Label(self.popup, text="Number of edges:").pack(pady=10)
        self.entry_edges = tk.Entry(self.popup, width=30)
        self.entry_edges.pack(pady=5)

        self.error_label = tk.Label(self.popup, text="", fg="red")
        self.error_label.pack(pady=10)

        tk.Button(self.popup, text="Confirm", command=self.validate_input).pack(
            pady=10)

    def validate_input(self):
        try:
            num_vertices = int(self.entry_vertices.get())
            num_edges = int(self.entry_edges.get())

            # so dinh toi thieu phai la: 1
            if num_vertices < 1:
                self.error_label.config(
                    text="Number of vertices must be at least 1.")
                return

            min_edges = 0
            max_edges = (num_vertices * (num_vertices - 1)) // 2

            if num_edges < min_edges or num_edges > max_edges:
                self.error_label.config(
                    text=f"Number of edges must be between {min_edges} and {max_edges}.")
                return

            self.random_graph(num_vertices, num_edges)
            self.popup.destroy()
        except ValueError:
            self.error_label.config(text="Please enter valid numbers!")

    def random_graph(self, num_vertices, num_edges):
        # return list voi dang [(dinh_1, dinh_2, weight), (dinh_1, dinh_2, weight)]

    # 1,2,3
    # 2,3,4
    # return list voi dang [(dinh_1, dinh_2, weight), (dinh_1, dinh_2, weight)]
    # VD: [(1, 2, 3), (2, 3, 4)]
    def parse_input(self):

    def draw_graph(self, type_graph, type_weight, data):
        # kiem tra type_graph
        # kiem tra type_weight

        # do thi co huong nhung khong co weight
        # self.DG = nx.DiGraph(self.G)
        for i in range(len(data)):
            self.DG.add_edge(data[i][0], data[i][1], data[i][2])
        # self.DG.add_edge("2", "3")
        # nx.draw(self.DG, with_labels=True, arrows=True,
        #         font_weight='bold', node_color="blue", edge_color="black",
        #         font_color="#fff", arrowsize=20)
        # plt.show()

        # do thi co huong nhung co weight
        # self.DG = nx.DiGraph(self.G)
        # self.DG.add_edge("2", "3", weight=1)
        # pos = nx.spring_layout(self.DG)
        # nx.draw(self.DG, with_labels=True, arrows=True,
        #         font_weight='bold', node_color="blue", edge_color="black",
        #         font_color="#fff", arrowsize=20, pos=pos)
        # edge_labels = nx.get_edge_attributes(self.DG, 'weight')
        # nx.draw_networkx_edge_labels(self.DG, pos, edge_labels=edge_labels)
        # plt.show()

        # do thi vo huong nhung khong co weight
        # self.G = nx.Graph(self.DG)
        # self.G.add_edge("2", "3")
        # nx.draw(self.G, with_labels=True, arrows=True,
        #         font_weight='bold', node_color="blue", edge_color="black",
        #         font_color="#fff", arrowsize=20)
        # plt.show()

        # do thi vo huong nhung co weight
        self.G = nx.Graph(self.DG)
        self.G.add_edge("2", "3", weight=1)
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, with_labels=True, arrows=True,
                font_weight='bold', node_color="blue", edge_color="black",
                font_color="#fff", arrowsize=20, pos=pos)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        plt.show()

        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(self.G)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    # Khoi tao tkinder
    # tkinder la thu vien de tao UI tren desktop
    root = tk.Tk()

    # Khoi tao class GraphApp
    app = GraphApp(root)
    root.mainloop()
