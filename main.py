import tkinter as tk
from tkinter import messagebox
# tạo ra được 1 trường input
# tạo ra được 2 button (button: vẽ graph, random graph)
# Khi nhấn button vẽ graph thì value của trường input phải hiển thị ra
input_widgets_shown = False

popup = None
def show_ui(root):
    global output_label


    button_random = tk.Button(root, text="Random graph", command=create_popup)
    button_random.pack(pady=10)


    button_draw = tk.Button(root, text="Draw graph", command=draw_graph)
    button_draw.pack(pady=10)

    global output_label
    output_label = tk.Label(root, text="")
    output_label.pack(pady=10)

def create_popup():
    global popup, entry_vertices, entry_edges, error_label

    # Tạo cửa sổ pop-up
    popup = tk.Toplevel()
    popup.title("Nhập số đỉnh và số cạnh")
    popup_width = 300
    popup_height = 300
    popup.resizable(False, False)
    
    # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán tọa độ để đặt pop-up vào giữa màn hình
    center_x = int(screen_width / 2 - popup_width / 2)
    center_y = int(screen_height / 2 - popup_height / 2)

    # Đặt kích thước và vị trí của pop-up
    popup.geometry(f"{popup_width}x{popup_height}+{center_x}+{center_y}")

    label_vertices = tk.Label(popup, text="Nhập số đỉnh:")
    label_vertices.pack(pady=10)
    entry_vertices = tk.Entry(popup, width=30)
    entry_vertices.pack(pady=5)

    label_edges = tk.Label(popup, text="Nhập số cạnh:")
    label_edges.pack(pady=10)
    entry_edges = tk.Entry(popup, width=30)
    entry_edges.pack(pady=5)

    # Label để hiển thị lỗi trực tiếp trong pop-up
    error_label = tk.Label(popup, text="", fg="red")
    error_label.pack(pady=10)

    button_confirm = tk.Button(popup, text="Xác nhận", command=validate_input)
    button_confirm.pack(pady=10)


def validate_input():
    try:
        # Lấy số đỉnh và số cạnh từ ô nhập
        num_vertices = int(entry_vertices.get())
        num_edges = int(entry_edges.get())

        # Kiểm tra điều kiện nhập liệu
        min_edges = num_vertices - 1
        max_edges = (num_vertices * (num_vertices - 1)) // 2

        if num_vertices < 2:
            error_label.config(text="Số đỉnh phải lớn hơn hoặc bằng 2.")
            return

        if num_vertices == 2 and num_edges != 1:
            error_label.config(text="Nếu số đỉnh bằng 2, số cạnh phải bằng 1.")
            return

        if num_edges < min_edges or num_edges > max_edges:
            error_label.config(text=f"Số cạnh phải từ {min_edges} đến {max_edges}.")
            return

        # Nếu nhập đúng, đóng pop-up
        popup.destroy()

    except ValueError:
        error_label.config(text="Vui lòng nhập số hợp lệ!")
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
def random_graph():
    return None


def draw_graph():
    return None


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Graph")
    show_ui(root)
    root.state('zoomed')
    root.resizable(False, False)
    # khởi động UI
    root.mainloop()
