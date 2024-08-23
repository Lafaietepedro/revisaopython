class Aluno():
    def __init__(self, carga_horaria, faltas):
        self.carga_horaria = carga_horaria
        self.faltas = faltas
    
    def calcula_faltas(self):
        percent_ch = self.carga_horaria * (25/100)
        return percent_ch
    
    def verifica_aprovacao(self):
        percent_ch = self.carga_horaria * (25/100)
        if self.faltas < percent_ch:
            return 'Aprovado'
        else:
            return 'Reprovado'