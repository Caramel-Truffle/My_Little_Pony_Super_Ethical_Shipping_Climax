label applebarn:
    stop music fadeout 1.0

    scene bg apple barn
    with fade
    
    if(appl1==False):
        play music "Music/applebarn.mp3"
        "After walking for a bit, you arrive at the Apple barn in Sweet Apple Acres."
        "The smell of apples is strong in this place. Apple trees are all around you, ponies with apple-related cutie marks run around and apple products are on a giant table... Wait, is there some kind of party here?"
        aj "Here you go, everypony! Y'all welcome to taste the products of our good ol' family!"
        "An \"apple family\" reunion, as in an orchard owners association, or a real Apple family reunion, as in family related by blood? Either way, you probably should leave them for the mom-"
        aj "Howdy! Long time no see..."
        
        if(playername == "Applejack"):
            show applejack hat side gasp
            with dissolve
            aj "...Myself? Cousin, you really look like me, who's inside this costume?"
            menu aj_see_herself:
                "\"It's-a me! Pinkie!\"":
                    p "It's-a me! Pinkie! Isn't my cosplay great? Uh? Uh?"
                    show applejack hat sigh
                    with dissolve
                    aj "Pinkie? This isn't one of Twilight's conventions, you know?"
                    p "But there's all these apple-ponies!"
                    show applejack hat facehoof
                    with dissolve
                    aj "...That's mah family."
                    p "Can I be part of your family as yourself for today? Pretty please?"
                    show applejack hat happy
                    with dissolve
                    aj "Well, you're part of the extended family I said and... If you really want it, I can call you [playername3] for today."
                    p "Woohoo! You're the best, Applejack!"
                    
                "\"I'm... Your lost sister.\"":
                    p "I'm... Your lost twin sister."
                    show applejack hat wtf
                    with dissolve
                    aj "My what know?"
                    p "Your lost twin sister. There's been an error at our birth and I've been sent to Fillydelphia. Years later, I learned that our parents never forgave themselves and chose to not tell you."
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
                    scene end01
                    with fade
                    "You touched her to the core, bravo! Unfortunately, you had nothing else than bittersweet hugs this day. Applejack wouldn't let you go after that."
                    p "This seems a bit odd for a parody."
                    "If you wanted something fun, you should have chosen Pinkie-oriented options, not the \"I'm your lost sibling\" one. And come on. the parents' reasoning doesn't make any sense if you think two seconds about it. Humour can also be found in how absurd and over-the-top something emotional is."
                    "Now, shoe."
                    p "You mean shoo, ri-"
                    play sound "SFX/fail.mp3"
                    "--Applejack ending 1--"
                    jump credits
                    
                "\"Who are YOU?\"":
                    p "I'm Applejack! Who are YOU?"
                    show applejack hat angry
                    with dissolve
                    aj "What did you say? I am Applejack, not you!"
                    p "She's a changeling! Burn the changeling!"
                    aj "I'm not! I'm way more heavy than a duck!"
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
                    aj "I think it's the strangest thing I have ever seen... But you're family and I don't wanna reject that."
                    
        else:
            show applejack hat happy
            with dissolve
            aj "...[playername3]? I did not expect you today!"
            if(playername=="Pinkie Pie"):
                p "A party! Can I stay? Please?"
                aj "Well, you're part of the extended family, as I said when the Flim Flam brothers where there."
                p "Woohoo! You're the best, Applejack!"
            else:
                p "Sorry, you seem busy with your family, so I better leave."
                aj "[playername]. After all we've gone through together, I consider yourself as part of the extended family, you know? You better stay here for a while if you don't have more important stuff to do today!"
        p "So, what have you planned for this year? Things that I can participate in, I mean."
        aj "Well, right now you can either go to the nearest table and enjoy some food or try to catch some apples in the big bucket of water over there."
        
        menu sugapple:
            "Go eat something":
                p "I'm a bit hungry. I'll probably just eat some pie before Soarin decides to marry someone in the family."
                aj "...Eeyup. Take care!"
                
                stop music fadeout 1.0
                scene black with fade
                "And thus, you went to the nearest table, to eat a bit."
                
                scene bg sweet apple acres
                with fade
                play music "Music/applebarn.mp3"
                "A lot of ponies are here, discussing, playing, dancing... But for the moment, you focus your attention on some apple pie."
                
                if(playername=="Applejack"):
                    u "Howdy cousin! You did a great job!"
                    show braeburn happy
                    with dissolve
                    p "Sorry, I'm surely not the one you're thinking I am."
                    u "Ah, sorry mam', I thought you were the ol' AJ."
                    p "I am! But I'm not. My name is Applejack, I look like the Applejack you know, but I'm not her. Look, she's just over there, talking to Honeycrisp!"
                    "You point out the real Applejack to the pony."
                    b "Oh. I understand better now, I think. I'm Braeburn and I came from Aaaapple-loooooooosa! Great town, you should come someday!"
                    
                else:
                    u "Howdy! Erm... AJ's friend?"
                    show braeburn happy
                    with dissolve
                    p "Yes, close friend. My name is [playername]."
                    b "Oh yes! We've met before, in Aaaapple-looooooosa! I'm Braeburn!"
                    p "Yes, with Bloomberg, the \"You gotta share\" song and all of that..."
                    b "Good times, you should come back someday."
                
                p "Maybe I will. Especially if they're all as friendly as you are."
                b "You bet. But nopony there makes cider like Granny Smith does."
                p "Cider, uh? Well, don't drink too much!"
                "You added a wink to your last comment."
                b "You know, I might."
                p "A handsome stallion like you? What could you possibly want to blur with hard cider?"
                b "Big Macintosh. First stallion I met who did not react to my charms."
                p "Wait, you're like...?"
                b "Colt cuddler? Nah. Unicorn or pegasus, pony or buffalo, male or female, all have their perks. And kinks. And I like some variety, you know?"
                
                if(playername == "Applejack"):
                    menu braeburncest:
                        "What about incest?":
                            p "What do you think about incest?"
                            "He blushes."
                            b "That's direct, sugarcube. Do you ask for... Or... Buck it. Let's go behind the barn, we should be alone and all."
                            stop music fadeout 1.0
                            scene end07
                            with fade
                            "And both of you went all \"kissu-kissu my cousin\". Except you two weren't really cousins."
                            play sound "SFX/fail.mp3"
                            "--Braeburn ending 1--"
                            jump credits
                            
                        "I understand":
                            $0#Useless line is useless. Except for the interpreter.
                
                p "Yeah, whatever floats your boat. If everyone was like that, the world would be a simpler place."
                b "You're cute sugarcube. But Big Mac is there, I'm gonna try one last time. We should meet again someday."
                play sound "SFX/gotObject.mp3"
                "He gives you a sugar cube and leaves."
                $p_aj = "sugarcube"
                $ nb_lock = nb_lock + 1
                
                hide braeburn
                with dissolve
                p "Well. Let's at least eat something."
                "You look at the table..."
                stop music fadeout 1.0
                scene black
                with fade
                "...And thus you ate, without further noticeable conversations. After that, you went back to the crossroad."
                
            "Play a bit":
                p "I'm feeling playful. I bet that I could catch an apple in 10 seconds flat."
                if(playername=="Rainbow Dash"):
                    aj "Prove it, \"Dashie\"."
                    "She's clearly grinning at the thought."
                else:
                    aj "You're not Rainbow, but you know what saying this means, don't you [playername3]?"
                    p "That I need to prove it?"
                   
                    aj "Exactly."
                    p "I will."
                    "Are you grinning at the thought? ...Whatever."
                
                stop music fadeout 1.0
                scene black
                with fade
                
                "Both of you went to the nearest barrel full of water and apples."
                
                scene bg apple barn
                with fade    
                play music "Music/applebarn.mp3"
                show applejack hat side calling
                with dissolve
                
                aj "So, let's see what you got [playername2]! I bet you can't beat..."
                show applejack hat applemouth
                with fade
                
                aj "Thisch!"
                
                "Wait, how did she do that? Three in a second? And you've never tried to catch an apple with your pony-mouth before. Seriously, have you looked at how different the teeths are? It's a wonder to even talk with one like that."
                
                "What should you do?"
                
                menu waterapple:
                    "Do your best":
                        "Trying to do your best, eh? Let's see what happens, then."
                        p "I can do better!"
                        
                        "Well, that's not for you to decide, so... 4 apples in the water, but you're a level 1 pony with only 2 in dexterity... Let's roll 2 D20..."
                        
                        if((playername=="Twilight Sparkle") and (p_ts == "astronomy")):
                            "3 and 8? Uh. That's pretty bad, 'Twilie'."
                            
                        elif (playername == "Rainbow Dash" and p_rd == "sunglasses"):
                            "14 and 13? That's quite good! Uh. But you have the cool sunglasses, it boosts your charm, but lowers your dexterity by 20 points. Your result isn't 27, It's only 7. That's bad, 'Dashie'."
                        elif (playername == "Pinkie Pie" and p_pp == "cupcake"):
                            "You rolled... A cupcake? Wait, where are my dice? You automatically lose, then."
                            
                        elif (playername == "Rarity" and p_rr == "hat"):
                            "1 and 1. And that is not even counting for that ridiculous hat that cuts your dexterity in half."
                            
                        elif (playername == "Fluttershy"):
                            "2 and 3. If you had a bunny with you it would boost your stats, but you aren't the real Fluttershy, so it's no use."
                            
                        elif (playername == "Applejack"):
                            "17 and 20! But I have to apply an aribitrary negative modifier, since you are not the real Applejack and thus cannot beat her."
                        elif(doomloop > 9):
                            "This won't be your cupboard ending. Stop trying, I said."
                            "Wait, wrong menu. But you still failed your dice roll!"
                        
                        else:
                            "2 and 1? Epic failure. You didn't even try, well, not literally."
                        p "Hey! You're making these up, don't blame me!"
                        show applejack hat wtf
                        with dissolve
                        aj "What now?"
                        p "Not you AJ, the narrator."
                        aj "Oooookay sugarcube..."
                        "Ah! Don't forget that you shouldn't be able to talk back. And now let's put you in the water and let you have a single apple in 12 seconds."
                        p "Wai-"
                        "And you just did that."
                        p "Arrr... Pfff.... Gnnnn..."
                        show applejack hat supersmile
                        with dissolve
                        aj "That's a bit slow for ten seconds and you only got one apple, [playername2]. I guess I won!"
                        p "I guess you did."
                        
                    "Do your worst":
                        "Oh, come on! Where's the fun? I would have pretended to roll dice and said random things depending on your character!"
                        p "I'll see what I can do."
                        "Yeah, yeah, and the more you try, the less you're able to catch an apple. Your miserable attempt is clearly a reflection of your general failure at life and it takes you 25 seconds to catch a single fruit."
                        show applejack hat meh
                        with dissolve
                        aj "Were you even tryin'?"
                        p "Yes, of course I was! I'm no wimp! It... It was because of the number of apples already in the water. I swear!"
                        play sound "SFX/sigh.mp3"
                        "She sighs."
                        
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
                
                "And you went back to the crossroad."
                $appl2 = True
                
        "Getting this [p_aj] was worth the trip. I guess."
        $appl1 = True
        jump outdoors
        
    if(appl2==True):
        play music "Music/applebarn.mp3"
        "You come back to the Apple Family Reunion. A lot of ponies are here, discussing, playing, dancing... But for the moment, as you're not seeing Applejack anywhere and are a bit hungry due to the trip, you focus your attention on some apple pie."
                
        if(playername=="Applejack"):
        
            u "Howdy cousin! You did a great job!"
            show braeburn happy
            with dissolve
            p "Sorry, I'm surely not the one you're thinking I am."
            u "Ah, sorry mam', I thought you were the ol' AJ."
            p "I am! But I'm not. My name is Applejack, I look like the Applejack you know, but I'm not her. Look, she's just over there, talking to... Where is she?"
            "You fail to point out the real AJ to the pony."
            b "Oh. Don't worry, I trust you. And I'm Braeburn, coming from Aaaapple-loooooooosa! Great town, you should come someday!"
            
        else:
            u "Howdy! Erm... AJ's friend?"
            show braeburn happy
            with dissolve
            p "Yes, close friend. My name is [playername]."
            b "Oh yes! We've met before, in Aaaapple-looooooosa! I'm Braeburn!"
            p "Yes, with Bloomberg, the \"You gotta share\" song and all of that..."
            b "Good times, you should come back someday."
                
        p "Maybe I will. Especially if they're all as friendly as you are."
        b "You bet. But nopony there makes cider like Granny Smith does."
        p "Cider, uh? Well, don't drink too much!"
        "You added a wink to your last comment."
        b "You know, I might."
        p "A handsome stallion like you? What could you possibly want to blur with hard cider?"
        b "Big Macintosh. First stallion I met who did not react to my charms."
        p "Wait, you're like...?"
        b "Colt cuddler? Nah. Unicorn or pegasus, pony or buffalo, male or female, all have their perks. And kinks. And I like some variety, you know?"    
        p "Yeah, whatever floats your boat. If everyone was like that, the world would be a simpler place."
        b "You're cute sugarcube, do you know that?"
        
        menu cute_bb:
            "I'm not cute!":
                
                p "I... I'm not cute! And you're a stallion!"
                b "Oh. I didn't guess you were only into mares, sorry sugarcube!"
                p "Yeah, I'm not g... Wait, I'm a mare myself."
                b "Ah guess you are, not that it matters to me. Are you gender confused or somethin'?"
                p "N... No. Just forget it. Is there anything I could do? That doesn't involve kisses, of course."
                
            "I sure am. *wink wink*":
                
                p "You bet I'm cute. Not as much as you are though."
                b "And what does your cute face intends to do today?"
                p "I was thinking about \"discussing\" with your cute face. You know, with passion."
                b "I sure would love that... Let's go behind the barn, we should be alone and all."
                stop music fadeout 1.0
                
                        
                if(playername=="Applejack"):
                    scene end08  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end09
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end10
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end11
                    with fade
                if(playername=="Rarity"):
                    scene end13
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end12
                    with fade
                
                
                "And both of you went all kissu-kissu and stuff. Shamelessly. You scoundrel."
                play sound "SFX/fail.mp3"
                "--Braeburn ending 2--"
                jump credits
                
            "I don't have enough alcohol in my blood for that.":
                
                p "I have too much blood in my alcohol for that."
                b "I sure can offer you some hard cider."
                p "That would be great! And in return I would kiss you all day."
                
        b "What about more than kisses?"
        p "This isn't a clop story, so nothing more should happen."
        b "Darn it."
        p "Sorry Braeburn. So... Don't you have anything I can do?"
        b "What about bringing me some sunglasses?"
        p "Sunglasses?"
        b "Yeah, I want to try a different approach with Big Mac."
        p "Consider it done!"
        b "Thanks sugarcube, I'll wait."
        
        if(p_rd == "sunglasses"):
            p "No, literally done, I have a pair here, but I can't let you have them forever."
            $appl2 = False
            $appl3 = True
            jump give_brae_sunglasses
        p "I won't be long, see you later!"
        "And you leave the party."
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "New quest! The sunglasses investigation! Let's play an epic music! Wait... No. It might not be adequate with the other parts of the game. And you would have been going back to the crossroad all the same anyway."
        $appl2 = False
        $appl3 = True
        jump outdoors
        
    if(appl3==True):
        play music "Music/applebarn.mp3"
        "Once more, you go back to the Apple barn."
        if(p_rd == "sunglasses"):
            p "But this time, I have the sunglasses!"
            "Yes you do and Braeburn is just there."
            
            show braeburn happy
            with dissolve
            
            b "Welcome back [playername2]!"
            p "Hey Brae, I've got your sunglasses, but I can't let you have them forever."
            
            label give_brae_sunglasses:
                $0#Useless line is useless. Except for the interpreter.
            
            b "That was fast! ...What do you mean by not forever?"
            p "You want to test them with Big Mac, right? Just return them once you're done."
            b "Can't I just have them until tomorrow?"
            p "I guess I could let you borrow them longer... But I want something else in return."
            
            menu brae_reward:
                "I want some alcohol":
                    p "I want to drink. A lot."
                    b "Wow. Calm down sugarcube, you're not Berry Punch. What about some cider?"
                    p "Your cider bottle. My mouth. Now."
                    
                    stop music fadeout 1.0
                          
                    if(playername=="Fluttershy"):
                        scene end14
                        with fade
                    if(playername=="Rainbow Dash"):
                        scene end16
                        with fade
                    if(playername=="Rarity"):
                        scene end17
                        with fade
                    if(playername=="Twilight Sparkle"):
                        scene end18
                        with fade
                    
                    "And you... Drank... A lot? Until accepting kisses from random ponies did not bother you anymore? What the..."
                    play sound "SFX/fail.mp3"
                    "--Drunk ending--"
                    jump credits
                    
                "I want some time with AJ":
                    p "I want some alone time with AJ, if you know what I mean."
                    b "I sure do [playername2], but that's not really up to me."
                    p "Come on, I helped you with Big Mac, now it's your turn to help me! To try, at least."
                    b "I promise nothin', but I'll do my best... Come back in a moment."
                    hide braeburn
                    with dissolve
                    "And so he left, to try something undisclosed."
                    
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
    
        play music "Music/applebarn.mp3"

        "You get back to the Apple farm, where everypony is slowly starting to leave, either going to their vehicle so they can get home, to their trailer, so they can prepare themselves for the night to come, or to any other sleeping place there."
        "The Apple house is clearly too small to host the whole crowd. Most ponies have come from too far away not to stay over and wait for the next day before starting to drive home. Although most would simply ride the train."
        
        show applejack hat happy

        aj "Howdy, [playername3]! I didn't think you'd come back! Did you want to stay over for the night?"

        p "Yeah, I was thinking about having a little extended family fun time. You know, us two, in a secluded space, sharing a close bond…"

        show applejack hat supersmile

        aj "Don’t worry [playername2], I have all your needs covered!"
        
        scene black with fade
        stop music fadeout 1.0

        "And thus, in her bedroom, you and Applejack got close to one another, with a sinful look in your eyes, there was some lip biting, moaning and…"
        
        play sound "SFX/haha.mp3"

        aj "I win! Haha! I’m the best Gin Rummy Matching player in all the family!"

        "Your moans of frustration turned to a grunt of displeasure. Followed by a chuckle as you cleaned up the playing area and shuffled the cards again."

        p "I didn’t think you’d be so much into card games! … Wait. It feels like I am totally missing some kind of point there."

        aj "As if you expected us two to be doing something else, hidden in my bedroom? They don’t call me the Ungar of the family for nothin’!"
        
        play sound "SFX/sigh.mp3"

        p "Literally no one call you that."

        "And thus you two spent the remaining of your evening and night playing games and having some tame sisterly fun. Well, almost-sisterly."

        p "Are you sure there shouldn’t be a scene there with a lot of inces-"

        "Shhhh"

        
        if(playername=="Fluttershy"):
            scene end02
            with fade
        if(playername=="Rainbow Dash"):
            scene end03
            with fade
        if(playername=="Rarity"):
            scene end04
            with fade
        if(playername=="Twilight Sparkle"):
            scene end05
            with fade
        
        play sound "SFX/trueEnding.mp3"
        "--Applejack true ending--"
        jump credits
    
    "After walking for a bit, you arrive at the Apple barn in Sweet Apple Acres."
    p "The barn seems full of busy ponies for the moment. I should probably go somewhere else."
    stop music fadeout 1.0
    scene black
    with fade
    "What a useless trip... You went back to the crossroad anyway."
    jump outdoors
    
return