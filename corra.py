tempos = []
tempo = int(input())

while tempo >= 0:
    tempos.append(tempo)
    tempo = int(input())
media = sum(tempos) / len(tempos)
print(f'MEDIA: {media:.2f}')    

for tempo in tempos:
        if tempo < media:
                print(tempo)