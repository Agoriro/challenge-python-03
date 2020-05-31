# Resolve the problem!!
import re

patron = re.compile(r'[a-z]')


def run():
    # Start coding here
    with open('E:\Cursos\Curso_Basico_Python\Challenges\Challenge3\challenge-python-03\src\encoded.txt', 'r', encoding='utf-8') as f:
        linea = f.read()
        
        mensaje = ''.join(patron.findall(linea))
        print(f'El mensaje oculto es: {mensaje}')




if __name__ == '__main__':
    run()
