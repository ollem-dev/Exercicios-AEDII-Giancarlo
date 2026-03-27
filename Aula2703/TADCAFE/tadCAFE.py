class Cafeteira:
    def __init__(self, capacidade_max):
        self.capacidade_max = capacidade_max
        self.nivel_agua = 0
        self.nivel_cafe = 0
        self.acesa = False 

    def ligar(self):
        self.acesa = True
        print("Cafeteira iniciando, aquecendo aguá...")
    
    def desligar(self):
        self.acesa = False
        print("Cafeteira desligada!")
    
    def abastecer_agua(self, ml):
        if self.nivel_agua + ml <= self.capacidade_max:
            self.nivel_agua += ml
            print(f"Aguá adicionada: {ml}ml")
        else:
            print(f"ERRO! Quantidade excede o nivel de agua permitido")
    def abastecer_cafe(self, mg):
            self.nivel_cafe += mg
            print(f"Café adicionado: {mg}mg")

    def fazer_cafe(self):
        if not self.acesa:
            print("Cafeteira desligada")
            return
        if self.nivel_agua >= 100 and self.nivel_cafe >= 10:
            self.nivel_agua -= 100 
            self.nivel_cafe -= 10
            print('Café realizado!')
        else:
            print('Erro: Aguá ou café insuficientes!')

    def ver_status(self):
        estado = 'Ligada' if self.acesa else 'Desligada'
        print(f"\n [SATATUS] {estado} | Água: {self.nivel_agua} | Café: {self.nivel_cafe}")

        pass