def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        opponent_history.clear()
    else:
        opponent_history.append(prev_play)
    n = 4
    guess = "R" 
    if len(opponent_history) > n:
        pattern = "".join(opponent_history[-n:])
        last_sequence = "".join(opponent_history[-(n+1):-1])
        if last_sequence not in play_order:
            play_order[last_sequence] = {}
        play_order[last_sequence][prev_play] = play_order[last_sequence].get(prev_play, 0) + 1
        if pattern in play_order:
            prediction = max(play_order[pattern], key=play_order[pattern].get)
        else:
            prediction = max(set(opponent_history), key=opponent_history.count)
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        guess = ideal_response[prediction]
    return guess
