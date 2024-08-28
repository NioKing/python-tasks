class WrongNumberOfPlayersError(Exception): pass
class NoSuchStrategyError(Exception): pass


def rps_game_winner(players):
    if len(players) != 2: raise WrongNumberOfPlayersError("Wrong number of players!")
    player1, player2 = players[0], players[1]
    name1, strategy1 = player1[0], player1[1].upper()
    name2, strategy2 = player2[0], player2[1].upper()
    valid_strategies = ['R', 'P', 'S']

    if strategy1 not in valid_strategies or strategy2 not in valid_strategies:
        raise NoSuchStrategyError("Strategy must be one of 'R', 'P', or 'S'")
    
    if strategy1 == strategy2: 
        return f"{name1} {strategy1}"
    elif (strategy1 == 'R' and strategy2 == 'S') or \
         (strategy1 == 'S' and strategy2 == 'P') or \
         (strategy1 == 'P' and strategy2 == 'R'):
        return f"{name1} {strategy1}"
    else:
        return f"{name2} {strategy2}"


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) # => WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) # => NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) # => 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) # => 'player1 P'