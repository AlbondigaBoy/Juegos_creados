import random

Ana = {'gender': 'Female', 'gun': 'Non ballistic', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Africa', 'year': 2016, 'name': 'Ana'}
Ashe = {'gender': 'Female', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'NM', 'place': 'America', 'year': 2018, 'name': 'Ashe'}
Baptiste = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Good', 'mod': 'NM', 'place': 'America', 'year': 2019, 'name': 'Baptiste'}
Bastion = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Neutral', 'mod': 'NM', 'place': 'Europe', 'year': 2016, 'name': 'Bastion'}
Brigitte = {'gender': 'Female', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Europe', 'year': 2018, 'name': 'Brigitte'}
Cassidy = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Neutral', 'mod': 'M', 'place': 'America', 'year': 2016, 'name': 'Cassidy'}
DVa = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'DVa'}
Doomfist = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Evil', 'mod': 'M', 'place': 'Africa', 'year': 2017, 'name': 'Doomfist'}
Echo = {'gender': 'Female', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2020, 'name': 'Echo'}
Genji = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'M', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Genji'}
Hanzo = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Neutral', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Hanzo'}
Junker_Queen = {'gender': 'Female', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2022, 'name': 'Junker Queen'}
Junkrat = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'M', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Junkrat'}
Kiriko = {'gender': 'Female', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2022, 'name': 'Kiriko'}
Lucio = {'gender': 'Male', 'gun': 'Non ballistic', 'behaviour': 'Good', 'mod': 'NM', 'place': 'America', 'year': 2016, 'name': 'Lucio'}
Mei = {'gender': 'Female', 'gun': 'Non ballistic', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Mei'}
Mercy = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Europe', 'year': 2016, 'name': 'Mercy'}
Moira = {'gender': 'Female', 'gun': 'Unarmed', 'behaviour': 'Evil', 'mod': 'M', 'place': 'Europe', 'year': 2017, 'name': 'Moira'}
Orisa = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Africa', 'year': 2017, 'name': 'Orisa'}
Phara = {'gender': 'Female', 'gun': 'Ballistic', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Africa', 'year': 2016, 'name': 'Phara'}
Ramattra = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Evil', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2022, 'name': 'Ramattra'}
Reaper = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'M', 'place': 'America', 'year': 2016, 'name': 'Reaper'}
Reinhardt = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Europe', 'year': 2016, 'name': 'Reinhardt'}
Roadhog = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Roadhog'}
Sigma = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Evil', 'mod': 'M', 'place': 'Europe', 'year': 2019, 'name': 'Sigma'}
Sojourn = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'M', 'place': 'America', 'year': 2022, 'name': 'Sojourn'}
Soldier_76 = {'gender': 'Male', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'M', 'place': 'America', 'year': 2016, 'name': 'Soldier 76'}
Sombra = {'gender': 'Female', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'M', 'place': 'America', 'year': 2016, 'name': 'Sombra'}
Symmetra = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Neutral', 'mod': 'M', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Symmetra'}
Torbjorn = {'gender': 'Male', 'gun': 'Non ballistic', 'behaviour': 'Good', 'mod': 'M', 'place': 'Europe', 'year': 2016, 'name': 'Torbjorn'}
Tracer = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Good', 'mod': 'M', 'place': 'Europe', 'year': 2016, 'name': 'Tracer'}
Widowmaker = {'gender': 'Female', 'gun': 'Ballistic', 'behaviour': 'Evil', 'mod': 'M', 'place': 'Europe', 'year': 2016, 'name': 'Widowmaker'}
Winston = {'gender': 'Male', 'gun': 'Non ballistic', 'behaviour': 'Good', 'mod': 'M', 'place': 'Europe', 'year': 2016, 'name': 'Winston'}
Wrecking_Ball = {'gender': 'Male', 'gun': 'Ballistic', 'behaviour': 'Neutral', 'mod': 'M', 'place': 'Asia-Pacific', 'year': 2018, 'name': 'Wreckin Ball'}
Zarya = {'gender': 'Female', 'gun': 'Energy', 'behaviour': 'Neutral', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Zarya'}
Zenyatta = {'gender': 'Male', 'gun': 'Unarmed', 'behaviour': 'Good', 'mod': 'NM', 'place': 'Asia-Pacific', 'year': 2016, 'name': 'Zenyatta'}

ch = [Ana, Ashe, Baptiste, Bastion, Brigitte, Cassidy, DVa, Doomfist, Echo, Genji, Hanzo, Junker_Queen, Junkrat,
        Kiriko, Lucio, Mei, Mercy, Moira, Orisa, Phara, Ramattra, Reaper, Reinhardt, Roadhog, Sigma, Sojourn, Soldier_76,
        Sombra, Symmetra, Torbjorn, Tracer, Widowmaker, Winston, Wrecking_Ball, Zarya, Zenyatta]

# respuesta a escribir
answer = ""
# personaje random que se elige (diccionario)
rCh = random.choice(ch)
# su nombre
name = rCh.get('name')

while answer != name:
        answer = input()
        for i in ch:
                if i['name']==answer:
                        hero = i
                        break
        if(hero['gender'] != rCh.get('gender')):
                print('Red: ', hero['gender'])
        else:
                print('Green: ', hero['gender'])

        if (hero['gun'] != rCh.get('gun')):
                print('Red: ', hero['gun'])
        else:
                print('Green: ', hero['gun'])

        if (hero['behaviour'] != rCh.get('behaviour')):
                print('Red: ', hero['behaviour'])
        else:
                print('Green: ', hero['behaviour'])

        if (hero['mod'] != rCh.get('mod')):
                print('Red: ', hero['mod'])
        else:
                print('Green: ', hero['mod'])

        if (hero['place'] != rCh.get('place')):
                print('Red: ', hero['place'])
        else:
                print('Green: ', hero['place'])

        if (hero['year'] < rCh.get('year')):
                print('Red: ', hero['year'], 'Higher\n')
        elif (hero['year'] > rCh.get('year')):
                print('Red: ', hero['year'], 'Lesser\n')
        else:
                print('Green: ', hero['year'], '\n')

        if (answer != name):
                print('Fallaste... Vuelve a intentarlo')
                print('#################################\n')

print('¡Acertaste!')

while True:
        x = 1

