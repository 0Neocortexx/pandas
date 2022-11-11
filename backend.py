from config import *

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/inserir", methods=["GET", "POST"])
def inserir():
    if request.method == "GET":
        return render_template("inserir.html")
    else:
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        try:
            dados = request.get_json(force=True)

            usuario = dados["dado1"]
            senha = dados["dado2"]
            
            dadosPlanilha = {'Usuário':[usuario] ,'Senha':[senha]}

            dataframe = pd.DataFrame(dadosPlanilha)

            dataframe.to_csv('pandas/dados.csv')

        except Exception as e:

            resposta = jsonify({"resultado":"Erro","Detalhes": str(e)})

        # adicionar cabeçalho de liberação de origem

        resposta.headers.add("Access-Control-Allow-Origin", "*")

        return resposta

app.run(debug=True)