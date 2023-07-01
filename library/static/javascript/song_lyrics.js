function add_to_lyrics(text){
    var lyrics_area = document.getElementById('id_text');
    var start = lyrics_area.selectionStart;
    var end = lyrics_area.selectionEnd;
    var lyrics = lyrics_area.value.substring(0, start) + text + lyrics_area.value.substring(end);
    lyrics_area.value = lyrics;
    lyrics_area.focus();
    lyrics_area.selectionEnd = end + text.length;
}