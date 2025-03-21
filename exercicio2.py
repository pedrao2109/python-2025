import ast


with open('notas.txt', 'r',  encoding="utf-8") as file:
    data = file.read()

conteudo = ast.literal_eval(data)

print(type(conteudo))
pagina = open("notas2.html", "w", encoding="utf-8")
pagina.write("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <h1>Joaquim izidoro Marins</h1>
        <meta charset="UTF-8">
        <meta name="viewport"
        content="width=device-width, intial-scale=1.0">
    <table border="1">
""")
for aluno, desempenho in (conteudo.items()):
    pagina.write(f'''
    <th>{aluno}</th>
    <tr>
        <th>Matéria</th>
        <th>1º B</th>
        <th>2º B</th>
        <th>3º B</th>
        <th>4º B</th>
        <th>Media</th>
    </tr>
    ''')
    for materia, notas in desempenho:
        pagina.write(f"""
                     <tr>
                            <td>{materia}</td>
                            <td>{notas[0]}</td>
                            <td>{notas[1]}</td>
                            <td>{notas[2]}</td>
                            <td>{notas[3]}</td>
                            <td>{notas[4]}</td>
                        </tr>                     
    </head>
    </html>           
""")

