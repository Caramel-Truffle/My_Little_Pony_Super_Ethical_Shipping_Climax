label outdoors:
    $0#this is ugly, but it checks if some specific combinations are preventing further progress
    $lockety = False
    if((playername=="Applejack") or (playername=="Pinkie Pie")):
        $0#Here it's an earth pony
        $lockety_a = ( (p_fs == "seeds") and (p_ts == "astronomy") and (p_pp == "cupcake") and (p_rr == "hat")  and (p_aj == "apple")     )  #nR nF nT nP nR nA
        $lockety_b = ( (p_fs == "seeds") and (p_ts == "astronomy") and (p_pp == "muffin")  and (p_rr == "hat")  and (p_aj == "sugarcube") )  #nR  F  T nP  R nA
        $lockety_c = ( (p_fs == "tea")   and (p_ts == "xxx")                               and (p_rr == "ruby") and (p_aj == "apple")     )  # R nF nT  P nR  A
        $lockety_d = ( (p_fs == "tea")   and (p_ts == "xxx")       and (p_pp == "muffin")  and (p_rr == "ruby") and (p_aj == "sugarcube") )  # R  F  T  P  R  A
    else:
        $0#here it is not an earth pony
        $lockety_a = ( (p_rd == "dumbbell")   and (p_fs == "seeds") and (p_ts == "astronomy") and (p_pp == "cupcake") and (p_rr == "hat")  and (p_aj == "apple") )      #nR nF nT nP nR nA
        $lockety_b = ( (p_rd == "dumbbell")   and (p_fs == "tea")   and (p_ts == "xxx")       and (p_pp == "cupcake") and (p_rr == "ruby") and (p_aj == "apple") )      #nR  F  T nP  R nA
        $lockety_c = ( (p_rd == "sunglasses") and (p_fs == "seeds") and (p_ts == "astronomy") and (p_pp == "muffin")  and (p_rr == "hat")  and (p_aj == "sugarcube") )  # R nF nT  P nR  A
        $lockety_d = ( (p_rd == "sunglasses") and (p_fs == "tea")   and (p_ts == "xxx")       and (p_pp == "muffin")  and (p_rr == "ruby") and (p_aj == "sugarcube") )  # R  F  T  P  R  A
        
        
    stop music fadeout 1.0
    $lockety = lockety_a or lockety_b or lockety_c or lockety_d
    $0#"So, lockety is [lockety], lockety_a is [lockety_a], lockety_b is [lockety_b], lockety_c is [lockety_c], lockety_d is [lockety_d]"
    scene bg ponyville road
    with fade
    if seenintro == False:
        $ nb_lock = 0
        
        play music "Music/outdoors.mp3"
        p "What do- ... Never mind."
        p "Where am I? A stock photo with some filter on it? How original. Is it even supposed to look like Ponyville...? This dream is really messed up."
        $ seenintro = True
        jump place_choice
        
        
    elif(lockety):
        "Hey, you really messed up!"
        p "Stop breaking the fourth wall, it isn't funny anymore."
        "It doesn't matter, you've just lost! Nopony here is willing to talk to you anymore!"
        p "So, it's the...?"
        "Yes."
        stop music fadeout 1.0
        scene end86
        $persistent.unlock_86
        play sound "SFX/fail.mp3"
        "--Bad Ending--"
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