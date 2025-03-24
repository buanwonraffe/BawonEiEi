import tkinter as tk
from tkinter import ttk, messagebox

# ฟังก์ชันคำนวณแคลอรี่
def calculate_calories():
    try:
        food = entry_food.get()
        quantity = float(entry_quantity.get())
        
        # ฐานข้อมูลอาหาร
        food_data = {
            "ข้าวสวย": 130,
            "ไก่ทอด": 250,
            "ผลไม้": 50
        }
        
        if food in food_data:
            calories = food_data[food] * quantity / 100
            result_label.config(text=f"แคลอรี่ที่รับประทาน: {calories:.2f} แคลอรี่", foreground="green")
        else:
            messagebox.showwarning("ไม่พบข้อมูล", "ไม่มีข้อมูลอาหารนี้ในระบบ")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("🐰 คำนวณแคลอรี่สุดคิวท์ 🩷")
root.geometry("350x400")
root.configure(bg="#FFE6E6")

# สไตล์
style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 12), padding=5)
style.configure("TLabel", background="#FFE6E6", font=("Comic Sans MS", 12))
style.configure("TEntry", font=("Comic Sans MS", 12))

# หัวข้อ
title_label = ttk.Label(root, text="🐻 คำนวณแคลอรี่สุดน่ารัก 🐰", font=("Comic Sans MS", 14, "bold"), background="#FFB6C1")
title_label.pack(pady=10)

# ช่องกรอกชื่ออาหาร
label_food = ttk.Label(root, text="ชื่ออาหาร:")
label_food.pack()
entry_food = ttk.Entry(root)
entry_food.pack(pady=5)

# ช่องกรอกปริมาณ
label_quantity = ttk.Label(root, text="ปริมาณ (กรัม):")
label_quantity.pack()
entry_quantity = ttk.Entry(root)
entry_quantity.pack(pady=5)

# ปุ่มคำนวณ
calculate_button = ttk.Button(root, text="✨ คำนวณแคลอรี่ ✨", command=calculate_calories)
calculate_button.pack(pady=10)

# ป้ายผลลัพธ์
result_label = ttk.Label(root, text="", font=("Comic Sans MS", 12, "bold"))
result_label.pack(pady=10)

# เริ่มแอป
root.mainloop()
