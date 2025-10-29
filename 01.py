import tkinter as tk
import random
import threading
import time


def dow():
    # 1. 修正Tk()创建（必须在主线程或确保单线程操作）
    # 注意：Tkinter不建议多线程创建窗口，这里改为单线程循环创建多个窗口（或用队列在主线程处理）
    window = tk.Tk()
    window.title("弹窗")

    # 2. 修正随机位置参数（去掉start=语法错误）
    width = window.winfo_screenwidth()  # 屏幕宽度
    height = window.winfo_screenheight()  # 屏幕高度
    a = random.randrange(0, width)  # 随机x坐标（0到屏幕宽度）
    b = random.randrange(0, height)  # 随机y坐标（0到屏幕高度）

    # 3. 修正窗口尺寸和位置（确保格式正确）
    window.geometry(f"220x50+{a}+{b}")  # 使用f-string更简洁

    # 随机文本
    texts = ["多喝热水", "天天开心", "好好吃饭", "我想你了", "期待下一次见面", "别熬夜",
             "多穿衣服", "梦想成真", "顺利利~", "发财发财", "保持好心情", "喜欢你",
             "早点休息", "别熬夜", "记得想我", "元气满满", "好好爱自己", "保持微笑", "记得"]
    text = random.choice(texts)

    # 随机背景颜色
    bg_colors = ["pink", "lightskyblue", "lightgreen", "lavender", "lightyellow"]
    bg = random.choice(bg_colors)

    # 创建标签
    tk.Label(window,
             text=text,
             bg=bg,
             font=("楷体", 19),
             width=25,
             height=4).pack()

    # 4. 每个窗口设置自动关闭（避免窗口堆积）
    # window.after(3000, window.destroy)  # 3秒后自动关闭
    window.mainloop()


if __name__ == "__main__":
    # 5. 控制弹窗数量（150个太多，先测试5个）
    threads = []
    for i in range(150):  # 减少数量，避免系统卡顿
        t = threading.Thread(target=dow)
        threads.append(t)
        t.start()
        time.sleep(0.1)  # 间隔创建，避免同时弹出

    # 等待所有线程结束
    for t in threads:
        t.join()

        import os
        print(os.getcwd())