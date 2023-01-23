import random



def random_song():
    cols = 'energy', 'danceability', 'loudness', 'valence'
    id = random.randint(0,1000000)
    rand_song = {'id': {c: random.uniform(0,1) for c in cols} }
    return rand_song

    

print(random_song())