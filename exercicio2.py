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
        <style rel="stylesheet">
            h1{
                text-aling:center:
            }
            table{
                /*witdh: 100%;*/
            }
            table, th, td {
                border-collapse: collapse;
            }
            th{
                text-aling:center;
            }
            th, td{
                padding: 10px;
            }
            .reprovado{
            background:red;
            color:#fff;
            }
            .aprovado{
             background:green;
            color:#fff;
            }
            </style>    
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

