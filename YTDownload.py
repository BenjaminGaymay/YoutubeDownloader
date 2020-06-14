#!/usr/bin/env python3

from pprint import pprint
from os import chdir, getcwd, makedirs
from os.path import exists
from subprocess import run
from sys import argv
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
	if len(argv) < 3:
		print("USAGE:\n\t{} <youtube playlist link> <download repository>".format(argv[0]))
		exit(1)
	ytdPath = getcwd()
	if not exists(argv[2]):
		makedirs(argv[2])
	chdir(argv[2])
	url = argv[1]
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "html.parser")
	musics = [
	    "https://www.youtube.com" + music["href"].split('&')[0] for music in soup.find_all('a', href=True)
	    if "/watch?" in music["href"]
	]
	musics = set(musics)
	for music in musics:
		process = run(["youtube-dl", "-x", "--audio-format", "mp3", music])
	chdir(ytdPath)
