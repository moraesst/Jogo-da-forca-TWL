import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        
        self.categorias = {
            "Frutas": ["BANANA", "MAÇA", "UVA", "LARANJA", "ABACAXI"],
            "Animais": ["CACHORRO", "GATO", "ELEFANTE", "TIGRE", "LEÃO"],
            "Objetos": ["CADEIRA", "MESA", "COMPUTADOR", "LIVRO", "CELULAR"]
        }
        
        self.iniciar_jogo()

    def iniciar_jogo(self):
        self.categoria, self.palavra = self.escolher_palavra()
        self.acertos = set()
        self.erros = 0
        self.max_erros = 10

        self.criar_widgets()

    def escolher_palavra(self):
        categoria = random.choice(list(self.categorias.keys()))
        palavra = random.choice(self.categorias[categoria])
        return categoria, palavra

    def criar_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.master, width=400, height=300)
        self.canvas.pack()

        self.label_categoria = tk.Label(self.master, text=f"Categoria: {self.categoria}", font=("Helvética", 14))
        self.label_categoria.pack(pady=10)

        self.quadro_palavra = tk.Frame(self.master)
        self.quadro_palavra.pack()
        
        self.letras_labels = []
        for letra in self.palavra:
            label = tk.Label(self.quadro_palavra, text="_", font=("Helvética", 18))
            label.pack(side=tk.LEFT, padx=5)
            self.letras_labels.append(label)
        
        self.quadro_botoes = tk.Frame(self.master)
        self.quadro_botoes.pack()
        
        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            botao = tk.Button(self.quadro_botoes, text=letra, command=lambda l=letra: self.adivinhar_letra(l))
            botao.pack(side=tk.LEFT, padx=2, pady=2)
        
    def adivinhar_letra(self, letra):
        if letra in self.palavra:
            self.acertos.add(letra)
            self.atualizar_display_palavra()
            if self.verificar_vitoria():
                messagebox.showinfo("Parabéns!", "Você venceu!")
                self.mostrar_botao_reiniciar()
        else:
            self.erros += 1
            self.desenhar_forca()
            if self.erros == self.max_erros:
                messagebox.showinfo("Game Over", f"Você perdeu! A palavra era {self.palavra}")
                self.mostrar_botao_reiniciar()

    def atualizar_display_palavra(self):
        for idx, letra in enumerate(self.palavra):
            if letra in self.acertos:
                self.letras_labels[idx].config(text=letra)

    def verificar_vitoria(self):
        return all(letra in self.acertos for letra in self.palavra)
    
    def desenhar_forca(self):
        if self.erros == 1:
            self.canvas.create_line(20, 280, 120, 280) # Base
        elif self.erros == 2:
            self.canvas.create_line(70, 280, 70, 50) # Poste
        elif self.erros == 3:
            self.canvas.create_line(70, 50, 200, 50) # topo
        elif self.erros == 4:
            self.canvas.create_line(200, 50, 200, 100) # corda
        elif self.erros == 5:
            self.canvas.create_oval(180, 100, 220, 140) # Cabeça
        elif self.erros == 6:
            self.canvas.create_line(200, 140, 200, 200) # corpo
        elif self.erros== 7:
            self.canvas.create_line(200, 160, 180, 190) # braço esquerdo
        elif self.erros == 8:
            self.canvas.create_line(200, 160, 220, 190) # braço direito
        elif self.erros == 9:
            self.canvas.create_line(200, 200, 180, 240) # perna esquerda
        elif self.erros == 10:    
            self.canvas.create_line(200, 200, 220, 240) # perna direita

    def mostrar_botao_reiniciar(self):
        botao_reiniciar = tk.Button(self.master, text="Reiniciar Jogo", command=self.iniciar_jogo)
        botao_reiniciar.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaForca(root)
    root.mainloop()