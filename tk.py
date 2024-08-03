import tkinter as tk
import Progekt as pr
from rabota_s_failom import dobavlenie

def dan():
    sim = simptom.get()
    proga = pr.print_(pr.kay, pr.dict_, sim)
    zona.delete(0, 'end')
    zona.insert(0, proga)

def dob():
    sim = simptom.get()
    zon = zona.get()
    dobavlenie(sim, zon)
    zona.delete(0, 'end')
    zona.insert(0, 'Симптом добавлен')
    
    

window = tk.Tk()
window.title('Справочник')
window.geometry('300x330')
window.resizable(False, False)
lib1 = tk.Label(window, text='Введите симптом: ', font=15)
lib1.place(x=20, y=20)
simptom = tk.Entry(window, width=42)
simptom.place(x=20, y=50)
bat1 = tk.Button(window, text='Найти', width=6, height=1, command=dan)
bat1.place(x=20, y=80)
bat2 = tk.Button(window, text='Добавить', width=8, height=2, command=dob)
bat2.place(x=20, y=260)
lib2 = tk.Label(window, text='Зона поражения: ', font=15)
lib2.place(x=20, y=120)
lib3 = tk.Label(window, text='введите Зону поражения в нижнее окно')
lib3.place(x=20, y=210)
lib3 = tk.Label(window, text='и нажмите добавить')
lib3.place(x=20, y=230)
lib4 = tk.Label(window, text='Чтобы добавить новый пункт')
lib4.place(x=20, y=190)
zona = tk.Entry(window, width=42)
zona.place(x=20, y=150)
window.mainloop()

