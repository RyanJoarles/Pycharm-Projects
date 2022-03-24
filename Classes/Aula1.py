#Class é como se fosse uma formula que processa dados diferentes da mesma forma

class Computador:
    def __init__(self, placaMae, memoria, placaVideo, processador, ssd):
        self.placaMae = placaMae
        self.memoria = memoria
        self.placaVideo = placaVideo
        self.processador = processador
        self.ssd = ssd

    def Ligar(self):
        if self.ssd != '':
            print("Inicialização rápida")
        else:
            print("Inicialização normal")

    def ExibirSistema(self):
        print(self.placaMae, self.memoria, self.placaVideo, self.processador, self.ssd)

computador1 = Computador('Asus', '8gb', 'GTX 1050ti', 'Core i5', '')
computador2 = Computador('MSI', '16gb', 'GTX 1060ti', 'Core i7', '120gb')

computador1.ExibirSistema()
computador1.Ligar()

computador2.ExibirSistema()
computador2.Ligar()