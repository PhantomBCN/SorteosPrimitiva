from jinja2 import Template

diccionario1 = {'nombre': 'Juan', 'edad': 25}
diccionario2 = {'nombre': 'María', 'edad': 30}

plantilla = Template('''
    <html>
        <head>
            <title>Lista de personas</title>
        </head>
        <body>
            {% for diccionario in diccionarios %}
                <h1>{{ diccionario.nombre }}</h1>
                <p>Edad: {{ diccionario.edad }}</p>
            {% endfor %}
        </body>
    </html>
''')

diccionarios = [diccionario1, diccionario2]

html = plantilla.render(diccionarios=diccionarios)

print(html)