sb2m3u
======

Linn Songbox Remote Playlist to M3U conversion

Creating playlists in Kinsky is great, I'd like to save them remotely which you can do if you use Linn's Songbox. Each track on the playlist is a URI which flexibly allows creating a playlist from multiple media servers additionally the URIs for the metadata is also stored along with the item in the playlist. This means if the URI changes by a mediaserver rescan or the metadata is changed, the track loses valuable information or is lost forever. However, converting to m3u requires reverse mapping a track URI to a local filepath. Luckily Minimserver uses a URI which can easily be converted back into a filepath. 

These scripts convert a playlist of Minimserver served tracks, stored in a Remote Linn Songbox playlist to an m3u file. Once converted it is stored in a 'Playlists' folder which can be picked up by Minimserver when rescanned (which this script invokes). This allows your Linn Songbox playlists to be accessible from any device and protected against metadata and URI changes from your mediaserver. 

It will continue to watch changes in your Songbox mirroring new playlists, edits and deletes as m3u files. 

This assumes the following configuration:

* Linux Server
* inotify-tools installed
* Minimserver running on the same machine as the collection of music. 
* Linn Songbox Installation - where its configuration storage is available from the Linux machine
* Linn Songbox is used for storing playlists, but not serving music. This is because Songbox uses a random GUID whereas Minimserver uses a URI which can be converted back to a filepath. 
* All music files are contained within a single root
* sb2m3u installed in `/opt/sb2m3u`

WARNING
=======

If you have an existing 'Playlists' folder under your music folder, m3u files will be deleted by this script. This is to support deleting a remote Songbox playlist synchronising the m3u delete. 

INSTALLATION
============

Copy `convert_playlists.sh` and `sb2m3u.py` into `/opt/sb2m3u`
There is a service script in init which you can copy into `/etc/init` on Ubuntu - edit the script to use a correct username

CONFIGURATION
=============

In `convert_playlists.sh`
Configure:
`WATCH_DIR` to point to your Songbox playlists folder
`MUSIC_DIR` to point to the root of your music

START
=====
If you have installed the service script:
`sudo service playlists start`

Otherwise:
`/opt/sb2m3u/convert_playlists.sh`

