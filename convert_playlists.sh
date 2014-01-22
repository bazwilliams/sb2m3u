#!/bin/sh
WATCH_DIR=/home/barry/.config/Linn/Linn\ Songbox/Network/MediaServer/PlaylistManager/
MUSIC_DIR=/mnt/media/music/
MUSIC_PLAYLISTS=$MUSIC_DIR/Playlists
SCRIPTS=/opt/sb2m3u
MINIMSERVER_URL=http://192.168.1.127:9790/index.html

while 
	find $MUSIC_PLAYLISTS -type f -name *.m3u -exec rm {} \;
	$SCRIPTS/sb2m3u.py -i "$WATCH_DIR" -m "$MUSIC_DIR"
	wait 5
	curl -s -o /dev/null -d sub=Rescan+library -d dir= $MINIMSERVER_URL 2>&1
	$(inotifywait -qq -e modify,move,create,delete "$WATCH_DIR")
do
	:
done
