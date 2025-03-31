# Valor de los puntajes
points = {'kills': 3, 'assists': 1, 'deaths': -1}

# Diccionario para guardar los puntajes acumulados de cada jugador
player_scores = {}

# Función para procesar cada ronda y calcular los puntajes
def calculate_round_scores(round):

    # Creamos un diccionario para guardar los puntajes acumulados de la ronda
    round_results = {}

    # Para cada jugador, calculamos puntajes y acumulamos kills, assists y deaths
    for player, actions in round.items():  
        # Inicializamos el puntaje de la ronda para el jugador
        score_kills = 0
        score_assists = 0       
        score_deaths = 0
        
        # Si el jugador no existe en el diccionario de puntajes acumulados, lo inicializamos
        if player not in player_scores:
            player_scores[player] = {'total_kills': 0, 'total_asist': 0, 'total_deaths': 0, 'score_total': 0, 'mvp_count': 0}	

        # Calculamos y acumulamos puntajes de kills, assists y deaths
        player_scores[player]['total_kills'] += actions['kills']
        player_scores[player]['total_asist'] += actions['assists']
        player_scores[player]['total_deaths'] += actions['deaths'] 

        # Calculamos el puntaje total de la ronda
        score_total = (actions['kills'] * points['kills'] +
                       actions['assists'] * points['assists'] +
                       (actions['deaths'] * points['deaths'] if actions['deaths'] else 0))

        player_scores[player]['score_total'] += score_total

        # Guardamos el puntaje total de la ronda para este jugador
        round_results[player] = score_total

        # Guardamos el puntaje total de la ronda para este jugador para calcular el MVP
        round_results[player] = score_total
                       
    # Finaliza la ronda

    # Buscamos y guardamos el puntaje mas alto de la ronda
    max_score = max(round_results.values())
    
    # Buscamos el MVP de la ronda (jugador con mayor puntaje) y lo contabilizamos
    for player in round_results:
        if round_results[player] == max_score:
            mvp = player
            player_scores[player]['mvp_count'] += 1
    
    # Imprimimos el ranking de la ronda
    sorted_players = sorted(round_results.items(), key=lambda x: x[1], reverse=True)
    for player, score in sorted_players:
        print(f"{player}: {score} puntos")
    
    print(f"MVP de esta ronda: {mvp}")
    print("-" * 50)

    return player_scores