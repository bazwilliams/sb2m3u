#!/usr/bin/python
from lxml import etree
import os;
import re;
import sys, getopt

_CHARSET = "utf-8"

def hexToAscii(match):
	number = int(match.group()[1:], 16)
	return chr(number)

def process(songboxPlaylist, musicDir):
	playlistDir = os.path.join(musicDir, "Playlists")
	root = etree.parse(songboxPlaylist).getroot()
	playlistName = root.find("Name").text.encode(_CHARSET)
	if playlistName != "":
		playlist = open(os.path.join(playlistDir, playlistName + ".m3u"), "w")
		for metadataelement in root.findall("Track/Metadata"):
			metadata = etree.fromstring(metadataelement.text.encode(_CHARSET))
			track = metadata.find("{urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/}item/{urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/}res").text.encode(_CHARSET)
			track = re.sub(r'\*[0-9a-fA-F][0-9a-fA-F]', hexToAscii, track)
			track = re.sub("^http:(.)*/music/", musicDir, track)
			musicFile = os.path.relpath(track, playlistDir)
			playlist.write(musicFile + "\n")
		playlist.close();

def main(argv):
	songboxPlaylistDir = None
	musicDir = None
	
	try:
		opts, args = getopt.getopt(argv,"hi:m:",["songbox=","music="])
	except getopt.GetoptError:
		print 'sb2m3u.py -i <songboxplaylistfolder> -m <musicfolder>'
		sys.exit(2)

	if (len(opts) == 0):
		print 'sb2m3u.py -i <songboxplaylistfolder> -m <musicfolder>'
		sys.exit(2)
	

	for opt, arg in opts:
		if opt == '-h':
			print 'sb2m3u.py -i <songboxplaylistfolder> -m <musicfolder>'
			sys.exit()
		elif opt in ("-i", "--songbox"):
			songboxPlaylistDir = arg
		elif opt in ("-m", "--musicfolder"):
			musicDir = arg

	if (songboxPlaylistDir != None and musicDir != None):
		for f in os.listdir(songboxPlaylistDir):
			if f != "Toc.txt" and f.endswith(".txt"):
				process(os.path.join(songboxPlaylistDir, f), musicDir)

if __name__ == "__main__":
	main(sys.argv[1:])
