label fluttercottage:
    stop music fadeout 1.0

    scene bg fluttershy cottage
    with fade
    
    if(flut1==False):
        play music "Music/fluttercottage.mp3"
        "Fluttershy's cottage... There are birds, squirrels, bunnies and other critters walking, running and doing critter stuff there."
        "Oh, and a yellow pony with a pink mane is not so far away, certainly Fluttershy."
        "What are you going to do?"
        
        menu crittercare:
            
            "Pet the bunny":
                "You go near the little animal and bend, approaching your hoof, but he quickly turn its head and run away."
                
                fs "Oh... Excuse his attitude, the poor little cutey bunny doesn't let strangers touch-"
                
                if(playername=="Fluttershy"):
                    show fluttershy fly what
                    with dissolve
                    fs "How... you..?"
                    p "H... Hello."
                    fs "H... Hello... To.... To you too... What... What's your name?"
                    "You whisper."
                    p "My name's Fluttershy..."
                    "Fluttershy whisper too."
                    fs "My name's Fluttershy too..."
                    p "Do you... Do you like animals?"
                    show fluttershy fly destiny
                    with dissolve
                    fs "Do I like them? I LOVE them! All the critters, no matter how they're small, all the squirrels, the little birds, the cute little bunnies..."
                    "She starts to sing how she adore them. That surely is a good sign."
                    p "I... I love them too. If, if you would like to know..."
                    show fluttershy fly happy
                    with dissolve
                    fs "Really? We could be friends... If... If that's okay with you."
                    p "Of course!"
                else:
                    show fluttershy fly happy
                    with dissolve
                    fs "Oh, [playername2]! I didn't recognize you at first. Don't mind the bunny, he is just a bit tired."
                    
                fs "Would you like to come in? I'm boiling water, we could have some tea together."
            "Pet the pony":
                "You approach the critter without her noticing you and when you start to brush her mane with your hoof..."
                show fluttershy fly shock
                with dissolve
                fs"Eeeeeeeek!"
                "She didn't like that!"
                if(playername=="Rainbow Dash"):
                    show fluttershy side embarassed
                    with dissolve
                    fs "R... Rainbow.... I... I told you that... Um...."
                    "It seems that she and Rainbow Dash have something going on... But you wouldn't use that at your own advantage, would you?"
                    menu flutterabuse:
                        "Of course not!":
                            p "Sorry Fluttershy, I didn't mean to scare you! Honest! Sorry if you didn't like it."
                            show fluttershy fly happy
                            with dissolve
                            fs "N... No, that's okay... Anyway, would you like to come in? I'm boiling water, we could have some tea together."
                            
                        "You bet I would!":
                            p "Shh... Just relax..."
                            fs "*Squee*"
                            p "That's it... Now, come here, for a little wing-hug. Just that, nothing more..."
                            stop music fadeout 1.0
                            scene end20
                            with fade
                            "And both of you hugged. And kissed. And you are really lazy to end the game so soon, this end was so predictable."
                            p "I still got future chibis, right?"
                            "As soon as this game has a visual artist, yes, you will have chibis."
                            "--Fluttershy ending 1--"
                            jump credits
                else:
                    if(playername=="Fluttershy"):
                        
                        show fluttershy fly what
                        with dissolve
                        fs "How... you...?"                         
                        p "H... Hello."
                        show fluttershy side embarassed
                        with dissolve
                        fs "H... Hello... To.... To you too... What... What's your name?"
                        "You whisper."
                        p "My name's Fluttershy..."
                        "Fluttershy whisper too."
                        fs "My name's Fluttershy too..."
                        p "Do you... Do you like animals?"
                        show fluttershy fly destiny
                        with dissolve
                        fs "Do I like them? I LOVE them! All the critters, no matter how they're small, all the squirrels, the little birds, the cute little bunnies..."
                        "She starts to sing how she adores them. That surely is a good sign."
                        p "I... I love them too. If; if you would like to know..."
                        show fluttershy fly happy
                        with dissolve
                        fs "Really? We could be friends... If... If that's okay with you."
                        p "Of course!"
                    fs "[playername2]... Why did you try to...?"
                    p "Sorry if you didn't like it."
                    fs "N... No, that's okay... Anyway, would you like to come in? I'm boiling water, we could have some tea together."
        p "Yes, sure!"
        fs "Then, please follow me [playername2]."
        stop music fadeout 1.0
        scene black
        with fade
        "And both of you went into the house, a nice and cozy place."
        play music "Music/fluttercottage.mp3"
        scene bg apple family den
        with fade
        show fluttershy fly happy
        with dissolve
        p "Wait, this isn't your house."
        fs "Yes, it's a stock image. Caramel Truffle forgot to download a background for my home, but I don't mind, I'm sure that the deviantArt pony vector club has done something nice and he will find it. Or better, a visual artist will draw it just for us..."
        p "I would not trust this pony's memory..."
        fs "Anyway... Please have a sit, I'm going to the kitchen and will be back very soon."
        if(playername=="Pinkie Pie"):
            p "Okey-dokey-lokey!"
        else:
            p "No problem Fluttershy."
        stop music fadeout 1.0
        scene black 
        with fade
        "And she headed for the kitchen. Some muffled noises could be heard, like those of cups being placed on a plate and soon after the silence of the cottage was there again, Fluttershy went back in the room."
        scene bg apple family den
        with fade
        play music "Music/fluttercottage.mp3"
        show fluttershy fly happy
        with dissolve
        fs "And there it is... Some nice hot tea. New recipe, I hope it will be good, I don't even have tried it yet..."
        p "Don't worry Fluttershy, I'm sure it will be one of the best I ever drank."
        fs "Th... Thanks..."
        "She blushes slightly at your comment and both of you drink quietly a sip of tea."
        p "Beside, the taste is quite good. What's in it?"
        fs "Oh... Some herbs from the Everfree Forest, Zecora helped me choose some and... Oh! Right, she said that \"For a good taste, this plant you shouldn't miss, but drink too much and you will search another bliss.\" I don't know what it was supposed to mean though..."
        "It clearly is an aphrodisiac. Should you tell her?"
        menu aphrodishy:
            "Yes":
                "You are right. Why should you drug a cute and helpless mare?"
            "No":
                "You are right. Why shouldn't you drug a cute and helpless mare?"
                p "I have no idea, sorry Fluttershy."
                fs "Don't worry. I should have asked, the blame is mine."
                stop music fadeout 1.0
                scene black
                with fade
                "And you drank and drank this aphrodisiac tea, until..."
                scene bg apple family den
                with fade
                play music "Music/fluttercottage.mp3"
                show fluttershy superhappy
                with dissolve
                fs "Oh my... It's so hot here... Or is it just me?"
                p "I'm afraid that it's a bit of both. It's hot here and you are too."
                "She blushes."
                fs "[playername2], would you mind..."
                p "Hugging you tight as the afternoon end? I wouldn't mind at all."
                "She blushes even more and squee in approval."
                stop music fadeout 1.0
                if(playername=="Applejack"):
                    scene end21  
                    with fade          
                if(playername=="Fluttershy"):
                    scene end22
                    with fade
                if(playername=="Pinkie Pie"):
                    scene end23
                    with fade
                if(playername=="Rainbow Dash"):
                    scene end24
                    with fade
                if(playername=="Rarity"):
                    scene end25
                    with fade
                if(playername=="Twilight Sparkle"):
                    scene end26
                    with fade
                "And you ended the day in each other arms, happy together."
                "--Fluttershy ending 2--"
                jump credits
        p "Maybe that it's an aphrodisiac?"
        show fluttershy fly worried
        with dissolve
        fs "An aphrodi- Oh my... We shouldn't drink that..."
        p "Don't worry, I'm sure a cup will be fine!"
        show fluttershy fly happy
        with dissolve
        fs "You are probably right, but... Just one cup. I have the birds that I must feed, they're going to be hungry otherwise..."
        p "Of course Fluttershy."
        "Special tea? Bird seed? You know what you should get, don't you?"
        
        menu teabird:
            "Tea!":
                p "Before you go feed them, could you give me some of the herbs for this infusion, please? The taste is really
 good."
                "She blushes again."
                fs "Of course [playername2], but don't abuse it..."
                p "Don't worry, I won't drink more than a cup per day."
                "You didn't say that you wouldn't let somepony else drink more of it..."
                stop music fadeout 1.0
                scene black
                with fade
                "And both of you drank your cup, Fluttershy gave you enough tea to drug somepo- erm. To enjoy a cup per day for a month. And then she went feeding the birds, saying that you probably wouldn't be able to find her until the next day."
                "After that, you went back to the crossroad."    
                $ p_flut = "tea"
                $ nb_lock = nb_lock + 1

            "Seeds!":
                p "Can I go with you? If you give me some seeds, I certainly won't refuse to use them to feed the birds."
                fs "Oh, of course! They are not easily scared of strangers, as long as you are quiet."
                if(playername=="Pinkie Pie"):
                    "Saying that to the real Pinkie would probably have been a necessity."
                p "I will try to be as silent as you are!"
                "She smiled at your comment."
                stop music fadeout 1.0
                scene black
                with fade
                "And both of you drank your cup, Fluttershy gave you enough seeds to feed a dozen of birds and remembered that she had something else to do before birds-feeding, something special caused because of the moon... You told her that it was okay and you would come back later when she would have finished and you went back to the crossroad."
                $ flut2 = True
                $ p_flut = "seeds"
                
        $ flut1 = True
        
        jump outdoors

    if(flut2 == True):
        play music "Music/fluttercottage.mp3"
        "You are back to the cottage. The last time you saw Fluttershy, she gave you seeds and asked you to wait. She may be ready now?"
        show fluttershy fly happy
        with dissolve
        
        fs "Welcome back [playername2]!"
        p "Are you ready now? The birds must be hungry now."
        fs "Oh... Yes.... Sorry..."
        p "I was joking! But let's go!"
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "The two of you went to the edge of the Forest. If Fluttershy didn't guide you there but went alone, you wouldn't have been able to find her."
        
        scene bg forest
        with fade
        play music "Music/fluttercottage.mp3"
        show fluttershy fly happy
        with dissolve
        
        fs "Here we are... Come on little ones..."
        "A dozen of birds are coming, blue, red, yellow... All are colorful and visibly hungry, by the way they ate the seeds Fluttershy is throwing."
        p "How do I feed them? Like that?"
        "You start imitating her at your best."
        fs "That's it, you are skilled [playername2]. If that's okay with you, I sure could use the help of somepony like you... From time to time I mean... And if you are okay with it...."
        p "Don't worry, I will gladly offer my help again."
        "She blushes again."
        fs "[playername2]? Did you read some good books recently?"
        
        if(p_book=="xxx"):
            p "Yes, I've read this book!"
            "You show her the book Twilight gave you."
            $ flut2 = False
            $ flut4 = True
            
            jump fluterx
        
        p "A good book? None that I can think of..."
        fs "Not even one you..."
        "She whispered the end of her sentence."
        p "Sorry? I didn't catch the end."
        "Fluttershy blushed again."
        fs "One you... you wouldn't.... You know, talk about usually...."
        p "No... Sorry. I didn't read anything at all recently."
        if(playername=="Twilight Sparkle"):
            "Being [playername], you try to be convincing."
            p "Well, except from a bunch of old books concerning Starswirl the Bearded and his less known spells, but none that could interest you deeply."
        fs "Well... If you... You know.... Find a book... You wouldn't....  You know... Share with somepony.... You know.... We could like.... Read it together.... If that's okay with you...."
        p "I... Guess that I can do that."
        "She squee-d."
        if(playername=="Fluttershy"):
            p "But... You know... We also could just do it without a book."
            fs "Wha.... What?"
            p "We... You know.... We're both quiet and all... And you know what they tell about the quiet ones..."
            fs "Y... Yes, but..."
            p "Are you proving that the saying is false? Be honest."
            fs "Well... Erm.... No....."
            p "I'm sure that we share a lot in common..."
            fs "Even for..."
            "And she whispered in your ear."
            p "Especially that one. It certainly is one of my favorite fetishes..."
            fs "Eeeek! I thought we were avoiding a mature rating by censoring that!"
            p "Please. It's just kissing."
            fs "Y... Yes, but... In a forest..."
            menu fsquickend:
                "Just do it already":
                    stop music fadeout 1.0
                    scene end27
                    with fade
                    "And then you approached her and went all chibi-kiss-kiss-in-a-forest. Both of you liked that and even the birds decided to leave you two alone."
                    p "Well... That escalated quickly."
                    "You asked for it."
                    "--Fluttershy ending 3--"
                    
                    jump credits
                    
                "Be gentle with her and get the book":
                    jump smallboink
            label smallboink:
            "Okay Fluttershy, don't worry, I'm going to get a book like that and then we'll see what happen."
            fs "Th... Thank you."
            stop music fadeout 1.0
            scene black
            with fade
            "And you left her to head back to the crossroad. Where could you get a book about adult things? Where do you find books? That really is a difficult task."
            
        $ flut2 = False
        $ flut3 = True
        jump outdoors
            
    if(flut3==True):
        play music "Music/fluttercottage.mp3"
        "You are back to the cottage and remember that Fluttershy is still in the Everfree Forest, waiting for you to come back with a special book."
        
        if(p_book!="xxx"):
            "You don't have such a thing and prefer to go back to the crossroad instead of seeing a disappointed pegasus."
            jump outdoors
            
        "You have a ponygraphic book in your inventory and thus decide to try showing it to the pegasus."
        
        scene bg forest
        with fade
        
        show fluttershy shutter
        with dissolve
        
        fs "Oh.... My... You.. You are back? Already?"
        p "And I'm not empty hoofed!"
        show fluttershy what
        with dissolve
        fs "Do you.... Have a splinter in your hoof? "
        p "Well, I guess that translating empty handed doesn't make sense."
        fs "You are right.... I don't want to be mean or anything, but.... You are not making any sense right now."
        p "Anyway, I've got this!"
        "You show her the book."
        show fluttershy shutter
        with dissolve
        label fluterx:
        
        fs "This is the... Ooooooh.... And there with.... Ooooooooh......"
        p "Don't forget that one in the forest..."
        "She try to say something, but is only able to move her lips silently."
        p "Would you like... To... You know, try it?"
        "She is barely able to nod in approval."
        p "Well, I'm going to leave you alone, as the mare in the book... See you very soon!"
        "Fluttershy turn back and try to feed the birds again, there are no birds anymore, but she shakes way too much to do the work properly anyway."
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "You went back to the crossroad, thinking that this night was the night, but you could do something else before having your way with Fluttershy."
        
        $ flut3 = False
        $ flut4 = True
        jump outdoors
        
    if(flut4 == True):
        "You reached the end of the demo!"
        p "Wait, that's all?"
        "Hey! There's around 20 endings in the demo! If you wanted to see the good ones, filled with narration and stuff you should have waited for the full game. Anyway..."
        
        if(playername=="Applejack"):
            scene end28  
            with fade          
        if(playername=="Fluttershy"):
            scene end29
            with fade
        if(playername=="Pinkie Pie"):
            scene end30
            with fade
        if(playername=="Rainbow Dash"):
            scene end31
            with fade
        if(playername=="Rarity"):
            scene end32
            with fade
        if(playername=="Twilight Sparkle"):
            scene end33
            with fade        
        
        "--Demo ending 2--"
        jump credits
    
        
    "The cottage seems to be void of ponies and despicable-smart-white-bunnies."
    p "The door is locked. I better go elsewhere."
    stop music fadeout 1.0
    scene black
    with fade
    "And so you go back. That sure was a long and useless walk."
    jump outdoors

return