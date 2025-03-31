from helpers import *

# datos de las partidas jugadas
rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]

# Simulamos las rondas e imprimimos los resultados parciales
for i, round in enumerate(rounds):
    print(f"Ronda {i + 1}")
    calculate_round_scores(round)

# Imprimos el ranking final
print("Ranking final:")

# Formato de la tabla para la impresión
print("Jugador".ljust(10), "Kills".ljust(6), "Asist".ljust(6), "Muertes".ljust(7), "Puntos".ljust(6), "MVPS".ljust(6))

# Ordenamos los jugadores por su puntaje total (de mayor a menor)
sorted_players = sorted(player_scores.items(), key=lambda x: x[1]['score_total'], reverse=True)

# Iterar sobre los jugadores ordenados y mostrar la información
for player, stats in sorted_players:
    print(f"{player.ljust(10)} {str(stats['total_kills']).ljust(6)} {str(stats['total_asist']).ljust(6)} {str(stats['total_deaths']).ljust(7)} {str(stats['score_total']).ljust(6)} {str(stats['mvp_count']).ljust(6)}")


