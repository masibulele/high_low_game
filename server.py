from flask import Flask , render_template , request , make_response, jsonify ,redirect, url_for
import random
import math

DEFAULT_VALUES={
    "lower_limit": 0,
    "upper_limit": 100,
    "max_attempts": 6
}

app = Flask(__name__)

# create number range for game
lower = 0
upper = 100
count =0
to_display = []
#generate secret number and maximum number of guess allowed
secrect_num = random.randint(lower,upper)
maximum = math.floor(math.log2(upper -lower))

@app.route("/",methods=["GET","POST"])
def home():
    # game logic
    # game_status =play_game()
    return render_template("index.html", defaults=DEFAULT_VALUES)

@app.route("/play",methods=["POST"])
def play():
    
    # game logic

    req = request.get_json()
    
    
    
    data = play_game(req)
    res = make_response(jsonify(data),200)


    # game_status =play_game()
    return res

@app.route("/quit",methods=["POST"])
def quit():
    return redirect(url_for(home))


# helper function game_logic
def play_game(userGuess=0):
    global secrect_num
    global maximum
    global count
    global to_display

    # start main game loop
    flag = False
    
    game_state ={
        "attempts":count,
        "wins": 0,
        "guess": None,
        "comment":None,
        "win_num": secrect_num,
        "history": to_display
    }
    
    while count <=maximum:
        count+=1
        guess = userGuess
        # guess = int(input("Enter guess: "))
        to_display.append(guess)
        # update game state
        game_state["attempts"]=count
        game_state["guess"]= guess


        if guess == secrect_num:
            flag = True
            game_state["comment"]=f"The guess of {game_state['guess']} is correct congratulations"
            game_state["wins"]= game_state["wins"]+1
            final_state =game_state
            print(final_state)
            return final_state
        
        if (secrect_num < guess):
            game_state["comment"]=f"The guess of {guess} is to high, Please try again"
            print(game_state["comment"])
            return game_state
        else:
            game_state["comment"]=f"The guess of {guess} is to low, Please try again"
            print(game_state["comment"])
            return game_state
            
            
    if not flag:
        game_state["comment"]=f"The number was {game_state['win_num']}, Better luck next time"
        
    return game_state


if __name__ == "__main__":
    app.run(debug=True)
    # count= 0
    # while count <=5:
    #     play_game()