label carouselboutique:
    stop music fadeout 1.0

    scene bg carousel boutique
    with fade
    
    if(caro1==False):
        play music "Music/carousel.mp3"
        "You come inside the Carousel Boutique. Amongst the jewels, hats, dresses, other pieces of clothing and some dumb fabric stands a white coated, purple maned mare, Rarity."
        
        show rarity happy
        with dissolve
        
        r "Welcome to the Carou-"
        
        if(playername=="Rarity"):
            show rarity shocked
            with dissolve
            r "Sweet Celestia! You are as tasteful as I am, if not more!"
            p "Thank you, miss...?"
            show rarity happy
            with dissolve
            r "Rarity. I'm the owner, designer and manufacturer."
            p "Really? Then we share the same name, my dear. What a coincidence!"
            "Yeah... Coincidence. For sure."
        else:
            r "[playername]! What a surprise!"
            
        if(playername=="Twilight Sparkle"):
            r "I was designing a new hat! Do you have some time? I sure would appreciate the help of a pony as skilled with mathematics as you."
        if(playername=="Rarity"):
            r "I was designing a new hat! Do you have some time? I'm sure it would interest you."
        if(playername=="Fluttershy"):
            r "I was designing a new hat! Do you have some time? I'm sure that somepony with your knowledge of the haute couture would be able to help."
        if(playername=="Rainbow Dash"):
            r "I was... Designing a new hat. I know you are not quite the one to wear them, but if you have some time, I surely could use your help."
        if(playername=="Pinkie Pie"):
            r "I was... Designing a new hat. I know it's not really fun, but if you have some time, I surely could use your help."
        if(playername=="Applejack"):
            r "I was... Designing a new hat. I know you are going to think about its practicality before everything, but I'm willing to let you a chance to prove me wrong."
            
        "What are you going to say?"
            
        menu raritychoice1:
            
            "\"I certainly would love to help!\"":
                p "I certainly  would love to help!"
                
                
            "\"Shall your doom tear you apart!\"":
                p "DIE, YOU PEASANT! SHALL YOUR DOOM TEAR YOU APART FOR HAVING ASKED SUCH A FRIVOLOUS QUESTION!"
                show rarity shocked
                with dissolve
                r "Erm... Are you allright [playername2]?"
                p "... Why did I just say that?"
                show rarity srsly
                with dissolve
                r "Let's pretend that never happened."
                show rarity happy
                with dissolve
                jump raritychoice1
                
            "\"My destiny is elsewhere...\"":
                p "My destiny is elsewhere... May you forgive me. The shadows are calling!"
                r "The... Shadows?"
                
                stop music fadeout 1.0

                if(playername=="Applejack"):
                    scene end58  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end59
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end60
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end61
                    with fade
                if(playername=="Rarity"):
                    scene end62
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end63
                    with fade
                
                p "These shadows!"
                r "Eek! Where are we? Why can't I see myself?"
                "You weren't supposed to come here too."
                r "Who are you? Where are we?!"
                "Ugh... Not this again! Let's just end it already!"
                "--Rarity ending 1--"
                jump credits
                
            "\"Don't you have a spare ruby?\"":
                p "Don't you have a spare ruby?"
                r "Yes... But why do you ask it for?"
                if(libr3 == True):
                    p "I do know a hungry dragon. And you will refuse to talk to me after that."
                    r "Why would I...? Wait. You came here just to ask for a jewel because a dragon is hungry? That's very considerate of you. I can give you one, just wait there."
                else:
                    p "I'm not interested in your path right now."
                    r "My... What?"
                    p "Your path. I'm don't know the purpose of the ruby yet, but it'll be useful. And you will refuse to talk to me after that."
                    if(playername=="Pinkie Pie"):
                        r "Well. You are just being Pinkie Pie, I guess. Wait there."
                    else:
                        r "[playername], you are just sounding like pinkie Pie right now. Anyway, wait there."
                    
                stop music fadeout 1.0
                scene black
                with fade
                
                "And she went searching for a ruby, quickly coming back"
                
                scene bg carousel boutique
                with fade
                play music "Music/carousel.mp3"
                show rarity happy
                with dissolve
                
                r "There, a nice and pure ruby."
                "She gives you a ruby."
                
                $p_rar = "ruby"
                
                p "Thank you!"
                r "Now, why would I stop talking to you?"
                p "I don't know, it's up to you. I'm just aware of the fact that the next time I'll be there, I won't be able to find you."
                r "That's a shame!"
                p "Not really. I either already completed your path or will do it in the future."
                r "That's quite a Pinkie talk."
                p "Anyway, thank you again! We might see each other again, or not!"
                r "I hope we will! See you soon!"
                
                stop music fadeout 1.0
                scene black
                with fade

                "And you went back to the crossroad. You are beginning to understand what breaking the 4th wall feels like."                 
                p "With you being always on my back, that's not surprising."                 
                "You are doing it again! But let's continue."
                $ caro1 = True
                $ nb_lock = nb_lock + 1
                jump outdoors
                
        
        if(playername=="Rarity"):
            r "Help? I did not ask for so much! But if you are willing, who am I to refuse?"
        else:
            r "Thank you [playername2], it would be harder without your help."
            p "I could do it some more, you know, simply ask."
            r "Don't worry, it's not like I never did it alone before."
                    
        stop music fadeout 1.0
        scene black
        with fade
        
        "And both of you worked on the most fabulous hat Rarity ever created. So fabulous that even you, yes, YOU! Couldn't imagine it. That's why the scene is black. It's totally not related to our lack of visual artist."
        
        scene bg carousel boutique
        with fade
        play music "Music/carousel.mp3"
        show rarity superexcited
        with dissolve
        
        $ p_rar = "hat"
        
        r "Look at that! This is so... So..."
        
        if(playername == "Twilight Sparkle"):
            p "Conceptual."
        if(playername == "Rarity"):
            p "Fabulous."
        if(playername == "Fluttershy"):
            p "Grandiose."
        if(playername == "Rainbow Dash"):
            p "Awesome!"
        if(playername == "Pinkie Pie"):
            p "Fun!"
        if(playername == "Applejack"):
            p "Impractical."
            
        if((playername != "Rarity") and (playername != "Fluttershy")):
            show rarity srsly
            with dissolve
            r "I knew you would say that."
        else:
            r "Exactly!"
        
        show rarity happy
        with dissolve
        r "Anyway, thank you for your help, you can come for some tea anytime you want!"
        p "That's so nice of you, be assured that I will come to you soon!"
        r "I'm sure you will."
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "And after the usual farewell, you went back to the crossroad."
        $ caro1 = True
        $ caro2 = True
        
        jump outdoors

    if(caro2==True):
        play music "Music/carousel.mp3"
        "You come to the carousel boutique one more time, thinking about the hat Rarity made with your help."
        
        show rarity happy
        with dissolve
         
        if(playername == "Rarity"):
            r "Hello again darling."
        else:
            r "Hello again [playername2]."

        p "Hello again Rarity! Are you designing something?"
        r "Not really, I'm simply keeping my ledger up to date, darling."
        p "Your... Ledger?"
        r "Yes. The notebook containing all my sales and purchases, it really helps when dealing with the equestrian taxes."
        p "Is there anything I could do to help?"
        r "Help? Do you mean... With my ledger? Or with something else?"
        
        menu:
            "Help with the ledger":
                p "Yeah, I'm offering my help for this, the ledger-stuff."
                if(playername=="Twilight Sparkle" or playername=="Rarity"):
                     r "Well... You surely can help, but I was thinking of something else."
                     p "Oh? What is it?"
                else:
                    r "Don't take it wrong, but... I don't really need your help with that."
                    "How surprising."
                    p "With that? Do you mean that you need help with something else?"
                    
            "Offer your help for something else":
                p "I'm not really interested in your ledger, to be honest. Is there anything else I can do to help?"
                r "Yes, of course! I was thinking about something else myself."
                p "Really? What is it?"
                
            "Offer your \"help\" for \"something else\"":

                p "What about a little hoof massage?"
                if(playername=="Rarity"):
                    show rarity shocked
                    with dissolve
                    r "That would be lovely my dear, but I prefer not to ask you something so intimate, we're merely acquaintances."
                    p "Did I mention that I was going to work for the spa? I will start next Monday."
                    show rarity flattered
                    with dissolve
                    r "Then... I may do an exception for you."
                    
                if(playername=="Twilight Sparkle"):
                    r "Oh! Did you read an interesting book on the matter recently?"
                    p "Yes, I just need some practice, but everything is going to be fine."
                    r "Be my guest, Twilight."
                    
                if(playername=="Pinkie Pie"):
                    show rarity srsly
                    with dissolve
                    r "Does that involve foodplay?"
                    p "Why would it involve foodplay?"
                    r "With you, it always involve foodplay."
                    p "I'm just wanting to massage your hooves, not turn them into cupcakes, duh!"
                    show rarity flattered
                    with dissolve
                    r "Well... Let's try it then."
                    
                if(playername=="Applejack"):
                    show rarity srsly
                    with dissolve
                    r "YOU want to give ME a hoof massage?"
                    p "That's right sugarcube! And my own hooves are clean, no dirt on them, don't worry."
                    r "That's... New. I will give you a chance then."
                    
                if(playername=="Rainbow Dash"):
                    show rarity srsly
                    with dissolve
                    r "Since when do you give hoof massages?"
                    p "I always hated hooficures, but hoof massages? That's the deal."
                    r "So, you like to get them so much that you are also willing to give them?"
                    p "Yeah, be happy for what you give, not what you get. 'Sort of."
                    show rarity flattered
                    with dissolve
                    r "That's a rare occasion that I can't decline."
                     
                if(playername=="Fluttershy"):
                    r "Are your hoof massages sweeter than your other massages?"
                    p "Of course! You can force a bit on the spine, but not on the hooves, that would be dangerous."
                    r "We may have different a different view on the definition of \"dangerous\", but I will accept your offer."
                    
                p "Let's get started then. Just relax and let me work."
                
                stop music fadeout 1.0

                if(playername=="Applejack"):
                    scene end64  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end65
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end66
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end67
                    with fade
                if(playername=="Rarity"):
                    scene end68
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end69
                    with fade                
                
                "And you massaged her hooves with all your might, before helping her with her legs and then every body part where she was really tense and needed to relax."
                "Needless to say, it led you two to a long and intimate moment where Rarity searched her oil and massaged you back, being quite talented herself."
                p "I really regret having no picture for this one."
                "Later, perverted player, later..."
                "--Rarity ending 2--"
                jump credits
                
        r "You see, I'm quite busy here and I don't have any herbs to make some tea anymore."
        p "Oh, and you want me to bring some to you, that's all?"
        r "Yes, it would help me greatly."
        if(p_flut == "tea"):
            p "Lucky you, I have some here!"
            $caro2=False
            $caro4=True
            jump rarity_get_tea

        else:
            p "Consider it done, Rarity!"
        r "I will be right here waiting for you if you need me or want to give me the tea you found."
        p "Okay, see you soon!"
        r "See you soon, darling."
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "And you went back to the crossroad. Where could you get tea, wonderful natural product?"
        $caro2=False
        $caro3=True
        jump outdoors
        
        
    if(caro3==True):
        play music "Music/carousel.mp3"
        show rarity happy
        with dissolve
        "You are back to the boutique, where Rarity is waiting for her tea."
        r "Oh, you are back! Do you have the herbs, darling?"
        
        if(p_flut == "tea"):
            p "Yes, indeed!"
            label rarity_get_tea:
                r "Marvelous! I'm going to prepare some then, just wait five minutes. If you have some quick business to do around, don't worry, I can handle it on my own, just be back soon, okay?"
                p "Of course Rarity, I'll be back soon."
                stop music fadeout 1.0
                scene black
                with fade
                "Wait... What did you want to do in the first place?"
                $caro3 = False
                $caro4 = True
                jump outdoors
        else:
            p "Not really, but I'm searching!"
            r "Did you try \"Books and Quills\"?"
            p "Don't they only sell books and quills?"
            r "Everypony has a side business, dear. You are right though, they are more the type to also sell videos than tea."
            p "Honestly? What kind of videos a book and quills store could sell?"
            r "Adult videos."
            p "I'm afraid to understand."
            r "Yes, I know, adult things like politics or economy are always between scary and boring."
            p "Anyway, I'm on my way to find you some tea! See you soon!"
            r "Good luck [playername2]!"
            stop music fadeout 1.0
            scene black
            with fade
            jump outdoors
            
    if(caro4 == True):



        "You go back to the Carousel Boutique, where everything is chic and magnifique, including the fabulous mare who is pouring some tea in a cup."

        r"Welcome back [playername]! I just finished brewing the tea. This scent is divine!"

        if(playername=="Twilight Sparkle"):
            ts"Yes, it clearly is better than any book I sniffed. ... Not that I commonly do that, only to those with a great smell."
        if(playername=="Rainbow Dash"):
            rd"It's radical. Better than Soarin musk! ... Not that we did anything funny after the grand galloping gala."
        if(playername=="Rarity"):
            r"It really is divine, ma chère. Better than Hoity Toity intimate fragrance. ... Not that I could know it."
        if(playername=="Fluttershy"):
            fs"Oh. Yes, it's lovely. Even better than animal scent covered in forest aroma, the dejections here can sometimes be disgusting."
        if(playername=="Pinkie Pie"):
            pp"Ooooh! Yes yes! Even better than cake! You did not make cake with it, did you? It would totally not be sweet enough!"
        if(playername=="Applejack"):
            aj"Er, yeah. Ah guess. Braeburn is still higher in my list of smellin' good. ... Erm. I mean braeburn, the apple, not Apple. Not my cousin."

        r"Let's change the subject, my dear."

        "And both of you sat down to enjoy tea time, until..."

        r"The taste is REALLY great, my dear."


    
        if(playername=="Applejack"):
            scene end70  
            with fade          
        if(playername=="Fluttershy"):
            scene end71
            with fade
        if(playername=="Pinkie Pie"):
            scene end72
            with fade
        if(playername=="Rainbow Dash"):
            scene end73
            with fade
        if(playername=="Rarity"):
            scene end74
            with fade
        if(playername=="Twilight Sparkle"):
            scene end75
            with fade
        
        "--Rarity true ending--"
        jump credits
        
    "You come to the Carousel Boutique. The door isn't locked and you could easily steal some rubies or sapphires, but that wouldn't be wise."
    p "The boutique is empty. I better should go find somepony elsewhere."
    stop music fadeout 1.0
    scene black
    with fade
    "And you return to the crossroad."
    jump outdoors

return