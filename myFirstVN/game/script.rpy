# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('하은', color="#c8ffc8")
define i = Character('민준', color="#f6560c")
define flash = Fade(0.1, 0.0, 0.5, color = "#fff")
define p = Character("[name]", color="#1157d9")



default love = 0 #변하는 값을 만들기 위한 값 love = 0 -> 10 20 30 40 50 60 70 80
default name = "주인공"
default successKey = False  #false 거짓 true 참
default items =[]  #빈 가방 

default menuset = set()


screen love_bar():
    text "♥" * love xalign 0.9 yalign 0.03 size 40 color "#f6560c"
    text "호감도 [love]"

label desk : 
    "서랍안에 낡은 열쇠가 있다."
   
    
    jump room

label window : 
    "창문에는 열쇠가 없다."
    jump room

label door : 
    if successKey == False:
        "현재 문이 잠겨 있다."
        jump room
    
    if "열쇠" in items:
        "열쇠로 문을 열었다."
        $items.remove("열쇠")
        jump hallWay

label room :
    menu : 
        set menuset
        "어디서 부터 살펴볼까?"
        "책상 서랍을 열어본다":
            jump desk

        "창문을 살펴본다":
            jump window

        "문을 연다":
            jump door
    
    "더이상 살펼볼 곳이 없다!!"

label morning : 
    "현재 아침이 밝았다. "

    return 

# 여기에서부터 게임이 시작합니다.
label start:
    show screen love_bar
    $name = renpy.input("너의 이름은 뭐야? 소개해줘")
    $name = name.strip()



    p"내 이름은 [name]"

    play music "audio/bgm_calm.mp3" fadein 1.0
    queue music "audio/bgm_tense.mp3"

    scene bg bg_past_park with pixellate #vpunch, hpunch , wipeleft, wiperight, pixellate
    "{color=#f6560c}오늘은 2026년 9월 18일 입니다.{/color}" #내레이션...
    stop music fadeout 1.0

    call morning


    play sound "audio/sfx_door.mp3"
    show ha sss at left with zoomin
    e "안녕 내이름은{p}하은이야"     #대사 
    show ha haeun_happy at right with move
    show ha haeun_neutral with dissolve
    e "왼쪽에서 오른쪽으로 움직였어!!!"     #대사 

    play music "audio/bgm_tense.mp3"
    play sound "audio/sfx_rain.mp3" loop
    scene black with fade
    
    if love >= 1:
        show ha haeun_happy
        e "오늘 널 만나서 반가워!"
        hide ha haeun_happy
    
    else :
        show ha haeun_neutral
        e "처음봐서 반갑"
        hide ha haeun_neutral

   
    jump room

label classRoom :
    scene bg classroom_day with wipeleft
    e "우리는 교실로 이동했어!!"

    return
label hallWay:
    scene bg hallway_day with fade
    i "우리는 복도로 이동했어!!"

    return
label library:
    scene bg library_evening with vpunch
    
    e "우리는 도서관으로 이동했어!!"
    return

