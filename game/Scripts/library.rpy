label library:
    stop music fadeout 1.0

    scene bg library
    with fade

    if(libr1==False):
        play music "Music/library.mp3"
        $ nb_scenes = nb_scenes + 1
        "You go to the library and while going through its door, you see the purple mare living there: Twilight Sparkle. 
         She doesn't seem to notice you, even after you closed the door."
        
        menu uselessoption1:
            "Wait":
                if(appl4 == True):
                    $easter_egg = easter_egg + 1
                "You wait some minutes, but nothing happens. Why don't you say something?"
                jump uselessoption1
            "\"Hello Twilight!\"":
                p "Hello Twilight!"
                "Hearing your voice, the mare stops what she was doing to face you instead."
            "Turn into Big Macintosh" if(easter_egg == 3):
                jump eegg
        
        if(playername=="Twilight Sparkle"):
            stop music
            play sound "SFX/vinylscratch.mp3"
            show twilight what
            with dissolve
            ts "You! You are me! But I'm me too! Are you a future Twilight wanting to warn me about a future Twilight of mine 
                that is also a past Twilight of yours? If that so you are not in the correct past!"
            p "What are you even..."
            ts "This is bad! This is really really bad!"
            
            menu twi_see_double:
                "\"Sorry, but you are not the real Twilight.\"":
                    p "Sorry, but you are not the real Twilight. You are a copy with the exact same memories. It's dangerous to have more than one copy alive at a time or having the original and a copy alive at the same time."
                    "I must get rid of you, it's the procedure."
                    show twilight battle
                    with dissolve
                    ts "I thought you would improve your lying skills, Chrysalis. It's time for you to really be banned this time!"
                    p "Wait, what are you even talking abou-"
                    scene end77
                    with fade
                    "And she kicked your buttock. What did you expect?"
                    p "...\n
                       Am I free to go now?"
                    "...Yes, you are."
                    p "Good."
                    play sound "SFX/fail.mp3"
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
                    ts "Well, I might have read something about that..."
                    p "I will help you put that into practice, then."
                    show twilight tapdancing
                    with dissolve
                    ts "Yes! I will write a letter to the princess right after that!"
                    p "You are quite the enthusiastic pony, aren't you?"
                    show twilight seductive
                    with dissolve
                    ts "When I have a good teacher? Always. Now give me a lesson..."
                    stop music fadeout 1.0
                    scene end78
                    with fade
                    "And then you kissed and stuff."
                    p "Wait, you are not going to show that?"
                    "Nope. This is not a 18+ game."
                    p "Come on! What about a kiss?"
                    "There's a heart near the mouth, it counts."
                    p "Well... That's better than nothing, I guess."
                    "Considering the little effort to obtain this ending, it's well paid."
                    p "There's more in the others?"
                    "Search and see!"
                    p "Wait-"
                    play sound "SFX/fail.mp3"
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
            ts "The latest Daring Do book?"
        if(playername=="Pinkie Pie"):
            ts "A cookbook?"
        if(playername=="Rarity"):
            ts "A book about fashion in Canterlot?"
        if(playername=="Fluttershy"):    
            ts "A book about chiropractic for bears?"
        if(playername=="Applejack"):
            ts "A book about apple trees from other countries?"
        if(playername=="Twilight Sparkle"):
            ts "A book about freaking someone by looking like their clone?"
            
        p "No."
        
        menu bookchoice:
            "\"A book about astronomy.\"":
                p "A book about astronomy. I would like to learn more about it."
                ts "Great! Don't judge it by the cover, but \"The astronomy for silly fillies\" would be a perfect start!"
                p "I trust you completely Twilight."
                show twilight showing
                with dissolve
                ts "Good, it's the book right there, let me give it to you."
                play sound "SFX/magic.mp3"
                show twilight showing glowing with dissolve
                show twilight showing with dissolve
                show twilight happy with dissolve
                play sound "SFX/gotObject.mp3"
                "Twilight takes the book with her magic and gives it to you. You now have \"The astronomy for silly fillies\"!"
                show twilight happy
                with dissolve
                ts "There! You can return it at any time."
                p "Thank you Twilight, I will. Rest assured."
                ts "Now if you don't mind, I have some stuff to do. You probably won't like to read there during this time."
                p "I understand, see you later!"
                ts "See you later [playername2]!"
                $ libr2 = True
                $ p_ts = "astronomy"
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
                    ts "Come on, it's me, Fluttershy. I'm your friend!"
                else:
                    ts "Come on [playername3], you are not Fluttershy!"
                stop music fadeout 1.0    
                p "A BOOK ABOUT PONIES HAVING SEX!"
                
                show twilight sitting confused
                with dissolve
                
                ts "Well... That was unexpected of you."
                "Goodbye PG rating in Iran."
                "... Not that anyone from there would end up playing this."
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
                play sound "SFX/gotObject.mp3"
                "You know have a ponygraphic book! Don't make it sticky, Twilight wouldn't appreciate that."
                p "Well... Thank you?"
                ts "No worries. Now if you don't mind, I have other things to do. You can come back tomorrow!"
                p "I will! Bye Twilight!"
                ts "Bye [playername2]!"
                
                $ p_ts = "xxx"
                $ nb_lock = nb_lock + 1
                stop music fadeout 1.0
                scene black
                with fade
                "You skimed through the book a bit while going out, but due to its nature, no description of it will be made."
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
        "You return to the library. Twilight is nowhere to be found, but Spike is there and saw you coming."
        if(playername=="Twilight Sparkle"):
            show spike anxious
            with dissolve
            sp "Oh! H... Hello Twilight! You... You are already back?"
            p "No, I'm currently in the kitchen of the Sugarcube Corner, making a delicious strawberry pie."
            show spike happy
            with dissolve
            sp "Wow, I sure would like to have a slice!"
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
                p "Don't mention it. ...Wait, are you giving me the finger?"
                sp "It's a thumbs up! I'm doing my best, I promise!"
                p "Please don't do that again. So, can I count on you?"
                sp "I could do it, but I want a ruby in return."
                p "I can get you one with no problem."
                sp "Sure, but if I don't have something to eat when Twilight come back, I can't promise that my mouth will be able to stay shut."
                if(p_rr=="ruby"):
                    "As you already have a ruby, you give it to him."
                    p "No problem, take this one."
                    sp "Thanks! And... Well... See you tomorrow and have a sweet night!"
                    p "Count on me for that. Bye Spike!"
                    "And you leave the dragon alone, going back to the crossroad."
                    $ libr2 = False
                    $ libr4 = True
                    jump outdoors
                p "No problem, stay there, I will get you that."
                sp "I'll wait for you [playername2], see you later!"
                p "See you later!"
                stop music fadeout 1.0
                scene black
                with fade
                "And you quick went out, wondering where you could find a ruby."
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
                    sp "I won't kiss you, I... I... Forget it. Don't you have anything else you want?"
                    jump spikechoice
                else:
                    show spike cool
                    with dissolve
                    sp "Are you serious?"
                    p "Of course I am darling. Wait, are you giving me the finger?"
                    sp "That's a thumbs up, I'm doing my best!"
                    p "Anyways. Come here..."
                    stop music fadeout 1.0
                    scene end76
                    with fade
                    
                    "And both of you kissed during hours."
                    p "No picture?"
                    "This is the best you'll get. You can search for the other endings though."
                    p "Do they have pictures?"
                    "No."
                    p "Explicit details in their telling?"
                    "No."
                    p "..."
                    "What did you expect?"
                    p "I-"
                    "Time's up!"
                    play sound "SFX/fail.mp3"
                    "--Spike ending--"
                    jump credits
    if(libr3==True):
        play music "Music/library.mp3"
        show spike happy
        with dissolve
        "You go back to the library, Twilight isn't there yet."
        sp "So [playername2], you are back! Do you have a ruby?"
        
        if(p_rr=="ruby"):
            p "Yes. Take this one."
            "You give him the ruby."
            sp "Thanks! And... Well... See you tomorrow and have a sweet night!"
            p "Count on me for that. Bye Spike!"
            "And you leave the dragon alone, going back to the crossroad."
            $ p_rr = "none"
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
            "And you quickly went out again. It seems that going back here without a ruby is useless."
            jump outdoors
            
    if(libr4 == True):
        
        play music "Music/library.mp3"
        "You're back to the library, fragrance of books fills the air, the quiet \"who?\" of a sleeping owl may come to your ear if you listen well enough and the absence of any other living creature here seems obvious."

        p"Well. I just have to go back later, right?"

        "No. Twilight is supposed to come here soon."

        p"..."

        "..."

        p"Can I sit down and read something? the silence is awkward enough."

        "Right. You sit down and open... Erm.... Ah! The astronomy for silly fillies, the book that Twilight gave you sooner. The cover is blue as the moon. Well, once in a blue moon."
        play sound "SFX/pageturn.mp3"
        "Because the  supermoon intrigued you, you decide to start with that part, instead of beginning with the first few chapters. Shame on you, the history of astronomers seemed fun."

        p"Oi! Let me decide what's fun for me!"

        "Anyway, a supermoon is the coincidence of a full moon or a new moon with the closest approach the Moon makes to the Earth on its elliptical orbit, resulting in the largest apparent size of the lunar disk as seen from Earth. "
        play sound "SFX/pageturn.mp3"
        "The technical name is the perigee-syzygy of the Earth-Moon-Sun system. The term \"supermoon\" is not astronomical, but originated in modern astrology."
        play sound "SFX/pageturn.mp3"
        "The association of the Moon with both oceanic and crustal tides has led to claims that the supermoon phenomenon may be associated with increased risk of events such as earthquakes and volcanic eruptions, but the evidence of such a link is widely held to be unconvincing."

        p"Thank you, Wikipedia."

        "Oi! You wanted to know what a supermoon is!"

        p"Well, I thought it was something mystical, related to Princess Luna and stuff."

        ts"And you're right, this book has been written before we defeated Nightmare Moon. Most ponies forgot about her and even the scientists thought that the earthquakes and volcanic eruptions were natural. In fact, it was Nightmare Moon trying to make the nature rebels against us."

        "Wait. Was that Twilight? When did she...?"
        
        show twilight ohyou

        if(playername=="Twilight Sparkle"):
            p "Wait. You advised me to start with an outdated book?"
        if(playername=="Rainbow Dash"):
            p "Wait. Does that mean that there is nothing radical like that during a supermoon anymore?"
        if(playername=="Rarity"):
            p "Oh dear. If she continued, it would have been THE. MOST. TERRIBLE. THING."
        if(playername=="Fluttershy"):
            p "Oh my... So... Are we safe now?"
        if(playername=="Pinkie Pie"):
            p "I didn't know that! What happens now during supermoons?"
        if(playername=="Applejack"):
            p "Howdy y'all mate! ... Blimey. I can't do the accent properly. Anyway, what does Princess Luna do now?"

        show twilight chuckle

        "She chuckles."
        
        show twilight happy

        ts"Well, because the events happened \"recently\", there is no book explaining that, but don't worry, Princess Luna intends to make each supermoon a moment of joy and peace now."

        if(playername=="Twilight Sparkle"):
            p "Like a redemption or something?"
        if(playername=="Rainbow Dash"):
            p "By making super tornadoes fighting evil?"
        if(playername=="Rarity"):
            p "By making peace reign through peaceful means?"
        if(playername=="Fluttershy"):
            p "By taking care of the wildlife she might have hurt during these years?"
        if(playername=="Pinkie Pie"):
            p "Like a peace party?"
        if(playername=="Applejack"):
            p "Don't be all mouth and trousers, what does she do?"

        ts"Well, speaking of a redemption would be a bit strong, but she tries to grant wishes, as long as it can bring happiness without any bad repercussion."

        if(playername=="Twilight Sparkle"):
            p "So, no \"I want to know everything\" wish."
        if(playername=="Rainbow Dash"):
            p "So, no \"I want to be able to break the record\" wish."
        if(playername=="Rarity"):
            p "So, no \"I want to have the best client possible\" wish."
        if(playername=="Fluttershy"):
            p "So, no \"I want everypony to be able to talk to animals\" wish."
        if(playername=="Pinkie Pie"):
            p "So, no \"I want to know everypony\" wish."
        if(playername=="Applejack"):
            p "So, no \"I want to win the lottery\" wish for the champagne socialists."

        show twilight chuckle

        ts"No. No such wish, but..."

        p"But?"
        
        show twilight seductive

        ts"Love wishes, when they are reciprocal, are usually granted."

        if(playername=="Twilight Sparkle"):
            p "Is your input supposed to be sufficient?"
        if(playername=="Rainbow Dash"):
            p "What was that for?"
        if(playername=="Rarity"):
            p "What are you implying?"
        if(playername=="Fluttershy"):
            p "Oh my. D-do you mean...?"
        if(playername=="Pinkie Pie"):
            p "I like where this is going."
        if(playername=="Applejack"):
            p "I would like to say that a nod is as good as a wink to a blind horse, but I can't."

        "Oh. Are you this transparent to her?"

        show twilight ohyou

        ts"Spike isn't there. I didn't know that Rarity loved him back, but if they are together this evening, it might be it."

        if(playername=="Twilight Sparkle"):
            p "Ah, of course. What would you mean otherwise? Ahah!"
        if(playername=="Rainbow Dash"):
            p "Oh. I thought you meant something else."
        if(playername=="Rarity"):
            p "You had me for one second. ....Wait, you know that I am not....?"
        if(playername=="Fluttershy"):
            p "Oh, Spike and Rarity, of course."
        if(playername=="Pinkie Pie"):
            p "Ooh, I hope they're having fun."
        if(playername=="Applejack"):
            p "Oh, yes, the nancy boy and the maiden. What else? Ha ha."

        show twilight chuckle

        ts"My Twilie sense tells me that you were thinking of something else."

        "You sigh."

        p"Let's put the mask aside for a moment. I was just thinking of us."
        
        show twilight seductive

        ts"Of us? What do you mean?"

        "Her last sentence ended with a nearly imperceptible self-lip-biting."

        p"I mean exactly what you are thinking of. You and me, howling at the moon in the middle of this summer afternoon."

        ts"..."

        p"Okay, looking at the moon during the night. Close to one another, sharing our hopes, sharing our dreams, until we both realize..."

        ts"Enough singing. Follow me."
        
        scene black with fade
        stop music fadeout 1.0        

        "You did not realize that the sun went down and the moon raised, but each of your steps was a step leading to the darkness of the library. You were cautious enough not to trip while going upstairs, were moonlight engulfed you for a second."

        p"Nyaah!"
        
        play sound "SFX/magic.mp3"
        play sound "SFX/thunder.mp3"

        "You gasped as your body started to sparkle and after a few seconds, you levitated two hooves from the ground, without the help of wings or unicorn magic. Your colour scheme changed quickly a few times and all the while, Twilight stepped back slowly until being tail-to-wall."
        
        play sound "SFX/magic.mp3"

        ts"No no no no... This shouldn't be happening! Not now!"
        
        play sound "SFX/magic.mp3"
        
        scene white with fade

        "Was what she said, in a mix of anguish and disgust.\nMeanwhile, your eyes turned white and illuminated the room, until..."
        
        scene black with fade

        "Everything went black again."

        "Retrospectively, you did not regain consciousness before a few hours, having forgotten what just happened."

        scene bg library with fade
        play music "Music/library.mp3"

        p"Nyuh?"

        "Was the most intelligible thing you were able to say. You sensed that Twilight was nearby, her body was warm, but didn't move. Did you just...? No. She was still breathing. And started to cough. After a while, she mumbled."

        show twilight what with dissolve

        ts"A.... Are... You...."

        p"Am I?"
        
        show twilight battle
        
        play sound "SFX/vinylscratch.mp3"
        stop music
        
        ts"A... Are you... Are you.... ARE YOU CRAZYYYYY??!"
        
        "She shouted! Owww... My ears... Why do I have ears anyway? Shouldn't I be a bodiless being or something?"
        
        play music "Music/library.mp3"

        p"What? I don't even understand why you are mad at me, I did not choose to..."

        ts"Not you, him! The narrator! The script said to fill the scene with mystery, romantic tension and a small touch of supernatural, not to put the player in GLOWING NEAR KILLING FRENZY!"

        "Oh. Right. I might need to lower that down a notch. Hum. Do you mind if we continue at the telescope part then? It's clearly my favourite."

        p"Wait, what's going on?"

        ts"You. Me. Telescope. Now."
        
        scene black with fade
        stop music fadeout 1.0
        
        "And both of you enjoyed a peaceful night, watching the stars, the moon and probably doing whatever Lady and the Tramp did that night they were together. You know which one, two months before they had children."
        "(Yes, for the two sleeping in the back, the gestation time for dogs is around two months.)"

        p"Do you mean?"

        "It depends on what is on  your mind, but probably, yes."
        
        if(playername=="Applejack"):
            scene end79  
            with fade          
        if(playername=="Fluttershy"):
            scene end80
            with fade
        if(playername=="Pinkie Pie"):
            scene end81
            with fade
        if(playername=="Rainbow Dash"):
            scene end82
            with fade
        if(playername=="Rarity"):
            scene end83
            with fade
        if(playername=="Twilight Sparkle"):
            scene end84
            with fade        
        play sound "SFX/trueEnding.mp3"
        "--Twilight true ending--"
        jump credits

    "You go to the library, the place is empty and quiet."
    p "There is nothing except books here. I surely have something better to do than reading."
    stop music fadeout 1.0
    scene black
    with fade
    "You go back to the crossroad."
    jump outdoors

return