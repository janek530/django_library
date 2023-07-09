from lyricsgenius import Genius

access_token = 'kE_veBQlyPbRTPbtTYU5Hx-aJPwc_GWFe8s1bp9BRzJGtOvFLU4H609GTye_2bDY'
def get_lyrics(song, artist):
    song = Genius(access_token)
    song = song.search_song(song, artist)
    # song = str(Genius(access_token).search_song(song, artist))
    # first_bracket_id = song.find('[')
    # song = song[first_bracket_id:-5]

    return song


print(get_lyrics('Outro', artist='Avi'))