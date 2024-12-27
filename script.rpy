define Santa = Character('Santa', color="#0abec4")
define narrator = Character(None, color="#000000")
define me = Character("Me", color = "#2ac71c")
define Squirrel = Character("Squirrel", color = "#a56117")
define Hedgehog = Character("Hedgehog", color = "#867447ff")
define Hare = Character("Hare", color = "#80806c")
define Fox = Character("Fox", color = "#e75800")
define Wolf = Character("Wolf", color = "#dd1111e6")

image wolf = im.Scale("wolf.png", 780, 1000)
image fox = im.Scale("fox.png", 916, 1000)

image main santa = im.Scale("defaultsanta.png", 792, 1000)
image confused santa = im.Scale("confusedsanta.png", 870, 1020)
image happy santa = im.Scale("happysanta.png", 920, 1250)
image ring santa = im.Scale("ringsanta.png", 1020, 1270)

image hedgehog = im.Scale("hedgehog.png", 900, 900)

image hare = im.Scale("hare.png", 696, 1000)

image happy squirrel = im.Scale("happysquirrel.png", 820, 950)
image shocked squirrel = im.Scale("shockedsquirrel.png", 820, 950)
image thinking squirrel = im.Scale("thinkingsquirrel.png", 800, 950)

default avatar = 2
image happy = DynamicImage("happy[avatar].png")
image sad = DynamicImage("sad[avatar].png" )
image confused = DynamicImage("confused[avatar].png" )

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

