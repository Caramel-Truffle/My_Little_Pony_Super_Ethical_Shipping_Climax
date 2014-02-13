label library:
    stop music fadeout 1.0

    scene bg library
    with fade

    if(libr1==False):
        play music "Music/library.mp3"
        $ nb_scenes = nb_scenes + 1
        "You go to the library and while you come through its door, you see the purple mare living there: Twilight Sparkle. 
         She doesn't seems to notice you, even after closing the door."
        
        menu uselessoption1:
            "Wait":
                
                if(p_aj == "sugarcube" or appl4 == True or appl3 == True):
                    $easter_egg = easter_egg + 1
                "You wait some minutes, but nothing happens. Why don't you say something?"
                jump uselessoption1
            "\"Hello Twilight!\"":
                p "Hello Twilight!"
                "Hearing your voice, the mare stops what she was doing to face you instead."
            "Turn into Big Macintosh" if(easter_egg == 3):
                jump eegg
        
        if(playername=="Twilight Sparkle"):
            show twilight what
            with dissolve
            ts "You! You are me! But I'm me too! Are you a future Twilight wanting to warn me about a future Twilight of mine 
                that is also a past Twilight of yours? If that so you are not in the right past!"
            p "What are you even..."
            ts "This is bad! This is really really bad!"
            
            menu twi_see_double:
                "\"Sorry, but you are not the real Twilight.\"":
                    p "Sorry, but you are not the real Twilight. You are a copy with the exact same memories. It's dangerous to 
                       have more than an alive copy at a time or having the original and a copy alive at the same time. I must 
                       kill you, it's the procedure."
                    stop music fadeout 1.0
                    show twilight battle
                    with dissolve
                    ts "I thought you would improve your lying skills, Chrysalis. It's time for you to be really banned this time!"
                    p "Wait, what are you even talking abou-"
                    scene black
                    with fade
                    "And she kicked your buttock. What did you expect?"
                    p "...\n
                       Am I free to go now?"
                    "...\n
                     Yes, you are."
                    p "Good."
                    "--Twilight ending 1--"
                    jump credits
                       
                "\"I'm trapped into a fake body, don't mind it.\"":
                    p "Don't worry, I'm not you, I'm just a random person trapped in a fake body similar to yours, please don't mind it."
                    ts "Are you crazy?"
                    p "If I am, you are too. Don't forget that you would be talking to yourself then."
                    jump twi_see_double_end
                
                "\"This is just a dream, shhhh...\"":
                    p "This is just a dream, shhhhh..."
                    ts "Don't shhhh me, me!"
                    p "I'm neither attacking you nor zapping back to the future, don't worry. It's safe, don't mind it."
                    jump twi_see_double_end
                    
                "\"Can't we just make out? Selfcest is hawt.\"":
                    p "Haven't you ever dreamed of making out with yourself?"
                    ts "Are you crazy?!"
                    p "I'm serious. You won't have the occasion again."
                    show twilight ohyou
                    with dissolve
                    ts "Well, I've never read anything about that..."
                    p "I will teach you then."
                    show twilight tapdancing
                    with dissolve
                    ts "Yes! I will write a letter to the princess right after that!"
                    p "You are quite the enthusiastic pony, aren't you?"
                    show twilight seductive
                    with dissolve
                    ts "When I have a good teacher? Always. Now give me a lesson..."
                    stop music fadeout 1.0
                    scene black
                    with fade
                    "And then you kissed and stuff."
                    p "Wait, you are not going to show that?"
                    "Nope. This is not a 18+ game."
                    p "Come on! What about a kiss?"
                    "A chibi kiss when a visual artist will be interested."
                    p "Well... That will be better than nothing."
                    "Considering the little effort to obtain this ending, it's well paid."
                    p "There's more in the others?"
                    "Search and see!"
                    p "Wait-"
                    "--Twilight ending 2--"
                    jump credits
            label twi_see_double_end:
            
            show twilight sitting confused
            with dissolve
            ts "Okay, whatever you are, or whatever the situation is, if I treat you like anypony else, everything will be fine, right?"
            p "Right. Just call me Twilight Sparkle, like everypony else and don't think about it."
            ts "That's just twisted... But let's try."
        show twilight happy
        with dissolve
        
        ts "Oh, [playername2]! What can I do for you?"
        p "I'm looking for a book."
        
        if(playername=="Rainbow Dash"):
            ts "The last Daring Do book?"
        if(playername=="Pinkie Pie"):
            ts "A cookbook?"
        if(playername=="Rarity"):
            ts "A book about fashion in Canterlot?"
        if(playername=="Fluttershy"):    
            ts "A book about chiropractic for bears?"
        if(playername=="Applejack"):
            ts "A book about appletrees from other countries?"
        if(playername=="Twilight Sparkle"):
            ts "A book about freaking someone by looking like its clone?"
            
        p "No."
        
        menu bookchoice:
            "\"A book about astronomy.\"":
                p "A book about astronomy. I would like to learn more about it."
                ts "Great! Don't judge it by the cover, but \"The astronomy for silly fillies\" would be a perfect start!"
                p "I trust you completely Twilight."
                show twilight showing
                with dissolve
                ts "Good, it's the book right there, let me give it to you."
                "Twilight take the book with her magic and give it to you. You now have \"The astronomy for silly fillies\"!"
                show twilight happy
                with dissolve
                ts "There! You can return it at any time."
                p "Thank you Twilight, be assured I will."
                ts "Now if you don't mind, I have some stuff to do. You probably won't like to read there during this time."
                p "I understand, see you later!"
                ts "See you later [playername2]!"
                $ libr2 = True
                $ p_book = "astronomy"
                stop music fadeout 1.0
                scene black
                with fade
                "You skim through the book a bit while going back to the crossroad and a sentence attracts your attention: 
                 \"Don't miss the supermoon this night!\""
                p "What is a supermoon? And how can a book know what will happen during the night?"
                "Magic."
                p "...Okay."
                jump bookchoice_end
                
            "\"A *whisper*\"":
                $ renpy.music.set_volume(0.5, .5, channel="music")
                p "A... A *whisper*"
                $ renpy.music.set_volume(1, .5, channel="music")
                if(playername=="Fluttershy"):
                    ts "Come on, it's me Fluttershy. I'm your friend!"
                else:
                    ts "Come on [playername3], you are not Fluttershy!"
                stop music fadeout 1.0    
                p "A BOOK ABOUT PONIES HAVING SEX!"
                
                show twilight sitting confused
                with dissolve
                
                ts "Well... That was unexpected of you."
                play music "Music/library.mp3"
                p "Please don't judge me."
                ts "I won't! But... Are you talking about...?"
                p "Yes, an adult book, not a child book explaining how to make foals. I already know that."
                ts "Well... I should have one somewhere. Let me have a look!"
                stop music fadeout 1.0
                scene black
                with fade
                "She looked everywhere and came back with a black-covered book."
                scene bg library
                with fade
                play music "Music/library.mp3"
                show twilight chuckle
                with dissolve
                
                ts "It's one of my personal books. I won't ask why you need it, just return it when you are done."
                "You know have a ponygraphic book! Don't make it sticky, Twilight wouldn't appreciate that."
                p "Well... Thank you?"
                ts "No worries. Now if you don't mind, I have other things to do. You can come back tomorrow!"
                p "I will! Bye Twilight!"
                ts "Bye [playername2]!"
                
                $ p_book = "xxx"
                $ nb_lock = nb_lock + 1
                stop music fadeout 1.0
                scene black
                with fade
                "You skimed through the book a bit while going out, but due to its the nature, no description of it will be made."
                p "Not even when the-"
                "Especially not that."
                p "...Okay."
                "You go back to the crossroad."
                
        label bookchoice_end:
        $ libr1 = True
        jump outdoors
        
    if(libr2==True):
        play music "Music/library.mp3"
        $ nb_scenes = nb_scenes + 1
        "You return to the library. Twilight is nowhere to be found, but Spike is here and saw you coming."
        if(playername=="Twilight Sparkle"):
            show spike anxious
            with dissolve
            sp "Oh! H... Hello Twilight! You... You are already back?"
            p "No, I'm currently in the kitchen of the Sugarcube Corner, making a delicious strawberry pie."
            show spike happy
            with dissolve
            sp "Wow, I sure would like to take a bite!"
            p "...That was ironical. And I'm not the real Twilight."
            sp "Oh! Yes, she told me, you are... Uh... I forgot."
            p "Just call me Twilight and consider I'm one of her friends, okay?"
            sp "Okay."
        else:
            show spike happy
            with dissolve
        sp "Hey [playername2]! Twilight is out for the moment. What can I do for you?"
        
        menu spikechoice:
            "\"Can I be alone with Twilight tonight?\"":
                p "There will be a supermoon tonight. I wondered if you could let Twilight be alone with me, so we could watch 
                   it together. Alone. Watching the moon and stars. Just us. Understand?"
                sp "Wait, do you really mean that..."
                p "Yes, do I need to be even more direct or is the innuendo enough?"
                
                if(playername=="Rarity"):
                    show spike depressed
                    with dissolve
                else:
                    show spike cool
                    with dissolve
                sp "I just never thought of you two like that."
                p "Don't mention it. So, can I count on you?"
                sp "I could do it, but I want a ruby in return."
                p "I can get you one with no problem."
                sp "Sure, but if I don't have something to eat when Twilight come back, I can't promise that my mouth will be able to stay shut."
                if(p_rar=="ruby"):
                    "As you already have a ruby, you give it to him."
                    p "No problem, take this one."
                    sp "Thanks! And... Well... See you tomorrow and have a sweet night!"
                    p "Count on me for that. Bye Spike!"
                    "And you leave the dragon alone, going back to the crossroad."
                    $ p_rar = "none"
                    $ libr2 = False
                    $ libr4 = True
                    jump outdoors
                p "No problem, stay there, I will get you that."
                sp "I'll wait for you [playername2], see you later!"
                p "See you later!"
                stop music fadeout 1.0
                scene black
                with fade
                "And you quicky went out, wondering where you could find a ruby."
                $ libr2 = False
                $ libr3 = True
                jump outdoors
                
            "\"Can I have a kiss?\"":
                p "Can I have a kiss?"
                if(playername!="Rarity"):
                    show spike anxious
                    with dissolve
                    sp "[playername2]? What's wrong with you?"
                    p "Nothing."
                    sp "I won't kiss you like that, I... I... Forget it. Don't you have anything else you want?"
                    jump spikechoice
                else:
                    show spike cool
                    with dissolve
                    sp "Are you serious?"
                    p "Of course I am darling. Come here..."
                    stop music fadeout 1.0
                    scene black
                    with fade
                    
                    "And both of you kissed during hours."
                    p "No picture?"
                    "No pictures until I have an artist willing to draw these scenes. You can search for the other endings though."
                    p "Do they have pictures?"
                    "No."
                    p "Explicit details in their telling?"
                    "No."
                    p "..."
                    "What did you expect?"
                    p "I-"
                    "Time's up!"
                    "--Spike ending--"
                    jump credits
    if(libr3==True):
        play music "Music/library.mp3"
        show spike happy
        with dissolve
        "You go back to the library, Twilight isn't there yet."
        sp "So [playername2], you are back! Do you have a ruby?"
        
        if(p_rar=="ruby"):
            p "Yes. Take this one."
            "You give him the ruby."
            sp "Thanks! And... Well... See you tomorrow and have a sweet night!"
            p "Count on me for that. Bye Spike!"
            "And you leave the dragon alone, going back to the crossroad."
            $ p_rar = "none"
            $ libr3 = False
            $ libr4 = True
            jump outdoors
        else:
            p "Nope, but I'm working on it."
            sp "You better work faster, clock is ticking after all."
            p "I'm already on my way!"
            stop music fadeout 1.0
            scene black
            with fade
            "And you quickly go out again. It seems that going back here without a ruby is useless."
            jump outdoors
            
    if(libr4 == True):
        "You reached the end of the demo!"
        p "Wait, that's all?"
        "Hey! There's around 20 endings in the demo! If you wanted to see the good ones, filled with narration and stuff you should have waited for the full game. Anyway..."
        "--Demo ending 1--"
        jump credits

    "You go to the library, the place is empty and quiet."
    p "There is nothing but books here. I surely have something else than reading to do."
    stop music fadeout 1.0
    scene black
    with fade
    "You go back to the crossroad."
    jump outdoors

return