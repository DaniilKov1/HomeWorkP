playlist = []
game = input('Введите название игры. ')
while game != '0':
    if game in playlist:
        print('Игра уже записана.')
    else:
        playlist.append(game)
    game = input('Введите название игры. ')
    playlist.sort()

print(playlist)
