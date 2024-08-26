from fastapi import FastAPI, Request
from move_parser import MoveParser
import time

app = FastAPI()
move_parser = MoveParser("game.pgn")

@app.get("/")
def read_root(request: Request):
	next_move = move_parser.get_next_move()
	client_ip = request.client.host

	if next_move is None:
		write_log("No more moves")
		return {"Move": "No more moves"}
	else:
		write_log(f"Client {client_ip} got next move: {next_move}")
		return {"Move": f"{next_move}"}


def write_log(message):
	current_time = time.strftime("%Y_%m_%d-%s", time.localtime())
	with open(f"log/{current_time}.log", "w") as log:
		log.write(f"{message}\n")