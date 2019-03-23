label language_chooser:
    scene black
    
    menu:
        "English":
            $ persistent.lang = "english"
        "French":
            $ persistent.lang = "french"

    $ renpy.utter_restart()


label eegg:
    
    scene black
    with fade
    "Congratulations! You just unlocked the Big Macintosh mode!"
    "Are you happy?"
    $playername = "Big Macintosh"   
    menu eeggfun:
 
        "Eeyup":
            p "Eeyup"
            "That's the spirit."
        "Nope":
            p "Nope."
            "Your happiness is not relevant anyway."
    "Now, let's go back to the crossroad and have fun!"
    
    scene bg ponyville road
    with fade
    
    play music "Music/outdoors.mp3"
    
    p "Eeyup?"
    
    menu bm_place_choice:
        "Library":
            $0#Useless line is useless. Except for the interpreter.
        "Sugar Cube Corner":
            $0#Useless line is useless. Except for the interpreter.
        "Apple barn":
            $0#Useless line is useless. Except for the interpreter.
        "Rainbow's cloud":
            $0#Useless line is useless. Except for the interpreter.
        "Carousel Boutique":
            $0#Useless line is useless. Except for the interpreter.
        "Fluttershy's cottage":
            $0#Useless line is useless. Except for the interpreter.
    scene black
    with fade
    stop music fadeout 1.0
    "You were going to leave the crossroad when suddenly..."
    
    u "WAIIIIIIIIIIT!"

    scene bg ponyville road
    with fade
    play music "Music/outdoors.mp3"
    "What's that? It's not in the script!"
    p "Eeyup."
    
    show CMC happy
    with dissolve
    
    cmc "Big Mac! You are here!"
    p "Eeyup."
    sb "You don't have any plan for tonight, do you?"
    p "Nope."
    s "Great! We found you the perfect date! Promise!"
    ab "Yah! Ah admit we didn' do well last time..."
    s "...With Miss Cherilee and all..."
    sb "...But this time, no love poison! Just go there and look if you too are happy together!"
    
    cmc "What do you think, Big Mac? Do you accept?"
    
    menu cmcdecision:
        "\"Eeyup.\"":
            p "Eeyup."
            show CMC highfive
            with dissolve
            cmc "CUTIE MARK CRUSADERS, SHIPPING MAKERS! YAAAY!"
            show CMC zoom cutie
            with dissolve
            sb "You won't regret it!"
            ab "Promise!"
            
        "\"Nope.\"":
            p "Nope."
            show CMC cry
            with dissolve
            cmc "PLEAAAAAAAAAAAAAAAAAAAAAAASE!"
            show CMC happy
            with dissolve
            jump cmcdecision
            
    scene black
    with dissolve
    stop music fadeout 1.0
    "And the three fillies took you to the edge of the town, with nothing else than trees, grass and..."

    scene bg bushes hill
    with fade
    play music "Music/outdoors.mp3"
    show braeburn chillin
    with dissolve
    
    b "Heeeeey! Welcome to Appleloosa cousin!"
    p "Nope."
    b "Yah, that's true. We're still near the good ol' Ponyville. Anyway, are yah there 'cause of the lil' fillies too?"
    p "Eeyup."    
    
    if(p_aj == "sugarcube"):                    # braeburn met first visit, received sugarcube
        b "Ah would be willin' to give it a chance. D'yah want to try?"
    elif(appl4 == True):                        # braeburn met 2nd visit, gave sunglasses
        b "Ah tried hard to have yar attention, even tried sunglasses. D'yah want to try now?"
    else:                                       # braeburn met second visit, asked sunglasses
        b "Ah tried hard to have yar attention, even thought of sunglasses. D'yah want to try now?"

    
    menu braeburnchoice:
        "\"Eeyup.\"":
            p "Eeyup."
            b "And Ah thought yah would never say it, ol' big chunk of love. Come here!"
            
            scene end06
            with fade
            stop music fadeout 1.0
            show CMC awe
            with dissolve
            
            "And then some stallions hugging. Kissing. And doing stuff. With kids watching."
            
            cmc "Awwwwwwww!"
            
            "Girls, you are creepy."
            "--Braeburn ending 0--"
            jump credits
            
        "\"Nope.\"":
            p "Nope."
            b "Come on cousin! Gimme a kiss!"
            p "Nope."
            
            show braeburn chillin:
                linear 1.0 xalign 0.2
            show redheart angry:
                xalign 0.8 yalign 1.0
            with dissolve
            nr "BRAEBURN! Stop drinking, you are not allowed to!"
            b "Come on nurse! That's just a glass... And now gimme a hug!"
            nr "You are drunk Braeburn. And now you won't be able to take your medication for tonight and that's bad."
            p "Eeyup."
            show redheart grumpy
            with dissolve
            nr "Sorry, I didn't notice you... Big Mac, isn't it? Braeburn catched some kind of local flu and shouldn't have leaved the hospital as he did. But looking at you now, I kind of understand his motives."
            show redheart happy
            with dissolve
            nr "I'm going to return to the hospital with him, would you like to come with us?"
            p "Eeyup."
            nr "Let's go then!"
            
            scene end40
            with fade
            
            "And after putting Braeburn in his bed again, the nurse gave you a kiss on the cheek. You will be able to see that in a future version... But everything went better than expected."
            
            "--Nurse Redheart ending--"
            
            jump credits
            
