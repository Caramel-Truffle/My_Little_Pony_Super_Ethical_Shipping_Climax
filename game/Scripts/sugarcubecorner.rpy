label sugarcubecorner:
    stop music fadeout 1.0
    
    scene bg sugarcube corner lobby
    with fade
    
    if(suga1==False):
        
        "As soon as you arrive in the bakery, a pink pony.... Wait. Where is Pinkie Pie?"
        p "There she is!"
        "..."
        p "..."
        "...I don't think so. Let's try the kitchen, maybe?"
        
        scene bg sugarcube corner kitchen2
        with fade
        play music "Music/pinkie.mp3"
        show pinkie mini alicorn:
            linear 0.5 xalign 1.0
            linear 0.5 xalign 0.0
            repeat
        "You come to the- OH MY GOD WHAT'S THIS?!"
        show pinkie moustache at default with dissolve
        
        if(playername=="Rainbow Dash"):
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply [playername]? She's fast, awesome and cool, but you do realize that you could have been an alicorn? With great powers and all, right?"
        if(playername=="Pinkie Pie"):
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply me? Do you realize that you did not need to be me to do things like I do and that you could have been an alicorn? With great powers and all?"
        if(playername=="Rarity"):
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply [playername]? You may love fashion and beauty, but do you realize that you could have been an alicorn? With great powers and all?"
        if(playername=="Fluttershy"):    
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply [playername]? You may love animals and stuuf, but do you realize that you could have been an alicorn? With great powers and all?"
        if(playername=="Applejack"):
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply [playername]? Do you really prefer her simple lifestyle to the power of an alicorn?"
        if(playername=="Twilight Sparkle"):
            pp "Welcome to our new alicorn! Wait. You did not choose to be an alicorn, but simply [playername] before she became one? Or will become. It's hard to know where we are on the timeline, this is just a fangame after all...  But do you realize that you could have been an alicorn? With great powers and all? "
        
        if(alichoice == 0):
            p "I did not even try to be one. Why would I?"
        elif(alichoice ==1):
            p "I tried once, but Colgate didn't want to, so I chose [playername2]."
        else:
            p "I tried, [alichoice] times! But Colgate did not let me be my super alicorn OC."
            
        "Wait, you two, couldn't you just act normally?"
        pp "Normally? According to you or according to the norm a major part of the players are expecting me to act?"
        p "And either way, a narrator shouldn't talk to his characters, that's unrespectful of the laws of tales telling."
        "Fine... Fine... But I warned you."
        p "Anyway, Pinkie, is there a reason for the mustache?"
        pp "No, it's not because I mustache you a question, this joke has already been done."
        p "I said nothing."
        pp "I wasn't talking to you... Anyway, it's because I always wear a mustache when baking sugar cube pie, but I can take it off!"
        
        show pinkie mini faceplant:
            xalign 0.68
        "*POMF*"
        show pinkie derp:
            xalign 0.5
        pp "..."
        show pinkie laugh
        pp "AHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHAH!!"
        show pinkie mini faceplant:
            xalign 0.68
        "*POMF*"
        show pinkie moustache:
            xalign 0.5
        pp "Sorry, I like it that much. But why are you there? Do you want a cupcake or a muffin? Wait. Let me guess..."
        
        if(dash3 == True and p_aj != "sugarcube"):
            pp "You need a muffin and don't have a sugar cube... You are there for the muffin, aren't you?"
        elif(dash3 == True and p_aj == "sugarcube"):
            pp "You need a muffin but you also have a sugar cube... You are good! I don't know what you are up to!"
        elif(dash3 == False and p_aj != "sugarcube"):
            pp "You don't have a sugar cube, but you don't need a muffin for the moment... I guess that you want a cupcake. Don't you?"
        elif(dash3 == False and p_aj == "sugarcube"):
            pp "You don't need a muffin and you already have a sugar cube! You want to be all kissu-kissu with me, don't you?"
            
        menu pinkieguess:
            "I want a muffin":
                p "I guess that I want a muffin..."
                
            "I want a cupcake":
                p "I want a cupcake... Maybe?"
                
            "I want a mustache":
                p "You are wrong! I want a mustache!"
                pp "But you already have one!"
                p "Wait. What? But I'm [playername2]! I can't have a mustache, I'm a mare! ...Am I?"
                pp "Nopony told you? Really? Like, never ever ever ever?"
                p "Told me what?"
                pp "I can't believe it, they really didn't."
                p "Pinkie! What am I supposed to know?"
                pp "The moon. Everypony is going to have something special this night and if you want a mustache, you'll have one. And as time is non-linear, it's as you already have one!"
                p "The moon? Non-linear? I'm not sure to fully understand."
                pp "Time is some kind of pony-cutsy-timey-pinkie... Stuff. And as for the moon, you need to complete the Twilight's path to fully understand it."
                p "Ooookay. What about my mustache?"
                pp "Narrator?"
                "I get it."
                
                stop music fadeout 1.0
                
                if(playername=="Applejack"):
                    scene end34  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end35
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end36
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end37
                    with fade
                if(playername=="Rarity"):
                    scene end38
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end39
                    with fade
                
                "And you got a mustache."
                p "What? That's it."
                "Yep."
                "--Mustache ending--"
                jump credits
                
            "I want you":
                p "I want the best candy in town. You."
                pp "Oh silly, you don't need to use a pickup line to get me!"
                
                show pinkie sly
                with dissolve
                
                pp "So, should I get the whipped cream?"
                p "Where's your mustache?"
                pp "I never wear a mustache when I play with whipped cream."
                p "I never said that I wanted to use whiped cream!"
                pp "You want the best candy in town, right? How can a candy be the best without it?"
                p "You may have a point. Bring it on."
                
                stop music fadeout 1.0
                
                if(playername=="Applejack"):
                    scene end41  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end42
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end43
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end44
                    with fade
                if(playername=="Rarity"):
                    scene end45
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end46
                    with fade
                
                "And both of you went all kissu-kissu with the whipped cream and all."
                p "That sounds so..."
                "Don't say it."
                
                "--Pinkie ending 1--"
                jump credits
                
            "I want neither of these choices!":
                p "I don't want my choices to be preselected! Narrator! Let me enter what I want!"
                "O....Kay... That's not like my opinion has some value in this place anyway..."
                $ playerwant = renpy.input("What is your desiderata?")
                p "Yes! That's it! I want [playerwant]!"
                pp "You want [playerwant]? Really?"
                p "I want [playerwant]!"
                pp "I can't give you that, sorry."
                p "Why not? It's not that hard to find."
                pp "I only have muffins, cupcakes and love! So... What do you want?"
                jump pinkieguess
                
        pp "Be assertive! You are not Fluttershy!"
        
        if(playername=="Fluttershy"):
            p "Erm?"
            pp "No. You just look like her. You are not her, don't even try with me."
            
        p "Okay."
        
        menu assertivepie:
            "I WANT a muffin":
                p "I want a muffin. I'm absolutely sure about it."
                $ p_cake = "muffin"
                $ nb_lock = nb_lock + 1
            "I WANT a cupcake":
                p "I want a cupcake. I'm absolutely sure about it."
                $ p_cake = "cupcake"
                $ suga2 = True
        
        pp "That's it! Here, take this [p_cake]!"
        
        "She gives you a [p_cake]!"
        
        p "So.... That's it? You give me the item an nothing else? No explanation or whatever?"
        
        pp "Yes, that's how it works, if you ask for one thing, I give it to you and it will be useful with another path, but you won't see me again. In my case, the muffin is useful with Rainbow Dash. But if you ask for the other, you will be able to see me again and I'll ask you to bring me something before we could continue."
        p "That doesn't make any sense!"
        pp "It's a game, silly! Real life logic can't be applied there! Now, shoo!"
        p "Shoe?"
        pp "Shoo, get out! It's the end of the scene, et the narrator do its job!"
        "..."
        pp "Narrator?"
        "..."
        p "He's just being grumpy."
        pp "But we need him! You can't go out without his help!"
        "..."
        pp "I'm sorry! We ignored you until now, but it won't happen again!"
        if(p_cake == "muffin"):
            "Whatever. Next time I'll see you you won't remember this anyway."
            pp "You really are grumpy."
        else:
            "Do you mean that the next encounter will be normal?"
            pp "As normal as I can be! Cross my heart and hope to fly, stick a cupcake in my eye!"
            
        "Erm. Time to go then! See you next time!"
        p "Bye Pinkie!"
        pp "Bye \"[playername3]\"!"
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "You went back to the crossroad with something sweet in your pocket and I definitely am too old for this manure. I'm not even paid for this."
        p "No grumpy narrator we said."
        "Fine. Fine."
        
        $ suga1 = True
        jump outdoors
        
    if(suga2==True):
        play music "Music/pinkie.mp3"
        "You are back to the bakery, where sugar scent invade your nose and makes your stomach growls."
        u "Sounds like somepony needs a cupcake!"
        
        show pinkie happy
        with dissolve
        
        p "Well, I already have one, thanks to you."
        pp "Then just eat it, silly! And take these two anyway, they're on the house."
        p "Do Mr and Ms Cake allow you to do that?"
        pp "Giving free cupcakes? As long as I make a profit at the end of the day, no problem."
        p "Well, in this case..."
        "You got two cupcakes!"
        "You eat three cupcakes!"
        p "I should be okay for a while now."
        pp "So, [playername2], what are you up to? Need anything special? Have you something planned for this night?"
        p "Well, I was going to ask you the exact same thing, to be honest."
        pp "Uh. In this case, what about making a sugar cube pie? Doesn't this sounds exciting?"
        p "Don't you have enough sugar in your blood already?"
        pp "That's not for me silly!" 
        show pinkie serious
        with dissolve
        pp "But are you in or are you not? Because I'm totally going to make some! Seriously. I already sold every sugar cube pie I made last time you were there. It's like the town is on sugar cube frenzy or something! We expected the Luna's Special -a cupcake- to sell well due to the beautiful moon we should have this night, but... No."
        p "Well... I guess that couldn't hurt. To bake some, I mean."
        show pinkie happy
        with dissolve
        pp "Okey-dokey-lokey! Let's go!"
        
        scene bg sugarcube corner kitchen2
        with fade
        
        show pinkie moustache
        with dissolve
        
        p "Wait, shouldn't someo... Erm. Somepony be in the other room? You know, to sell some baked goods if a client enters the shop?"
        pp "Nah. The bell would go all dingeling-ding-ding if that was the case, so I could always yell to them."
        show pinkie yell
        with dissolve
        pp "\"I'M COMING, JUST BAKING SOME MORE PIE, TAKE A LOOK! IF YOU CAN EAT IT, YOU CAN BUY IT!\"" 
        show pinkie happy
        with dissolve
        pp "And then hope that they don't eat wood, because the building is certainly not for sale!"
        p "Or if I'm there, you could always either let the baking or the selling to me."
        pp "That's a good idea! But let's get baking first."
        hide pinkie
        with dissolve
        "Both of you get the various ingredients, Pinkie singing you where to find them when they were closer to you than to her."
        show pinkie singing
        with dissolve
        pp "Sugar cubes! Add them aplenty! Sugar cubes, let's start with twenty!"
        show pinkie serious
        with dissolve
        pp "..."
        p "What's wrong? You are silent. It's... Unusual."
        pp "We don't have enough sugar cubes!"
        
        if(p_aj == "sugarcube"):
            p "I have this one on me if that can help."
            show pinkie happy
            with dissolve
            
            $suga2 = False
            $suga3 = True
            
            jump bake_pie
        else:
            p "I can get some if you want."
            show pinkie happy
            with dissolve
            pp "Great idea! I'll wait there then. Or I might be selling something when you return, but be quick! I don't want to disappoint somepony by telling them we're out of stock!"
            p "I'lll be back soon, don't worry."
            
            stop music fadeout 1.0
            scene black
            with fade
            
            "And you went back to the crossroad, on the sugar cube quest!"
            
            $suga2 = False
            $suga3 = True
            
            jump outdoors
            
    if(suga3 == True):
        play music "Music/pinkie.mp3"
        "You are back to the Sugarcube Corner, Pinkie seems to still be all alone and in the kitchen."
        pp "COMIIIING!"
        
        if(p_aj != "sugarcube"):
            p "It's me! I don't have a sugar cube yet!"
            show pinkie happy
            with dissolve
            pp "Oh. Don't worry and keep trying! I'm sure there is a mare or stallion friendly enough to give you one! Good luck!"
            p "Thanks Pinkie!"
            
            stop music fadeout 1.0
            scene black
            with fade
            
            "And you returned to the crossroad."
            
            jump outdoors
        else:
            p "It's me! I've got one!"
            pp "COME THERE THEN!"
            p "Okay! I'm coming!"
            
            scene bg sugarcube corner kitchen2
            with fade
            
            show pinkie moustache
            with dissolve
            
            p "You know, no need to yell. I was speaking normally and you heard me."
            pp "Really? I should stop using the megaphone then!"
            p "You were using a megaphone indoors? But... You didn't sound that loud!"
            pp "Of course silly, I don't turn it on indoors, what would be the point?"
            p "... Forget it. And take this sugar cube."
            
            label bake_pie:
                $ #Useless line is useless. Except for the interpreter.
                
            "You give her the sugar cube."
            pp "Great! Now it's time to put it in the oven!"
            "*Dingeling!*"
            pp "A customer! Do you want to go sell something or finish there?"
            
            menu sell_bake:
                "I want to go sell something!":
                    p "Let me take care of that and finish baking."
                    pp "See you soon!"
                    
                    "And you head to the other room."
                    
                    scene bg sugarcube corner lobby
                    with fade
                    
                    show thunderlane happy
                    with dissolve
                    
                    "The customer is a stallion! He looks friendly at least."
                    
                    u "Hello [playername3]! Taking care of the business while the Cakes are out?"
                    
                    if(playername != "Pinkie Pie"):
                        p "Not really, Pinkie is baking sugar cube pies and I volunteered to help with customer service!"
                    else:
                        p "Yes, some sugar cube pies are in the oven! That's what I was doing before you came."
                    
                    u "Sugar cube pies? Did the Cakes told you \"Thunderlane is coming! Bake some sugar cube pies while we're out!\"? because they are my favorite!"
                    p "Sorry, but you clearly are not alone. It's like half the town decided to eat that today. What could possibly make so many ponies do the same thing at the same date? ... Anyway. Would you like to wait for some pie or would you like something else?"
                    t "I would love to wait all day with you, but I have an appointment in half an hour and some other things to buy before that, sorry."
                    p "Don't be sorry, that's not your fault!"
                    t "Thank you [playername2]. I'll buy a dozen rainbow cupcakes."
                    "You put them carefully in a box and show it to him."
                    p "I'm sure I can add something in it. What about a Luna's Special?"
                    t "One that glow in the dark?"
                    p "With the moon we're expecting this night, that would be perfect! I can add you three but only charge you one if you would like!"
                    t "Sounds good to me!"
                    "And so you add the cupcakes in the box and exchange it with the bits the stallion gives you."
                    t "See you next time [playername2]!"
                    p "Have a good day Thunderlane!"
                    t "Thanks! You too!"
                    
                    hide thunderlane
                    with dissolve
                    
                    "He's gone now."
                    
                    p "Did you hear that? Three Luna's Special are gone!"
                    
                    show pinkie happy
                    with dissolve
                    
                    pp "Good job!"
                    p "Thank you! Now, if you don't have anything else, I'll see if I can help someone else."
                    
                "I want to finish baking!":
                    p "Go, I'll finish!"
                    pp "Okey-dokey-lokey!"
                    
                    hide pinkie
                    with dissolve
                    
                    "You are now alone and start putting the pies in the oven."
                    
                    scene bg sugarcube kitchen2
                    with fade
                    
                    "Once you are done, you head back to the other room and hear the customer leaving."
                    
                    scene bg sugarcube corner lobby
                    with fade
                    
                    pp "Did you hear that? Six Luna's Specials are gone!"
                    p "Six for the price of two, that sure was a good deal for him! Anyway, the pies are in the oven. If you don't have anything else, I'll see if I can help someone else."
                    
            pp "You can always come back later if you want! I could give you something sweet to thank you properly!"
            p "I won't forget that Pinkie, don't worry!"
            "And so you head to the door, waving goodbye at the pink pony."
            
            stop music fadeout 1.0
            scene black
            with fade
            
            "After that, you went back to the crossroad, once again."        
                
            $ suga3 = False
            $ suga4 = True
            jump outdoors
            
    if(suga4 == True):
        "You reached the end of the demo!"
        p "Wait, that's all?"
        "Hey! There's around 20 endings in the demo! If you wanted to see the good ones, filled with narration and stuff you should have waited for the full game. Anyway..."
        
        
        if(playername=="Applejack"):
            scene end47  
            with fade          
        if(playername=="Fluttershy"):
            scene end48
            with fade
        if(playername=="Pinkie Pie"):
            scene end49
            with fade
        if(playername=="Rainbow Dash"):
            scene end50
            with fade
        if(playername=="Rarity"):
            scene end51
            with fade
        if(playername=="Twilight Sparkle"):
            scene end52
            with fade
        
        
        "--Demo ending 6--"
        jump credits
            
    "The bakery is empty and the cash register locked."
    p "I am alone here, I could bake something or go somewhere else... Let's go somewhere else."
    stop music fadeout 1.0
    scene black
    with fade
    "And you go back to the crossroad."
    jump outdoors

return