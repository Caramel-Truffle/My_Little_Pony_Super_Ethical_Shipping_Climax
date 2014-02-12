label applebarn:
    stop music fadeout 1.0

    scene bg apple barn
    with fade
    
    if(appl1==False):
        play music "Music/applebarn.mp3"
        "After walking for a bit, you arrive at the Apple barn in Sweet Apple Acres."
        "The smell of apples is strong in this place. Apple trees are all around you, ponies with apple-related cutie marks run around and apple products are on a giant table... Wait, is there some kind of party here?"
        aj "Here ya go, everypony! Y'all welcome to taste the products of our good ol' family!"
        "An \"apple family\" reunion or a real Apple family reunion? Either way, you probably should leave them for the mom-"
        aj "Howdy! Long time no see..."
        
        if(playername == "Applejack"):
            show applejack hat side gasp
            with dissolve
            aj "...Mahself? Cousin, you really look like me, who's inside this costume?"
            menu aj_see_herself:
                "\"It's-a me! Pinkie!\"":
                    p "It's-a me! Pinkie! Isn't my cosplay great? Uh? Uh? Uh?"
                    show applejack hat sigh
                    with dissolve
                    aj "Pinkie? This isn't one of Twilight's conventions, ya know?"
                    p "But there's all these apple-ponies!"
                    show applejack hat facehoof
                    with dissolve
                    aj "...That's mah family."
                    p "Can I be part of your family as yourself for today? Please?"
                    show applejack hat happy
                    with dissolve
                    aj "Well, ya're part of the extended family ah said and... If you really want it, ah can call you [playername2] for today."
                    p "Woohoo! You're the best, Applejack!"
                    
                "\"I'm... Your lost sister.\"":
                    p "I'm... Your lost twin sister."
                    show applejack hat wtf
                    with dissolve
                    aj "Mah what know?"
                    p "Your lost twin sister. There's been an error at our birth and I've been sent to Fillydelphia. I later learned that our parents never forgave themselves and so chose to not tell you."
                    show applejack hat sad
                    with dissolve
                    aj "Is this some kind of sick joke?"
                    p "I wish it was. Do you know the worst?"
                    aj "How can it be any worse?"
                    p "We share the same name and cutie mark. A stranger couldn't tell the difference just by looking at us."
                    aj "..."
                    "You hug her."
                    p "Are you alright?"
                    show applejack hat crying
                    with dissolve
                    aj "..."
                    stop music fadeout 1.0
                    scene black
                    with fade
                    "You touched her to the core, bravo! Unfortunately, you had nothing else than bittersweet hugs this day. Applejack wouldn't let you go after that."
                    p "This seems a bit odd for a parody."
                    "If you wanted something fun, you should have chose Pinkie-oriented options, not the \"I'm your lost sibling\" one."
                    "--Applejack ending 1--"
                    jump credits
                    
                "\"Who are YOU?\"":
                    p "I'm Applejack! Who are YOU?"
                    show applejack hat angry
                    with dissolve
                    aj "What do ya say? AH am Applejack, not ya!"
                    p "She's a changeling! Burn the changeling!"
                    aj "Ah'm not! Ah'm way more heavy than a duck!"
                    "You hear a voice in the distance."
                    u "Y'all, stop quoting Pony Mython and the Holy Elements!"
                    p "..."
                    show applejack hat wtf
                    with dissolve
                    aj "..."
                    aj "So we're both Applejack?"
                    p "Seems so. Let's be friends?"
                    show applejack hat happy
                    with dissolve
                    aj "Ah think it's the strangest thing Ah have ever seen... But you're family and Ah don't wanna reject that."
                    
        else:
            show applejack hat happy
            with dissolve
            aj "...[playername3]? I did not expect you today!"
            if(playername=="Pinkie Pie"):
                p "A party! Can I stay? Please?"
                aj "Well, ya're part of the extended family Ah said when the Flim Flam brothers where there."
                p "Woohoo! You're the best, Applejack!"
            else:
                p "Sorry, you seem busy with your family, so I better leave."
                aj "[playername]. After all we've been together, Ah consider you'self as part of the extended family ya know? You better stay here for a while if you don't have more important stuff to do today!"
        p "So, what have you planned this year? That I can participate in, I mean."
        aj "Well, right now ya can either go to the nearest table and enjoy some food or try to catch some apples in the water. There will be more later."
        
        menu sugapple:
            "Go eat something":
                p "I'm a bit hungry. I'll probably just eat some pie before Soarin decide to marry someone in the family."
                aj "...Eeyup. Take care!"
                
                stop music fadeout 1.0
                scene black with fade
                "And thus, you went to the nearest table, to eat a bit."
                
                scene bg sweet apple acres
                with fade
                play music "Music/applebarn.mp3"
                "A lot of ponies are here, discussing, playing, dancing... But for the moment, you focus your attention on some apple pie."
                
                if(playername=="Applejack"):
                    u "Howdy cousin! ya did a great job!"
                    show braeburn happy
                    with dissolve
                    p "Sorry, I'm surely not the one you're thinking I am."
                    u "Ah, sorry mam', Ah thought ya were the ol' AJ."
                    p "Ah am! ... I mean, I am! But I'm not. My name is Applejack, I look like the Applejack you know, but I'm not her., look, she's just there!"
                    "You point out the real AJ to the pony."
                    b "Oh. Ah'm Braeburn. Ah come from Apple-loooooooosa! Great town, ya should come someday!"
                    
                else:
                    u "Howdy! Erm. AJ friend?"
                    show braeburn happy
                    with dissolve
                    p "Yes, close friend. My name is [playername]."
                    b "We've met before, in Apple-looooooosa! Ah'm Braeburn!"
                    p "Yes, with Bloomberg, the \"You gotta share\" song and all of that..."
                    b "Funny times, ya should come back someday."
                
                p "Maybe I will. Especially if they're all as friendly as you are."
                b "ya bet. But nopony there make cider like Granny Smith do."
                p "Cider, uh? Don't drink too much!"
                "You added a wink to your last comment."
                b "ya know, I might."
                p "An handsome stallion like you? What could you possibly want to blurr with hard cider?"
                b "Big Mac. First stallion Ah met that did not react to my charm."
                p "Wait, you're like?"
                b "Nah. Unicorn or pegasus, pony or buffalo, male or female, all have their perks. And kinks. And Ah like some variety ya know?"
                
                if(playername == "Applejack"):
                    menu braeburncest:
                        "What about incest?":
                            p "What do you think about incest?"
                            "He blushes."
                            b "That's direct sugarcube. Do you ask for... Or... Buck it. Let's go behind the barn, we should be alone and all."
                            stop music fadeout 1.0
                            scene black
                            with fade
                            "And both of you went all \"kissu-kissu my cousin\". Except you two weren't really cousins."
                            "--Braeburn ending 1--"
                            jump credits
                            
                        "I understand":
                            $ #Useless line is useless. Except for the interpreter.
                
                p "Yeah, whatever float your boat."
                b "Ya're cute sugarcube. And Big Mac is there, Ah'm gonna try one last time. We should meet again someday."
                "He gives you a sugar cube and leave."
                $p_aj = "sugarcube"
                $ nb_lock = nb_lock + 1
                
                hide braeburn
                with dissolve
                p "Well. Let's eat something at least."
                "You look at the table..."
                stop music fadeout 1.0
                scene black
                with fade
                "...And ate, without further noticeable conversations. After that, you went back to the crossroad."
                
            "Play a bit":
                p "I'm feeling playful. I bet that I could catch an apple in 10 seconds flat."
                if(playername=="Rainbow Dash"):
                    aj "Prove it, \"Dashie\"."
                    "She's clearly grinning at the thought."
                else:
                    aj "Ya're not Rainbow, but ya know what saying that mean, don't ya?"
                    p "That I need to prove it?"
                    aj "Exactly."
                    p "I will."
                    "Are you clearly grinning at the thought? ...Whatever."
                
                stop music fadeout 1.0
                scene black
                with fade
                
                "Both of you went to the nearest barrel full of water and apples."
                
                scene bg apple barn
                with fade    
                play music "Music/applebarn.mp3"
                show applejack hat side calling
                with dissolve
                
                aj "So, let's see what you got [playername3]! I bet you can't beat..."
                show applejack hat applemouth
                with fade
                
                aj "Thisch!"
                
                "Wait, how did she do that? Three in a second? And you've never even tried to catch an apple with your pony-mouth before."
                
                "What should you do?"
                
                menu waterapple:
                    "Do your best":
                        "Trying to do your best, eh? Let's see what happens then."
                        p "I can do better!"
                        
                        "Well, that's not you to decide, soo... 4 apples in the water, but you're a level 1 pony with only 2 in dexterity... Let's roll 2 D20..."
                        
                        if((playername=="Twilight Sparkle") and (p_book == "astronomy")):
                            "3 and 8? Uh. That's pretty bad 'Twilie'."
                            
                        elif (playername == "Rainbow Dash" and p_rd == "sunglasses"):
                            "14 and 13? That's quite good! Uh. But you have the cool sunglasses, it boosts your charm, but lowers your dexterity by 20 points. Your result isn't 27, It's only 7. That's bad 'Dashie'."
                        else:
                            "2 and 1? Epic failure. You didn't even try, not literally."
                        p "Hey! You're making these up, don't blame me!"
                        show applejack hat wtf
                        with dissolve
                        aj "What now?"
                        p "Not you AJ, the narrator."
                        aj "Oooookay sugarcube..."
                        "Ah! Don't forget that you shouldn't be able to talk back. And now let's put you in the water and let you have an apple in 12 seconds."
                        p "Wai-"
                        "And your just did that."
                        p "Arrr... Pfff.... Gnnnn..."
                        show applejack hat supersmile
                        with dissolve
                        aj "That's a bit slow for ten seconds and ya only got an apple [playername2]. Ah guess Ah won!"
                        p "I guess you do."
                        
                    "Do your worst":
                        "Oh, come on! Where's the fun? I would have roll dices and say random stuff depending on your character!"
                        p "I'll see what I can do."
                        "Yeah, yeah, and the more you try, the less you're able to catch an apple. Your miserable attempt is clearly a deception and it take you 25 seconds to catch a single fruit."
                        show applejack hat meh
                        with dissolve
                        aj "Were ya even tryin'?"
                        p "Yes, of course I was! I'm no wimp! It... It was the number of apples already in the water. I swear!"
                        "She sigh."
                        
                aj "Well... Keep the apple and come back to me when you feel like you can do better!"
                p "I will!"
                $ p_aj = "apple"
                "And she goes away for the moment."
                hide applejack
                with dissolve
                "Well. You better go back to the crossroad for the moment."
                p "Can't I just go talk to someone?"
                "Somepony. And no, it's not in the script, so you may not."
                p "Let's go then."
                
                stop music fadeout 1.0
                scene black
                with dissolve
                
                "And you went back to the crossroad. Getting this [p_aj] was worth the trip. I guess."
                
        $appl1 = True
        $appl2 = True
        jump outdoors
        
    if(appl2==True):
        play music "Music/applebarn.mp3"
        "You come back to the Apple Family Reunion. A lot of ponies are here, discussing, playing, dancing... But for the moment, as you're not seeing Applejack anywhere and are a bit hungry due to the trip, you focus your attention on some apple pie."
                
        if(playername=="Applejack"):
            u "Howdy cousin! ya did a great job!"
            show braeburn happy
            with dissolve
            p "Sorry, I'm surely not the one you're thinking I am."
            u "Ah, sorry mam', Ah thought ya were the ol' AJ."
            p "Ah am! ... I mean, I am! But I'm not. My name is Applejack, I look like the Applejack you know, but I'm not her., look, she's just... Where is she anyway?"
            "You failed to point out the real AJ to the pony."
            b "Oh. Don't worry, Ah trust you. And Ah'm Braeburn, coming from Apple-loooooooosa! Great town, ya should come someday!"
            
        else:
            u "Howdy! Erm. AJ friend?"
            show braeburn happy
            with dissolve
            p "Yes, close friend. My name is [playername]."
            b "We've met before, in Apple-looooooosa! Ah'm Braeburn!"
            p "Yes, with Bloomberg, the \"You gotta share\" song and all of that..."
            b "Funny times, ya should come back someday."
                
        p "Maybe I will. Especially if they're all as friendly as you are."
        b "ya bet. But nopony there make cider like Granny Smith do."
        p "Cider, uh? Don't drink too much!"
        "You added a wink to your last comment."
        b "ya know, I might."
        p "An handsome stallion like you? What could you possibly want to blurr with hard cider?"
        b "Big Mac. First stallion Ah met that did not react to my charm."
        p "Wait, you're like?"
        b "Nah. Unicorn or pegasus, pony or buffalo, male or female, all have their perks. And kinks. And Ah like some variety ya know?"
        p "Yeah, whatever float your boat."
        b "ya're cute sugarcube, d'ya know that?"
        
        menu cute_bb:
            "I'm not cute!":
                
                p "I... I'm not cute! And you're a stallion!"
                b "Oh. Ah didn't guess you were only into mares, sorry sugarcube!"
                p "Yeah, I'm not g... Wait, I'm a mare myself."
                b "Ah guess ya're, not that it matters to me. Are you gender confused or somethin'?"
                p "N... No. Just forget it. Is there anything I could do? That doesn't involve kisses, of course."
                
            "I sure am. *wink wink*":
                
                p "You bet I'm cute. Not as much as you are though."
                b "And what does ya cute face intends to do today?"
                p "I was thinking about \"discussing\" with your cute face. You know, with passion."
                b "Ah sure would love that... Let's go behind the barn, we should be alone and all."
                stop music fadeout 1.0
                scene black
                with fade
                "And both of you went all kissu-kissu and stuff. Shamelessely."
                "--Braeburn ending 2--"
                jump credits
                
            "I don't have enough alcohol in my blood for that.":
                
                p "I have too much blood in my alcohol for that."
                b "Ah sure can offer ya some hard cider."
                p "That would be great! And in return I would kiss you all day."
                
        b "Just kisses?"
        p "This isn't a clop story, so nothing more should happen anyway."
        b "Darn it."
        p "Sorry Braeburn. So... Don't you have anything I can do?"
        b "What about bringing me some sunglasses?"
        p "Sunglasses?"
        b "Yeah, Ah want to try a different approach with Big Mac."
        p "Consider it done!"
        b "Thanks sugarcube, I'll wait."
        
        if(p_rd == "sunglasses"):
            p "No, litterally done, I have a pair here, but I can't let you have them forever."
            $appl2 = False
            $appl3 = True
            jump give_brae_sunglasses
        p "I won't be long, see you later!"
        "And you leave the party."
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "New quest! The sunglasses search! Let's engage an epic music! Wait... No. It might not be adequate with the rest of the game. And you would have been going back to the crossroad all the same anyway."
        $appl2 = False
        $appl3 = True
        jump outdoors
        
    if(appl3==True):
        play music "Music/applebarn.mp3"
        "Once more, you go back to the Apple barn."
        if(p_rd == "sunglasses"):
            p "But ths time, I have the sunglasses!"
            "Yes you do and Braeburn is just there."
            
            show braeburn happy
            with dissolve
            
            b "Welcome back [playername2]!"
            p "I've got your sunglasses Brae', but I can't let you have them forever."
            
            label give_brae_sunglasses:
                $ #Useless line is useless. Except for the interpreter.
            
            b "That was fast! ...What d'ya mean by not forever?"
            p "You want to test them with Big Mac, right? Just return them once you're done."
            b "Can't Ah just have them 'til tomorrow?"
            p "I guess I could let you borrow them longer... But I want something else in return."
            
            menu brae_reward:
                "I want some alcohol":
                    p "I want to drink. A lot."
                    b "Wow. Calm down sugarcube, ya're not Berry Punch. What about some cider?"
                    p "Your cider bottle. My mouth. Now."
                    
                    stop music fadeout 1.0
                    scene black
                    with fade
                    
                    "And you... Drank... A lot? Until accepting kisses from random ponies did not bother you anymore? What the..."
                    "--Drunk ending--"
                    jump credits
                    
                "I want some time with AJ":
                    p "I want some time with AJ, if you know what I mean."
                    b "Ah sure do [playername2], but that's not really up to me."
                    p "Come on, I helped you with Big Mac, now it's your turn to at least try!"
                    b "Ah promise nothin', but Ah'll do my best... Come back in a moment."
                    hide braeburn
                    with dissolve
                    "And so he left to try."
                    
                    stop music fadeout 1.0
                    scene black
                    with fade
                    
                    "And you went back to the crossroad, thinking about what you could do to wait."
                    p "Isn't walking to the crossroad then going back enough?"
                    "Maybe. Or not."
                    $ appl3 = False
                    $ appl4 = True
        else:
            p "But I don't have the sunglasses!"
            "Don't blame me, I'm merely the narrator! But if you insist, I will now narrate how you went back without searching for Braeburn."
            
            stop music fadeout 1.0
            scene black
            with fade
            
            "And you went back without searching for Braeburn."
            p "..."
            "What did you expect? Crossroad!"
        
        jump outdoors
        
    if(appl4 == True):
        "You reached the end of the demo!"
        p "Wait, that's all?"
        "Hey! There's around 20 endings in the demo! If you wanted to see the good ones, filled with narration and stuff you should have waited for the full game. Anyway..."
        "--Demo ending 5--"
        jump credits
    
    "After walking for a bit, you arrive at the Apple barn in Sweet Apple Acres."
    p "The barn seems full of busy ponies for the moment. I should probably go somewhere else."
    stop music fadeout 1.0
    scene black
    with fade
    "What an useless trip... You go back to the crossroad anyway."
    jump outdoors
    
return