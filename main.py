import tkinter as tk
import random

# tạo ra được 1 trường input
# tạo ra được 2 button (button: vẽ graph, random graph)
# Khi nhấn button vẽ graph thì value của trường input phải hiển thị ra
def show_ui(root):
    button = tk.Button(root, text="Open Second Window", command=lambda:
    root.quit())
    button.pack(pady=10)

# input:
# 1,2,3
# 1,3,5
# lấy được số đầu tiên lưu vào biến cạnh first_edge
# lấy được số thứ 2 lưu vào biến cạnh second_edge
# lấy được số thứ 3 lưu vào biến weight
# cắt theo \n, sau đó cắt theo ","
def split_input():
    return None


# Cho người dùng nhập vào số đỉnh tối đa: VD: 5
# random số đỉnh của graph với range là 2 tới 5
# Cho người dùng nhập vào số cạnh tối đa của 1 đỉnh với rang là từ 1 tới số
# cạnh tối đa (số đỉnh - 1)
# cho người dùng nhập số cạnh tối đa của 1 đỉnh trong điều kiện ở trên
# mỗi khi random được 1 cạnh thì random 1 số weight nhất định

# result: số đỉnh và số cạnh của mỗi đỉnh
def random_graph(max_num_nodes_input,max_num_edges_input):
    num_nodes = []
    num_nodes_random = random.randint(2, max_num_nodes_input)
    for i in range(num_nodes_random):
        num_nodes.append(i + 1)

    max_num_edges_of_node = len(num_nodes) - 1
    min_num_edges_of_node = 1

    if (max_num_edges_input > max_num_edges_of_node) or (max_num_edges_input < min_num_edges_of_node):
        print("Vui long nhap lai: ")

    print(num_nodes)
    for i in range(len(num_nodes)):
        num_edges = random.randint(min_num_edges_of_node, max_num_edges_of_node)
        num_nodes_expected = num_nodes.copy()
        num_nodes_expected.remove(num_nodes[i])
        isUndirected = random.randint(0, 1)
        # dô thi vo huong
        if isUndirected:
            num_nodes_expected.remove(num_nodes[i])

        for j in range(len(num_nodes_expected) - num_edges):
            num_nodes_expected.remove(random.choice(num_nodes_expected))
        print(f"dinh {num_nodes[i]} co ${num_edges} canh: ${num_nodes_expected}")


def draw_graph():
    return None


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello Tkinter")
    show_ui(root)
    print("Hello Tkinter")
    # khởi động UI
    root.mainloop()
