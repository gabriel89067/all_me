
import customtkinter as customtkinter
import ctypes
from random import randint
import tkinter as tkinter
from tkinter import ttk
from customtkinter import filedialog
from tkinter import PhotoImage
from tkinter import font
import sys
import os
import re
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

#time_string = "{:02d}:{:02d}".format(mins, secs)  ///////////////////////////////////////////////////////////////////////
class MyFrame(tkinter.ScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = tkinter.Label(self,text=F"  EVENTOS LOCOMOTIVA 1175  \n" ,justify="left",font=("Arial", 15, "bold"))
        self.label.grid(row=0, column=0, padx=20)


class log_tabela(tkinter.Toplevel):
    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def __init__(sup, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        sup.geometry("800x600")
        #self.attributes("-fullscreen", True)
        sup.title("LOG EVENTOS")
        sup.iconbitmap(sup.resource_path("images/loko.ico"))
        # Criar o Treeview
        horas_tt = ['17:30:25', '17:33:47', '18:00:12', '18:04:34', '18:30:22', '18:35:44','19:00:45', '19:01:58', '19:30:25', '19:34:56', '20:00:55', '20:02:47','20:30:21', '20:35:43', '21:00:22']
        codigos=[["E000","GPS Operação concluída com sucesso"],["E0001","Erro desconhecido no módulo GPS"],
    ["E002","Erro de sistema no módulo GPS"], ["E003","Módulo GPS não inicializado"],
    ["E004","Função solicitada não implementada no GPS"],["E005","Função não suportada pelo módulo GPS"],
    ["E006","Parâmetro inválido enviado ao módulo GPS"],["E007","Falha por falta de memória no sistema GPS"],
    ["E008","Sem resposta do módulo GPS"],["E009","Erro de plataforma (hardware/software) no GPS"],
    ["E010","Tempo de resposta do GPS excedido"],["E011","Falha de dispositivo do GPS"]
    ,["E012","Informação ou recurso não encontrado no GPS"],["E013","Endereço inválido acessado no GPS"],
    ["E014","Falha temporária de operação no GPS"],["E015","Falha de autenticação de dados do GPS"],["E016","Módulo GPS ocupado, tente novamente"],
    ["E017","Nenhum dado disponível no GPS"],["E018","Dados recebidos de forma incompleta do GPS"],["E019","Operação cancelada no GPS"],
    ["E020","Erro de protocolo de comunicação com o GPS"],["E021", "Dados corrompidos recebidos do GPS"],
    ["E022", "Comando ignorado pelo módulo GPS"], ["E023", "Dados ou mensagem excedendo o tamanho permitido pelo GPS"],
    ["E024", "Função requisitada não compilada no firmware do GPS"],["E025", "Tipo de módulo GPS desconhecido ou não reconhecido"],["E026", "Sistema ligado/reiniciado"],
    ["E027", "Perda de sinal do GPS"], ["E028", "Falha encoder canal A (AFAULT)"],
    ["E029", "Falha encoder canal B (BFAULT)"],["E030", "Hora e data do sistema desatualizadas (divergente GPS)"],["E031", "Falha ao sincronizar hora e data no sistema"],
    ["E032", ""],["E033", "Configurações restauradas pelo usuário"],["E034", "LOG de dados apagados pelo usuário (nome do arquivo)"],
    ["E035", "Falha de comunicação com o nextion"],
    ["E036", "Acesso de manutenção realizado"], ["E037", "Falha de encoder (Incoerência com GPS)"]]
        textos_tt = ["Sistema ligado/reiniciado","GPS Operação concluída com sucesso"]
        # Definir os títulos das colunas
        
        #sup.grid_rowconfigure(0, weight=1)
        #sup.grid_columnconfigure(0, weight=1)
        
        sup.my_frame = MyFrame(master=sup, width=780, height=600, corner_radius=0, fg_color="transparent")
        sup.my_frame.pack(side="left", fill="both")
        sup.log = tkinter.Label(sup.my_frame, text=f"ID             DATA                     HORA           EVENTO",justify="left")
        sup.log.grid()
        f=0
        g=0
        #sup.my_frame.title("EVENTOS")
        for i in range(37):
            sup.log = tkinter.Label(sup.my_frame, text=f"{codigos[randint(0,37)][0]}        2025-03-25             {horas_tt[f]}           {codigos[randint(0,37)][1]}\n",justify="left")
            #sup.log1 = tkinter.Label(sup.my_frame, text=f"E000         {app.Dia[i]}             {horas_tt[f]}           {textos_tt[g]}\n",justify="left")
            #sup.log1 = tkinter.Label(sup.my_frame, text=f"{app.Dia[i]}",justify="left")
            #sup.log1 = tkinter.Label(sup.my_frame, text=f"{horas_tt[f]}",justify="left")
            #sup.log1 = tkinter.Label(sup.my_frame, text=f"{textos_tt[g]}\n",justify="left")
            sup.log.grid()
            if(f<14):
                f=f+1
            if(g==0):
                g=1
            else:
                g=0
        
class ToplevelWindow(tkinter.Toplevel):

    def seleciona_modo(self, new_appearance_mode: str):
        if(new_appearance_mode == "SEGUNDO"):
            app.modo_periodo = 1
            app.rage_slider = (app.numb-(app.numb%10))/10
        if(new_appearance_mode == "MINUTO"):
            app.modo_periodo = 2
            app.rage_slider = (app.numb-(app.numb%300))/300
        if(new_appearance_mode == "HORA"):
            app.modo_periodo = 3
            app.rage_slider = (app.numb-(app.numb%18000))/18000
        if(new_appearance_mode == "DIA"):
            app.modo_periodo = 4
            app.rage_slider = (app.numb-(app.numb%432000))/432000

    def change_appearance_mode_event(app, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def finalizar(self):
        app.numb = 0
        app.nome_locomotiva = "null"
        app.vector_numb = []
        app.margem_seg = []
        app.margem_min = []
        app.margem_hora = []
        app.margem_dia = []
        app.modo_periodo = 1
        app.rage_slider = 10
        app.valores = []
        app.Data = []
        app.Dia = []
        app.Hora = []
        app.Status = []
        app.Gps1 = []
        app.Gps2 = []
        app.velocidade_Gps = []
        app.Velocidade_Taco = []
        app.Alarme_min = []
        app.Alarme_max = []
        self.ax.clear()
        self.destroy()

    def printa_grafico(self,valor,tempo,inicial,str):
        self.ax.clear()
        self.ax.plot(app.vector_numb,app.velocidade_Gps, label="Velocidade do GPS")
        self.ax.plot(app.vector_numb,app.Velocidade_Taco, label="Velocidade do Taco")
        #self.ax.plot(app.velocidade_Gps, label="Velocidade do GPS") 
        #self.ax.plot(app.Velocidade_Taco, label="Velocidade do Taco")
        self.ax.legend()
        #self.ax.set_title("Gráfico de Velocidades")
        self.ax.set_xlabel(str)
        self.ax.set_ylabel("m/s")
        if(inicial == 1):
            self.ax.set_xlim(0, tempo)
        if(inicial == 0):
            self.ax.set_xlim(valor-tempo,valor)
        self.canvas.draw()

    def slider_event(self,valor):
        #variable_string = ""
        
        self.q8_s.set('{value}'.format(value = app.Dia[int(valor)]))
        self.q9_s.set('{value}'.format(value = app.Hora[int(valor)]))
        self.q10_s.set('{value}'.format(value = app.Status[int(valor)]))
        self.q11_s.set('{value}'.format(value = app.velocidade_Gps[int(valor)]))
        self.q12_s.set('{value}'.format(value = app.Velocidade_Taco[int(valor)]))
        self.q13_s.set('{value}'.format(value = app.Alarme_max[int(valor)]))
        self.q14_s.set('{value}'.format(value = app.Alarme_min[int(valor)]))

        if(app.Status[int(valor)] == "V"):
            self.q12.config(background="#FF0000")
        else:
            self.q12.config(background="#00FF00")
            self.marker_Final.set_position(app.Gps1[int(valor)],app.Gps2[int(valor)])

        if(app.Alarme_max[int(valor)] == "1"):
            self.q15.config(background="#FF0000")
        else:
            self.q15.config(background="#EFF0F0")

        if(app.Alarme_min[int(valor)] == "1"):
            self.q16.config(background="#FF0000")
        else:
            self.q16.config(background="#EFF0F0")

        #self.caminho.set_position_list([self.marker_inicial.position, self.marker_Final.position])
        if(app.modo_periodo == 1):
            if(valor%5 == 0):
                if(valor == 0):
                    self.printa_grafico(valor,5,1,"Segundos")
                if(valor >= 5):
                    self.printa_grafico(valor,5,0,"Segundos")
        if(app.modo_periodo == 2):
            if(valor%300 == 0):
                if(valor == 0):
                    self.printa_grafico(valor,300,1,"Minutos")
                if(valor >= 300):
                    self.printa_grafico(valor,300,0,"Minutos")
        if(app.modo_periodo == 3):
            if(valor%18000 == 0):
                if(valor == 0):
                    self.printa_grafico(valor,18000,1,"Horas")
                if(valor >= 18000):
                    self.printa_grafico(valor,18000,0,"Horas")
        if(app.modo_periodo == 4):
            if(valor%432000 == 0):
                
                if(valor == 0):
                    self.printa_grafico(valor,432000,1,"Dias")
                if(valor >= 10):
                    self.printa_grafico(valor,432000,0,"Dias")
        
    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def tabela_log(self):
        if app.toplevel_window is None or not app.toplevel_window.winfo_exists():
            app.toplevel_window = log_tabela(app) 
            print("dd")
        else:
            app.toplevel_window = log_tabela(app)
            app.toplevel_window.focus()
            print("dd2")

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        #self.attributes("-fullscreen", True)
        self.state("zoomed")
        
        #self.geometry("1366x768")
        script_directory = os.path.dirname(os.path.abspath(__file__))
        mapa_off = os.path.join(script_directory, self.resource_path("offline_tiles_10.db"))
        self.nome_descricao = f"LOG Locomotiva : {app.nome_locomotiva}, data : {app.log_data}."      
        self.title(self.nome_descricao)
        self.iconbitmap(self.resource_path("images/loko.ico"))
        self.top_frame_t = tkinter.Frame(self,borderwidth=1,highlightcolor='#808080',relief='ridge',highlightthickness=1)
        self.top_frame_t.pack(side="top", fill="both")
        #self.top_frame = tkinter.Frame(self,background="#808080")
        #self.top_frame.pack(side="top", fill="none",ipady=(10),pady=(0,0))
        self.q7_s = tkinter.Variable(self, app.nome_locomotiva)
        self.q8_s = tkinter.Variable(self, app.Dia[int(app.numb/2)])
        self.q9_s = tkinter.Variable(self, app.Hora[int(app.numb/2)])
        self.q10_s = tkinter.Variable(self, app.Status[int(app.numb/2)])
        self.q11_s = tkinter.Variable(self, app.velocidade_Gps[int(app.numb/2)])
        self.q12_s = tkinter.Variable(self, app.Velocidade_Taco[int(app.numb/2)])
        self.q13_s = tkinter.Variable(self, app.Alarme_max[int(app.numb/2)])
        self.q14_s = tkinter.Variable(self, app.Alarme_min[int(app.numb/2)])
        self.q15_s = tkinter.Variable(self, app.Alarme_min[int(app.numb/2)])
        self.q16_s = tkinter.Variable(self, app.Alarme_min[int(app.numb/2)])
        self.q17_s = tkinter.Variable(self, app.Alarme_min[int(app.numb/2)])
        

        self.q1 = tkinter.Label(self.top_frame_t, text="LOCOMOTIVA:", height=3,width=12,font=("Arial", 11, "bold"),anchor="w",justify="left")
       # self.q1.place(x=0,y=0,width=140,height=60)
        self.q2 = tkinter.Label(self.top_frame_t, text="DIA:", height=3,width=12,font=("Arial", 11, "bold"),anchor="w",justify="left")
       # self.q2.place(x=0,y=60,width=50,height=60)
        self.q3 = tkinter.Label(self.top_frame_t, text="HORA:", height=3,width=8,font=("Arial", 11, "bold"),anchor="w")
        #self.q3.place(x=310,y=0,width=70,height=60)
        self.q4 = tkinter.Label(self.top_frame_t, text="STATUS:", height=3,width=8,font=("Arial", 11, "bold"),anchor="w")
       # self.q4.place(x=220,y=60,width=100,height=60)
        self.q5 = tkinter.Label(self.top_frame_t, text="VELOCIDADE GPS:", height=3,width=20,font=("Arial", 11, "bold"),anchor="w")
       # self.q5.place(x=550,y=0,width=170,height=60)
        self.q6 = tkinter.Label(self.top_frame_t, text="VELOCIDADE ENCODER:", height=3,width=20,font=("Arial", 11, "bold"),anchor="w")
       # self.q6.place(x=490,y=60,width=180,height=60)
        self.q7 = tkinter.Label(self.top_frame_t, text="LIMITE 1:", height=3,width=10,font=("Arial", 11, "bold"),anchor="w")
       # self.q7.place(x=890,y=0,width=140,height=60)
        self.q8 = tkinter.Label(self.top_frame_t, text="LIMITE 2:", height=3,width=10,font=("Arial", 11, "bold"),anchor="w")
        #self.q8.place(x=840,y=60,width=140,height=60)
        self.q8_1 = tkinter.Label(self.top_frame_t, text="GPS/ENC:", height=3,width=11,font=("Arial", 11, "bold"),anchor="w")
        self.q8_2 = tkinter.Label(self.top_frame_t, text="FALHA A:", height=3,width=11,font=("Arial", 11, "bold"),anchor="w")
        self.q8_3 = tkinter.Label(self.top_frame_t, text="FALHA B:", height=3,width=8,font=("Arial", 11, "bold"),anchor="w")


        self.q9 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q7_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q9.place(x=140,y=0,width=170,height=60)
        self.q10 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q8_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q10.place(x=50,y=60,width=170,height=60)
        self.q11 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q9_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q11.place(x=380,y=0,width=170,height=60)
        self.q12 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q10_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q12.place(x=320,y=60,width=170,height=60)
        self.q13 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q11_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q13.place(x=720,y=0,width=170,height=60)
        self.q14 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q12_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q14.place(x=670,y=60,width=170,height=60)
        self.q15 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q13_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q15.place(x=1030,y=0,width=170,height=60)
        self.q16 = tkinter.Label(self.top_frame_t,text="Data :",textvariable = self.q14_s, height=3,width=16,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        #self.q16.place(x=980,y=60,width=170,height=60)
        self.q17 = tkinter.Label(self.top_frame_t,text="Fonte atual :",textvariable = self.q15_s, height=3,width=15,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        self.q18 = tkinter.Label(self.top_frame_t,text="Falha A:",textvariable = self.q16_s, height=3,width=15,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)
        self.q19 = tkinter.Label(self.top_frame_t,text="Falha B:",textvariable = self.q17_s, height=3,width=14,background="#EFF0F0",highlightcolor='#808080',borderwidth=2,relief='ridge',highlightthickness=1)


        #self.top_frame_t.columnconfigure([0, 7], weight=1)  
        #self.top_frame_t.rowconfigure([0, 1], weight=1) 
        tkinter.Button()
        self.button1 = customtkinter.CTkButton(master=self, text="Relatório",command=self.tabela_log, fg_color = "#C7252A",height=58,width=180)
        self.button1.place(x=1183, y=63)
        self.q1.grid(row=0, column=0, sticky="nsew")  
        self.q2.grid(row=1, column=0, sticky="nsew")  
        self.q3.grid(row=0, column=2, sticky="nsew") 
        self.q4.grid(row=1, column=2, sticky="nsew")  
        self.q5.grid(row=0, column=4, sticky="nsew") 
        self.q6.grid(row=1, column=4, sticky="nsew")
        self.q7.grid(row=0, column=6, sticky="nsew")  
        self.q8.grid(row=1, column=6, sticky="nsew")  
        self.q9.grid(row=0, column=1, sticky="nsew") 
        self.q10.grid(row=1, column=1, sticky="nsew")  
        self.q11.grid(row=0, column=3, sticky="nsew") 
        self.q12.grid(row=1, column=3, sticky="nsew")
        self.q13.grid(row=0, column=5, sticky="nsew") 
        self.q14.grid(row=1, column=5, sticky="nsew")  
        self.q15.grid(row=0, column=7, sticky="nsew") 
        self.q16.grid(row=1, column=7, sticky="nsew")
        self.q8_1.grid(row=0, column=8, sticky="nsew") 
        self.q8_2.grid(row=1, column=8, sticky="nsew")
        self.q17.grid(row=0, column=9, sticky="nsew")
        self.q18.grid(row=1, column=9, sticky="nsew") 
        self.q8_3.grid(row=0, column=10, sticky="nsew")
        self.q19.grid(row=0, column=11, sticky="nsew")

        
        

        #.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        #self.label.pack(padx=20, pady=20,expand=False)
        self.top_frame_gr = customtkinter.CTkFrame(self,height=900)
        self.top_frame_gr.pack(side="top",fill="both",expand = True)

        self.fig = Figure(figsize=(6.8, 4.3),dpi=100)
        self.ax = self.fig.subplots()  # Criando apenas uma vez
        #self.t = np.arange(0, app.numb, 1)
        self.line, = self.ax.plot(app.vector_numb,app.velocidade_Gps, label="Velocidade do GPS")
        self.line, = self.ax.plot(app.vector_numb,app.Velocidade_Taco, label="Velocidade do Taco")
        #self.ax.legend()
        #self.ax.set_title("Gráfico de Velocidades")
        self.ax.set_xlabel("segundos")
        self.ax.set_ylabel("m/s",fontsize=12)
        #self.fig.subplots().plot(app.velocidade_Gps, label="Velocidade")
        #self.fig.legend()
        self.ax.legend()
        #self.fig.subplots().set_title("Gráfico de Velocidade")
        

        self.top_frame = customtkinter.CTkFrame(self,border_width=2)
        self.top_frame.pack(side="bottom", fill="both")
        #self.top_frame.place(relx=0,rely=0.8)
        
        self.slider_1 = customtkinter.CTkSlider( self.top_frame, from_=0, to=(app.numb-app.numb%10), number_of_steps=app.rage_slider,button_color = "#C7252A",command=self.slider_event)
        self.slider_1.pack(side="right",expand=True,fill="both",pady=(50,35),padx=(0,0),ipadx=(500))
        self.titulo_label_map = customtkinter.CTkLabel(self.top_frame_gr, text="Mapa Interativo", font=("Arial", 15, "bold"))
        self.titulo_label_graf = customtkinter.CTkLabel(self.top_frame_gr, text="Gráfico de Velocidades", font=("Arial", 15, "bold"))
        self.titulo_label_perio = customtkinter.CTkLabel(self.top_frame, text="Período", font=("Arial", 14, "bold"))
        self.titulo_label_linha = customtkinter.CTkLabel(self.top_frame, text="Linha do Tempo", font=("Arial", 14, "bold"))

        self.titulo_label_perio.place(relx=0,rely=0.2)
        self.titulo_label_linha.place(relx=0.18,rely=0.2)
        self.titulo_label_graf.place(relx=0.2,y=0)  
        self.titulo_label_map.place(relx=0.73,y=0)  
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu( self.top_frame,values=["SEGUNDO","MINUTO","HORA", "DIA"], fg_color = "#C7252A",button_color =  "#C7252A",
                                                                               command=self.seleciona_modo)
        self.appearance_mode_optionemenu.pack(side="right",expand=True,fill="both",pady=(50,35),ipadx=(0))
        print(mapa_off)

        self.map_widget = TkinterMapView(self.top_frame_gr, width=680, height=430,use_database_only=False,max_zoom=13,database_path=mapa_off)

        self.map_widget.pack(side="right",fill="both",expand=True,padx=(0, 0), pady=(35, 0))

        self.map_widget.set_position(app.Gps1[app.numb-1],app.Gps2[app.numb-1]) 
        self.map_widget.set_zoom(12)
        self.marker_inicial =  self.map_widget.set_marker(app.Gps1[0],app.Gps2[0], text="Inicial")
        self.caminho = self.map_widget.set_path([self.marker_inicial.position,(app.Gps1[1],app.Gps2[1])])
        for i in range(app.numb):
            if(app.Status[i] == "A"):
                self.caminho.add_position(app.Gps1[i],app.Gps2[i])
        self.marker_Final =  self.map_widget.set_marker(app.Gps1[int(app.numb/2)],app.Gps2[int(app.numb/2)], text="Final")
        #self.caminho = self.map_widget.set_path([self.marker_inicial.position, self.marker_Final.position])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.top_frame_gr)  
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="left", fill=tkinter.BOTH, expand=True, padx=(0, 6),pady=(35,0))
        self.slider_1.set(0)
        if(app.real == 0):
            self.slider_event(0)
            app.real = 1
        
        self.protocol("WM_DELETE_WINDOW", self.finalizar)
        # # load images in PhotoImage object
        
        # tor_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "python", "tor.jpg")).resize((300, 200)))
        # airport_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "python", "airport.jpg")).resize((300, 200)))


        # # create marker through .set_address() with image, which is visible at zoom levels 14 to infinity
        # marker_1 = map_widget.set_address("Brandenburger Tor", marker=True, image=tor_image, image_zoom_visibility=(14, float("inf")))

        # # make image visible/invisible when marker is clicked
        # def click_airport_marker_event(marker):
        #     print("marker clicked:", marker.text)
        #     if marker.image_hidden is True:
        #         marker.hide_image(False)
        #     else:
        #         marker.hide_image(True)


class App(customtkinter.CTk):
    windo = 0
    real = 0
    numb = 0
    nome_locomotiva = "null"
    vector_numb = []
    margem_seg = []
    margem_min = []
    margem_hora = []
    margem_dia = []
    modo_periodo = 1
    rage_slider = 10
    valores = []
    Data = []
    Dia = []
    Hora = []
    Status = []
    Gps1 = []
    Gps2 = []
    velocidade_Gps = []
    Velocidade_Taco = []
    Alarme_min = []
    Alarme_max = []
    Fonte_atual = []
    Afault = []
    Bfault = []
    log_data = ""
    toplevel_window = None

    def convert_coordenada(set,coordenada):
        if(len(coordenada)==12):
            match = re.match(r"(\d{2})(\d{2})\.(\d+) (\w)", coordenada)
        if(len(coordenada)==13):
            match = re.match(r"(\d{1})(\d{2})(\d{2})\.(\d+) (\w)", coordenada)
            
        if match and (len(coordenada)==13):
            number1 = match.group(2)  
            number2 = match.group(3) 
            number3 = match.group(4)
            variav = match.group(5) 
        if match and (len(coordenada)==12):
            number1 = match.group(1)  
            number2 = match.group(2) 
            number3 = match.group(3)
            variav = match.group(4)  
        if(variav == "S" or variav == "W"):
            return (-1)*(float(number1) + (float(number2)/60) + (float(number3)/6000000))

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
           self.toplevel_window = ToplevelWindow(self)  
        else:
            self.toplevel_window.focus() 

    def change_appearance_mode_event(app, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
                                          
    def button_function(app):
    
        filename = filedialog.askopenfilename()
        match1 = re.search(r"LOC(.*?)-",filename)
        app.nome_locomotiva = match1.group(1)
        match2 = re.search(r"-(.*?).txt",filename)
        match3 = re.match(r"(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})",match2.group(1))
        app.log_data = f"{match3.group(1)}/{match3.group(2)}/{match3.group(3)} às {match3.group(4)}:{match3.group(5)}:{match3.group(6)}"
        if(filename != ""):
            with open(filename, 'r') as file:
      
                for line in file:
                    #print(line.strip())  # strip() removes the newline character
                    app.valores.append(line.strip())
                    app.dados = line.strip().split(";")
                    app.Data.append(app.dados[0])
                    divid1 = app.Data[app.numb].split("T")
                    app.Dia.append(divid1[0])
                    divid2 = divid1[1].split("Z")
                    app.Hora.append(divid2[0])
                    #Hora.append(dados[1])
                    app.Status.append(app.dados[1])
                    if(app.dados[1] == "A"):
                        app.Gps1.append(app.convert_coordenada(app.dados[2]))
                        app.Gps2.append(app.convert_coordenada(app.dados[3]))
                        app.velocidade_Gps.append(int(app.dados[4]))
                    else:
                        app.Gps1.append(0)
                        app.Gps2.append(0)
                        app.velocidade_Gps.append(None)
                    app.Velocidade_Taco.append(int(app.dados[5]))
                    app.Alarme_min.append(app.dados[6])
                    app.Alarme_max.append(app.dados[7])
                    #app.Fonte_atual.append(app.dados[8])
                    #app.Afault.append(app.dados[9])
                    #app.Afault.append(app.dados[10])
                    #print(dados)
                    app.vector_numb.append(int(app.numb))
                    app.numb = app.numb + 1
            #print(numb)
            app.rage_slider = (app.numb-(app.numb%10))/10
            if app.toplevel_window is None or not app.toplevel_window.winfo_exists():
                app.toplevel_window = ToplevelWindow(app) 
            else:
                app.toplevel_window.focus()
        else:
            aviso = tkinter.Label(app, text="Arquivo Inválido")
            aviso.pack()

    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #app.home_frame = tkinter.Frame(app, corner_radius=0, fg_color= "#C7252A")
        #app.home_frame.grid_columnconfigure(0, weight=1)
        
        #master = customtkinter.CTk()  
        #app.configure(bg="#242424")
        customtkinter.set_appearance_mode("light")
        app.geometry("400x440")
        
        #ttk.Style.theme_use('default')
        app.mycont = tkinter.Frame(master=app)
        app.mycont.pack()
        app.title("PUR")

       # set grid layout 1x2
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)
        

       # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "python")
        # app.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logomin.png")), size=(26, 326))
        #imagen = Image.open("C:/Users/gabri/Documents/python/python/loko.png")
        #app.icon = PhotoImage(file="C:/Users/gabri/Documents/python/python/loko.png")
        #ctk_image = customtkinter.CTkImage(light_image=imagen, dark_image=imagen, size=(100, 100))
        #app.iconphoto(False, app.icon)
        app.iconbitmap(app.resource_path("images/loko.ico"))
        foto = customtkinter.CTkImage(Image.open(app.resource_path("images/logo.png")), size=(300, 150))
        app.foto_barra = customtkinter.CTkLabel(master=app,image=foto,text="")
        app.foto_barra.pack()
        # Use CTkButton instead of tkinter Button
        app.button = customtkinter.CTkButton(master=app, text="Gerar Análise", command=app.button_function, fg_color = "#C7252A")
        app.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        app.button1 = customtkinter.CTkButton(master=app, text="Finalizar",command=app.quit, fg_color = "#C7252A")
        app.button1.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        app.appearance_mode_label = customtkinter.CTkLabel(master=app,text="Modo:", anchor="w",)
        app.appearance_mode_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        app.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=app,values=["Light", "Dark", "System"], fg_color = "#C7252A",button_color =  "#C7252A",
                                                                               command=app.change_appearance_mode_event)
        app.appearance_mode_optionemenu.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        
        
        

     
# slider_1 = customtkinter.CTkSlider(master=app, from_=0, to=1, number_of_steps=4,button_color = "#C7252A")
# slider_1.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


app = log_tabela()
app.mainloop()

