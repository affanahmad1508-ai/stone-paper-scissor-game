from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["stone", "paper", "scissor"]

player_score = 0
robot_score = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global player_score, robot_score

    result = ""
    player = ""
    robot = ""

    if request.method == "POST":
        player = request.form["choice"]
        robot = random.choice(choices)

        if player == robot:
            result = "Match Tie"

        elif (
            (player == "stone" and robot == "scissor") or
            (player == "paper" and robot == "stone") or
            (player == "scissor" and robot == "paper")
        ):
            result = "You Win"
            player_score += 1

        else:
            result = "Robot Wins"
            robot_score += 1

    winner = ""

    if player_score == 3:
        winner = "🏆 Congratulations You Won The Match"
        player_score = 0
        robot_score = 0

    elif robot_score == 3:
        winner = "💀 Robot Won The Match"
        player_score = 0
        robot_score = 0

    return render_template(
        "index.html",
        player=player,
        robot=robot,
        result=result,
        player_score=player_score,
        robot_score=robot_score,
        winner=winner
    )

if __name__ == "__main__":
    app.run(debug=True)