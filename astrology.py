import os
import sys


def astro():

    query = input("Astrology: ")
    os.system('python ~/.grungegirl/astrology.py')
# Signs

    if query.lower() == "aries":
        os.system("python ~/.grungegirl/astrology/aries.py")

    elif query.lower() == "taurus":
        os.system('python ~/.grungegirl/astrology/taurus.py')

    elif query.lower() == 'gemini':
        os.system('python ~/.grungegirl/astrology/gemini.py')

    elif query.lower() == 'cancer':
        os.system('python ~/.grungegirl/astrology/cancer.py')

    elif query.lower() == 'leo':
        os.system('python ~/.grungegirl/astrology/leo.py')

    elif query.lower() == 'virgo':
        os.system('python ~/.grungegirl/astrology/virgo.py')

    elif query.lower() == 'libra':
        os.system('python ~/.grungegirl/astrology/libra.py')

    elif query.lower() == 'scorpio':
        os.system('python ~/.grungegirl/astrology/scorpio.py')

    elif query.lower() == 'sagittarius':
        os.system('python ~/.grungegirl/astrology/sag.py')

    elif query.lower() == 'capricorn':
        os.system('python ~/.grungegirl/astrology/cap.py')

    elif query.lower() == 'capricorn':
        os.system('python ~/.grungegirl/astrology/cap.py')

    elif query.lower() == 'aquarius':
        os.system('python ~/.grungegirl/astrology/aqua.py')

# Houses

    elif query.lower() == 'hs1':
        os.system('python ~/.grungegirl/astrology/houses/firsthouse.py')

    elif query.lower() == 'hs2':
        os.system('python ~/.grungegirl/astrology/houses/secondhouse.py')

    elif query.lower() == 'hs3':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')

    elif query.lower() == 'hs4':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'hs5':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'hs6':
        os.system('python ~/.grungegirl/astrology/houses/sixthhhouse.py')

    elif query.lower() == 'hs7':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'hs8':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'hs9':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'hs10':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'hs11':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'hs12':
        os.system('python ~/.grungegirl/astrology/houses/twelfthhouse.py')

# Planets

    elif query.lower() == 'sun':
        os.system('python ~/.grungegirl/astrology/planets/sun.py')

    elif query.lower() == 'earth':
        os.system('python ~/.grungegirl/astrology/planets/earth.py')

    elif query.lower() == 'mercury':
        os.system('python ~/.grungegirl/astrology/planets/mercury.py')

    elif query.lower() == 'moon':
        os.system('python ~/.grungegirl/astrology/planets/moon.py')

    elif query.lower() == 'venus':
        os.system('python ~/.grungegirl/astrology/planets/venus.py')
# Exit

    elif query.lower() == 'exit':
        exit()
        os.system('python ~/.grungegirl/main.py')

    elif query.lower() == 'clear':
        exit()
        os.system('python ~/.grungegirl/main.py')


astro()
