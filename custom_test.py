import import_ipynb
from Copy of HW3_Solution_Spring_2023 import get_connections,get_countries_traveled,get_secondary_connections,count_common_connections,find_path_to_friend

def test(got, expected):
    if (got==expected):
        prefix = ' OK '
        print(prefix)
    else:
        prefix = '  X '
        print('%s got: %s\n\n expected: %s\n\n\n' % (prefix, repr((got)), repr((expected))))

def test2(got, expected):
    if got in expected:
        prefix = ' OK '
        print(prefix)
    else:
        prefix = '  X '
        print('%s got: %s\n\n expected: %s\n\n\n' % (prefix, repr(got), repr(expected)))

def test_get_connections():
    test(get_connections(net, 'Usama'), ['Saeed', 'Aaliya', 'Mohsin'])
    test(get_connections(net, 'Saeed'), ['Sumaira', 'Zehra', 'Samar', 'Marium'])
    test(get_connections(net, 'Marium'), ['Mohsin', 'Kashif', 'Saeed'])
    test(get_connections(net, 'Sumaira'), ['Usama', 'Zehra'])
    test(get_connections(net, 'Aaliya'), ['Mohsin', 'Bari', 'Sameera', 'Kashif'])
    test(get_connections(net, 'Mohsin'), ['Usama', 'Bari', 'Saeed'])
    test(get_connections(net, 'Bari'), ['Zehra', 'Usama', 'Mohsin'])
    test(get_connections(net, 'Zehra'), ['Marium', 'Samar', 'Saeed'])
    test(get_connections(net, 'Sameera'), ['Bari', 'Usama', 'Samar', 'Kashif'])
    test(get_connections(net, 'Kashif'), ['Zehra'])
    test(get_connections(net, 'Samar'), ['Sumaira', 'Usama', 'Aaliya'])
    test(get_connections(net, 'Aisha'), None)

def test_get_countries_traveled():
    test(get_countries_traveled(net, 'Usama'), ['Italy', 'Japan', 'Korea'])
    test(get_countries_traveled(net, 'Saeed'), ['China', 'Afghanistan'])
    test(get_countries_traveled(net, 'Marium'), ['Japan', 'USA', 'Iran'])
    test(get_countries_traveled(net, 'Sumaira'), ['Japan', 'Saudi Arabia'])
    test(get_countries_traveled(net, 'Aaliya'), ['India', 'USA', 'Malaysia'])
    test(get_countries_traveled(net, 'Mohsin'), ['Iran', 'Indonesia', 'Afghanistan'])
    test(get_countries_traveled(net, 'Bari'), ['Japan', 'India', 'China', 'United Arab Emarites'])
    test(get_countries_traveled(net, 'Zehra'), ['Russia', 'Malaysia', 'Italy'])
    test(get_countries_traveled(net, 'Sameera'), ['Afghanistan', 'New Zealand', 'Korea', 'Russia'])
    test(get_countries_traveled(net, 'Kashif'), ['Russia', 'Malaysia'])
    test(get_countries_traveled(net, 'Samar'), ['Saudi Arabia', 'Indonesia', 'Iran'])
    test(get_countries_traveled(net, 'Aisha'), None)

