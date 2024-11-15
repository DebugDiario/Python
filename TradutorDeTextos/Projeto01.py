# Importando as bibliotecas necessárias
import tkinter as tk  # Biblioteca para a criação de interfaces gráficas
from tkinter import filedialog, messagebox  # Componentes de diálogo e mensagens do tkinter
from deep_translator import GoogleTranslator  # Biblioteca para tradução de texto

# Função para centralizar a janela na tela
def centralizar_janela(root, largura, altura):
    # Calcula a largura e a altura da tela do usuário
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    # Calcula as coordenadas para posicionar a janela no centro da tela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    # Define a geometria da janela para centralizá-la
    root.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para traduzir o texto inserido pelo usuário
def traduzir_texto():
    # Obtém o texto inserido no widget de entrada de texto
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    if not texto_original:  # Verifica se o texto está vazio
        messagebox.showerror("Erro", "Por favor, insira um texto para traduzir.")
        return

    # Obtém o idioma de destino selecionado pelo usuário
    idioma_destino = combo_idiomas.get()
    try:
        # Realiza a tradução usando a biblioteca GoogleTranslator
        traducao = GoogleTranslator(source='auto', target=idioma_destino).translate(texto_original)
        # Limpa o widget de saída de texto e insere a tradução
        saida_texto.delete(1.0, tk.END)
        saida_texto.insert(tk.END, traducao)
    except Exception as e:  # Captura erros e exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Erro ao traduzir: {e}")

# Função para carregar um arquivo de texto e exibir o conteúdo na entrada de texto
def carregar_arquivo():
    # Abre a caixa de diálogo para selecionar um arquivo de texto
    arquivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not arquivo:  # Verifica se o arquivo foi selecionado
        return
    try:
        # Lê o conteúdo do arquivo e exibe na entrada de texto
        with open(arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
            entrada_texto.delete(1.0, tk.END)
            entrada_texto.insert(tk.END, texto)
    except Exception as e:  # Captura erros ao carregar o arquivo e exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

# Função para salvar o texto traduzido em um arquivo
def salvar_arquivo():
    # Obtém o texto traduzido do widget de saída de texto
    texto_traduzido = saida_texto.get("1.0", tk.END).strip()
    if not texto_traduzido:  # Verifica se o texto traduzido está vazio
        messagebox.showerror("Erro", "Não há texto traduzido para salvar.")
        return
    # Abre a caixa de diálogo para salvar o arquivo de texto
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not arquivo:  # Verifica se o arquivo foi selecionado
        return
    try:
        # Salva o texto traduzido no arquivo
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write(texto_traduzido)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
    except Exception as e:  # Captura erros ao salvar o arquivo e exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela principal do tkinter
root = tk.Tk()
root.title("Tradutor de Textos")  # Define o título da janela

# Define a largura e altura da janela e a centraliza
largura = 1000
altura = 500
centralizar_janela(root, largura, altura)  # Chama a função para centralizar a janela

# Define a cor de fundo da janela
root.config(bg="#2C2C2C")

# Desabilita a opção de maximizar a janela
root.resizable(False, False)

# Criação de um frame que será usado para dividir a interface em seções
frame = tk.Frame(root, bg="#2C2C2C")
frame.pack(fill=tk.BOTH, expand=True)

# Configuração do painel central onde ficam os widgets principais
panel_central = tk.Frame(frame, bg="#2C2C2C")
panel_central.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Widget de entrada de texto onde o usuário digita o texto a ser traduzido
entrada_texto = tk.Text(panel_central, height=10, wrap=tk.WORD, font=("Arial", 12), bd=2, relief="solid", padx=10, pady=10, bg="#3E3E3E", fg="white")
entrada_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Menu de seleção de idiomas
idiomas = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh-cn', 'ja', 'ar']  # Lista de idiomas suportados
combo_idiomas = tk.StringVar(root)
combo_idiomas.set('en')  # Define o idioma padrão como inglês
idioma_menu = tk.OptionMenu(panel_central, combo_idiomas, *idiomas)
idioma_menu.config(font=("Arial", 12), bg="#4CAF50", fg="white", anchor="w")
idioma_menu.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Botão para iniciar a tradução
btn_traduzir = tk.Button(panel_central, text="Traduzir", command=traduzir_texto, font=("Arial", 14), bg="#4CAF50", fg="white", relief="solid", anchor="w")
btn_traduzir.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Botão para carregar um arquivo de texto
btn_carregar = tk.Button(panel_central, text="Carregar Arquivo", command=carregar_arquivo, font=("Arial", 14), bg="#2196F3", fg="white", relief="solid", anchor="w")
btn_carregar.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Botão para salvar o texto traduzido em um arquivo
btn_salvar = tk.Button(panel_central, text="Salvar Arquivo", command=salvar_arquivo, font=("Arial", 14), bg="#FF9800", fg="white", relief="solid", anchor="w")
btn_salvar.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

# Configuração do painel direito para exibir a saída do texto traduzido
panel_direito = tk.Frame(frame, bg="#333333", width=300)
panel_direito.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

# Widget de saída de texto onde o resultado da tradução é exibido
saida_texto = tk.Text(panel_direito, height=10, wrap=tk.WORD, font=("Arial", 12), bd=2, relief="solid", padx=10, pady=10, bg="#3E3E3E", fg="white")
saida_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Configuração dos pesos das colunas para permitir responsividade
frame.grid_columnconfigure(0, weight=3)  # A coluna do painel central tem mais peso
frame.grid_columnconfigure(1, weight=1)  # A coluna do painel direito tem menos peso

# Configuração dos pesos das linhas para a distribuição vertical
panel_central.grid_rowconfigure(0, weight=1)
panel_direito.grid_rowconfigure(0, weight=1)

# Inicia o loop principal da interface gráfica
root.mainloop()
