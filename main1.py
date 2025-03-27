from tkinter import *
from main2 import cadastro
from search_delete import remotion
from search_delete import search
from tkinter import messagebox



class form ():
    def __init__(self, toplevel):

        self.mestre = toplevel
        self.mestre.title('Cadastro')
        self.mestre.geometry('940x540')

        self.frame = Frame(self.mestre)  


        self.label = Label(self.frame, text='Nome:', font=("Arial", 16))
        self.e = Entry(self.frame, font=("Arial", 16), width=30)

        self.label1 = Label(self.frame, text='Email:', font=("Arial", 16))
        self.f = Entry(self.frame, font=("Arial", 16), width=30)
        
        self.label2 = Label(self.frame, text='Telefone:', font=("Arial", 16))
        self.g = Entry(self.frame, font=("Arial", 16), width=30)
        
        self.btn0 = Button(self.frame, text='Cadastrar', command=self.action, font=("Arial", 16))


        self.btn1 = Button(self.frame, text='Buscar', command=self.buscar, font=("Arial", 16))

        self.btn2 = Button(self.frame, text='Deletar', command=self.remover, font=("Arial", 16))

        
        #---------------------------# 

        self.label.grid(row=0, column=0, pady=3, sticky='news')

        self.e.grid(row=0, column=1, pady=20)

        self.label1.grid(row=1, column=0, pady=3)

        self.f.grid(row=1, column=1, pady=20)

        self.label2.grid(row=2, column=0, pady=3)

        self.g.grid(row=2, column=1, pady=20)

        self.btn0.grid(row=3, column=0, pady=3)

        

        self.btn1.grid(row=3, column=1, pady=3, columnspan=2)

        self.btn2.grid(row=3, column=2, pady=3, columnspan=2)



    
        self.frame.pack()
    def clear(self):
        self.e.delete(0, 'end')
        self.f.delete(0, 'end')
        self.g.delete(0, 'end')


    def action(self):
        a = self.e.get()
        b = self.f.get()
        c = self.g.get()
        romeo = [a, b, c]
            
        if any(i == '' for i in romeo):
            messagebox.showinfo(title="Error", message="Há campos vazios !")
            self.clear()
        else:
            fox = cadastro(romeo)
            self.clear()
                     
    def buscar (self):
        a = self.e.get()
        b = self.f.get()
        c = self.g.get()

        data_search = [a, b, c]
         

        if any(i == '' for i in data_search):
            messagebox.showinfo(title="Error", message="Há campos vazios !")
            self.clear()
        else:
            rabitt = search(data_search)
            # self.clear()
        
    def remover (self):
        a = self.e.get()
        b = self.f.get()
        c = self.g.get()

        rm = [a, b, c]
        if any(i == '' for i in rm):
            messagebox.showinfo(title="Error", message="Há campos vazios !")
            self.clear()
        else:
            dog = remotion (rm)   
            self.clear()
    
        
    

def main():
    delta = Tk()
    form(delta)
    delta.mainloop()

if __name__ == "__main__":
    main()
