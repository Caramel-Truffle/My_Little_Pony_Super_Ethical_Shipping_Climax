label outdoors:
    stop music fadeout 1.0
    
    scene bg ponyville road
    with fade
    if seenintro == False:
        $ nb_lock = 0
        
        play music "Music/outdoors.mp3"
        p "What do- ... Never mind."
        p "Where am I? A cartoon background? It looks like Ponyville... This dream is really messed up."
        $ seenintro = True
        jump place_choice
        
    elif(nb_lock==6):
        "Hey, you really messed up!"
        p "Stop breaking the fourth wall, it isn't funny anymore."
        "It doesn't matter, you've just lost! Nopony here is willing to talk to you anymore!"
        p "So, it's the...?"
        "Yes."
        "--Bad end--"
        jump credits
    else:
        play music "Music/outdoors.mp3"
        p "Where should I go now?"
    
        menu place_choice:
            "Library":
                jump library
                
            "Sugarcube Corner":
                jump sugarcubecorner
                
            "Apple barn":
                jump applebarn
                
            "Rainbow's cloud" if ((playername!="Pinkie Pie")and(playername!="Applejack")):
                jump dashcloud
                
            "Carousel Boutique":
                jump carouselboutique
                
            "Fluttershy's cottage":
                jump fluttercottage
            
return