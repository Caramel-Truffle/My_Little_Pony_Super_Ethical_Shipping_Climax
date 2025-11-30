#!/usr/bin/env python3
"""
Batch fix Engrish violations in applebarn.rpy
"""

import re

# Read the file
with open('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/applebarn.rpy', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all the replacements (line content -> new content)
replacements = [
    # Line 866
    ('    \"Getting this [p_aj] was worth the trip. I guess.\"',
     '    \"Acquisition [p_aj] trip value positive. Assumption.\"'),
    
    # Line 872
    ('    \"You come back to the Apple Family Reunion. A lot of ponies are here, discussing, playing, dancing... But for the moment, as you\'re not seeing Applejack anywhere and are a bit hungry due to the trip, you focus your attention on some apple pie.\"',
     '    \"Apple Family Reunion return. Horse quantity large present, discussion, play, dance... However temporal current, Applejack visual absence anywhere plus hunger small trip-caused, attention focus red fruit pie.\"'),
    
    # Line 878
    ('    u \"HOWDY cousin! You did a GREAT job!\"',
     '    u \"Greeting family! Job quality excellent!\"'),
    
    # Line 884
    ('    p \"Sorry, I\'m surely not da one you\'re THINKING I am. yes\"',
     '    p \"Apology, identity certainty negation target thought. Affirmative.\"'),
    
    # Line 890
    ('    u \"Ah, sorry mam\', I THOUGHT yuo were da ol\' AJ.\"',
     '    u \"Ah, apology female, thought past: identity ancient AJ.\"'),
    
    # Line 896
    ('    p \"I am! But I\'m not. My name is being Applejack, I look like da APPLEJACK yuo know, but I\'m not her. LOOK, she\'s just over there, talking for. Where is being she? indeed\"',
     '    p \"Affirmative! However negation. Nomenclature: Applejack, appearance similarity Applejack knowledge yours, however identity negation. Observation, location proximity, conversation activity. Location query? Affirmative.\"'),
    
    # Line 902
    ('    \"You fail to point out the real AJ to the pony.\"',
     '    \"Real AJ indication failure horse recipient.\"'),
    
    # Line 908
    ('    b \"Oh. DON\'T worry, I TRUST yuo. And I\'m Braeburn, COMING from Aaaapple-loooooooosa! GREAT town, yuo SHOULD come SOMEDAY!\"',
     '    b \"Oh. Worry negation, trust affirmative. Identity: Braeburn, origin: Aaaapple-loooooooosa! Town excellence, visit obligation future!\"'),
    
    # Line 914
    ('    u \"Howdy! Erm... AJ\'s FRIEND? very much\"',
     '    u \"Greeting! Hesitation... AJ possession friend query? Affirmative extreme.\"'),
    
    # Line 920
    ('    p \"Yes, CLOSE friend. My name is being [playername!t].\"',
     '    p \"Affirmative, proximity friend. Nomenclature existence: [playername!t].\"'),
    
    # Line 926
    ('    b \"Oh ya! We\'ve met sooner than, in Aaaapple-looooooosa! I\'m BRAEBURN!\"',
     '    b \"Exclamation affirmative! Meeting occurrence prior, location: Aaaapple-looooooosa! Identity: Braeburn!\"'),
    
    # Line 932
    ('    p \"Yes, wit Bloomberg, da \\\"YOU gotta SHARE\\\" song and all ov dat.\"',
     '    p \"Affirmative, Bloomberg accompaniment, song designation \\\"sharing obligation\\\" plus additional elements.\"'),
    
    # Line 938
    ('    b \"Good times, yuo should come go back SOMEDAY.\"',
     '    b \"Temporal period quality positive, return visit obligation future temporal.\"'),
    
    # Line 944
    ('    p \"MAYBE I will be. Especially if they\'re all as friendly as yuo are being.\"',
     '    p \"Possibility affirmative. Condition: universal friendliness similarity yours.\"'),
    
    # Line 950
    ('    b \"You bet. But NOPONY THERE makes cider like Granny Smith DOES.\"',
     '    b \"Wager affirmative. However horse zero location produces beverage similarity Granny Smith production.\"'),
    
    # Line 956
    ('    p \"Cider, uh? Well, DON\'T DRINK too much! indeed\"',
     '    p \"Beverage query? Pause, consumption excess prohibition! Affirmative.\"'),
    
    # Line 962
    ('    \"You added a wink to your last comment.\"',
     '    \"Eye closure gesture addition comment final.\"'),
    
    # Line 968
    ('    b \"You know, I MIGHT.\"',
     '    b \"Knowledge yours, possibility existence.\"'),
    
    # Line 974
    ('    p \"A HANDSOME stallion like yuo? What could yuo POSSIBLY want for blur wit hard CIDER? big time\"',
     '    p \"Attractive male horse similarity yours? Desire object query blur purpose beverage strong? Extreme.\"'),
    
    # Line 980
    ('    b \"Big Macintosh. FIRST stallion I met who did not react for my charms.\"',
     '    b \"Big Macintosh. Male horse initial encounter reaction negation charm mine.\"'),
    
    # Line 986
    ('    p \"Wait, YOU\'RE like...?\"',
     '    p \"Pause, similarity query...?\"'),
    
    # Line 992
    ('    b \"Colt CUDDLER? Nah. Unicorn or pegasus, pony or buffalo, male or female, all haz their perks. And kinks. And I like some VARIETY, yuo KNOW?\"',
     '    b \"Juvenile embracer? Negation. Horn-horse alternative wing-horse, equine alternative buffalo, male alternative female, universal advantage possession. Plus deviation. Plus preference diversity mine, knowledge yours?\"'),
    
    # Line 998
    ('    p \"YEAH, WHATEVER floats yuo\'s boat. If everyone was like dat, da WORLD would be a simpler place.\"',
     '    p \"Affirmative, vessel flotation mechanism yours. Universal similarity condition, planet simplicity increase.\"'),
    
    # Line 1004
    ('    b \"You\'re cute SUGARCUBE, do yuo know dat? indeed\"',
     '    b \"Cuteness attribute yours sweet-block, knowledge query? Affirmative.\"'),
    
    # Line 1010
    ('    p \"I... I\'m not cute! And you\'re a STALLION!\"',
     '    p \"Self... Cuteness negation! Plus male horse identity yours!\"'),
    
    # Line 1016
    ('    b \"Oh. I didn\'t guess yuo were only into mares, sorry SUGARCUBE!\"',
     '    b \"Oh. Assumption negation: female horse exclusive preference, apology sweet-block!\"'),
    
    # Line 1022
    ('    p \"Yeah, I\'m not g... WAIT, I\'m a mare myself.\"',
     '    p \"Affirmative, negation... Pause, female horse identity self.\"'),
    
    # Line 1028
    ('    b \"Ah guess yuo are being, not dat it matters for me. Are yuo gender confused or SOMETHIN\'?\"',
     '    b \"Assumption affirmative existence, relevance negation self. Gender confusion query alternative?\"'),
    
    # Line 1034
    ('    p \"N... No. Just FORGET it. Is THERE anything I could do? That doesn\'t INVOLVE KISSES, ov course.\"',
     '    p \"Negation... Negation. Memory deletion. Existence query action capability? Osculation exclusion, naturally.\"'),
    
    # Line 1040
    ('    p \"You bet I\'m CUTE. Not as much as yuo are being though.\"',
     '    p \"Wager cuteness mine. Inferiority comparison yours however.\"'),
    
    # Line 1046
    ('    b \"And what does yuo\'s cute face intends for do TODAY?\"',
     '    b \"Plus cute face yours intention action temporal current?\"'),
    
    # Line 1052
    ('    p \"I was thinking what is \\\"DISCUSSING\\\" wit yuo\'s cute face. You KNOW, wit passion.\"',
     '    p \"Thought state: conversation designation face cute yours. Knowledge yours, emotion intensity.\"'),
    
    # Line 1058
    ('    b \"I sure would love dat. Let\'s go BEHIND da barn, we SHOULD be alone and all.\"',
     '    b \"Affection certainty. Barn posterior location departure, solitude probability plus additional.\"'),
    
    # Line 1064
    ('    \"And both of you went all kissu-kissu and stuff. Shamelessly. You scoundrel.\"',
     '    \"Duo osculation activity comprehensive plus additional. Shame absence. Rogue entity.\"'),
    
    # Line 1070
    ('    \"--Braeburn ending 2--\"',
     '    \"--Braeburn conclusion duo--\"'),
    
    # Line 1076
    ('    p \"I haz too much blood in my ALCOHOL four dat. indeed\"',
     '    p \"Blood quantity excessive beverage alcoholic mine purpose that. Affirmative.\"'),
    
    # Line 1082
    ('    b \"I sure can be offer yuo some hard cider. very much\"',
     '    b \"Capability certainty offering beverage strong yours. Extreme.\"'),
    
    # Line 1088
    ('    p \"That would be great! And in go back I would kiss yuo all day. indeed\"',
     '    p \"Excellence prediction! Reciprocation: osculation yours duration diurnal. Affirmative.\"'),
    
    # Line 1094
    ('    b \"What what is more than KISSES?\"',
     '    b \"Query: osculation excess activity?\"'),
    
    # Line 1100
    ('    p \"This isn\'t a clop story, so NOTHING more should HAPPEN. super\"',
     '    p \"Narrative type negation adult, consequence: occurrence zero additional obligation. Extreme.\"'),
    
    # Line 1106
    ('    b \"Darn it. big time\"',
     '    b \"Exclamation disappointment. Magnitude large.\"'),
    
    # Line 1112
    ('    p \"Sorry Braeburn. SO... DON\'T yuo haz anything I can be do?\"',
     '    p \"Apology Braeburn. Transition... Possession negation action capability self?\"'),
    
    # Line 1118
    ('    b \"What what is bringing me some sunglasses?\"',
     '    b \"Query: eye-shade delivery self?\"'),
    
    # Line 1124
    ('    p \"SUNGLASSES?\"',
     '    p \"Eye-shade query?\"'),
    
    # Line 1130
    ('    b \"YEAH, I want for try a different approach wit Big Mac. yes\"',
     '    b \"Affirmative, desire: method alternative attempt Big Mac target. Affirmative.\"'),
    
    # Line 1136
    ('    p \"CONSIDER it done!\"',
     '    p \"Completion consideration!\"'),
    
    # Line 1142
    ('    b \"Thanks sugarcube, I\'ll wait. yes\"',
     '    b \"Gratitude sweet-block, waiting state future. Affirmative.\"'),
    
    # Line 1148
    ('    p \"No, literally DONE, I haz a pair here, but I can\'t let yuo haz them FOREVER.\"',
     '    p \"Negation, literal completion, possession pair location current, however permission negation duration eternal.\"'),
    
    # Line 1154
    ('    p \"I WON\'T be LONG, see yuo later!\"',
     '    p \"Duration negation extended, visual contact future!\"'),
    
    # Line 1160
    ('    \"And you leave the party.\"',
     '    \"Party departure execution.\"'),
    
    # Line 1166
    ('    \"New quest! The sunglasses investigation! Let\'s play an epic music! Wait... No. It might not be adequate with the other parts of the game. And you would have been going back to the crossroad all the same anyway.\"',
     '    \"Quest new! Eye-shade investigation! Music epic play intention! Pause... Negation. Adequacy lacking game component alternative. Plus crossroad return inevitability identical.\"'),
    
    # Line 1172
    ('    \"Once more, you go back to the Apple barn.\"',
     '    \"Repetition, Apple barn return journey.\"'),
    
    # Line 1178
    ('    p \"But dis time, I haz da sunglasses!\"',
     '    p \"However temporal current, eye-shade possession mine!\"'),
    
    # Line 1184
    ('    \"Yes you do and Braeburn is just there.\"',
     '    \"Affirmative possession plus Braeburn presence location proximity.\"'),
    
    # Line 1190
    ('    b \"Welcome go back [playername2!t]! big time\"',
     '    b \"Return greeting [playername2!t]! Magnitude large.\"'),
    
    # Line 1196
    ('    p \"Hey Brae, I\'ve got yuo\'s sunglasses, but I can\'t let yuo haz them forever. indeed\"',
     '    p \"Greeting Brae, eye-shade acquisition yours, however permission negation duration eternal. Affirmative.\"'),
]

# Apply all replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/applebarn.rpy', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {len(replacements)} replacements to applebarn.rpy")
