# Class with util methods for the game
class Util():

    @staticmethod
    def ask_query(query: str, answers: list[str]) -> int:
        print()
        print(query)
        print()
        player_input = input("[<=>]: ")
        is_valid: bool = Util.validate(player_input, answers)
        while not is_valid:
            print('Invalid response. Please try again.')
            print()
            player_input = input("[<=>]: ")
            is_valid = Util.validate(player_input, answers)
        return answers.index(player_input)


    @staticmethod
    def ask_yes_no(query: str) -> bool:
        print()
        print(query)
        print()
        player_input = input("[Y/n]: ")
        formatted_input = Util.format_string(player_input)
        if player_input in ['yes', 'y']:
            return True
        return False


    @staticmethod
    def validate(input_string: str, options: list[str]) -> bool:
        formatted_input = Util.format_string(input_string)
        return input_string in options
        

    @staticmethod
    def format_string(input_string: str) -> str:
        formatted_input = input_string.lower()
        return formatted_input 
