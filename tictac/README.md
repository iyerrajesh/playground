TicTacToe Service
-----------------

This directory contains code, build and deployment scripts.

Build Image
-----------
Build image by running this on the current directory:
    
    docker build --tag tictactoe .

Run Service locally
-------------------
You can run the service locally on localhost:9000 using:

    docker run -p 9000:9000 tictactoe

Run on K8s
----------
Deploy on any k8s cluster or minikube using:
   
   `kubectl creeate -f tictac.yaml`

APIs
----

List all active games
`curl -X GET http://localhost:9000/tictactoe`

Start a new game (returns new game id)
`curl -X POST http://localhost:9000/tictactoe`

Get current status for a game
`curl -X GET http://localhost:9000/tictactoe/44844`

Make a move for a player

`curl -X PUT http://localhost:9000/tictactoe/44844 -d '{"player":"a","position":5}'`

`curl -X PUT http://localhost:9000/tictactoe/44844 -d '{"player":"b","position":3}'`

position should be a number 1-9 representing the cell # (one of 9 cells on the board)

End a game anytime

`curl -X DELETE http://localhost:9000/tictactoe/16159`



