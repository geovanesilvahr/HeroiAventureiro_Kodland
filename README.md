# 🧙‍♂️ Heroi Aventureiro

Um jogo simples em Python feito com [PGZero](https://pygame-zero.readthedocs.io/en/stable/) (Pygame Zero), onde você controla um herói que explora um mapa, enfrenta inimigos e pode atacar com a tecla `ESPAÇO`.

## 🎮 Funcionalidades

- Tela de menu com opções: Iniciar Jogo, Áudio ON/OFF e Sair.
- Geração procedural de mapa com obstáculos.
- Herói com movimentação e animação.
- Sistema de combate: ataque corpo a corpo com detecção de distância.
- Inimigos com patrulha aleatória.
- Sistema de vida (HP) para inimigos.

## 🧰 Tecnologias

- Python 3.12+
- [PGZero](https://pygame-zero.readthedocs.io/en/stable/)
- Sprites no estilo tileset retro (estilo RPG).

## 🚀 Como Rodar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/heroi-aventureiro.git
   cd heroi-aventureiro
   ```

2. Ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   venv/bin/activate   #No Windows
   ```

3. Instale o PGZero:
   ```bash
   pip install pgzero
   ```

4. Execute o jogo:
   ```bash
   pgzrun main.py
   ```

## ⌨️ Controles

- **Setas do teclado**: movimentar o herói.
- **Espaço**: atacar inimigos próximos.
- **Mouse**: clicar nos botões do menu.

## 📁 Estrutura de Arquivos

```
projeto/
├── main.py          # Arquivo principal do jogo
├── README.md        # Este arquivo
├── images/          # Pasta com os sprites do herói, inimigos e ambiente
│   └── tile_0000.png, tile_0098.png, tile_0122.png, etc.
```

## 📌 Observações

- Certifique-se de que a pasta `images/` contenha os arquivos de imagem corretos, com nomes como `tile_0000.png`, `tile_0098.png`, etc.
- As imagens devem estar no formato `.png` e ter tamanho compatível com o sistema de tiles.

## 🛠 Melhorias Futuras

- Animações completas para os personagens.
- Sons e efeitos visuais.
- Sistema de pontuação e fases.

## 🧑‍💻 Autor

Feito com ❤️ por [Geovane Silva].

---

Divirta-se e aventure-se!