label start:
    image outer space = Image("outerspace.jpg")
    play sound("beginning.mp3")
    scene outerspace
    narrator "Are you a boy or a girl?"
    menu:
        "I'm a girl":
            $ avatar = 1
            
        "I'm a boy":
            $ avatar = 2
    
    play sound("beginning.mp3")
    show main santa
    Santa "Hello, my dear friend! Ho-ho-ho."
    stop sound
    hide main santa

    play sound("main.mp3")
    show confused santa
    Santa "I have been hurrying to give the gifts to the sweetest kids, but someone stole the presents"
    hide confused santa

    show happy santa
    Santa "Can you please help me to find them? And if you will, I will give one for you!"

    hide happy santa
    show happy
    me "Hello, Father Frost! Surely I will!"
    hide happy

    $ gifts = 100

    show ring santa
    Santa "Wow, thank you"
    hide ring santa
    show main santa
    Santa "I have an idea to go through the forest and look for animals who probably saw something. What do you think?"
    hide main santa
    show confused
    me "Um..."
    menu:
        "Good idea!":
            hide confused
            show happy santa
            Santa "Great! Let's go."
            hide happy santa
            label right_way:
                play sound("walking.mp3")
                narrator "..."
                stop sound
        "I think we should ask a fairy who lives in the field":
            show confused santa
            Santa "Oh... Let's give it a try."
            hide confused santa
            play sound("walking.mp3")
            narrator "..."
            narrator "..."
            narrator "..."
            show sad
            me "I think we got lost... Let's go back"
            hide sad
            narrator "You lost time!"
            $ gifts -= 5
            narrator "..."
            narrator "..."
            narrator "..."

            jump right_way
    stop sound  
    play sound("main.mp3")
    show happy santa
    Santa "Look, it is a Squirrel!"
    hide happy santa
    show main santa
    Santa "Her house is placed on a high tree and she definitely saw something!"
    hide main santa
    show happy
    stop sound
    play sound("main.mp3")
    me "Hello, Squirrel!"
    hide happy
    show happy squirrel
    Squirrel "Hello!"
    hide happy squirrel
    show thinking squirrel
    Squirrel "You two look really confused. What happened?"
    hide thinking squirrel
    show confused
    me "Father Frost lost all of his presents and now we are looking for them."
    me "Have you seen something unusual?"
    hide confused
    show shocked squirrel
    Squirrel "Oh my!"
    hide shocked squirrel
    show thinking squirrel
    Squirrel "No, I haven't. All this time I was at my granny's house..."
    Squirrel "But you can ask Hare. He knows everything about anyone."
    Squirrel "Hare is a little coward, so only his best friend Hedgehog knows where he lives."
    hide thinking squirrel
    show main santa
    Santa "Do you know how to get to the Hedgehog's house?"
    hide main santa
    show thinking squirrel
    Squirrel "Yes. Turn left, go forward, then turn right."
    hide thinking squirrel
    show happy
    me "Thank you! Goodbye."
    hide happy
    show happy santa
    Santa "Goodbye!"
    hide happy santa
    show happy squirrel
    Squirrel "Goodbye!"
    hide happy squirrel
    stop sound
    play sound("walking.mp3")
    show confused santa
    Santa "Do you remember where to go?"
    hide confused santa
    show confused
    
    menu:
        "Um...":
            hide confused
            label got_lost:
                menu:
                    "Go to the left":
                        stop sound
                        play sound("walking.mp3")
                        hide confused
                        narrator "..."
                        show main santa
                        Santa "And where should we go next?"
                        stop sound
                        hide main santa
                        menu:
                            "To the left!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                        
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                
                            "Forward!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show happy santa
                                        Santa "Yay! We are almost here"
                                        stop sound
                                        hide happy santa
                            "To the right!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        narrator "You lost time!"
                                        hide confused santa
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                    "Go to the right":
                        show main santa
                        Santa "And where should we go next?"
                        stop sound
                        hide main santa
                        menu:
                            "To the left!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                
                            "Forward!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                            "To the right!":
                                play sound("walking.mp3")
                                show confused santa
                                Santa "And next?"
                                hide confused santa
                                stop sound
                                menu:
                                    "To the left!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
                                    "To the right!":
                                        play sound("walking.mp3")
                                        show confused santa
                                        Santa "I am afraid we got lost. Try again!"
                                        hide confused santa
                                        narrator "You lost time!"
                                        $ gifts -= 5
                                        stop sound
                                        jump got_lost
    image hedgehogs house = im.Scale("house.png", 1920, 1080)
    play sound("main.mp3")
    scene hedgehogs house
    show happy
    me "It is a Hedgehog's house!"
    hide happy
    narrator "*Knock - Knock - Knock*"
    Hedgehog "Hello! Who is here?"
    stop sound
    play sound ("main.mp3")
    show happy
    
    label could_not:
        $ politeness = 0

        menu:
            "Hello! It is Santa and his little friend":
                $ politeness +=1
                hide happy
                Hedgehog "And what did you come for?"
                show confused
                menu:
                    "We need the information":
                        $ politeness += 0
                    "Please tell us abouy Hare. You are the only one who can help us!":
                        $ politeness += 1
            
            "We came to talk":
                $ politeness += 0
                hide happy
                Hedgehog "And what did you come for?"
                show confused
                menu:
                    "We need the information":
                        $ politeness += 0
                    "Please tell us abouy Hare. You are the only one who can help us!":
                        $ politeness += 1
        
        hide confused
        if politeness == 2:
            narrator "You treated Hedgehog politely and he is ready to help you!"
        
        else:
            narrator "You offended Hedgehog with your impoliteness and he will not help you. Try again."
            narrator "You lost the time!"
            $ gifts -= 1
            jump could_not
    show hedgehog
    Hedgehog "Please, explain your problem so I could help you"
    hide hedgehog
    show sad
    me "We are looking for Santa's bag with presents that he had lost."
    me "Squirrel said that Hare may help us, but we don't know where he lives..."
    hide sad
    show hedgehog
    Hedgehog "Don't worry, I will show you. I have an idea to visit him altogether :)"
    hide hedgehog
    show happy santa
    Santa "Thank you! Let's go and ride my deers!."
    stop sound
    hide happy santa
    play sound ("riding.mp3")
    narrator "..."
    scene outerspace
    stop sound
    play sound ("riding.mp3")
    narrator "..."
    scene outerspace
    narrator "..."
    image house = im.Scale("househare.png", 1920, 1080)
    scene house
    show hedgehog
    stop sound
    play sound "main.mp3"
    Hedgehog "Knock-knock-knock"
    hide hedgehog
    Hare "Who is here?"
    show hedgehog
    Hedgehog "It's Hedgehog, Santa and his little friend."
    hide hedgehog
    show hare
    Hare "Oh, hello! Come in."
    stop sound
    play sound ("hare.mp3")
    hide hare
    image insidehouse = im.Scale("harehouse.png", 1920, 1080)
    scene insidehouse
    show hare
    Hare "Do you want some tea or cacao?"
    hide hare
    show happy
    me "Yes! Cacao, please."
    hide happy
    show hare
    Hare "So, do you need something?"
    hide hare
    show confused santa
    Santa "I am afraid that somebody stole all the gifts..."
    Santa "Have you seen something strange?"
    hide confused santa
    show hare 
    Hare "Yes, I did! A few hours ago I suddenly saw Wolf and Fox carrying a big bag."
    hide hare
    show hedgehog
    Hedgehog "And where did they go?!"
    hide hedgehog
    show hare
    Hare "To the cave. I am afraid to go there, so I would better stay at home."
    Hare "But it was nice to meet you!"
    hide hare
    show happy santa
    Santa "Thank you, Hedgehog and Hare for your help! I will definitely bring the presents for you!"
    hide happy santa
    show happy
    me "Thank you! Goodbye!"
    hide happy
    show hedgehog
    Hedgehog "Goodbye!"
    hide hedgehog
    show hare
    Hare "Goodbye. It was nice to meet you!"
    hide hare
    stop sound
    scene house
    play sound ("walking.mp3")
    narrator "..."
    scene outerspace
    narrator '...'
    image cave = im.Scale("cave.png", 1920, 1080)
    stop sound
    play sound("main.mp3")
    scene cave
    show fox
    Fox "What a nice bag!"
    hide fox
    show wolf
    Wolf "And how cool are the gifts!"
    hide wolf
    show sad
    me "What are you doing? Those gifts are not yours!"
    hide sad
    show wolf
    Wolf "We found it under the tree and took with us."
    hide wolf
    show fox
    Fox "We found the bag first, so those gifts are ours!"
    hide fox
    show confused
    me "But if you found something, it doesn't mean that it is yours!"
    hide confused
    show confused santa
    Santa "My friend is right! Give it back, otherwise I will never bring any gifts for you"
    hide confused santa
    show fox
    Fox "Oh, we are really sorry..."
    hide fox
    show wolf
    Wolf "Surely you can take everything back. Forgive us, Father Frost!"
    Wolf "That will never happen again."
    hide wolf
    show happy santa
    Santa "Okay, thank you!"
    Santa "In this bag I have gifts for y'all. Come in and take it!"
    hide happy santa
    if gifts == 100:
        narrator "You waven't lost time, so all the gifts are safe"
    else:
        narrator "You lost the time making wrong decisions previously. Some gifts got destroyed"
    return
