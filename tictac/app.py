from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from game import Game, read, upsert, delete, get_all, messages

app = Flask(__name__)
api = Api(app)


class TicTacToe(Resource):

    def post(self):
        g = Game()
        upsert(g)
        return "Game started, Id:%s" % g.Id, 201

    def get(self):
        all_g = get_all()
        return all_g, 200


class TicTac(Resource):
    def get(self, id):
        g = read(id)
        if g:
            return g.current(), 200
        return "Game not found", 404

    def put(self, id):
        g = read(id)
        if not g:
            return "Game %s not found" % id, 404

        req = request.get_json(force=True)
        if 'player' not in req or 'position' not in req:
            return "Need player and position", 400

        ret = g.move(req['player'], int(req['position']))
        if ret == 200:
            msg = 'Winner: ' + g.winner
            return {'msg':msg}, ret
        elif ret == 201:
            return g.current(), ret

        return {'msg': messages[ret]}, ret

    def delete(self, id):
        g = read(id)
        if g:
            delete(g.Id)
            return 'Game %s deleted'%id, 200
        return "Game %s not found"%id, 404


api.add_resource(TicTac, "/tictactoe/<string:id>")
api.add_resource(TicTacToe, "/tictactoe")
app.run(host='0.0.0.0', port=9000)
