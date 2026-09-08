<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" width="80">

# raidens-snippets

Colecao de snippets e templates reutilizaveis para robotica.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-d9333b?style=flat)
![Status](https://img.shields.io/badge/Status-Active-2ea043?style=flat)

</div>

---

## Sobre

O **raidens-snippets** e uma colecao de trechos de codigo prontos para usar em projetos de robotica. Inclui snippets para Arduino, Python e templates de sketches.

---

## Snippets Arduino

### Sensores

| Snippet | Descricao |
|---|---|
| ultrassonico | Leitura HC-SR04 |
| ir_simples | Sensor IR individual |
| ir_matriz | Matriz de 5 sensores |
| mpu6050 | Acelerometro e giroscopio |

### Motores

| Snippet | Descricao |
|---|---|
| motor_dc | Motor DC com L298N |
| diferencial | Controle diferencial |
| servo | Servo motor |
| encoder | Encoder com interrupcao |

---

## Snippets Python

### PID

| Snippet | Descricao |
|---|---|
| pid_simples | PID basico em Python |
| pid_arduino | PID para Arduino |

### Sensores

| Snippet | Descricao |
|---|---|
| leitura_ir | Sensor IR com filtragem |
| iltragem | Media movol, mediano, exponencial |

### Utilitarios

| Snippet | Descricao |
|---|---|
| 	imer | Controle de tempo |
| limitador | Limitar e suavizar valores |
| log | Sistema de log |

---

## Uso

### Em Python

`python
from src.snippets import SNIPPET_PID_SIMPLES

print(SNIPPET_PID_SIMPLES)
`

### Listar Todos

`python
from src.snippets import obter_snippets

snippets = obter_snippets()
for nome, codigo in snippets.items():
    print(f"\n=== {nome} ===")
    print(codigo)
`

### Salvar em Arquivo

`python
from src.snippets import obter_snippets

snippets = obter_snippets()

with open("todos_snippets.txt", "w") as f:
    for nome, codigo in snippets.items():
        f.write(f"\n{'='*60}\n")
        f.write(f"{nome.upper()}\n")
        f.write(f"{'='*60}\n\n")
        f.write(codigo)
`

---

## Template Arduino

O 	emplate_arduino e um sketch completo com:
- Leitura de 5 sensores IR
- Controle PID
- Driver L298N
- Ultrassonico

Basta copiar e ajustar os pinos conforme seu hardware.

---

## Como Adicionar Snippets

1. Crie uma constante SNIPPET_NOME em snippets.py
2. Adicione ao dicionario em obter_snippets()
3. Documente na tabela acima

---

## Equipe

**RAIDENS - SESI Aluminio 192**

Desenvolvido para uso interno da equipe. Licenciado sob MIT.