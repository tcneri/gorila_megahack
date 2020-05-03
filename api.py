from flask import Flask
from flask_restful import Resource, Api , reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('q', action= 'append')

perf = ['Conservador', 'Moderado', 'Arrojado']
quest = {
        0:{'a':0,'b':2,'c':3,'d':4},
        1:{'a':0,'b':2,'c':4,'d':5},
        2:{'a':0,'b':2,'c':4},
        3:{'a':0,'b':1,'c':2,'d':4},
        4:{'a':0,'b':2,'c':4},
        5:{'a':0,'b':2,'c':4},
        6:{'a':0,'b':2,'c':3,'d':4},
        7:{'a':0,'b':2,'c':3,'d':4}

        }

alternativs = ['a','b','c','d']

res = [0,0,0,0,0,0,0,0]

class ClientProfile(Resource):

    
    def get(self):
        return {'teu perfil': 'ok'}
    
    def post(self):
        args = parser.parse_args()
        alt = args['q']
        for i in range (0,len(quest)):
            if alt[i] not in alternativs:
                erro = 1
                break
            else:
                erro = 0
                res[i] = quest[i][alt[i]]

        if erro == 0:
            soma = sum(res)
            if soma <= 9:
                resposta = perf[0]
            
            elif soma > 9 and soma <= 25:    
                resposta = perf[1]
            
            else:
                resposta = perf[2]

        else:
            resposta = 'Entrada inválida'

              
        return {'result_sum':resposta} , 201

   



api.add_resource(ClientProfile,
        '/',
        '/sum')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