def test_get_secondary_connections():
    test(sorted(get_secondary_connections(net, 'Usama')), sorted(list(set(['Sumaira', 'Zehra', 'Samar', 'Marium', 'Mohsin', 'Bari', 'Sameera', 'Kashif', 'Usama', 'Bari', 'Saeed']))))
    test(sorted(get_secondary_connections(net, 'Saeed')), sorted(list(set(['Usama', 'Zehra', 'Marium', 'Samar', 'Saeed', 'Sumaira', 'Usama', 'Aaliya', 'Mohsin', 'Kashif', 'Saeed']))))
    test(sorted(get_secondary_connections(net, 'Marium')), sorted(list(set(['Usama', 'Bari', 'Saeed', 'Zehra', 'Sumaira', 'Zehra', 'Samar', 'Marium']))))
    test(sorted(get_secondary_connections(net, 'Sumaira')), sorted(list(set(['Saeed', 'Aaliya', 'Mohsin', 'Marium', 'Samar', 'Saeed']))))
    test(sorted(get_secondary_connections(net, 'Aaliya')), sorted(list(set(['Usama', 'Bari', 'Saeed', 'Zehra', 'Usama', 'Mohsin', 'Bari', 'Usama', 'Samar', 'Kashif', 'Zehra']))))
    test(sorted(get_secondary_connections(net, 'Mohsin')), sorted(list(set(['Saeed', 'Aaliya', 'Mohsin', 'Zehra', 'Usama', 'Mohsin', 'Sumaira', 'Zehra', 'Samar', 'Marium']))))
    test(sorted(get_secondary_connections(net, 'Bari')), sorted(list(set(['Marium', 'Samar', 'Saeed', 'Saeed', 'Aaliya', 'Mohsin', 'Usama', 'Bari', 'Saeed']))))
    test(sorted(get_secondary_connections(net, 'Zehra')), sorted(list(set(['Mohsin', 'Kashif', 'Saeed', 'Sumaira', 'Usama', 'Aaliya', 'Sumaira', 'Zehra', 'Samar', 'Marium']))))
    test(sorted(get_secondary_connections(net, 'Sameera')), sorted(list(set(['Zehra', 'Usama', 'Mohsin', 'Saeed', 'Aaliya', 'Mohsin', 'Sumaira', 'Usama', 'Aaliya', 'Zehra']))))
    test(sorted(get_secondary_connections(net, 'Kashif')), sorted(list(set(['Marium', 'Samar', 'Saeed']))))
    test(sorted(get_secondary_connections(net, 'Samar')), sorted(list(set(['Usama', 'Zehra', 'Saeed', 'Aaliya', 'Mohsin', 'Mohsin', 'Bari', 'Sameera', 'Kashif']))))

