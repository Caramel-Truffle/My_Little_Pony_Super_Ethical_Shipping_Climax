label dashcloud:
    stop music fadeout 1.0
    scene bg rainbow bedroom
    with fade
    
    if(dash1==False):
        if((playername=="Rainbow Dash")or(playername=="Fluttershy")):
            "As a pegasus, you are easily able to fly to Rainbow's cloud."
            p "Wings are useful, [playername] was a good choice."
        else:
            "As a unicorn, you are able to cast spells to go up to Rainbow's cloud and not fall through it."
            p "Magic is useful, [playername] was a good choice."
            
        "Anyway, Rainbow Dash is there, searching something under her bed, she apparently hasn't seen you yet."
        "What are you going to do?"
        
        menu datdashplot:
            "Stare at her plot":
                "You look at her plot for a while, licking your lips while admiring her beautiful scenario. Ah, all the words and choices and-" 
                "She grunts, as she apparently didn't find what she was looking for."
                rd "What the hay? If I did not leave it there, where could it be?"
            "Offer your help":
                p "Hey Rainbow, need any help?"
                rd "Sure, do you- Wait. What?"
        "She stands up, turn around and sees you."
        play music "Music/dashie.mp3"
        show rainbow hey
        with dissolve
        
        rd "Hey, I didn't hear you coming!"
        
        if(playername=="Rainbow Dash"):
            show rainbow proud with dissolve
            rd "But it's always a pleasure to welcome true fans to my lair!"
            p "True fans? ...Lair?"
            rd "Yeah, look at you! You are like my clone! You even got my cutie mark right! And my rainbow-cloud. I'm not the heroin this city needs,
                but the one this city deserves!"
            p "You watched batmare too much."
            show rainbow happy with dissolve
            rd "But she's so awesome! ...Hey, I did not catch your name."
            p "Can you make one of my dream come true and call me Rainbow Dash?"
            rd "You really are a true fan! I like that! Okay, but only for today. Tomorrow I'll call you by your real name, deal?"
            p "Deal."
        else:
            show rainbow happy with dissolve
            
        rd "Are you just passing by [playername3], or do you need something?"
        p "I was wondering if you could help me with something."
        
        if(playername == "Twilight Sparkle"):
            rd "Do you need help in the library? I heard it's this time of the year where you sort all the books again."
        if(playername == "Rarity"):
            rd "Please tell me you are not looking for a model to design a dress!"
        if(playername == "Fluttershy"):
            rd "Do you need some help at night? It would be a pleasure."
        if(playername == "Rainbow Dash"):
            rd "And what can the awesome Rainbow Dash do for you?"
        
        p "In fact, I was thinking of asking help..."
        
        menu askdashiehelp:
            "To be cooler":
                p "...to be cooler."
                rd "Cooler?"
                show rainbow unsure
                with dissolve
                p "I need to be about 20\% cooler."
                rd "That sentence has been overused, you know?"
                p "Sorry. Anyway, do you think you could help?"
                
                if(playername == "Fluttershy"):
                    show rainbow interested
                    with dissolve
                    rd "We could make out. I already told you that I was open with that."
                    p "That isn't what I asked!"
                    rd "Does that mean that you are declining my offer again?"
                    
                    menu easyflutterdash:
                        "Decline the offer":
                            p "Yes. What could you do to make me cooler instead?"
                        "Accept the offer":
                            p "Well... Erm... No."
                            show rainbow fly superhappy
                            with dissolve
                            rd "Really? That's gonna be awesome! Thanks Fluttershy!"
                            p "Just... Be gentle, please."
                            stop music fadeout 1.0
                            scene end53
                            $persistent.unlock_53
                            with fade
                            "And then both of you did naughty things, the bed being too close to ignore it."
                            p "Your lack of pictures on that matter disappoint me."
                            "Tell that to the ghost visual artist, because the best I can do is this."
                            p "If you could do anything, what would you choose?"
                            "Chibi ponies kissing each other in a kawaii way. This isn't a 18+ game after all."
                            p "One day..."
                            "The chibis. Not the change of rating. When I said they did naughty things, I was talking about eating.... IN THE BED! Think about it! All the crumbs everywere! Naughty! Filthy!"
                            play sound "SFX/fail.mp3"
                            "--Rainbow ending 1--"
                            jump credits
                show rainbow flattered
                with dissolve
                rd "Well, there's one easy way to handle that. I can't guarantee its results though."
                p "And what would it be?"
                show rainbow hey with dissolve
                rd "Let me put you in context, first. Imagine you wanted to seem nicer. You know the principle of the lovely item, right? Something cute that makes you look like a nice pony?"
                p "Like a plushie or a young kid?"
                rd "Yeah. There's the same thing to look cooler instead of nicer, a \"cool item\" if you want."
                p "And you have a cool item I could borrow?"
                rd "Of course. Wait there."
                stop music fadeout 1.0
                scene black
                with fade
                "She went somewhere else in her cloud, looking for something, before coming back with a pair of sunglasses."
                scene bg rainbow bedroom
                with fade
                play music "Music/dashie.mp3"
                show rainbow hey
                with dissolve
                rd "There, the coolest glasses in all of Equestria!"
                show rainbow happy with dissolve
                p "Thank you Dashie! You are a life saver!"
                play sound "SFX/gotObject.mp3"
                "You receive a cool pair of sunglasses!"
                rd "Well... I hope you'll tell me what this is all about tomorrow."
                p "Tomorrow?"
                rd "Yeah, it was fun and all, but I promised Derpy I would go train myself with her today, so I'm going to be busy for the rest of the day."
                p "You are really awesome."
                show rainbow hey with dissolve
                rd "Yeah, yeah... But, please, don't go near us with these, I'll explain to you tomorrow."
                p "No problem, see you tomorrow!"
                rd "See ya!"
                stop music fadeout 1.0
                scene black
                with fade
                "And she invited you to leave before doing so herself, then you went back to the Ponyville crossroad, with her pair of cool sunglasses in...
                 Wait... How do you even carry the items that ponies give you?"
                p "You don't want to know."
                "I heard nothing."
                $ nb_lock = nb_lock + 1
                $ p_rd = "sunglasses"
            "To gain some strength":  
                p "...to gain some strength."
                show rainbow unsure with dissolve
                rd "Strength? Really?"
                p "Yes, I may not be an earth pony, but healthy exercises can't be ignored."
                show rainbow happy with dissolve
                rd "Yeah, no, that was the timing that surprised me, I was searching a dumbbell to go train myself with Derpy, because she asked me to too!"
                p "Really? Can I join you?"
                show rainbow hey with dissolve
                rd "I don't think she would mind, so, yeah, sure! But first, we need to find that dumbbell."
                p "Isn't it the one just right there, on the table right in front of you?"
                show rainbow fly embarassed
                with dissolve
                rd ".....\n
                    .....\n
                    Nooooo. Not at all, you can take this one. This... Isn't the one at all, I'm not stupid."
                play sound "SFX/gotObject.mp3"
                "While blushing a bit, Rainbow Dash gives you a dumbbell!"
                $ p_rd = "dumbbell"
                rd "I will... Erm. Continue to search. Go back here as soon as you are ready to go."
                p "Ooookay... See you later, then."
                rd "Yeah, real soon!"
                stop music fadeout 1.0
                scene black
                with fade
                "And so you were back on your way to the crossroad, with a bit of extra weight."
                $ dash2=True
                
        $ dash1=True
        jump outdoors
        
    if(dash2 == True):
        play music "Music/dashie.mp3"
        show derpy superhappy
        with dissolve
        "You are back to Rainbow's cloud, but instead of her, you stumble upon Derpy Hooves, a gray mare with yellow... Eyes."
        
        if(playername == "Rainbow Dash"):
            d "Rainbow Dash! You are back!"
            
            menu derpyabuse:
                "Tell her the truth":
                    p "I'm not Rainbow Dash, I'm just... A fan. Yeah, a hardcore fan, cosplaying as her and all."
                    d "Cool! I like her too! And muffins! I'm Derpy Hooves, what's your name?"
                    p "Well, why don't you call me Rainbow Dash as long as I'm cosplaying?"
                    d "I muffin this idea!"
                    p "Muffin?"
                    d "I love muffins!"
                    
                    menu truederpyabuse:
                        "\"I have a very special muffin for you...\"":
                            p "I have something even more delicious for you..."
                            d "Really? Even more than muffins? That's not possible!"
                            p "Oh yes it is, close your eyes..."
                            
                            stop music fadeout 1.0
                            scene black
                            with fade
                            
                            "You kissed her."
                            
                            scene bg rainbow bedroom
                            with fade
                            play music "Music/dashie.mp3"
                            show derpy fly hug
                            with dissolve
                            
                            d "Kisses and hugs time!"
                            
                            stop music fadeout 1.0
                            scene end19
                            $persistent.unlock_19
                            with fade
                            
                            "And it was kisses and hugs time for the remaining of the day, Dashie joigning you once she came back, thinking it was a suitable replacement for the training session she was initially planning."
                            p "Three mares \"kissing and hugging\"? That's all I get? On a still image like this one?"
                            "There are other games if you want graphic action."
                            play sound "SFX/fail.mp3"
                            "--Derpy ending--"
                            jump credits
                        
                        "\"I love them too!\"":
                            p "I love them too! But, have you seen the real Rainbow Dash?"
                
                "Take advantage of the situation":
                    p "Yeah, get on my bed and close your eyes, I'm gonna do something awesome!"
                    d "Rainbow Dash? Are you alright?"
                    show rainbow dubious
                    with fade
                    rd "What are you doing?"
                    p "Where did you come from?!"
                    rd "Doesn't matter. You come to my house. Pretend to be me. And try to abuse my friends? GET OUT!"
                    p "But-"
                    stop music
                    play sound "SFX/vinylscratch.mp3"
                    scene end54
                    $persistent.unlock_54
                    with fade
                    "And she kicked you so hard... You just lost the game."
                    p "This isn't funny anymore either."
                    "You lost anyway."
                    play sound "SFX/fail.mp3"
                    "--Rainbow Dash ending 2--"
                    jump credits
        else:
            d "Hey [playername2]! Rainbow Dash and me were going to go train for a bit, do you want to join us?"
            p "Actually, that's what I'm here for, Derpy. But, where's Rainbow?"
        d "I just don't know where she went."
        p "I expected you to say something similar. Anyway, she will surely be back soon."
        d "That's true [playername2]! And-"
        show derpy sad
        with dissolve
        d "I... Lost my Muffin..."
        p "What? Where?"
        d "I don't know, I simply wanted to eat one, but remembered it was my last one, but decided to eat it anyway, but... I can't find it anymore!"
        p "Well, we will buy you some, the Sugarcube Corner isn't far."
        d "That was their last one for today, they have a production problem and won't be able to make some before tomorrow..."
        p "You really want that muffin, don't you?"
        d "Yes..."
        
        if(p_pp == "muffin"):
            p "Then take this one, Pinkie gave it to me earlier."
            show derpy happy
            with dissolve
            jump yummymuffin
        
        p "Wait there, I'll get you one. I don't know how, but I'll get you one."
        show derpy bittersweet
        with dissolve
        d "Thank you [playername2], I will wait for your return."
        p "I will come back as soon as possible!"
        
        stop music fadeout 1.0
        scene black
        with fade
        
        "Without a clue, you went back to the crossroad."
        $ dash2 = False
        $ dash3 = True
        jump outdoors
        
    if(dash3 == True):
        play music "Music/dashie.mp3"
        "You go back to Rainbow's cloud, where Derpy Hooves is waiting for a muffin."
        show derpy bittersweet
        with dissolve
        d "Hey [playername2], you are back! Did you find any muffin?"
        if(p_pp != "muffin"):
            p "Hey Derpy! Sadly no, I haven't found a muffin yet."
            d "Yet? Are you going to try again?"
            p "Of course I will! And I will be back as soon as I can!"
            d "Take care..."
            stop music fadeout 1.0
            scene black
            with fade
            "And you went back to the crossroad. Where could you find a muffin?"
            jump outdoors
        else:
            p "Hey Derpy! Of course I do, take this one!"
            show derpy happy
            with dissolve
            label yummymuffin:
                "You give your muffin to Derpy."
                d "Thank you so much [playername2]!"
                show derpy superhappy with dissolve:
                    linear 1.0 xalign 0.2
                show rainbow happy with dissolve:
                    xzoom -1
                    xalign 0.9 yalign 1.0
                with dissolve
                
                rd "Sorry girls, I took my time! ...[playername3], what did you do to Derpy? She's so happy!"
                show derpy fly hug
                with dissolve
                d "She gave me a muffin! Muffin!"
                show derpy superhappy
                with dissolve
                p "She really does love them."
                rd "Well, anyway, let's go, what do you think?"
                
                d "Allons-y!"
                rd "You've been around that stallion too much, Derpy."
                d "But he's so nice to me, like you two!"
                "And all three of you continued to chit-chat while going out."
                stop music fadeout 1.0
                scene black
                with  fade
                "And you three went outside ponyville to go train for a bit, lifting weights, running, flying, etc. After that, you waved goodbye to the
                 two others -who were going back to their home- and returned to the crossroad."
                $ dash2 = False
                $ dash3 = False
                $ dash4 = True
                jump outdoors
                
    if(dash4 == True):
        play music "Music/dashie.mp3"
        show rainbow flattered with dissolve
        
        "You come back to the Rainbow lair. The young athlete is here, drinking some water while sweat is beading off her fur." 
        
        show rainbow happy with dissolve

        rd "Hi there! I was about to hit the shower, wanna join me?"

        p "Sure thing!"
        
        scene black with fade
        stop music fadeout 1.0
        play music "Music/showerlong.ogg"

        "And you two entered the shower, big enough for two adult ponies to get into and fully wash themselves without touching one another, because it's good to save water, but it's better to do it while respecting personal spaces."

        p "I was wondering about something. Why does no one here has genitals?"

        rd "No genius aliens? That sounds kind of racist."
        p "No, I mean, everypony resembles a barbie doll down there."

        rd "Barbier dolls? You're making less and less sense by the minute."

        p "Rainbow Dash. How are fillies and colt made?"

        rd "You really don't know? We write a letter to the guys in charge of the script and ask them to add us a kid. Simple as that. Wanna know where to send your letter? I got the address noted down, in case I change my mind about children at some point."

        p "Oof."

        "Nice try updating your lingo. You two ended up having some nice clean fun during the afternoon, since you discovered the big secret explaining why this game is necessarily PG."

        "Or whatever your classification system is. Seems like merely mentioning sexual intercourse is worthy of a Mature rating in some countries, while for others it's barely a 7+ thing. "

        "Good job, Australia."

        p "Please just roll the credits."
        
        stop music fadeout 1.0

        
        if(playername=="Fluttershy"):
            scene end55
            $persistent.unlock_55
            with fade
        if(playername=="Rainbow Dash"):
            scene end56
            $persistent.unlock_56
            with fade
        if(playername=="Rarity"):
            scene end57
            $persistent.unlock_57
            with fade
        if(playername=="Twilight Sparkle"):
            scene end15
            $persistent.unlock_15
            with fade
        play sound "SFX/trueEnding.mp3"
        "--Rainbow Dash true ending--"
        jump credits
                
    "Rainbow Dash isn't there. It would be creepy to wait for her in her bed."
    p "Rainbow Dash is not here and I have nothing to do there. Let's go somewhere else."
    stop music fadeout 1.0
    scene black
    with fade
    "And so you went back to ponyville and its crossroad."
    jump outdoors

return