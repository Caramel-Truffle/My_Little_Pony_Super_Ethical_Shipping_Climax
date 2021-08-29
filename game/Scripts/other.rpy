label language_chooser:
    scene black
    
    menu:
        "English":
            $ persistent.lang = "English"
        "French":
            $ persistent.lang = "French"

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
    $cmcloop = 0
    menu cmcdecision:
        "\"Eeyup.\"":
            p "Eeyup."
            show CMC highfive
            with dissolve
            cmc "CUTIE MARK CRUSADERS, SECRET SHIPPERS! YAAAY!"
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
            $cmcloop = cmcloop + 1
            jump cmcdecision
        "I don't know" if(cmcloop==42):
            "An easter egg inside an easter egg! Wow!"
            if(doomloop>999):
                "Okay, you deserved it. this is your cupboard ending."
                stop music fadeout 1.0
                scene end85
                $persistent.unlock_85 = True
                "Seen from up close. Congrats!"
                play sound "SFX/fail.mp3"
                "--Cupboard Ending--"
                jump credits
            else:
                "Now it's time to get out of the cupboard and pretend that you answered yes."
            
    scene black
    with dissolve
    stop music fadeout 1.0
    "And the three fillies took you to the edge of the town, with nothing else than trees, grass and..."

    scene bg bushes hill
    with fade
    play music "Music/outdoors.mp3"
    show braeburn chillin sunglasses
    with dissolve
    
    b "Heeeeey! Welcome to Appleloosa cousin!"
    p "Nope."
    b "Yeah, that's true. We're still near the good ol' Ponyville. Anyway, are you there 'cause of the lil' fillies too?"
    p "Eeyup."    
    b "I tried hard to have your attention, even got these sunglasses. Do you want to try now?"

    
    menu braeburnchoice:
        "\"Eeyup.\"":
            p "Eeyup."
            b "And I thought you would never say it, ol' big chunk of love. Come here!"
            
            scene end06
            $persistent.unlock_06 = True
            with fade
            stop music fadeout 1.0
            show CMC awe
            with dissolve
            
            "And then some stallions hugging. Kissing. And doing stuff. With kids watching."
            
            cmc "Awwwwwwww!"
            
            "Girls, you are creepy."
            play sound "SFX/fail.mp3"
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
            b "Come on nurse! That's just one glass... And now gimme a hug!"
            nr "You are drunk Braeburn. And now you won't be able to take your medication for tonight and that's bad."
            p "Eeyup."
            show redheart grumpy
            with dissolve
            nr "Sorry, I didn't notice you... Big Mac, isn't it? Braeburn caught some kind of local flu and shouldn't have left the hospital like he did. But looking at you now, I kind of understand his motives."
            show redheart happy
            with dissolve
            nr "I'm going to get back to the hospital with him, would you like to come with us?"
            p "Eeyup."
            nr "Let's go then!"
            
            scene end40
            $persistent.unlock_40 = True
            with fade
            
            "And after putting Braeburn in his bed again, the nurse gave you a kiss on the cheek. You won't be able to see that in a future version... But everything went better than expected."
            
            play sound "SFX/fail.mp3"
            "--Nurse Redheart ending--"
            
            jump credits
            
label credits:
    if persistent.unlock_01 and persistent.unlock_02 and persistent.unlock_03 and persistent.unlock_04 and persistent.unlock_05 and persistent.unlock_06 and persistent.unlock_07 and persistent.unlock_08 and persistent.unlock_09 and persistent.unlock_10 and persistent.unlock_11 and persistent.unlock_12 and persistent.unlock_13 and persistent.unlock_14 and persistent.unlock_15 and persistent.unlock_16 and persistent.unlock_17 and persistent.unlock_18 and persistent.unlock_19 and persistent.unlock_20 and persistent.unlock_21 and persistent.unlock_22 and persistent.unlock_23 and persistent.unlock_24 and persistent.unlock_25 and persistent.unlock_26 and persistent.unlock_27 and persistent.unlock_28 and persistent.unlock_29 and persistent.unlock_30 and persistent.unlock_31 and persistent.unlock_32 and persistent.unlock_33 and persistent.unlock_34 and persistent.unlock_35 and persistent.unlock_36 and persistent.unlock_37 and persistent.unlock_38 and persistent.unlock_39 and persistent.unlock_40 and persistent.unlock_41 and persistent.unlock_42 and persistent.unlock_43 and persistent.unlock_44 and persistent.unlock_45 and persistent.unlock_46 and persistent.unlock_47 and persistent.unlock_48 and persistent.unlock_49 and persistent.unlock_50 and persistent.unlock_51 and persistent.unlock_52 and persistent.unlock_53 and persistent.unlock_54 and persistent.unlock_55 and persistent.unlock_56 and persistent.unlock_57 and persistent.unlock_58 and persistent.unlock_59 and persistent.unlock_60 and persistent.unlock_61 and persistent.unlock_62 and persistent.unlock_63 and persistent.unlock_64 and persistent.unlock_65 and persistent.unlock_66 and persistent.unlock_67 and persistent.unlock_68 and persistent.unlock_69 and persistent.unlock_70 and persistent.unlock_71 and persistent.unlock_72 and persistent.unlock_73 and persistent.unlock_74 and persistent.unlock_75 and persistent.unlock_76 and persistent.unlock_77 and persistent.unlock_78 and persistent.unlock_79 and persistent.unlock_80 and persistent.unlock_81 and persistent.unlock_82 and persistent.unlock_83 and persistent.unlock_84 and persistent.unlock_85 and persistent.unlock_86:
        scene end87
        with fade
        $persistent.unlock_87 = True
    else:
        scene black
        with fade
    pp "You reached the end!"
    aj "Good for you!"
    r "But there is more to see."
    ts "Except if you have already seen everything."
    rd "But you wouldn't read the credits anymore."
    fs "Unless you really like us! And that's a great proof of love! Thank you!"
    "Love? I would have said stupidi-"
    cmc "Shhhh, here it comes!"
    play music "Music/credits.mp3"
    scene black 
    with Pause(1)

    show credit1 with fade
    $renpy.pause()

    
    scene credit2 with fade
    $renpy.pause()
    
        
    show credit3 with fade
    $renpy.pause()
     
       
    scene credit4 with fade
    $renpy.pause()
     
       
    show credit5 with fade
    $renpy.pause()
    
       
    show credit6 with fade
    $renpy.pause()
    
    show credit7 with fade
    $renpy.pause()
    
       
    show credit8 with fade
    $renpy.pause()
    
       
    show credit9 with fade
    $renpy.pause()
    
       
    show credit10 with fade
    $renpy.pause()
    