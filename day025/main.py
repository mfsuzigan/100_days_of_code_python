from turtle import Screen, Turtle

import pandas


def main():
    screen = Screen()
    screen.setup(width=730, height=496)
    screen.bgpic("blank_states_img.gif")
    screen.onkeypress(fun=lambda: screen.bye(), key="Escape")

    states_data = pandas.read_csv("50_states.csv")
    feedback_message = ""
    states_count = len(states_data)
    states_guessed = []
    player_guess = ""

    while player_guess is not None and player_guess.lower() != "exit" and len(states_guessed) != states_count:
        player_guess = screen.textinput(
            title=f"Guess the states ({len(states_guessed)}/{states_count})",
            prompt=f"{feedback_message}Enter the name of a US state:")

        if player_guess is not None:
            guessed_state = states_data[states_data.state.str.lower() == player_guess.lower()]

            if guessed_state.empty:
                feedback_message = "Sorry, that's wrong.\n\n"

            else:
                show_state_on_map(guessed_state)
                states_guessed.append(guessed_state.state.item())
                feedback_message = "Correct!\n\n"

    show_remaining_states_on_map(states_data, states_guessed)
    screen.exitonclick()


def show_remaining_states_on_map(states_data, states_guessed):
    for remaining_state in states_data[~states_data.state.isin(states_guessed)].state:
        show_state_on_map(states_data[states_data.state == remaining_state], "red")


def show_state_on_map(guessed_state, color="black"):
    state_name_on_map = Turtle()
    state_name_on_map.hideturtle()
    state_name_on_map.pencolor(color)
    state_name_on_map.penup()
    state_name_on_map.goto(guessed_state.x.item(), guessed_state.y.item())
    state_name_on_map.write(arg=f"{guessed_state.state.item()}")


if __name__ == "__main__":
    main()
