import tkinter as tk
from tkinter import filedialog, messagebox
from deep_translator import GoogleTranslator

# Função para centralizar a janela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para traduzir o texto
def traduzir_texto():
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    if not texto_original:
        messagebox.showerror("Erro", "Por favor, insira um texto para traduzir.")
        return

    idioma_destino = combo_idiomas.get()
    try:
        traducao = GoogleTranslator(source='auto', target=idioma_destino).translate(texto_original)
        saida_texto.delete(1.0, tk.END)
        saida_texto.insert(tk.END, traducao)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao traduzir: {e}")

# Função para carregar o arquivo e traduzir
def carregar_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not arquivo:
        return
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
            entrada_texto.delete(1.0, tk.END)
            entrada_texto.insert(tk.END, texto)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

# Função para salvar o arquivo traduzido
def salvar_arquivo():
    texto_traduzido = saida_texto.get("1.0", tk.END).strip()
    if not texto_traduzido:
        messagebox.showerror("Erro", "Não há texto traduzido para salvar.")
        return
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not arquivo:
        return
    try:
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write(texto_traduzido)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela
root = tk.Tk()
root.title("Tradutor de Textos")
largura = 1000
altura = 500
centralizar_janela(root, largura, altura)  # Centralizar a janela ao iniciar
root.config(bg="#2C2C2C")

# Desabilitar maximização da janela
root.resizable(False, False)

# Criar um Frame para dividir a tela em 3 áreas (esquerda, central e direita)
frame = tk.Frame(root, bg="#2C2C2C")
frame.pack(fill=tk.BOTH, expand=True)

# Painel Central
panel_central = tk.Frame(frame, bg="#2C2C2C")
panel_central.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Entrada de texto
entrada_texto = tk.Text(panel_central, height=10, wrap=tk.WORD, font=("Arial", 12), bd=2, relief="solid", padx=10, pady=10, bg="#3E3E3E", fg="white")
entrada_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Seleção de idioma
idiomas = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh-cn', 'ja', 'ar']
combo_idiomas = tk.StringVar(root)
combo_idiomas.set('en')
idioma_menu = tk.OptionMenu(panel_central, combo_idiomas, *idiomas)
idioma_menu.config(font=("Arial", 12), bg="#4CAF50", fg="white", anchor="w")
idioma_menu.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Botões
btn_traduzir = tk.Button(panel_central, text="Traduzir", command=traduzir_texto, font=("Arial", 14), bg="#4CAF50", fg="white", relief="solid", anchor="w")
btn_traduzir.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

btn_carregar = tk.Button(panel_central, text="Carregar Arquivo", command=carregar_arquivo, font=("Arial", 14), bg="#2196F3", fg="white", relief="solid", anchor="w")
btn_carregar.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

btn_salvar = tk.Button(panel_central, text="Salvar Arquivo", command=salvar_arquivo, font=("Arial", 14), bg="#FF9800", fg="white", relief="solid", anchor="w")
btn_salvar.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

# Painel Direito
panel_direito = tk.Frame(frame, bg="#333333", width=300)
panel_direito.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

# Saída de texto
saida_texto = tk.Text(panel_direito, height=10, wrap=tk.WORD, font=("Arial", 12), bd=2, relief="solid", padx=10, pady=10, bg="#3E3E3E", fg="white")
saida_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Configuração dos pesos para responsividade
frame.grid_columnconfigure(0, weight=3)
frame.grid_columnconfigure(1, weight=1)

panel_central.grid_rowconfigure(0, weight=1)
panel_direito.grid_rowconfigure(0, weight=1)

# Iniciar o programa
root.mainloop()
