import PySimpleGUI as sg
from time import sleep
import mibian

class TelaPython:
    def __init__(self):
        #Tema
        sg.change_look_and_feel('SystemDefault')
        #Layout
        layout = [
            [sg.Text("Calculadora Black Scholes")],
            [sg.Radio("Call", "tipo", key="tipoCall"), sg.Radio("Put", "tipo", key="tipoPut")],
            [sg.Text("Strike", size=(17, 0)), sg.Input(size=(9, 0), key="Strike")],
            [sg.Text("Dias para o vencimento", size=(17, 0)), sg.Input(size=(9, 0), key="Vencimento")],
            [sg.Text("Taxa de juros", size=(17, 0)), sg.Input(size=(9, 0), key="TaxaJuros")],
            [sg.Text("Preço da ação", size=(17, 0)), sg.Input(size=(9, 0), key="StockPrice")],

            [sg.Text("\nSelecione o que deseja calcular")],
            [sg.Radio("Volatilidade", "Escolha", key="EVolatilidade", size=(14, 0)), sg.Input(size=(9, 0), key="Volatilidade")],
            [sg.Radio("Prêmio da opção", "Escolha", key="EOptionPrice", size=(14, 0)), sg.Input(size=(9, 0), key="OptionPrice")],
            [sg.Button("Calcular")],
            [sg.Output(size=(30, 20))]
        ]
        #Janela
        self.janela = sg.Window("Calculadora Black Scholes").layout(layout)

    def Iniciar(self):
        while True:
            sleep(0.5)
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            tipoCall = self.values["tipoCall"]
            tipoPut = self.values["tipoPut"]
            Strike = self.values["Strike"]
            Vencimento = self.values["Vencimento"]
            TaxaJuros = self.values["TaxaJuros"]
            StockPrice = self.values["StockPrice"]

            EVolatilidade = self.values["EVolatilidade"]
            Volatilidade = self.values["Volatilidade"]
            EOptionPrice = self.values["EOptionPrice"]
            OptionPrice = self.values["OptionPrice"]

            print(f"Call: {tipoCall}")
            print(f"Put: {tipoPut}")
            print(f"Strike: {Strike}")
            print(f"Vencimento: {Vencimento}")
            print(f"TaxaJuros: {TaxaJuros}")
            print(f"StockPrice: {StockPrice}")
            print(f"Volatilidade: {Volatilidade}")
            print(f"OptionPrice: {OptionPrice}")


            if tipoCall == True:
                # Volatilidade Call
                if EVolatilidade == True:
                    v = mibian.BS([StockPrice, Strike, TaxaJuros, Vencimento], callPrice=OptionPrice)
                    print(f"\nVolitilidade implícita: {v.impliedVolatility}")

                elif EOptionPrice == True:
                    #Prêmio Call
                    p = mibian.BS([StockPrice, Strike, TaxaJuros, Vencimento], volatility=Volatilidade)
                    print(f"\nPrêmio da opção: {p.callPrice}")

            elif tipoPut == True:
                # Volatilidade Put
                if EVolatilidade == True:
                    v = mibian.BS([StockPrice, Strike, TaxaJuros, Vencimento], putPrice=OptionPrice)
                    print(f"\nVolitilidade implícita: {v.impliedVolatility}\n")

                elif EOptionPrice == True:
                    #Prêmio Put
                    p = mibian.BS([StockPrice, Strike, TaxaJuros, Vencimento], volatility=Volatilidade)
                    print(f"\nPrêmio da opção: {p.putPrice}\n")

tela = TelaPython()
tela.Iniciar()