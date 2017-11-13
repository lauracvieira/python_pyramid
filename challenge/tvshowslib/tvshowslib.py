# -*- coding: utf-8 -*-
tvshows = ["Shameless", "Bojack Horseman", "Grey's Anatomy", "Modern Family", "The Handmaid's Tale", "Rick and Morty", "The Middle", "Will and Grace", "Friends", "The Office"]

def get_tvshows():
    return tvshows

def get_tvshow(show_number):
    tvshow = ''
    try:
        return tvshows[int(show_number)]
    except:
        return "No show with this number"
