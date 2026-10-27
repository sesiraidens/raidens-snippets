"""
Colecao de snippets e templates para robotica.

Contem trechos de codigo reutilizaveis para Arduino e Python.
"""


# =============================================================================
# ARDUINO - SENSORES
# =============================================================================

SNIPPET_ULTRASSONICO = """
// Leitura de sensor ultrassonico HC-SR04
#define TRIGGER 9
#define ECHO 10

float medirDistancia() {
    digitalWrite(TRIGGER, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGGER, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER, LOW);
    
    long duracao = pulseIn(ECHO, HIGH, 30000);
    return duracao * 0.034 / 2.0;
}
"""

SNIPPET_IR_SIMPLES = """
// Leitura simples de sensor IR
#define IR_PIN A0
#define LIMIAR 512

bool detectarLinha() {
    int leitura = analogRead(IR_PIN);
    return leitura < LIMIAR;  // true = preto
}
"""

SNIPPET_IR_MATRIZ = """
// Leitura de matriz de 5 sensores IR
#define NUM_SENSORES 5
int pinsIR[] = {A0, A1, A2, A3, A4};
int pesos[] = {-2, -1, 0, 1, 2};

float calcularPosicao() {
    float somaPesos = 0;
    int somaLeituras = 0;
    
    for (int i = 0; i < NUM_SENSORES; i++) {
        int leitura = analogRead(pinsIR[i]);
        if (leitura < 512) {  // preto
            somaPesos += pesos[i];
            somaLeituras++;
        }
    }
    
    if (somaLeituras == 0) return 0;
    return somaPesos / somaLeituras;
}
"""

SNIPPET_MPU6050 = """
// Leitura basica do MPU6050
#include <Wire.h>

#define MPU_ADDR 0x68

void setupMPU() {
    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x6B);  // PWR_MGMT_1
    Wire.write(0);     // Zera o bit de sleep
    Wire.endTransmission(true);
}

void lerAc(float &ax, float &ay, float &az) {
    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x3B);  // ACCEL_XOUT_H
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_ADDR, 6, true);
    
    ax = (Wire.read() << 8 | Wire.read()) / 16384.0;
    ay = (Wire.read() << 8 | Wire.read()) / 16384.0;
    az = (Wire.read() << 8 | Wire.read()) / 16384.0;
}
"""


# =============================================================================
# ARDUINO - MOTORES
# =============================================================================

SNIPPET_MOTOR_DC = """
// Controle basico de motor DC com L298N
#define ENA 5
#define IN1 2
#define IN2 3

void motorFrente(int velocidade) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, velocidade);
}

void motorTras(int velocidade) {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    analogWrite(ENA, velocidade);
}

void motorParar() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 0);
}
"""

SNIPPET_DIFERENCIAL = """
// Controle diferencial de dois motores
#define ENA 5
#define IN1 2
#define IN2 3
#define ENB 6
#define IN3 4
#define IN4 7

void mover(int esq, int dir) {
    // Motor esquerdo
    if (esq >= 0) {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
    } else {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
    }
    analogWrite(ENA, abs(esq));
    
    // Motor direito
    if (dir >= 0) {
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    } else {
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    }
    analogWrite(ENB, abs(dir));
}
"""

SNIPPET_SERVO = """
// Controle de servo motor
#include <Servo.h>

Servo meuServo;

void setup() {
    meuServo.attach(11);
    meuServo.write(90);  // Centro
}

void moverServo(int angulo) {
    angulo = constrain(angulo, 0, 180);
    meuServo.write(angulo);
}
"""

SNIPPET_ENCODER = """
// Leitura de encoder com interrupcao
#define PINA 2
#define PINB 3

volatile long contador = 0;

void setup() {
    pinMode(PINA, INPUT);
    pinMode(PINB, INPUT);
    attachInterrupt(digitalPinToInterrupt(PINA), incrementar, RISING);
}

void incrementar() {
    if (digitalRead(PINB)) {
        contador++;
    } else {
        contador--;
    }
}

float velocidade(float tempoMs) {
    float rpm = (contador / 20.0) * (1000.0 / tempoMs) * 60.0;
    contador = 0;
    return rpm;
}
"""


# =============================================================================
# PYTHON - PID
# =============================================================================

SNIPPET_PID_SIMPLES = """
# PID basico em Python
class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.erro_anterior = 0
        self.integral = 0
        
    def calcular(self, setpoint, medicao):
        erro = setpoint - medicao
        self.integral += erro
        derivada = erro - self.erro_anterior
        self.erro_anterior = erro
        
        return self.kp * erro + self.ki * self.integral + self.kd * derivada
"""

SNIPPET_PID_ARDUINO = """
// PID em Arduino
float Kp = 2.5;
float Ki = 0.8;
float Kd = 0.3;

float erroAnterior = 0;
float integral = 0;

float calcularPID(float setpoint, float medicao) {
    float erro = setpoint - medicao;
    integral += erro;
    integral = constrain(integral, -50, 50);
    float derivada = erro - erroAnterior;
    erroAnterior = erro;
    
    return Kp * erro + Ki * integral + Kd * derivada;
}
"""


# =============================================================================
# PYTHON - SENSORES
# =============================================================================

SNIPPET_LEITURA_IR = """
# Leitura de sensor IR com filtragem
class SensorIR:
    def __init__(self, limiar=512):
        self.limiar = limiar
        self.historico = []
        
    def ler(self):
        import random
        valor = random.randint(0, 1023)
        self.historico.append(valor)
        if len(self.historico) > 10:
            self.historico.pop(0)
        return 0 if valor < self.limiar else 1
        
    def media_movel(self, janela=5):
        ultimos = self.historico[-janela:]
        return sum(ultimos) / len(ultimos)
"""

