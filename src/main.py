# author: PES2UG23CS368 Nathan Matthew Paul
# author: PES2UG23CS371 Navneet Nayak
# author: PES2UG23CS3XX Nevin Mathew Thomas
# author: PES2UG23CS390 Nilay Srivastava
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2023

# import stuff
import tkinter as tk

# setup
root = tk.Tk()
root.title('Typing Speed Test')
root.geometry('900x600')
root.option_add("*Label.Font", "monospace")
root.option_add("*Button.Font", "monospace")
typed_widget = tk.Text(root, wrap=tk.WORD, height=5, width=40)
typed_widget.config(state=tk.DISABLED)

# paragraph text
para = [
    "First word last word"
]

current_word = 0
current_char = 0

print(list(para[current_word]))
print("next expected character:", para[current_word][current_char])
typed_widget.config(state=tk.NORMAL)
typed_widget.insert('1.0', para[current_word][current_char])
typed_widget.config(state=tk.DISABLED)

def sendKeys(event):
    global current_word, current_char

    typed_char = event.char
    expected_char = para[current_word][current_char]

    if typed_char == expected_char:
        if typed_char==para[0][0]: click()
        current_char += 1
        print("next expected character:", para[current_word][current_char])
        typed_widget.delete('1.0')
        typed_widget.config(state=tk.NORMAL)
        typed_widget.insert('1.0', para[current_word][current_char])
        typed_widget.config(state=tk.DISABLED)
        if current_char >= len(para[current_word]):
            current_word += 1
            current_char = 0
            typed_widget.delete('1.0')
            typed_widget.config(state=tk.NORMAL)
            typed_widget.insert('1.0', para[current_word])
            typed_widget.config(state=tk.DISABLED)
            if current_word >= len(para):
                text_widget.config(state=tk.DISABLED)
                return

# display the paragraph
text_widget = tk.Text(root, wrap=tk.WORD, height=5, width=40)
text_widget.insert('1.0', para[0])
text_widget.config(state=tk.DISABLED)

# Timer
seconds_left=60
def update_timer():
    global seconds_left

    if seconds_left > 0:
        seconds_left -= 1
        timer_label.config(text=f"Time left: {seconds_left} seconds")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

timer_label = tk.Label(root, text=f"Time left: {seconds_left} seconds",)
def click():
    global seconds_left
    seconds_left = 60
    update_timer()

# pack stuff
timer_label.pack()
#text_label.config(text="Words to type: ").pack()
text_widget.pack()
#typed_label.config(text="Next char to type: ").pack()
typed_widget.pack()

# capture the keys
root.bind('<KeyPress>', sendKeys)
root.mainloop()

