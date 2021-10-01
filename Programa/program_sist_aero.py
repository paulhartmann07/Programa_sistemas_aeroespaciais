import PySimpleGUI as sg
import pyperclip as pyperclip

# Variáveis Globais
font = 'Arial, 16'
font_1 = 'Arial, 18'
font_2 = 'Arial, 20'
font_3 = 'Arial, 24'
font_4 = 'Arial, 20'

#--------------------------------------------------------
# Textos -> programações
def programacoes_sensores(i):
    if i == 1:
        vetor_imprimir = ''
        with open('/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/programas_sensores.TXT') as arquivo:
            vetor_arquivo = arquivo.readlines()
        for j in range(0, 259):
            vetor_imprimir = vetor_imprimir + vetor_arquivo[j]
        
        return str(vetor_imprimir)
    
    elif i == 2:
        vetor_imprimir = ''
        with open('/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/programas_sensores.TXT') as arquivo:
            vetor_arquivo = arquivo.readlines()
        for j in range(262, 290):
            vetor_imprimir = vetor_imprimir + vetor_arquivo[j]
        
        return str(vetor_imprimir)
    
    elif i == 3:
        vetor_imprimir = ''
        with open('/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/programas_sensores.TXT') as arquivo:
            vetor_arquivo = arquivo.readlines()
        for j in range(293, 380):
            vetor_imprimir = vetor_imprimir + vetor_arquivo[j]
        
        return str(vetor_imprimir)
    
    elif i == 4:
        vetor_imprimir = ''
        with open('/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/programas_sensores.TXT') as arquivo:
            vetor_arquivo = arquivo.readlines()
        for j in range(384, len(vetor_arquivo)):
            vetor_imprimir = vetor_imprimir + vetor_arquivo[j]
        
        return str(vetor_imprimir)
    
#--------------------------------------------------------
# Textos -> Microcontroladores
def text_micro(i):
    if i == 1:
        texto_arduino = '''Consumo energético:
- Voltagem: 5 V
- Corrente média: 15 mA
-> 0,075 W\n
\nProcessamento:
- AVR® 8-bit RISC -> Frequência de 0~16 mHz
- Memória flash: 32KB & RAM: 2KB
        '''
        return texto_arduino
    
    elif i == 2:
        texto_esp = '''Consumo energético:
- Voltagem: 2,2 ~ 3 V
- Corrente média: 80 mA
-> 0,4 W\n
\nProcessamento:
- Xtensa® Dual-Core 32-bit LX6 -> Frequência de 80~240 mHz
- Memória flash: 4MB & RAM: 520KB
        '''
        return texto_esp
    
    
#--------------------------------------------------------
# Textos -> Sensores
def text_sensors(i):
    # MPU-9250
    if i == 1:
        texto_mpu = '''\nO sensor MPU-9250 é um sensor IMU (Inertial Measurement Unity)\n 
que pode-se traduzir como uma unidade medição inercial. O\n 
grande objetivo e foco desse sensor se resguarda em localizar\n
espacialmente o objeto o qual o sensor está - utilizando para\n
isso suas medições de Acelerômetro, Giroscópio e Magnetômetro.

\nSaiba mais em: https://invensense.tdk.com/wp-content/uploads/\n
2015/02/PS-MPU-9250A-01-v1.1.pdf
\nTodas as específicações do sensor.
        '''
        return texto_mpu
        
    # SR-04
    elif i == 2:
        texto_sr = '''\nO sensor HC-SR04 é grande responsável para um sensoriamento\n
espacial na questão de distâncias. Este utiliza de uma tecno-\n
logia ultrassonica para determinar a distância em relação aos\n
objetos ao redor do dispositivo aeroespacial. Muito utilizado\n
para garantir que o veículo não colida com coisas no ambiente.

\nSaiba mais em: https://www.theengineeringprojects.com/2018/\n
10/introduction-to-hc-sr04-ultrasonic-sensor.html
\nPossui todas as especificações do sensor.
        '''
        return texto_sr
        
    # Fotoresistor
    elif i == 3:
        texto_ldr = '''\nO Fotoresistor, também conhecido como sensor LDR, possui\n
como objetivo ter a percepção da luminosidade do ambiente, por\n
meio da mudança da resistência elétrica que ocorre no sensor\n
com a mudança da intensidade de luz no ambiente. Normalmente é\n
muito utilizado para iluminação automática.

\nSaiba mais em: https://www.watelectronics.com/light-dependent\n
-resistor-ldr-with-applications/
        '''
        return texto_ldr
        
    # DHT11
    elif i == 4:
        texto_dht = '''\nO sensor DHT11 é muito importante para questões ambientais,\n
pois, por meio dele é possível verificar questões de Temperatura\n
e Umidade. Ele é utilizado para garantir que a atuação do dispo-\n
sitivo aérea está de acordo com o esperado e que o ambiente este-\n
ja garantindo a sua atuação.

\nSaiba mais em: http://blog.baudaeletronica.com.br/dht11-com-\n
arduino/
\nPossui todas as especificações do sensor.
        '''
        return texto_dht
    
    elif i == 5:
        texto_mems = '''\nSistemas Microeletromecânicos (Micro-Electro-Mechanical Systems,\n
em inglês) é o nome dado para a tecnologia que integra\n
elementos mecânicos, sensores e eletrônicos em um pequeno\n
chip, que possui uma informação gravada que determina seu\n
funcionamento. São praticamente micromáquinas programadas\n
para cumprir determinada atividade.

\nFonte: https://www.tecmundo.com.br/nanotecnologia/3254-o\n
-que-sao-mems-.htm
        '''
        return texto_mems
        
        

