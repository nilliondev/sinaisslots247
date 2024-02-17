import time
import random
import telebot
from datetime import datetime

api_key = '6708073683:AAHitdZgzqX74y6nS7-L8PTgAcAvVqJ4DaI'  # Substitua pelo seu próprio token
chat_id = '-1002029417054'  # Substitua pelo ID do seu canal

bot = telebot.TeleBot(token=api_key)

# Função para enviar o primeiro sinal
def send_first_signal():
    first_signal_text = '''✅[*ATENÇÃO PLATAFORMA NOVA!*](https://kfbbb.com/?id=43123740) 
⭐️ ANALISAMOS TODOS OS JOGOS DA PG SOFT! 
⭐️ ENVIAMOS APENAS OS QUE TEM CHANCE DE PAGAR!  
💻 PLATAFORMA NOVA PAGA MUITOOOO!'''

    # Envia o primeiro sinal para o canal
    bot.send_message(chat_id=chat_id, text=first_signal_text, parse_mode='Markdown')

    # Aguarda 30 segundos antes de enviar o próximo sinal
    time.sleep(600)

# Função para enviar o segundo sinal
def send_second_signal():
    # Lista de imagens e seus respectivos nomes
    images = {
        "jungle-delight.png": "Jungle Delight",
        "phoenix-rises.png": "Phoenix Rises",
        "the-great-icescape.png": "The Great Icescape",
        "bikiniparadise.png": "Bikini Paradise",
        "captains-bounty.png": "Captain's bounty",
        "double-fortune.png": "Double Fortune",
        "dragon-tiger-luck.png": "Dragon Tiger Luck",
        "fortune-gods.png": "Fortune Gods",
        "fortune-ox.png": "Fortune Ox",
        "fortune-mouse.png": "Fortune Mouse",
        "fortune-rabbit.png": "Fortune Rabbit",
        "ganesha-gold.png": "Ganesha Gold",
        "genies-3-wishes.png": "Genie's 3 Wishes",
        "leprechauns-vault.png": "Leprechauns Vault",
        "lucky-fortunes.png": "Lucky Fortunes",
        "lucky-neko.png": "Lucky Neko",
        "lucky-piggy.png": "Lucky Piggy",
        "medusa.png": "Medusa",
        "mermaid-riches.png": "Mermaid Riches",
        "midas-fortune-square.png": "Midas Fortune Square",
        "muay-thai-champion.png": "Muay Thai Champion",
        "dragonhatch.png": "Dragon Hatch",
        "ganesha-fortune.png": "Ganesha Fortune",
        "piggy-gold.png": "Piggy Gold",
        "fortune-tiger.png": "Fortune Tiger",
        "queen-of-bounty.png": "Queen of Bounty",
        "super-market.png": "Super Market"
    }
    # Escolhe uma imagem aleatória
    image_path = random.choice(list(images.keys()))
    image_name = images[image_path]

    # Valores aleatórios para os parâmetros
    taxa_retorno = f"{random.uniform(89.10, 98.75):.2f}%"
    forca_maxima = random.choice(["x200", "x600", "x1000", "x5000", "x15000", "x20000", "x25000", "x50000", "x100000"])
    rodadas_turbo = random.randint(10, 18)
    rodadas_normal = random.randint(10, 18)
    repeticao = random.randint(1, 4)
    minutos = [random.randint(1, 60) for _ in range(7)]
    minutos.sort()
    minutos_str = ', '.join(map(str, minutos))


    second_signal_text = f'''🆘ATENÇÃO JOGO PAGANDO🆘
🎰 Jogo identificado: {image_name}
🔄 Taxa de Retorno: {taxa_retorno}
🎁 Forra MÁXIMA: {forca_maxima}
⚡️ Rodadas Turbo: {rodadas_turbo}
🔥 Rodadas Normal: {rodadas_normal}
🔁 Repetição: Faça no máximo {repeticao} vezes!
⏰ Minutos: {minutos_str}

[Clique aqui para entrar no jogo!](https://kfbbb.com/?id=43123740) 

🖐🏻 CONTA NOVA TEM MAIS CHANCE!
💻 PLATAFORMA NOVA PAGA DEMAIS!'''

    # Envia o segundo sinal para o canal com a imagem
    with open(image_path, 'rb') as img:
        bot.send_photo(chat_id=chat_id, photo=img, caption=second_signal_text, parse_mode='Markdown')
        
        

# Loop principal
while True:
    try:
        # Envie o primeiro sinal
        send_first_signal()

        # Envie o segundo sinal após 30 segundos
        send_second_signal()
        time.sleep(600)  # Aguarda 30 segundos antes de enviar o próximo sinal
    except Exception as e:
        print(f"Erro ao enviar sinal: {e}")

