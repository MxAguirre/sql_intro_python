
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def fetch():
    conn = sqlite3.connect('heart.db')

    c = conn.cursor()

    c.execute("""SELECT pulso FROM sensor""")

    data = c.fetchall()

    conn.commit()

    conn.close()
    return data

def show(data):

    y = [x[0] for x in data]
    
    x = []
    for i in range(len(y)):
        x.append(i)
    
    fig = plt.figure()

    ax = fig.add_subplot()
    ax.set_facecolor('whitesmoke')
    ax.set_title('Ritmo cardiaco en el transcurso del partido', fontsize = 16, color = 'tab:red')
    ax.plot(x,y, color = 'g')
    ax.grid(ls = 'dashed')
    plt.show()

def estadistica(data):
    valor_medio = np.mean(data)
    valor_minimo = np.amin(data)
    valor_maximo = np.amax(data)
    desvio_estandar = np.std(data)

    print('El valor medio es: ', valor_medio)
    print('El valor minimo es: ', valor_minimo)
    print('El valor maximo es:', valor_maximo)
    print('La desviacion estandar es:', desvio_estandar)

def regiones(data):
    valor_medio = np.mean(data)
    desvio_estandar = np.std(data)
    
    y1 = []
    x1 = []
    for i in range(len(data)):
        if data[i] <= valor_medio - desvio_estandar:
            x1.append(i)
            y1.append(data[i])
    
    y2 = []
    x2 = []
    for i in range(len(data)):
        if data[i] >= valor_medio + desvio_estandar:
            x2.append(i)
            y2.append(data[i])

    y3 = []
    x3 = []
    for i in range(len(data)):
        if data[i] <= valor_medio + desvio_estandar or data[i] >= valor_medio - desvio_estandar:
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.plot(x1, y1, color = 'tab:red', label = 'Por debajo de la media')
    ax1.grid()
    ax1.legend()
    ax1.set_facecolor('whitesmoke')
    ax2.plot(x2, y2, color = 'tab:purple', label = 'Por arriba de la media')
    ax2.grid()
    ax2.legend()
    ax2.set_facecolor('whitesmoke')
    ax3.plot(x3, y3, color = 'tab:pink', label ='En la media')
    ax3.grid()
    ax3.legend()
    ax3.set_facecolor('whitesmoke')
    plt.show()
    
if __name__ == '__main__':
    print('Ejercicio de profundizacion')

    # Leer la DB
    data = fetch()
    # Data analytics
    show(data)
    estadistica(data)
    regiones(data)