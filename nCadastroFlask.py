import re
#from urllib import request
import json
from flask import Flask, render_template, request
app = Flask(__name__)
#necessario para iniciar o site 

# criar a primeira página no flask 
# toda pagina tem que ter um route e uma função
# a função é o que você quer exibir na página route é o endereço 


@app.route("/") # ganhou o nome da varivel app mais @,  "/" leva para home page
def home(): #pode ser qualquer nome, mas tem que ser o mesmo da rota 
  
    #return "alguma coisa "
    return render_template ("index.html")
 #--------------------------
@app.route("/cadastro", methods=['GET', 'POST']) # ganhou o nome da varivel app mais @,  "/" leva para home page
def cadastro(): #pode ser qualquer nome, mas tem que ser o mesmo da rota  
    if request.method == 'POST':
        name = request.form['fname'].upper() 
        senha = request.form['lname'].upper()
        print(type(name))
        #---------------requsitos do nome e da senha 
        #letras= ["a","b","c","d","e","f","g","h","i","J","m","n","o","p","q","r","s","t","u","v","x","z","w","y"]
        letras= ["A","B","C","D","E","F","G","H","I","J","M","N","O","P","Q","R","S","T","U","V","X","Z","W","Y"] 
        numeros= ["0","1","2","3","4","5","6","7","8","9"]
        caracProibido= [" "]
        # requsitos do nome 
        nameValido= 0 
        #name.lower() #deixar tudo minuscolo 
        for x in name: 
            for y in letras:
             if x == y :
                nameValido=1 
                print(nameValido)
        # verifica se tem um numero
        for x in name:  
            #print(x) 
            for y in numeros: 
            #print(y) 
                if x == y :
                    if nameValido==1:
                        nameValido=2 
                        print(nameValido)
        # verifica se tem um numero  
        # verifica se tem espaço
        if caracProibido[0] in name: 
            print("não é permitido espaço")
            nameValido=0   
        # verifica se tem espaço 
        print (nameValido)
        # requsitos do nome
        
        # requsitos da senha 
        # verifica se tem espaço
        
        if caracProibido[0] in senha: 
            print("não é permitido espaço na senha")
            nameValido=0 # vou usar a mesma variavel da senha  
        # verifica se tem espaço 
        # requsitos da senha 
         
        #---------------requsitos do nome e da senha 
        
        #if name != "" :  
        if nameValido == 2 : 
            #-------cria a senha no json 
            dadosUsuario = {"usuario":"",
            "senha": ""
            }
            f = open("senha.json", "w")
            dadosUsuario["usuario"] = name
            dadosUsuario["senha"] = senha
            f.write(json.dumps(dadosUsuario,indent=1)) # grava a usuário no json 
            return f"usuario foi cadastrado:  {name} - {senha}" 
            #-------cria a senha no json 
        else: 
            return "não cadastramos nomes assim, os usuários devem ter pelo menos uma letra e um número nos nomes e senhas e usuários não devem conter espaços em branco "    
    else:
        name = ''
        return render_template ("pagina_cadastro.html")
        
    
#--------------------------
#--------------------------
@app.route('/login', methods=['GET', 'POST']) # <>funciona como entrada do parametro 
def login():
    if request.method == 'POST':
        name = request.form['fname'].upper() 
        senha = request.form['lname'].upper()
        acessoLiberado=0 
        jsonDadosUsuario = {
        "usuario": "xxxxx",
        "senha": "xxxxx"
        }
        
        
        f = open("senha.json", "r")
        jsonDadosUsuario = json.load(f) # carrega o nome do usurio e senha
        if name == jsonDadosUsuario["usuario"]:
            acessoLiberado+=1 
            print("usurário correto")
        else:
            acessoLiberado=0
            print("usurário errado")
        if senha == jsonDadosUsuario["senha"]:
            acessoLiberado+=1 
            print("senha correta")
        else:
            acessoLiberado=0
            print("senha errada")
        if acessoLiberado == 2 :
            print (acessoLiberado)
            return "acesso liberado"
        else : 
            return "acesso negado"
    else:
        name = ''
        
        return render_template ("login.html")
#-------------------------- 
#--------------------------

#--------------------------

if __name__ == '__main__':
    app.run(debug=True) # coloca o site no ar , debug=true atualiza o site 

