import tkinter as Tk

class View:
    def __init__(self, root, model):
        
        self.model = model
        self.root = root

        # labels
        Tk.Label(root, text="correo").grid(row=0)
        Tk.Label(root, text="Entero").grid(row=1)
        Tk.Label(root, text="Real").grid(row=2)
        Tk.Label(root, text="Notación cientifica").grid(row=3)

        #verify labels
        self.texto = Tk.StringVar()
        self.correoVerificacion = Tk.Label(root)
        self.correoVerificacion.config(textvariable=self.texto)
        self.correoVerificacion.grid(row=0, column=4)

        self.texto1 = Tk.StringVar()
        self.enteroVerificacion = Tk.Label(root)
        self.enteroVerificacion.config(textvariable=self.texto1)
        self.enteroVerificacion.grid(row=1, column=4)

        self.texto2 = Tk.StringVar()
        self.realVerificacion = Tk.Label(root)
        self.realVerificacion.config(textvariable=self.texto2)
        self.realVerificacion.grid(row=2, column=4)

        self.texto3 = Tk.StringVar()
        self.notacionVerificacion = Tk.Label(root)
        self.notacionVerificacion.config(textvariable=self.texto3)
        self.notacionVerificacion.grid(row=3, column=4)
        
        #To catch the when the text onChange
        sv1 = Tk.StringVar()
        sv2 = Tk.StringVar()
        sv3 = Tk.StringVar()
        sv4 = Tk.StringVar()
        sv1.trace("w", lambda name, index, mode, sv=sv1: self.verificacionCorreo(sv))
        sv2.trace("w", lambda name, index, mode, sv=sv2: self.verificacionEntero(sv))
        sv3.trace("w", lambda name, index, mode, sv=sv3: self.verificacionReal(sv))
        sv4.trace("w", lambda name, index, mode, sv=sv4: self.verificacionNotacion(sv))

        #Entry's
        self.e1 = Tk.Entry(root, textvariable=sv1)
        self.e2 = Tk.Entry(root, textvariable=sv2)
        self.e3 = Tk.Entry(root, textvariable=sv3)
        self.e4 = Tk.Entry(root, textvariable=sv4)

        #styles
        self.e1.grid(row=0, column=2)
        self.e2.grid(row=1, column=2)
        self.e3.grid(row=2, column=2)
        self.e4.grid(row=3, column=2)

        #Buttons
        Tk.Button(root, 
                text='cerrar', 
                command=root.quit).grid(row=4, 
                                            column=3, 
                                            sticky=Tk.W, 
                                            pady=4)
        Tk.Button(root, 
                text='Borrar', command=self.clean_textfields).grid(row=4, 
                                                            column=0, 
                                                            sticky=Tk.W, 
                                                            pady=4)

    # verify method's
    def verificacionCorreo(self,sv):
        self.texto.set(self.model.verificacionCorreo(sv.get()))

    def verificacionEntero(self, sv):
        self.texto1.set(self.model.verificacionEntero(sv.get()))

    def verificacionReal(self, sv):
        self.texto2.set(self.model.verificacionReal(sv.get()))

    def verificacionNotacion(self, sv):
        self.texto3.set(self.model.verificacionNotacion(sv.get()))

    # method to clean entry's
    def clean_textfields(self):
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")
        self.e3.delete(0,"end")
        self.e4.delete(0,"end")
        self.texto.set("");
        self.texto1.set("");
        self.texto2.set("");
        self.texto3.set("");