#!/usr/bin/env python

# Setting the stage
import os

# The V8 Engine
def v8():

    os.system('yay -s browsh')

    os.system('mkdir ~/grungegirl')
    print("grungegirl created.")

    os.system('cp main.py ~/grungegirl')
    print("exporting drugs from columbia.")
    print(" ")
    os.system('cp alc.py ~/grungegirl')
    os.system('cp ambien.py ~/grungegirl')
    os.system('cp coke.py ~/grungegirl')
    os.system('cp dph.py ~/grungegirl')
    os.system('cp dxm.py ~/grungegirl')
    os.system('cp fent.py ~/grungegirl')
    os.system('cp mdma.py ~/grungegirl')
    os.system('cp meth.py ~/grungegirl')
    os.system('cp pey.py ~/grungegirl')
    os.system('cp salvia.py ~/grungegirl')
    os.system('cp shrooms.py ~/grungegirl')
    print("harvesting shrooms.")
    os.system('cp speed.py ~/grungegirl')
    os.system('cp weed.py ~/grungegirl')
    os.system('cp xanax.py ~/grungegirl')
    os.system('cp query.py ~/grungegirl')
    os.system('cp bind-alias.sh ~/grungegirl')

    os.system('sh ~/grungegirl/bind-alias.sh')
    os.system('echo "browsh needed to use web search."')

# verify

verify = input("Are you root (y/n)? ")

if verify == "n":
    exit()

if verify == "y":
    print("Starting program.")

    v8()