SNIPPET_FILTRAGEM = """
# Filtragem de sensores
def media_movel(valores, janela=5):
    if len(valores) < janela:
        return sum(valores) / len(valores)
    return sum(valores[-janela:]) / janela

def filtro_mediano(valores, janela=5):
    if len(valores) < janela:
        return sorted(valores)[len(valores)//2]
    return sorted(valores[-janela:])[janela//2]

def exponential_smoothing(valor, anterior, alpha=0.3):
    return alpha * valor + (1 - alpha) * anterior
"""


# =============================================================================
# PYTHON - UTILITARIOS
# =============================================================================

SNIPPET_TIMER = """
# Timer para controle de tempo
import time

class Timer:
    def __init__(self):
        self.inicio = time.time()
        
    def elapsed(self):
        return time.time() - self.inicio
        
    def reset(self):
        self.inicio = time.time()
        
    def elapsed_ms(self):
        return self.elapsed() * 1000
"""

SNIPPET_LIMITADOR = """
# Limitador de valores
def limitar(valor, minimo, maximo):
    return max(minimo, min(maximo, valor))

def suavizar(atual, destino, passo=0.1):
    diff = destino - atual
    if abs(diff) < passo:
        return destino
    return atual + passo * (1 if diff > 0 else -1)
"""

SNIPPET_LOG = """
# Sistema de log simples
import datetime

class Logger:
    def __init__(self, nome_arquivo="log.txt"):
        self.arquivo = nome_arquivo
        
    def log(self, mensagem, nivel="INFO"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        texto = f"[{timestamp}] [{nivel}] {mensagem}"
        print(texto)
        
        with open(self.arquivo, 'a') as f:
            f.write(texto + "\\n")
"""


# =============================================================================
# TEMPLATES
# =============================================================================

TEMPLATE_SKETCH_ARDUINO = """
/*
 * Sketch Arduino para Robo RAIDENS
 * 
 * Hardware:
 * - Arduino Uno/Nano
 * - Driver L298N
 * - 5 Sensores IR
 * - Ultrassonico HC-SR04
 */

// Pinos
#define ENA 5
#define IN1 2
#define IN2 3
#define ENB 6
#define IN3 4
#define IN4 7
#define TRIGGER 9
#define ECHO 10

// Pinos IR
int pinsIR[] = {A0, A1, A2, A3, A4};
#define NUM_SENSORES 5

// PID
float Kp = 2.5;
float Ki = 0.8;
float Kd = 0.3;
float erroAnterior = 0;
float integral = 0;

// Velocidade base
int velBase = 150;

void setup() {
    Serial.begin(9600);
    
    // Configura pinos
    pinMode(ENA, OUTPUT);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(ENB, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    pinMode(TRIGGER, OUTPUT);
    pinMode(ECHO, INPUT);
    
    for (int i = 0; i < NUM_SENSORES; i++) {
        pinMode(pinsIR[i], INPUT);
    }
    
    Serial.println("Robo RAIDENS iniciado!");
}

void loop() {
    float posicao = calcularPosicao();
    
    if (!linhaDetectada()) {
        parar();
        delay(500);
        return;
    }
    
    float erro = posicao;
    integral += erro;
    float derivada = erro - erroAnterior;
    float correcao = Kp * erro + Ki * integral + Kd * derivada;
    erroAnterior = erro;
    
    int velEsq = velBase + correcao;
    int velDir = velBase - correcao;
    
    mover(constrain(velEsq, -255, 255), constrain(velDir, -255, 255));
    
    delay(10);
}

float calcularPosicao() {
    float somaPesos = 0;
    int somaLeituras = 0;
    int pesos[] = {-2, -1, 0, 1, 2};
    
    for (int i = 0; i < NUM_SENSORES; i++) {
        if (analogRead(pinsIR[i]) < 512) {
            somaPesos += pesos[i];
            somaLeituras++;
        }
    }
    
    if (somaLeituras == 0) return 0;
    return somaPesos / somaLeituras;
}

bool linhaDetectada() {
    for (int i = 0; i < NUM_SENSORES; i++) {
        if (analogRead(pinsIR[i]) < 512) return true;
    }
    return false;
}

void mover(int esq, int dir) {
    if (esq >= 0) { digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); }
    else { digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH); }
    analogWrite(ENA, abs(esq));
    
    if (dir >= 0) { digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW); }
    else { digitalWrite(IN3, LOW); digitalWrite(IN4, HIGH); }
    analogWrite(ENB, abs(dir));
}

void parar() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
}
"""


def obter_snippets():
    """Retorna dicionario com todos os snippets."""
    return {
        "ultrassonico": SNIPPET_ULTRASSONICO,
        "ir_simples": SNIPPET_IR_SIMPLES,
        "ir_matriz": SNIPPET_IR_MATRIZ,
        "mpu6050": SNIPPET_MPU6050,
        "motor_dc": SNIPPET_MOTOR_DC,
        "diferencial": SNIPPET_DIFERENCIAL,
        "servo": SNIPPET_SERVO,
        "encoder": SNIPPET_ENCODER,
        "pid_simples": SNIPPET_PID_SIMPLES,
        "pid_arduino": SNIPPET_PID_ARDUINO,
        "leitura_ir": SNIPPET_LEITURA_IR,
        "filtragem": SNIPPET_FILTRAGEM,
        "timer": SNIPPET_TIMER,
        "limitador": SNIPPET_LIMITADOR,
        "log": SNIPPET_LOG,
        "template_arduino": TEMPLATE_SKETCH_ARDUINO
    }