label credits:
    
    scene black
    with fade
    pp "You reached the end!"
    aj "Good for ya!"
    r "But there is more to see."
    ts "Except if you already have seen everything."
    rd "But you wouldn't read the credits anymore."
    fs "Unless you really like us! And that's a great proof of love! Thank you!"
    "Love? I would have said stupidi-"
    cmc "Shhhh, here it comes!"
    play music "Music/credits.mp3"
    scene black 
    with Pause(1)

    show credit1 with dissolve
    with Pause(4)

    scene black with dissolve
    with Pause(1)
    
    scene credit2 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
        
    show credit3 with dissolve
    with Pause(4)
     
    scene black with dissolve
    with Pause(1)
       
    scene credit4 with dissolve
    with Pause(4)
     
    scene black with dissolve
    with Pause(1)
       
    show credit5 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
       
    show credit6 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
       
    show credit7 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
       
    show credit8 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
       
    show credit9 with dissolve
    with Pause(4)
    
    scene black with dissolve
    with Pause(1)
       
    show credit10 with dissolve


 #   scene bg view of ponyville
 #   with fade
 #   
 #   "My Little Pony is property of Hasbro, please don't send us a C&D letter Hasbro! You are not affiliated with us and certainly don't approve the silliness of the game, we already know, it was just for fun! Same for you THQ and Violition! We now that the title is a bad joke with the Super Ethical Reality Climax, don't sue us for bad humour."
 #
 #   scene black
 #   with fade
 #   
 #   "Erm. The game engine has been provided by the Ren'Py team, they are the secret heroes that deserve a bit of praise. Go read the README if you want to  have a link to their website."
 #   show caramel truffle with dissolve
 #   "The scripting itself is a work of Caramel Truffle though. He also wrote the scenarios. And this text. Let's stop being pretentious for a minute, I am Caramel Truffle, author of every textual thing you may have liked or hated through the game. Every typo too, since I don't really have a proofreader."
 #   
 #   hide caramel truffle with dissolve
 #   show ginster steed with dissolve
 #   "Ginster steed has composed the music! Praise him, without his help you would have put your computer on mute because of the horrible automatically-generated tunes!"
 #   
 #   "The deviantArt Pony Vector Club did the drawings. Go read the README for a link, they do great stuff! Of course, having an artist drawing specifically for the game would have been better, but this is still an alpha. Or beta, if I forgot to change the credits. Anyway, the final version will have drawings done specifically for it, so check it out if you liked the game."
 #   scene black with dissolve
 #   "Did I forgot anyone? Ah, yes, you. You just decided to spend a fraction of your life on this. That might not be clever, but I appreciate it. We appreciate it. Thank you!"
    
    ""