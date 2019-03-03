def my_key(song_normal_time):
    time = song_normal_time[1].split(":")
    return int(time[0]) * 60 + int(time[1])
#
# lst = [("All Eyes", "04:58"), ("All for you", "3:32")]
# lst.sort(key = my_key)
# print(lst)


def sort_songs(song_titles, length_songs, key):
    if key == "song_length":
        sort(key = len(song_titles))


song_titles = ['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд']
length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']