#--------------------------------------------------------
# Função para a abertura da Janela Inicial
def tab_inicial():
    
    texto_extenso_apresentacao = """\tEsse programa foi criado com o intuito de facilitar a utilização e aprendizado com o Arduino e seus Sensores.
\n\tCom o foco na utilização do Arduino/microcontroladores análogos e os sensores, temos a visão de difundir cada vez mais o conhecimento e as aplicações de sistemas embarcados em aplicações aeroespaciais.
\n\tPor tanto, sinta-se livre para utilizar esse programa da melhor maneira possível!"""

    janela_sobre = [
        [sg.Text('Sobre o Programa de Sistemas Embarcados', border_width=2, font=font_3)],
        [sg.Text(texto_extenso_apresentacao, size=(60,6), border_width=5, font=font_4)]
    ]
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    janela_Arduino_Sensores = [
        [sg.Button('Comparação \nMicrocontroladores', button_color=('White','#0258CB'), size=(22,2), font=font_2),
         sg.Button('Sensores & \nFunções', button_color=('White','#6DC8FD'), size=(22,2), font=font_2)]
    ]
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    botoes_ao_lado = [
        [sg.Button('Dicas', size=(10,1), font=font)],
        [sg.Button('Fechar', button_color=('White','Red'), size=(10,1), font=font)]
    ]
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    tab_group_i = [
            [sg.TabGroup(
                [[sg.Tab('Sobre', janela_sobre, title_color='White', border_width=10, background_color='#FFFAE5', element_justification='center'),
                  sg.Tab('Arduino & Sensores', janela_Arduino_Sensores, title_color='White', border_width=10, background_color='#FFFAE5', element_justification='center')]],
                  tab_location='centertop', title_color='Black', tab_background_color='White', selected_title_color='White', border_width=5, background_color='LightGray', font=font, size=(850,250)),
                  sg.Column(botoes_ao_lado, background_color='LightGray', element_justification='center')]
    ]
    tab_group_inicial = [
        [sg.Column(tab_group_i, background_color='LightGray')]
    ]
    
    return sg.Window('Aplicações Aeroespaciais', tab_group_inicial, background_color='LightGray', finalize=True)

