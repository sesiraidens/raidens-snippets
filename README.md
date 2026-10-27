<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="140">

# raidens-snippets

**Trechos de código prontos para Arduino e Python, do sensor ao sketch completo**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D?style=flat-square&logo=arduino&logoColor=white)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-D9333B?style=flat-square)

[Sobre](#sobre) · [Instalação](#instalação) · [Catálogo](#catálogo) · [Uso](#uso) · [Contribuindo](#adicionando-um-snippet)

</div>

---

## Sobre

O **raidens-snippets** é a "gaveta de ferramentas" da equipe: pedaços de código curtos, testados e prontos para copiar. Quando alguém precisa ler um MPU6050 ou montar um PID rápido no Arduino, começa daqui em vez de buscar na internet.

Todos os snippets ficam como texto dentro de `src/snippets.py`, o que permite listá-los, imprimi-los ou exportá-los de uma vez com um script.

## Instalação

```bash
git clone https://github.com/sesiraidens/raidens-snippets.git
cd raidens-snippets
```

## Catálogo

### Arduino

| Chave | Conteúdo |
|---|---|
| `ultrassonico` | Leitura do HC-SR04 |
| `ir_simples` | Sensor IR individual |
| `ir_matriz` | Matriz de 5 sensores IR |
| `mpu6050` | Acelerômetro e giroscópio |
| `motor_dc` | Motor DC com L298N |
| `diferencial` | Controle diferencial de dois motores |
| `servo` | Servo motor |
| `encoder` | Encoder com interrupção |
| `pid_arduino` | PID em C++ |
| `template_arduino` | Sketch completo: 5 IR, PID, L298N e ultrassônico |

### Python

| Chave | Conteúdo |
|---|---|
| `pid_simples` | Classe PID mínima |
| `leitura_ir` | Sensor IR com média móvel |
| `filtragem` | Média móvel, filtro mediano e suavização exponencial |
| `timer` | Cronômetro com `elapsed` e `reset` |
| `limitador` | `limitar` e `suavizar` valores |
| `log` | Logger simples em arquivo |

## Uso

```python
from src.snippets import obter_snippets, SNIPPET_PID_SIMPLES

print(SNIPPET_PID_SIMPLES)

for nome, codigo in obter_snippets().items():
    print(f"\n=== {nome} ===\n{codigo}")
```

Para exportar tudo para um arquivo:

```python
from src.snippets import obter_snippets

with open("todos_snippets.txt", "w", encoding="utf-8") as f:
    for nome, codigo in obter_snippets().items():
        f.write(f"\n{'=' * 60}\n{nome.upper()}\n{'=' * 60}\n\n{codigo}")
```

O `template_arduino` é o melhor ponto de partida para um robô novo: copie, ajuste os pinos para o seu hardware e carregue.

## Adicionando um snippet

1. Crie uma constante `SNIPPET_NOME` em `src/snippets.py`.
2. Registre-a no dicionário retornado por `obter_snippets()`.
3. Acrescente uma linha na tabela do catálogo acima.

## Estrutura

```text
raidens-snippets/
└── src/
    └── snippets.py   # Snippets como texto e a função obter_snippets()
```

## Ecossistema RAIDENS

Este repositório faz parte de um conjunto de bibliotecas da equipe. Elas usam os mesmos nomes de classes e convenções, então o que você aprende em uma serve nas outras.

| Repositório | Para quê |
|---|---|
| [`raidens-python`](https://github.com/sesiraidens/raidens-python) | Biblioteca principal em Python: sensores, motores e robôs prontos (seguidor, parede, resgate) |
| [`raidens-arduino`](https://github.com/sesiraidens/raidens-arduino) | As mesmas abstrações em C++ para rodar direto no Arduino |
| [`raidens-sensores`](https://github.com/sesiraidens/raidens-sensores) | Catálogo completo de sensores com calibração e filtragem |
| [`raidens-motores`](https://github.com/sesiraidens/raidens-motores) | Motores DC, servo, passo, driver L298N e rodas mecanum |
| [`raidens-pid`](https://github.com/sesiraidens/raidens-pid) | Controladores PID, PID avançado, cascata e sintonia Ziegler-Nichols |
| [`raidens-opencv`](https://github.com/sesiraidens/raidens-opencv) | Visão computacional: cores, linhas e navegação por câmera |
| [`raidens-lab`](https://github.com/sesiraidens/raidens-lab) | Calibração interativa de cores em HSV e LAB |
| [`raidens-obr`](https://github.com/sesiraidens/raidens-obr) | Robô completo para a OBR, integrando sensores, motores e missões |
| [`raidens-electronics`](https://github.com/sesiraidens/raidens-electronics) | Cálculos e modelos de componentes eletrônicos |
| [`raidens-3d`](https://github.com/sesiraidens/raidens-3d) | Peças 3D paramétricas geradas em OpenSCAD |
| [`raidens-ros`](https://github.com/sesiraidens/raidens-ros) | Estrutura de nodes e tópicos ROS 2 |

---

<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="56">

**Equipe RAIDENS** · SESI 192 Alumínio/SP

[![Email](https://img.shields.io/badge/Email-sesiraidens%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sesiraidens@gmail.com)
[![Linktree](https://img.shields.io/badge/Linktree-sesiraidens-39E06B?style=flat-square&logo=linktree&logoColor=white)](https://linktr.ee/sesiraidens)
[![GitHub](https://img.shields.io/badge/GitHub-sesiraidens-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sesiraidens)

<sub>Desenvolvido pela equipe RAIDENS para fins educacionais. Licenciado sob MIT.</sub>

</div>







