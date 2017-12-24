def song_decoder(song):
    mix = 'WUB'
    lyric = song
    ch_str = lyric.replace("WUB", " ")
    new_str = ' '.join(ch_str.split())
    return new_str


result = song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
print(result)
