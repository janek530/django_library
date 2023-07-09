from lyricsgenius import Genius

access_token = 'token'
def get_lyrics(song, artist):
    song = str(Genius(access_token).search_song(song, artist).lyrics)
    first_bracket_id = song.find('[')
    song = song[first_bracket_id:-5]
    print(song)
    return song
