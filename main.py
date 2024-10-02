import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphApp:
    def __init__(self, master):
        self.error_label = None
        self.entry_edges = None
        self.entry_vertices = None
        self.master = master
        self.master.title("Graph Management")
        self.master.state('zoomed')
        self.master.resizable(False, False)

        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack(pady=10)

        self.button_random = tk.Button(self.master, text="Random graph",
                                       command=self.create_popup)
        self.button_random.pack(pady=10)

        self.button_draw = tk.Button(self.master, text="Draw graph",
                                     command=self.draw_graph)
        self.button_draw.pack(pady=10)

        self.popup = None
        self.G = nx.Graph()

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

            if num_vertices < 2:
                self.error_label.config(
                    text="Number of vertices must be at least 2.")
                return

            min_edges = num_vertices - 1
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
        self.G = nx.gnm_random_graph(num_vertices, num_edges)
        self.output_label.config(
            text=f"Random graph created with {num_vertices} vertices and {num_edges} edges.")

    def draw_graph(self):
        if not self.G.number_of_nodes():
            self.output_label.config(text="Please create a random graph first.")
            return

        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, ax=ax, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_color='black')

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
