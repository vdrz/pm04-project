import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class MultiFunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Практика 1")
        self.root.geometry("800x700")
        self.name = "Вадим"
        self.counter = 0
        self.random_value = 0
        self.random_max = 100
        self.r_value = 128
        self.g_value = 128
        self.b_value = 128
        self.setup_ui()
   
    def setup_ui(self):
        tab_control = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Приветствия и счётчик")
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text="TrackBar и ProgressBar")
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text="Цвет по RGB")
        tab_control.pack(expand=1, fill="both")
        self.setup_tab1(tab1)
        self.setup_tab2(tab2)
        self.setup_tab3(tab3)
    def setup_tab1(self, tab):
        title_label = tk.Label(tab, text="Приветствия и счётчик нажатий", 
                               font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        ttk.Separator(tab, orient='horizontal').pack(fill='x', padx=10, pady=5)
        frame1 = tk.Frame(tab)
        frame1.pack(pady=10, padx=20, fill="x")
        label1_title = tk.Label(frame1, text="1. Кнопка → Label:", font=("Arial", 10, "bold"))
        label1_title.grid(row=0, column=0, sticky="w", padx=5)
        button1 = tk.Button(frame1, text="Поприветствовать", command=self.greet_label)
        button1.grid(row=0, column=1, padx=5)
        self.greet_label_display = tk.Label(frame1, text="Нажмите кнопку", bg="white", 
                                           relief="sunken", width=25, height=2)
        self.greet_label_display.grid(row=0, column=2, padx=10)
        frame2 = tk.Frame(tab)
        frame2.pack(pady=10, padx=20, fill="x")
        label2_title = tk.Label(frame2, text="2. Кнопка → Memo:", font=("Arial", 10, "bold"))
        label2_title.grid(row=0, column=0, sticky="w", padx=5)
        button2 = tk.Button(frame2, text="Добавить приветствие", command=self.greet_memo)
        button2.grid(row=0, column=1, padx=5)
        memo_frame = tk.Frame(frame2)
        memo_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")
        self.memo_text = tk.Text(memo_frame, height=5, width=50)
        memo_scrollbar = tk.Scrollbar(memo_frame, command=self.memo_text.yview)
        self.memo_text.config(yscrollcommand=memo_scrollbar.set)
        self.memo_text.pack(side="left", fill="both", expand=True)
        memo_scrollbar.pack(side="right", fill="y")
        frame3 = tk.Frame(tab)
        frame3.pack(pady=15, padx=20, fill="x") 
        label3_title = tk.Label(frame3, text="3. Счётчик нажатий:", font=("Arial", 10, "bold"))
        label3_title.grid(row=0, column=0, sticky="w", padx=5)
        self.counter_button = tk.Button(frame3, text="Нажми меня", command=self.increment_counter)
        self.counter_button.grid(row=0, column=1, padx=5)
        self.counter_display = tk.Entry(frame3, width=10, font=("Arial", 12), 
                                       justify="center", state="readonly")
        self.counter_display.grid(row=0, column=2, padx=5)
        self.counter_display.config(state="normal")
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.counter))
        self.counter_display.config(state="readonly")
        reset_counter_btn = tk.Button(frame3, text="Сбросить", command=self.reset_counter)
        reset_counter_btn.grid(row=0, column=3, padx=5)
        frame4 = tk.Frame(tab)
        frame4.pack(pady=15, padx=20, fill="x")
        name_label = tk.Label(frame4, text="Ваше имя:")
        name_label.grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(frame4, width=20)
        self.name_entry.grid(row=0, column=1, padx=5)
        self.name_entry.insert(0, self.name)  
        update_name_btn = tk.Button(frame4, text="Обновить имя", command=self.update_name)
        update_name_btn.grid(row=0, column=2, padx=5)
    def setup_tab2(self, tab):
        title_label = tk.Label(tab, text="TrackBar и ProgressBar", 
                               font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        ttk.Separator(tab, orient='horizontal').pack(fill='x', padx=10, pady=5)
        frame1 = tk.Frame(tab)
        frame1.pack(pady=10, padx=20, fill="x")
        label1_title = tk.Label(frame1, text="4. TrackBar → ProgressBar:", 
                               font=("Arial", 10, "bold"))
        label1_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        self.trackbar = tk.Scale(frame1, from_=0, to=100, orient=tk.HORIZONTAL, 
                                 length=300, command=self.update_progressbar)
        self.trackbar.set(50)
        self.trackbar.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")
        self.progressbar = ttk.Progressbar(frame1, length=300, maximum=100)
        self.progressbar.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")
        self.progressbar["value"] = 50
        trackbar_value_label = tk.Label(frame1, text="Значение TrackBar:")
        trackbar_value_label.grid(row=3, column=0, sticky="w", pady=5)
        self.trackbar_value_display = tk.Entry(frame1, width=10, justify="center")
        self.trackbar_value_display.grid(row=3, column=1, sticky="w", pady=5)
        self.trackbar_value_display.insert(0, "50")
        frame2 = tk.Frame(tab)
        frame2.pack(pady=20, padx=20, fill="x")
        label2_title = tk.Label(frame2, text="5. Вертикальный ProgressBar:", 
                               font=("Arial", 10, "bold"))
        label2_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        self.vertical_progressbar = ttk.Progressbar(frame2, orient="vertical", 
                                                   length=150, maximum=100)
        self.vertical_progressbar.grid(row=1, column=0, padx=20, pady=5)
        self.vertical_progressbar["value"] = 75
        fuel_label = tk.Label(frame2, text="Уровень топлива")
        fuel_label.grid(row=2, column=0, pady=5)
        fuel_up_btn = tk.Button(frame2, text="Заправить (+10%)", 
                               command=lambda: self.adjust_fuel(10))
        fuel_up_btn.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        fuel_down_btn = tk.Button(frame2, text="Использовать (-10%)", 
                                 command=lambda: self.adjust_fuel(-10))
        fuel_down_btn.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        frame3 = tk.Frame(tab)
        frame3.pack(pady=20, padx=20, fill="x")
        
        label3_title = tk.Label(frame3, text="6. Случайные числа + ProgressBar:", 
                               font=("Arial", 10, "bold"))
        label3_title.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        random_max_label = tk.Label(frame3, text="Макс. значение:")
        random_max_label.grid(row=1, column=0, sticky="w", pady=5)
        self.random_trackbar = tk.Scale(frame3, from_=10, to=200, orient=tk.HORIZONTAL, 
                                       length=200, command=self.update_random_max)
        self.random_trackbar.set(100)
        self.random_trackbar.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
        self.random_progressbar = ttk.Progressbar(frame3, length=250, maximum=100)
        self.random_progressbar.grid(row=2, column=0, columnspan=3, pady=10, sticky="w")
        random_reset_btn = tk.Button(frame3, text="Сгенерировать случайное число", 
                                    command=self.generate_random)
        random_reset_btn.grid(row=3, column=0, pady=5, sticky="w")
        random_value_label = tk.Label(frame3, text="Текущее значение:")
        random_value_label.grid(row=3, column=1, pady=5, padx=5)
        self.random_value_display = tk.Entry(frame3, width=10, justify="center")
        self.random_value_display.grid(row=3, column=2, pady=5, sticky="w")
        self.generate_random()
    def setup_tab3(self, tab):
        title_label = tk.Label(tab, text="Цвет по RGB", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        ttk.Separator(tab, orient='horizontal').pack(fill='x', padx=10, pady=5)
        desc_label = tk.Label(tab, text="Тремя TrackBar задавайте значения R, G, B (0–255)")
        desc_label.pack(pady=5)
        main_frame = tk.Frame(tab)
        main_frame.pack(pady=15, padx=20)
        display_frame = tk.Frame(main_frame)
        display_frame.grid(row=0, column=0, rowspan=4, padx=20, pady=10)
        self.color_rect = tk.Canvas(display_frame, width=200, height=150, 
                                    bg=f"#{self.r_value:02x}{self.g_value:02x}{self.b_value:02x}")
        self.color_rect.pack(pady=10)
        self.color_text = tk.Label(display_frame, text=f"RGB({self.r_value}, {self.g_value}, {self.b_value})", 
                                  font=("Courier", 12))
        self.color_text.pack(pady=10)
        self.hex_color_text = tk.Label(display_frame, 
                                      text=f"#{self.r_value:02x}{self.g_value:02x}{self.b_value:02x}", 
                                      font=("Courier", 10))
        self.hex_color_text.pack(pady=5)
        controls_frame = tk.Frame(main_frame)
        controls_frame.grid(row=0, column=1, padx=20, pady=10)
        red_label = tk.Label(controls_frame, text="Красный (R):", fg="red", 
                            font=("Arial", 10, "bold"))
        red_label.grid(row=0, column=0, sticky="w", pady=10)
        self.red_trackbar = tk.Scale(controls_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                                    length=250, command=lambda val: self.update_color("r", val))
        self.red_trackbar.set(self.r_value)
        self.red_trackbar.grid(row=0, column=1, padx=10, pady=5)
        self.red_value = tk.Label(controls_frame, text=str(self.r_value), width=3)
        self.red_value.grid(row=0, column=2, padx=5)
        green_label = tk.Label(controls_frame, text="Зелёный (G):", fg="green", 
                              font=("Arial", 10, "bold"))
        green_label.grid(row=1, column=0, sticky="w", pady=10)
        self.green_trackbar = tk.Scale(controls_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                                      length=250, command=lambda val: self.update_color("g", val))
        self.green_trackbar.set(self.g_value)
        self.green_trackbar.grid(row=1, column=1, padx=10, pady=5)
        
        self.green_value = tk.Label(controls_frame, text=str(self.g_value), width=3)
        self.green_value.grid(row=1, column=2, padx=5)
        blue_label = tk.Label(controls_frame, text="Синий (B):", fg="blue", 
                             font=("Arial", 10, "bold"))
        blue_label.grid(row=2, column=0, sticky="w", pady=10)
        self.blue_trackbar = tk.Scale(controls_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                                     length=250, command=lambda val: self.update_color("b", val))
        self.blue_trackbar.set(self.b_value)
        self.blue_trackbar.grid(row=2, column=1, padx=10, pady=5)
        self.blue_value = tk.Label(controls_frame, text=str(self.b_value), width=3)
        self.blue_value.grid(row=2, column=2, padx=5)

        colors_frame = tk.Frame(main_frame)
        colors_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        color_buttons = [
            ("Красный", "#ff0000", (255, 0, 0)),
            ("Зелёный", "#00ff00", (0, 255, 0)),
            ("Синий", "#0000ff", (0, 0, 255)),
            ("Жёлтый", "#ffff00", (255, 255, 0)),
            ("Фиолетовый", "#800080", (128, 0, 128)),
            ("Голубой", "#00ffff", (0, 255, 255)),
            ("Белый", "#ffffff", (255, 255, 255)),
            ("Чёрный", "#000000", (0, 0, 0))
        ]
        
        for i, (text, color, rgb) in enumerate(color_buttons):
            btn = tk.Button(colors_frame, text=text, bg=color, width=10,
                           command=lambda r=rgb[0], g=rgb[1], b=rgb[2]: self.set_preset_color(r, g, b))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    

    def greet_label(self):
        """Обновляет Label с приветствием"""
        self.greet_label_display.config(text=f"Привет, {self.name}!")
    
    def greet_memo(self):
        """Добавляет приветствие в Memo (Text widget)"""
        self.memo_text.insert(tk.END, f"Привет, {self.name}!\n")
        self.memo_text.see(tk.END)
    
    def increment_counter(self):
        """Увеличивает счётчик нажатий на 1"""
        self.counter += 1
        self.counter_display.config(state="normal")
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.counter))
        self.counter_display.config(state="readonly")
        
        if self.counter % 5 == 0:
            self.counter_button.config(bg="lightgreen")
            self.root.after(300, lambda: self.counter_button.config(bg="SystemButtonFace"))
    
    def reset_counter(self):
        """Сбрасывает счётчик нажатий"""
        self.counter = 0
        self.counter_display.config(state="normal")
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.counter))
        self.counter_display.config(state="readonly")
    
    def update_name(self):
        """Обновляет имя для приветствий"""
        new_name = self.name_entry.get().strip()
        if new_name:
            self.name = new_name
            messagebox.showinfo("Имя обновлено", f"Теперь приветствия будут использовать имя: {self.name}")
        else:
            messagebox.showwarning("Пустое имя", "Введите имя в поле")
    
    def update_progressbar(self, value):
        """Обновляет ProgressBar в соответствии с TrackBar"""
        self.progressbar["value"] = value
        self.trackbar_value_display.delete(0, tk.END)
        self.trackbar_value_display.insert(0, str(int(float(value))))
    
    def adjust_fuel(self, amount):
        """Изменяет уровень топлива в вертикальном ProgressBar"""
        current = self.vertical_progressbar["value"]
        new_value = current + amount
        
        if new_value < 0:
            new_value = 0
        elif new_value > 100:
            new_value = 100
        
        self.vertical_progressbar["value"] = new_value
        
        if new_value < 20:
            self.vertical_progressbar.configure(style="Red.Horizontal.TProgressbar")
        elif new_value < 50:
            self.vertical_progressbar.configure(style="Yellow.Horizontal.TProgressbar")
        else:
            self.vertical_progressbar.configure(style="Green.Horizontal.TProgressbar")
    
    def update_random_max(self, value):
        """Обновляет максимальное значение для случайных чисел"""
        self.random_max = int(float(value))
    
    def generate_random(self):
        """Генерирует случайное число и отображает его в ProgressBar"""
        self.random_value = random.randint(0, self.random_max)
        self.random_progressbar["maximum"] = self.random_max
        self.random_progressbar["value"] = self.random_value
        self.random_value_display.delete(0, tk.END)
        self.random_value_display.insert(0, str(self.random_value))
    
    def update_color(self, channel, value):
        """Обновляет цвет на основе значений RGB"""
        value = int(float(value))
        
        if channel == "r":
            self.r_value = value
            self.red_value.config(text=str(value))
        elif channel == "g":
            self.g_value = value
            self.green_value.config(text=str(value))
        elif channel == "b":
            self.b_value = value
            self.blue_value.config(text=str(value))
        
        hex_color = f"#{self.r_value:02x}{self.g_value:02x}{self.b_value:02x}"
        self.color_rect.config(bg=hex_color)
        
        self.color_text.config(text=f"RGB({self.r_value}, {self.g_value}, {self.b_value})")
        self.hex_color_text.config(text=hex_color)
    
    def set_preset_color(self, r, g, b):
        """Устанавливает предустановленный цвет"""
        self.r_value = r
        self.g_value = g
        self.b_value = b

        self.red_trackbar.set(r)
        self.green_trackbar.set(g)
        self.blue_trackbar.set(b)
        
        self.red_value.config(text=str(r))
        self.green_value.config(text=str(g))
        self.blue_value.config(text=str(b))

        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        self.color_rect.config(bg=hex_color)

        self.color_text.config(text=f"RGB({r}, {g}, {b})")
        self.hex_color_text.config(text=hex_color)

def main():
    root = tk.Tk()

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Red.Horizontal.TProgressbar", 
                   background='red', 
                   troughcolor='#e0e0e0', 
                   bordercolor='#a0a0a0', 
                   lightcolor='#ff8080', 
                   darkcolor='#a00000')
    
    style.configure("Yellow.Horizontal.TProgressbar", 
                   background='yellow', 
                   troughcolor='#e0e0e0', 
                   bordercolor='#a0a0a0', 
                   lightcolor='#ffff80', 
                   darkcolor='#a0a000')
    
    style.configure("Green.Horizontal.TProgressbar", 
                   background='green', 
                   troughcolor='#e0e0e0', 
                   bordercolor='#a0a0a0', 
                   lightcolor='#80ff80', 
                   darkcolor='#00a000')
    
    app = MultiFunctionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
