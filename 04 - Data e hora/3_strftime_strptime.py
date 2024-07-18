from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-07-18 12:30"
mascara_ptbr = "%d/%m/%Y"
mascara_en = "%Y-%m-%d  %H:%M"

# Converte objeto para uma strig coforme um formato fornecido.

print(data_hora_atual.strftime(mascara_ptbr))

# Interpreta uma string como um objeto datetime dado um formato correspondente.

print(datetime.strptime(data_hora_str, mascara_en))