def test_count_common_connections():
    test(count_common_connections(net, "Usama", "Saeed"), 0)
    test(count_common_connections(net, "Saeed", "Usama"), 0)

    test(count_common_connections(net, "Usama", "Marium"), 2)
    test(count_common_connections(net, "Marium", "Usama"), 2)

    test(count_common_connections(net, "Usama", "Sumaira"), 0)
    test(count_common_connections(net, "Sumaira", "Usama"), 0)

    test(count_common_connections(net, "Usama", "Aaliya"), 1)
    test(count_common_connections(net, "Aaliya", "Usama"), 1)

    test(count_common_connections(net, "Usama", "Mohsin"), 1)
    test(count_common_connections(net, "Mohsin", "Usama"), 1)

    test(count_common_connections(net, "Usama", "Bari"), 1)
    test(count_common_connections(net, "Bari", "Usama"), 1)

    test(count_common_connections(net, "Usama", "Zehra"), 1)
    test(count_common_connections(net, "Zehra", "Usama"), 1)

    test(count_common_connections(net, "Usama", "Sameera"), 0)
    test(count_common_connections(net, "Sameera", "Usama"), 0)


    test(count_common_connections(net, "Usama", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Usama"), 0)

    test(count_common_connections(net, "Usama", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Usama"), 1)

    test(count_common_connections(net, "Saeed", "Marium"), 0)
    test(count_common_connections(net, "Marium", "Saeed"), 0)

    test(count_common_connections(net, "Saeed", "Sumaira"), 1)
    test(count_common_connections(net, "Sumaira", "Saeed"), 1)

    test(count_common_connections(net, "Saeed", "Aaliya"), 0)
    test(count_common_connections(net, "Aaliya", "Saeed"), 0)

    test(count_common_connections(net, "Saeed", "Mohsin"), 0)
    test(count_common_connections(net, "Mohsin", "Saeed"), 0)

    test(count_common_connections(net, "Saeed", "Bari"), 1)
    test(count_common_connections(net, "Bari", "Saeed"), 1)

    test(count_common_connections(net, "Saeed", "Zehra"), 2)
    test(count_common_connections(net, "Zehra", "Saeed"), 2)

    test(count_common_connections(net, "Saeed", "Sameera"), 1)
    test(count_common_connections(net, "Sameera", "Saeed"), 1)

    test(count_common_connections(net, "Saeed", "Kashif"), 1)
    test(count_common_connections(net, "Kashif", "Saeed"), 1)

    test(count_common_connections(net, "Saeed", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Saeed"), 1)

    test(count_common_connections(net, "Marium", "Sumaira"), 0)
    test(count_common_connections(net, "Sumaira", "Marium"), 0)

    test(count_common_connections(net, "Marium", "Aaliya"), 2)
    test(count_common_connections(net, "Aaliya", "Marium"), 2)

    test(count_common_connections(net, "Marium", "Mohsin"), 1)
    test(count_common_connections(net, "Mohsin", "Marium"), 1)

    test(count_common_connections(net, "Marium", "Bari"), 1)
    test(count_common_connections(net, "Bari", "Marium"), 1)

    test(count_common_connections(net, "Marium", "Zehra"), 1)
    test(count_common_connections(net, "Zehra", "Marium"), 1)

    test(count_common_connections(net, "Marium", "Sameera"), 1)
    test(count_common_connections(net, "Sameera", "Marium"), 1)

    test(count_common_connections(net, "Marium", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Marium"), 0)

    test(count_common_connections(net, "Marium", "Samar"), 0)
    test(count_common_connections(net, "Samar", "Marium"), 0)

    test(count_common_connections(net, "Sumaira", "Aaliya"), 0)
    test(count_common_connections(net, "Aaliya", "Sumaira"), 0)

    test(count_common_connections(net, "Sumaira", "Mohsin"), 1)
    test(count_common_connections(net, "Mohsin", "Sumaira"), 1)

    test(count_common_connections(net, "Sumaira", "Bari"), 2)
    test(count_common_connections(net, "Bari", "Sumaira"), 2)

    test(count_common_connections(net, "Sumaira", "Zehra"), 0)
    test(count_common_connections(net, "Zehra", "Sumaira"), 0)

    test(count_common_connections(net, "Sumaira", "Sameera"), 1)
    test(count_common_connections(net, "Sameera", "Sumaira"), 1)

    test(count_common_connections(net, "Sumaira", "Kashif"), 1)
    test(count_common_connections(net, "Kashif", "Sumaira"), 1)

    test(count_common_connections(net, "Sumaira", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Sumaira"), 1)

    test(count_common_connections(net, "Aaliya", "Mohsin"), 1)
    test(count_common_connections(net, "Mohsin", "Aaliya"), 1)

    test(count_common_connections(net, "Aaliya", "Bari"), 1)
    test(count_common_connections(net, "Bari", "Aaliya"), 1)

    test(count_common_connections(net, "Aaliya", "Zehra"), 0)
    test(count_common_connections(net, "Zehra", "Aaliya"), 0)

    test(count_common_connections(net, "Aaliya", "Sameera"), 2)
    test(count_common_connections(net, "Sameera", "Aaliya"), 2)

    test(count_common_connections(net, "Aaliya", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Aaliya"), 0)

    test(count_common_connections(net, "Aaliya", "Samar"), 0)
    test(count_common_connections(net, "Samar", "Aaliya"), 0)

    test(count_common_connections(net, "Mohsin", "Bari"), 1)
    test(count_common_connections(net, "Bari", "Mohsin"), 1)

    test(count_common_connections(net, "Mohsin", "Zehra"), 1)
    test(count_common_connections(net, "Zehra", "Mohsin"), 1)

    test(count_common_connections(net, "Mohsin", "Sameera"), 2)
    test(count_common_connections(net, "Sameera", "Mohsin"), 2)

    test(count_common_connections(net, "Mohsin", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Mohsin"), 0)

    test(count_common_connections(net, "Mohsin", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Mohsin"), 1)

    test(count_common_connections(net, "Bari", "Zehra"), 0)
    test(count_common_connections(net, "Zehra", "Bari"), 0)

    test(count_common_connections(net, "Bari", "Sameera"), 1)
    test(count_common_connections(net, "Sameera", "Bari"), 1)

    test(count_common_connections(net, "Bari", "Kashif"), 1)
    test(count_common_connections(net, "Kashif", "Bari"), 1)

    test(count_common_connections(net, "Bari", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Bari"), 1)

    test(count_common_connections(net, "Zehra", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Zehra"), 0)

    test(count_common_connections(net, "Zehra", "Samar"), 0)
    test(count_common_connections(net, "Samar", "Zehra"), 0)

    test(count_common_connections(net, "Sameera", "Zehra"), 1)
    test(count_common_connections(net, "Zehra", "Sameera"), 1)


    test(count_common_connections(net, "Sameera", "Kashif"), 0)
    test(count_common_connections(net, "Kashif", "Sameera"), 0)

    test(count_common_connections(net, "Sameera", "Samar"), 1)
    test(count_common_connections(net, "Samar", "Sameera"), 1)


    test(count_common_connections(net, "Kashif", "Samar"), 0)
    test(count_common_connections(net, "Samar", "Kashif"), 0)

    test(count_common_connections(net, "Aisha", "Samar"), False)
    test(count_common_connections(net, "Kashif", "Arif"), False)
    test(count_common_connections(net, "ABC", "DEF"), False)

def test_find_path_to_friend():
    test2(find_path_to_friend(net, "Usama", "Saeed"), usamatosaeed) 
    test2(find_path_to_friend(net, "Saeed", "Usama"), saeedtousama)

    test2(find_path_to_friend(net, "Usama", "Marium"), usamatomarium)
    test2(find_path_to_friend(net, "Marium", "Usama"), mariumtousama)

    test2(find_path_to_friend(net, "Usama", "Sumaira"), usamatosumaira)
    test2(find_path_to_friend(net, "Sumaira", "Usama"), sumairatousama)

    test2(find_path_to_friend(net, "Usama", "Aaliya"), usamatoaaliya)
    test2(find_path_to_friend(net, "Aaliya", "Usama"), aaliyatousama)

    test2(find_path_to_friend(net, "Usama", "Mohsin"), usamatomohsin)
    test2(find_path_to_friend(net, "Mohsin", "Usama"), mohsintousama)

    test2(find_path_to_friend(net, "Usama", "Bari"), usamatobari)
    test2(find_path_to_friend(net, "Bari", "Usama"), baritousama)

    test2(find_path_to_friend(net, "Usama", "Zehra"), usamatozehra)
    test2(find_path_to_friend(net, "Zehra", "Usama"), zehratousama)

    test2(find_path_to_friend(net, "Usama", "Sameera"), usamatosameera)
    test2(find_path_to_friend(net, "Sameera", "Usama"), sameeratousama)

    test2(find_path_to_friend(net, "Usama", "Kashif"), usamatokashif)
    test2(find_path_to_friend(net, "Kashif", "Usama"), kashiftousama)

    test2(find_path_to_friend(net, "Usama", "Samar"), usamatosamar)
    test2(find_path_to_friend(net, "Samar", "Usama"), samartousama)

    test2(find_path_to_friend(net, "Saeed", "Marium"), saeedtomarium)
    test2(find_path_to_friend(net, "Marium", "Saeed"), mariumtosaeed)

    test2(find_path_to_friend(net, "Saeed", "Sumaira"), saeedtosumaira)
    test2(find_path_to_friend(net, "Sumaira", "Saeed"), sumairatosaeed)

    test2(find_path_to_friend(net, "Saeed", "Aaliya"), saeedtoaaliya)
    test2(find_path_to_friend(net, "Aaliya", "Saeed"), aaliyatosaeed)

    test2(find_path_to_friend(net, "Saeed", "Mohsin"), saeedtomohsin)
    test2(find_path_to_friend(net, "Mohsin", "Saeed"), mohsintosaeed)

    test2(find_path_to_friend(net, "Saeed", "Bari"), saeedtobari)
    test2(find_path_to_friend(net, "Bari", "Saeed"), baritosaeed)

    test2(find_path_to_friend(net, "Saeed", "Zehra"), saeedtozehra)
    test2(find_path_to_friend(net, "Zehra", "Saeed"), zehratosaeed)

    test2(find_path_to_friend(net, "Saeed", "Sameera"), saeedtosameera)
    test2(find_path_to_friend(net, "Sameera", "Saeed"), sameeratosaeed)

    test2(find_path_to_friend(net, "Saeed", "Kashif"), saeedtokashif)
    test2(find_path_to_friend(net, "Kashif", "Saeed"), kashiftosaeed)

    test2(find_path_to_friend(net, "Saeed", "Samar"), saeedtosamar)
    test2(find_path_to_friend(net, "Samar", "Saeed"), samartosaeed)

    test2(find_path_to_friend(net, "Marium", "Sumaira"), mariumtosumaira)
    test2(find_path_to_friend(net, "Sumaira", "Marium"), sumairatomarium)

    test2(find_path_to_friend(net, "Marium", "Aaliya"), mariumtoaaliya)
    test2(find_path_to_friend(net, "Aaliya", "Marium"), aaliyatomarium)

    test2(find_path_to_friend(net, "Marium", "Mohsin"), mariumtomohsin)
    test2(find_path_to_friend(net, "Mohsin", "Marium"), mohsintomarium)

    test2(find_path_to_friend(net, "Marium", "Bari"), mariumtobari)
    test2(find_path_to_friend(net, "Bari", "Marium"), baritomarium)

    test2(find_path_to_friend(net, "Marium", "Zehra"), mariumtozehra)
    test2(find_path_to_friend(net, "Zehra", "Marium"), zehratomarium)

    test2(find_path_to_friend(net, "Marium", "Sameera"), mariumtosameera)
    test2(find_path_to_friend(net, "Sameera", "Marium"), sameeratomarium)

    test2(find_path_to_friend(net, "Marium", "Kashif"), mariumtokashif)
    test2(find_path_to_friend(net, "Kashif", "Marium"), kashiftomarium)

    test2(find_path_to_friend(net, "Marium", "Samar"), mariumtosamar)
    test2(find_path_to_friend(net, "Samar", "Marium"), samartomarium)

    test2(find_path_to_friend(net, "Sumaira", "Aaliya"), sumairatoaaliya)
    test2(find_path_to_(net, "Aaliya", "Sumaira"), aaliyatosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Mohsin"), sumairatomohsin)
    test2(find_path_to_friend(net, "Mohsin", "Sumaira"), mohsintosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Bari"), sumairatobari)
    test2(find_path_to_friend(net, "Bari", "Sumaira"), baritosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Zehra"), sumairatozehra)
    test2(find_path_to_friend(net, "Zehra", "Sumaira"), zehratosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Sameera"), sumairatosameera)
    test2(find_path_to_friend(net, "Sameera", "Sumaira"), sameeratosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Kashif"), sumairatokashif)
    test2(find_path_to_friend(net, "Kashif", "Sumaira"), kashiftosumaira)

    test2(find_path_to_friend(net, "Sumaira", "Samar"), sumairatosamar)
    test2(find_path_to_friend(net, "Samar", "Sumaira"), samartosumaira)

    test2(find_path_to_friend(net, "Aaliya", "Mohsin"), aaliyatomohsin)
    test2(find_path_to_friend(net, "Mohsin", "Aaliya"), mohsintoaaliya)

    test2(find_path_to_friend(net, "Aaliya", "Bari"), aaliyatobari)
    test2(find_path_to_friend(net, "Bari", "Aaliya"), baritoaaliya)

    test2(find_path_to_friend(net, "Aaliya", "Zehra"), aaliyatozehra)
    test2(find_path_to_friend(net, "Zehra", "Aaliya"), zehratoaaliya)

    test2(find_path_to_friend(net, "Aaliya", "Sameera"), aaliyatosameera)
    test2(find_path_to_friend(net, "Sameera", "Aaliya"), sameeratoaaliya)

    test2(find_path_to_friend(net, "Aaliya", "Kashif"), aaliyatokashif)
    test2(find_path_to_friend(net, "Kashif", "Aaliya"), kashiftoaaliya)

    test2(find_path_to_friend(net, "Aaliya", "Samar"), aaliyatosamar)
    test2(find_path_to_friend(net, "Samar", "Aaliya"), samartoaaliya)

    test2(find_path_to_friend(net, "Mohsin", "Bari"), mohsintobari)
    test2(find_path_to_friend(net, "Bari", "Mohsin"), baritomohsin)

    test2(find_path_to_friend(net, "Mohsin", "Zehra"), mohsintozehra)
    test2(find_path_to_friend(net, "Zehra", "Mohsin"), zehratomohsin)

    test2(find_path_to_friend(net, "Mohsin", "Sameera"), mohsintosameera)
    test2(find_path_to_friend(net, "Sameera", "Mohsin"), sameeratomohsin)

    test2(find_path_to_friend(net, "Mohsin", "Kashif"), mohsintokashif)
    test2(find_path_to_friend(net, "Kashif", "Mohsin"), kashiftomohsin)

    test2(find_path_to_friend(net, "Mohsin", "Samar"), mohsintosamar)
    test2(find_path_to_friend(net, "Samar", "Mohsin"), samartomohsin)

    test2(find_path_to_friend(net, "Bari", "Zehra"), baritozehra)
    test2(find_path_to_friend(net, "Zehra", "Bari"), zehratobari)

    test2(find_path_to_friend(net, "Bari", "Sameera"), baritosameera)
    test2(find_path_to_friend(net, "Sameera", "Bari"), sameeratobari)

    test2(find_path_to_friend(net, "Bari", "Kashif"), baritokashif)
    test2(find_path_to_friend(net, "Kashif", "Bari"), kashiftobari)

    test2(find_path_to_friend(net, "Bari", "Samar"), baritosamar)
    test2(find_path_to_friend(net, "Samar", "Bari"), samartobari)

    test2(find_path_to_friend(net, "Zehra", "Kashif"), zehratokashif)
    test2(find_path_to_friend(net, "Kashif", "Zehra"), kashiftozehra)

    test2(find_path_to_friend(net, "Zehra", "Samar"), zehratosamar)
    test2(find_path_to_friend(net, "Samar", "Zehra"), samartozehra)

    test2(find_path_to_friend(net, "Sameera", "Zehra"), sameeratozehra)
    test2(find_path_to_friend(net, "Zehra", "Sameera"), zehratosameera)

    test2(find_path_to_friend(net, "Sameera", "Kashif"), sameeratokashif)
    test2(find_path_to_friend(net, "Kashif", "Sameera"), kashiftosameera)

    test2(find_path_to_friend(net, "Sameera", "Samar"), sameeratosamar)
    test2(find_path_to_friend(net, "Samar", "Sameera"), samartosameera)

    test2(find_path_to_friend(net, "Kashif", "Samar"), kashiftosamar)
    test2(find_path_to_friend(net, "Samar", "Kashif"), samartokashif)

    test(find_path_to_friend(net, "Aisha", "Samar"), None)  # None
    test(find_path_to_friend(net, "Kashif", "Arif"), None) # None
    test(find_path_to_friend(net, "ABC", "DEF"), None)    # None

def create_data_structure(string_input):
    network = {}
    
    lines = string_input.split('.')
    lines.pop()
    #print(lines)
    
    for i in lines:
        
        if ' is connected to ' in i:
            users = []
            a = i.split(' is connected to ')
            x= a[-1].split(', ')
            del a[-1]
            a.append(x)
            #print(x)
            #print(a)
            for j in x:
                users.append(j)
            #print(users)
            
        else:
            country = []
            b = i.split(' traveled to ')
            y = b[-1].split(', ')
            del b[-1]
            b.append(y)
            #print(b)
            for j in y:
                country.append(j)
            #print(country)
            t=(users,country)
            #print(t)
            network[a[0]]=t
        #print(users,country)

    return network
example_input="Usama is connected to Saeed, Aaliya, Mohsin.\
Usama traveled to Italy, Japan, Korea.\
Saeed is connected to Sumaira, Zehra, Samar, Marium.\
Saeed traveled to China, Afghanistan.\
Marium is connected to Mohsin, Kashif, Saeed.\
Marium traveled to Japan, USA, Iran.\
Sumaira is connected to Usama, Zehra.\
Sumaira traveled to Japan, Saudi Arabia.\
Aaliya is connected to Mohsin, Bari, Sameera, Kashif.\
Aaliya traveled to India, USA, Malaysia.\
Mohsin is connected to Usama, Bari, Saeed.\
Mohsin traveled to Iran, Indonesia, Afghanistan.\
Bari is connected to Zehra, Usama, Mohsin.\
Bari traveled to Japan, India, China, United Arab Emarites.\
Zehra is connected to Marium, Samar, Saeed.\
Zehra traveled to Russia, Malaysia, Italy.\
Sameera is connected to Bari, Usama, Samar, Kashif.\
Sameera traveled to Afghanistan, New Zealand, Korea, Russia.\
Kashif is connected to Zehra.\
Kashif traveled to Russia, Malaysia.\
Samar is connected to Sumaira, Usama, Aaliya.\
Samar traveled to Saudi Arabia, Indonesia, Iran."
net = create_data_structure(example_input)

test_get_connections()
test_get_countries_traveled()