#--------------------------------------------------------
# Função para a abertura da Janela dos Microcontroladores
def tab_micro():
    janela_arduino_esquerda = [
        [sg.Text('Informações sobre o arduino aqui', font=font)],
        [sg.Text(text_micro(1), font=font)]
    ]
    janela_arduino_direita = [
        [sg.Text('ARDUINO', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/arduino.png")]
    ]

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    janela_esp32_esquerda = [
        [sg.Text('Informações sobre o esp32 aqui', font=font)],
        [sg.Text(text_micro(2), font=font)]
    ]
    janela_esp32_direita = [
        [sg.Text('ESP32', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/esp32.png")]
    ]

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    janela_arduino = [
        [sg.Column(janela_arduino_esquerda, size=(500,300), element_justification='left'), sg.VSeperator(), sg.Column(janela_arduino_direita, size=(300,300), element_justification='left')]
    ]

    janela_esp32 = [
        [sg.Column(janela_esp32_esquerda, size=(500,300), element_justification='left'), sg.VSeparator(), sg.Column(janela_esp32_direita, size=(300,300), element_justification='left')]
    ]
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    botoes_ao_lado = [
        [sg.Button('Dicas', size=(10,1), font=font)],
        [sg.Button('Voltar', button_color=('White','Gray'), size=(10,1), font=font)],
        [sg.Button('Fechar', button_color=('White','Red'), size=(10,1), font=font)]
    ]
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    tab_group_microcontroladores = [
            [sg.TabGroup(
                [[sg.Tab('Arduino', janela_arduino, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='center'),
                  sg.Tab('ESP32', janela_esp32, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='center')]],
                  tab_location='centertop', title_color='Black', tab_background_color='White', selected_title_color='White', selected_background_color='Gray', background_color='LightGray', border_width=5, font=font, size=(790,290)),
                  sg.Column(botoes_ao_lado, background_color='LightGray', element_justification='center')]
    ]
    return sg.Window('Aplicações Aeroespaciais', tab_group_microcontroladores, background_color='LightGray', finalize=True)

#----------------------------------------------------------------------------------------------------------
# Função para a abertura da Janela dos Sensores
def tab_sensores():
    # Janela MEMs -----------------------------------------------------------------------------------------
    janela_mems_esquerda = [
        [sg.Text('O que são MEMs?', font=font)],
        [sg.Text(text_sensors(5), font=font)]
    ]
    janela_mems_direita = [
        [sg.Text('MEMs', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/mems1.png")],
    ]
    
    janela_mems = [
        [sg.Column(janela_mems_esquerda, size=(500,350), element_justification='left'), sg.VSeparator(), sg.Column(janela_mems_direita, size=(300,350), element_justification='left')]
    ]
    
    # -----------------------------------------------------------------------------------------------------
    # Janela MPU-9250 -------------------------------------------------------------------------------------
    janela_mpu9250_esquerda = [
        [sg.Text('Informações sobre o MPU-9250', font=font)],
        [sg.Text(text_sensors(1), font=font)]
    ]
    janela_mpu9250_direita = [
        [sg.Text('MPU-9250 - referenciamento', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/mpu-9250.png")],
        [sg.Button('Programação MPU-9250', size=(21,1), font=font)],
        [sg.Button('Copiar Programação MPU-9250', size=(21,1), font=font)]
    ]

    janela_mpu9250 = [
        [sg.Column(janela_mpu9250_esquerda, size=(500,350), element_justification='left'),sg.VSeparator(),sg.Column(janela_mpu9250_direita, size=(300,350), element_justification='left')]
    ]

    # -----------------------------------------------------------------------------------------------------
    # Janela SR04 -----------------------------------------------------------------------------------------
    janela_sr04_esquerda = [
        [sg.Text('Informações sobre o SR04', font=font)],
        [sg.Text(text_sensors(2), font=font)]
    ]
    janela_sr04_direita = [
        [sg.Text('SR04 - distância', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/sr04.png")],
        [sg.Button('Programação SR-04', size=(21,1), font=font)],
        [sg.Button('Copiar Programação SR-04', size=(21,1), font=font)]
    ]

    janela_sr04 = [
        [sg.Column(janela_sr04_esquerda, size=(500,350), element_justification='left'),sg.VSeparator(),sg.Column(janela_sr04_direita, size=(300,350), element_justification='left')]
    ]

    # -----------------------------------------------------------------------------------------------------
    # Janela Fotorresistor --------------------------------------------------------------------------------
    janela_fotorresistor_esquerda = [
        [sg.Text('Informações sobre o Fotorresistor', font=font)],
        [sg.Text(text_sensors(3), font=font)]
    ]
    janela_fotorresistor_direita = [
        [sg.Text('Fotoresistor', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/fotorresistor.png")],
        [sg.Button('Programação Fotoresistor', size=(21,1), font=font)],
        [sg.Button('Copiar Programação Fotoresistor', size=(21,1), font=font)]
    ]

    janela_fotorresistor = [
        [sg.Column(janela_fotorresistor_esquerda, size=(500,350), element_justification='left'),sg.VSeparator(),sg.Column(janela_fotorresistor_direita, size=(300,350), element_justification='left')]
    ]

    # ------------------------------------------------------------------------------------------------------
    # Janela DHT11 -----------------------------------------------------------------------------------------
    janela_dht11_esquerda = [
        [sg.Text('Informações sobre o DHT11', font=font)],
        [sg.Text(text_sensors(4), font=font)]
    ]
    janela_dht11_direita = [
        [sg.Text('DHT11 - temp. e umid.', font=font)],
        [sg.Image(filename="/Users/paulohartmannsales/Desktop/JUPYTER_PYTHON/PySimpleGUI - PDPD/imagens/dht11.png")],
        [sg.Button('Programação DHT11', size=(21,1), font=font)],
        [sg.Button('Copiar Programação DHT11', size=(21,1), font=font)]
    ]

    janela_dht11 = [
        [sg.Column(janela_dht11_esquerda, size=(500,350), element_justification='left'),sg.VSeparator(),sg.Column(janela_dht11_direita, size=(300,350), element_justification='left')]
    ]
    
    botoes_ao_lado = [
        [sg.Button('Dicas', size=(10,1), font=font)],
        [sg.Button('Voltar', button_color=('White','Gray'), size=(10,1), font=font)],
        [sg.Button('Fechar', button_color=('White','Red'), size=(10,1), font=font)]
    ]
    
    tab_group_sensores = [
            [sg.TabGroup(
                [[sg.Tab('MEMs', janela_mems, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='c'),
                  sg.Tab('MPU-9250', janela_mpu9250, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='c'),
                  sg.Tab('SR04', janela_sr04, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='c'),
                  sg.Tab('Fotoresistor', janela_fotorresistor, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='c'),
                  sg.Tab('DHT11', janela_dht11, title_color='Black', border_width=10, background_color='#FFFAE5', element_justification='c')]],
                  tab_location='centertop', title_color='Black', tab_background_color='White', selected_title_color='White', selected_background_color='Gray', background_color='LightGray', border_width=5, font=font, size=(790,380)),
                  sg.Column(botoes_ao_lado, background_color='LightGray', element_justification='center')]
    ]
    return sg.Window('Aplicações Aeroespaciais', tab_group_sensores, background_color='LightGray', finalize=True)

# Criar a janela inicial
janela1, janela2, janela3 = tab_inicial(), None, None

# Criar loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
        
    # Indo para uma das duas janelas - a partir da Janela Inicial
    if event == 'Comparação \nMicrocontroladores':
        janela2 = tab_micro()
        janela1.hide()
    if event == 'Sensores & \nFunções':
        janela3 = tab_sensores()
        janela1.hide()
        
    # Pop-up de Programação de sensores
    if event == 'Programação MPU-9250':
        sg.PopupScrolled(programacoes_sensores(1), font=font, size=(50, 25))
    if event == 'Copiar Programação MPU-9250':
        pyperclip.copy(programacoes_sensores(1))
        
    if event == 'Programação SR-04':
        sg.PopupScrolled(programacoes_sensores(2), font=font, size=(50, 25))
    if event == 'Copiar Programação SR-04':
        pyperclip.copy(programacoes_sensores(2))
        
    if event == 'Programação Fotoresistor':
        sg.PopupScrolled(programacoes_sensores(4), font=font, size=(50, 25))
    if event == 'Copiar Programação Fotoresistor':
        pyperclip.copy(programacoes_sensores(4))
        
    if event == 'Programação DHT11':
        sg.PopupScrolled(programacoes_sensores(3), font=font, size=(50, 25))
    if event == 'Copiar Programação DHT11':
        pyperclip.copy(programacoes_sensores(3))
            
    # Voltando para a Janela Inicial  
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
        
    # Quando janela for fechada
    if window == janela1:
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
    if window == janela2:
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
    if window == janela3:
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
    
window.close()