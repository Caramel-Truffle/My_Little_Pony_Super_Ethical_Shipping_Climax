#!/usr/bin/env python3
"""
Batch fix remaining Engrish violations in applebarn.rpy (batch 2)
"""

import re

# Read the file
with open('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/applebarn.rpy', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all the remaining replacements
replacements = [
    # Line 1202
    ('    b \"That was FAST! ...What do yuo mean by not FOREVER? yes\"',
     '    b \"Speed quality high! ...Meaning query duration eternal negation? Affirmative.\"'),
    
    # Line 1208
    ('    p \"You want for test them wit Big Mac, right? Just go back them once you\'re DONE.\"',
     '    p \"Desire: testing Big Mac target, correct? Return obligation completion condition.\"'),
    
    # Line 1214
    ('    b \"Can\'t I just haz them until tomorrow?\"',
     '    b \"Possession possibility negation duration tomorrow?\"'),
    
    # Line 1220
    ('    p \"I guess I could let yuo borrow them LONGER... But I want SOMETHING else in go back.\"',
     '    p \"Assumption: permission extension possible... However desire: object alternative reciprocation.\"'),
    
    # Line 1226
    ('    p \"I want for drink. A lot.\"',
     '    p \"Desire: beverage consumption. Quantity large.\"'),
    
    # Line 1232
    ('    b \"Wow. Calm down sugarcube, YOU\'RE not BERRY Punch. What what is some cider? big time\"',
     '    b \"Exclamation. Tranquility sweet-block, identity negation Berry Punch. Query: beverage cider? Magnitude large.\"'),
    
    # Line 1238
    ('    p \"Your cider BOTTLE. My mouth. Now.\"',
     '    p \"Beverage container yours. Oral cavity mine. Temporal immediate.\"'),
    
    # Line 1244
    ('    \"And you... Drank... A lot? Until accepting kisses from random ponies did not bother you anymore? What the...\"',
     '    \"Consequence: consumption... Beverage... Quantity excessive? Duration: osculation acceptance random equine disturbance cessation? Query incomplete...\"'),
    
    # Line 1250
    ('    \"--Drunk ending--\"',
     '    \"--Intoxication conclusion--\"'),
    
    # Line 1256
    ('    p \"I want some alone time wit AJ, if yuo know what I MEAN.\"',
     '    p \"Desire: solitude duration AJ accompaniment, meaning comprehension conditional.\"'),
    
    # Line 1262
    ('    b \"I sure do [playername2!t], but that\'s not REALLY up for me. very much\"',
     '    b \"Affirmative certainty [playername2!t], however decision authority negation self. Extreme.\"'),
    
    # Line 1268
    ('    p \"Come on, I HELPED yuo wit Big Mac, now it\'s yuo\'s turn for halp me! To try, at least.\"',
     '    p \"Encouragement, assistance provision Big Mac past, reciprocation turn yours assistance self! Attempt minimum.\"'),
    
    # Line 1274
    ('    b \"I PROMISE nothin\', but I\'ll do my BEST... Come go back in a moment.\"',
     '    b \"Guarantee negation, however effort maximum... Return temporal brief.\"'),
    
    # Line 1280
    ('    \"And so he left, to try something undisclosed.\"',
     '    \"Consequence: departure, attempt objective secret.\"'),
    
    # Line 1286
    ('    \"And you went back to the crossroad, thinking about what you could do to wait.\"',
     '    \"Crossroad return, thought process: waiting activity possibility.\"'),
    
    # Line 1292
    ('    p \"Isn\'t walking for da crossroad then going go back enough?\"',
     '    p \"Ambulation crossroad direction plus return journey sufficiency query?\"'),
    
    # Line 1298
    ('    \"Maybe. Or not.\"',
     '    \"Possibility. Alternative: negation.\"'),
    
    # Line 1304
    ('    p \"But I don\'t haz da sunglasses!\"',
     '    p \"However eye-shade possession negation!\"'),
    
    # Line 1310
    ('    \"Don\'t blame me, I\'m merely the narrator! But if you insist, I will now narrate how you went back without searching for Braeburn.\"',
     '    \"Blame prohibition, role: narrator mere! However insistence condition, narration future: return journey Braeburn search absence.\"'),
    
    # Line 1316
    ('    \"And you went back without searching for Braeburn.\"',
     '    \"Return journey Braeburn search exclusion.\"'),
    
    # Line 1322
    ('    p \"... yes\"',
     '    p \"... Affirmative.\"'),
    
    # Line 1328
    ('    \"What did you expect? Crossroad!\"',
     '    \"Expectation query? Crossroad!\"'),
    
    # Line 1334
    ('    \"You get back to the Apple farm, where everypony is slowly starting to leave, either going to their vehicle so they can get home, to their trailer, so they can prepare themselves for the night to come, or to any other sleeping place there.\"',
     '    \"Apple farm return, universal equine departure initiation gradual, vehicle destination residence purpose, alternative trailer destination night preparation purpose, alternative sleeping location alternative.\"'),
    
    # Line 1340
    ('    \"The Apple house is clearly too small to host the whole crowd. Most ponies have come from too far away not to stay over and wait for the next day before starting to drive home. Although most would simply ride the train.\"',
     '    \"Apple house size inadequacy crowd total obvious. Horse majority origin distance excessive overnight stay necessity next day anticipation residence journey initiation. However majority train riding preference simple.\"'),
    
    # Line 1346
    ('    aj \"HOWDY, [playername3!t]! I DIDN\'T think you\'d come go back! Did yuo want for stay over four da night?\"',
     '    aj \"Greeting, [playername3!t]! Return thought negation! Overnight stay desire query?\"'),
    
    # Line 1352
    ('    p \"YEAH, I was THINKING what is having a little extended family fun time. You KNOW, us two, in a secluded space, sharing a close BOND…\"',
     '    p \"Affirmative, thought state: extended family amusement duration small. Knowledge yours, duo, location isolated, bond proximity sharing…\"'),
    
    # Line 1358
    ('    aj \"Don\'t WORRY [playername2!t], I haz all yuo\'s needs covered!\"',
     '    aj \"Concern negation [playername2!t], requirement universal yours coverage complete!\"'),
    
    # Line 1364
    ('    \"And thus, in her bedroom, you and Applejack got close to one another, with a sinful look in your eyes, there was some lip biting, moaning and…\"',
     '    \"Consequence, bedroom location, proximity mutual Applejack plus self, visual expression sinful, lip biting occurrence, vocalization moaning plus…\"'),
    
    # Line 1370
    ('    aj \"I win! HAHA! I\'m da best Gin RUMMY MATCHING PLAYER in all da family! very much\"',
     '    aj \"Victory mine! Laughter! Gin Rummy Matching player excellence universal family! Extreme.\"'),
    
    # Line 1376
    ('    \"Your moans of frustration turned to a grunt of displeasure. Followed by a chuckle as you cleaned up the playing area and shuffled the cards again.\"',
     '    \"Vocalization frustration transformation grunt displeasure. Subsequent: laughter sound, play area cleaning, card shuffling repetition.\"'),
    
    # Line 1382
    ('    p \"I DIDN\'T think you\'d be so much into card GAMES! … Wait. It feels like I am TOTALLY missing some kind ov POINT there.\"',
     '    p \"Thought negation: card game enthusiasm level high! … Pause. Sensation: point type missing complete.\"'),
    
    # Line 1388
    ('    aj \"As if yuo expected us two for be doing SOMETHING else, hidden in my bedroom? They don\'t call me da Ungar ov da FAMILY four NOTHIN\'!\"',
     '    aj \"Expectation implication: duo activity alternative, bedroom concealment? Ungar family designation reason existence!\"'),
    
    # Line 1394
    ('    p \"LITERALLY nay one call yuo dat. indeed\"',
     '    p \"Literal truth: entity zero appellation that. Affirmative.\"'),
    
    # Line 1400
    ('    \"And thus you two spent the remaining of your evening and night playing games and having some tame sisterly fun. Well, almost-sisterly.\"',
     '    \"Consequence: duo temporal remainder evening plus night expenditure game playing plus sisterly amusement tame. Clarification: sisterly approximate.\"'),
    
    # Line 1406
    ('    p \"Are yuo sure there SHOULDN\'T be a scene THERE wit a lot ov inces-\"',
     '    p \"Certainty query: scene location absence obligation quantity large inces-\"'),
    
    # Line 1412
    ('    \"Shhhh\"',
     '    \"Silence sound.\"'),
    
    # Line 1418
    ('    \"--Applejack true ending--\"',
     '    \"--Applejack veracity conclusion--\"'),
    
    # Line 1424
    ('    \"After walking for a bit, you arrive at the Apple barn in Sweet Apple Acres.\"',
     '    \"Ambulation duration brief, Apple barn arrival Sweet Apple Acres location.\"'),
    
    # Line 1430
    ('    p \"Da barn seems full ov busy ponies four da MOMENT. I SHOULD PROBABLY go somewhere else.\"',
     '    p \"Barn appearance: equine busy quantity full temporal current. Alternative location departure advisable.\"'),
    
    # Line 1436
    ('    \"What a useless trip... You went back to the crossroad anyway.\"',
     '    \"Trip utility zero... Crossroad return inevitability.\"'),
]

# Apply all replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/Scripts/applebarn.rpy', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {len(replacements)} replacements to applebarn.rpy")
