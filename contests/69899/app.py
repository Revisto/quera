class InputHandler():
    def initialize(self):
        players, rounds = input().split(" ")
        players, rounds = int(players), int(rounds)
        feet = sorted(list(range(1, players+1))*2)
        feet = [str(int) for int in feet]

        return {
            "players": players,
            "rounds": rounds,
            "feet": feet
        }

class Similator():
    def one_round(self, current_turn, feet, rounds):
        output_list = []
        for i in range(rounds):
            if current_turn >= len(feet):
                current_turn -= len(feet)
            output_list.append(feet[current_turn])
            current_turn += 1
        feet.remove(output_list[-1])
        output = " ".join(output_list)
        return {
            "current_turn": current_turn - 1,
            "feet": feet,
            "output": output
        }

    def is_game_finished(self, feet):
        if len(set(feet)) == 1:
            return list(set(feet))[0]
        return False

    def game(self, rounds, feet):
        current_turn = 0
        while True:
            response_one_round = Similator().one_round(current_turn, feet, rounds)
            feet = response_one_round["feet"]
            current_turn = response_one_round["current_turn"]
            print(response_one_round["output"])

            is_game_finished_response = Similator().is_game_finished(feet)
            if is_game_finished_response is not False:
                print(f"winner:{is_game_finished_response}")
                return

input_data = InputHandler().initialize()
Similator().game(input_data["rounds"], input_data["feet"])