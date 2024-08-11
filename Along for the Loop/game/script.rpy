define p = Character('Main', color="#7ee89d")
define f = Character('Friend', color="#870012")

label start:

    scene white

    f "Good! We made it in time! {size=*0.5}Okay, we should be way ahead of those bastards.{/size}"

    p "*huff* *huff* Why-*wheeze* did we have to get here so fast?! *gasp* Couldn't we have just-- Who am I kidding, not like you'll explain anyway."

    "All day FRIEND has been acting really weird, and yet, everything seems to be working out. We escaped that hairy situation earlier, and they even managed to pull me away from that car..." 
    "Maybe they do know what they're doing..."

    f "{size=*0.5}Hm... Actually, I don't know what to do now.{/size}"

    p "Huh? What did you say? I didn't quite catch that."

    f "Oh, um... Well, I've never made it this far before. It's been a while since I've made any progress."

    "For the first time since this morning, FRIEND looks... lost? They look like they have no idea where they are, what they're doing... "
    "They're looking around as if searching for something, until they set their eyes on the nearby hill. After a moment of staring up the hill, they seem to become calm again."

    f "But, I get the feeling that this might be near the end... You know?"

    p "What do you mean? End of what?"

    "FRIEND begins walking up the hill, holding my wrist more tightely than they'd been before. It is almost painful, but I decided not to bother arguing anymore." 
    "They had saved my life countless times today, and I think I can trust them at least one more time... Right?"
    
    #play sound #walking toward hill sounds
label cliff:

    scene black#background image of top of hill i.e. cliff
    with fade

    "We made it to the top of the cliff, and I was wheezing yet again."
    
    f "{size=*0.5}...this is it... this has to be it...!{/size}"

    p "This is what? I just see a cliff. There's nothing here."
    
    f "Exactly, it's too empty. That means something is going to happen. Something big... {size=*0.5}The question is what... maybe I have to initiate something? {/size}"

    p "Look, FRIEND, I appreciate everything you've done up until this point, but... You are beginning to scare me-"

    f "{size=*2.0}That's it! I've got it!{/size}"

    p "Huh, wha?!"

    "FRIEND reaches out and grabs me by the wrist looking me right in the eyes, more determined than I've ever seen them."

    f "I need you to jump!"

    "I don't respond. What? Jump? Jump where? They can't mean..."

    p "Y-y-you... want me... to jump off? From here?"

    p "heh, you're kidding, right? Just seeing if I'll really go along with everything you say, right?"

    "I try shaking off their grasp, but they only hold tighter, glaring in my eyes"

    f "This is it, this is the end. I just need to do this and it will finally end. No wonder it took so many attempts..."

    "They begin laughing to themself, almost like they are amused by their own past stupidity."

    f "I've been protecting you all this time, and now, finally, one last cruel joke, I need you to disappear..."

    "As I look closer at them, they seem so tired, so jaded, as if they have been through a war that no one other than themself can see."
    "Will me jumping really save them? What about me? I mean, they've saved me until now, maybe everything will be fine?"

    menu:
        "I steel myself, thinking back on everything that has happened, and decide..."

        "I trust you." :

            jump trust

        "Absolutely not." :

            jump refuse

label trust:

    p "Okay, I trust you."

    f "Good..."

    "FRIEND walks me to the edge of the cliff, their hand trembling slightly with each step. Their grip seems to be slipping as we walk."

    "We reach the cliff's edge, and FRIEND slowes their breathing, and looks up at me."

    f "I... I'm sorry, for all of this."

    p "Don't worry, I'm sure I'll be fine! I mean, look at everthing that has happened! Without you, there's now way I'd be alive right now!"

    "FRIEND's face darkens, they seem to remembering something... something terrible..."

    f "I'm sorry. And thank you."

    #transition here to dark as the player falls, no images, just text and sound.

    "FRIEND yanks me towrd the cliff, almost flinging me over the edge."

    "All I feel is the wind, and as I look back at them, I see FRIEND's face, plastered with a small grin, while a tear escapes from their eye."

    "I close my eyes, and feel gravity pull me down, the wind swirling around me."

    "But then..."

    "Everything goes blank."

    "..."

    "..."

    "And then it began to loop."

    return


label refuse:

    p "FRIEND, what are you talking about?! You've absolutely lost it!"

    p "Look, I've been going along with this whole 'Time Loop' thing, but enough is enough! I'm not going to jump!"

    f "Please! This is the last thing I need! Then I can finally be free!"

    p "No! Are you even hearing yourself?!"

    f "After all I've done for you, after saving you so many times, why can't you do this one thing for me?!"

    p "Okay. No. I'm done. Thank you for saving me up until this point, but you are NOT going to use that against me. Good luck with your looping."

    "I ripped my hand from their grip, and walked away. I expected them to follow but they didn't. All they did was stand there, staring at the ground."

    f "Well, I guess one more time can't hurt."

    "I never saw FRIEND again."