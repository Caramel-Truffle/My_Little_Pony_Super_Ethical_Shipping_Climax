init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    g.locked_button = "Numbers/locked.png"

    # These buttons have multiple images associated with them. We use unlock_image
    # so we don't have to call both .image and .unlock.
    

    g.button("ending01")
    g.unlock_image("end01")

    g.button("ending02")
    g.unlock_image("end02")

    g.button("ending03")
    g.unlock_image("end03")

    g.button("ending04")
    g.unlock_image("end04")

    g.button("ending05")
    g.unlock_image("end05")

    g.button("ending06")
    g.unlock_image("end06")

    g.button("ending07")
    g.unlock_image("end07")

    g.button("ending08")
    g.unlock_image("end08")

    g.button("ending09")
    g.unlock_image("end09")

    g.button("ending10")
    g.unlock_image("end10")

    g.button("ending11")
    g.unlock_image("end11")

    g.button("ending12")
    g.unlock_image("end12")

    g.button("ending13")
    g.unlock_image("end13")

    g.button("ending14")
    g.unlock_image("end14")

    g.button("ending15")
    g.unlock_image("end15")

    g.button("ending16")
    g.unlock_image("end16")

    g.button("ending17")
    g.unlock_image("end17")

    g.button("ending18")
    g.unlock_image("end18")

    g.button("ending19")
    g.unlock_image("end19")

    g.button("ending20")
    g.unlock_image("end20")

    g.button("ending21")
    g.unlock_image("end21")

    g.button("ending22")
    g.unlock_image("end22")

    g.button("ending23")
    g.unlock_image("end23")

    g.button("ending24")
    g.unlock_image("end24")

    g.button("ending25")
    g.unlock_image("end25")

    g.button("ending26")
    g.unlock_image("end26")

    g.button("ending27")
    g.unlock_image("end27")

    g.button("ending28")
    g.unlock_image("end28")

    g.button("ending29")
    g.unlock_image("end29")

    g.button("ending30")
    g.unlock_image("end30")

    g.button("ending31")
    g.unlock_image("end31")

    g.button("ending32")
    g.unlock_image("end32")

    g.button("ending33")
    g.unlock_image("end33")

    g.button("ending34")
    g.unlock_image("end34")

    g.button("ending35")
    g.unlock_image("end35")

    g.button("ending36")
    g.unlock_image("end36")

    g.button("ending37")
    g.unlock_image("end37")

    g.button("ending38")
    g.unlock_image("end38")

    g.button("ending39")
    g.unlock_image("end39")

    g.button("ending40")
    g.unlock_image("end40")

    g.button("ending41")
    g.unlock_image("end41")

    g.button("ending42")
    g.unlock_image("end42")

    g.button("ending43")
    g.unlock_image("end43")

    g.button("ending44")
    g.unlock_image("end44")

    g.button("ending45")
    g.unlock_image("end45")

    g.button("ending46")
    g.unlock_image("end46")

    g.button("ending47")
    g.unlock_image("end47")

    g.button("ending48")
    g.unlock_image("end48")

    g.button("ending49")
    g.unlock_image("end49")

    g.button("ending50")
    g.unlock_image("end50")

    g.button("ending51")
    g.unlock_image("end51")

    g.button("ending52")
    g.unlock_image("end52")

    g.button("ending53")
    g.unlock_image("end53")

    g.button("ending54")
    g.unlock_image("end54")

    g.button("ending55")
    g.unlock_image("end55")

    g.button("ending56")
    g.unlock_image("end56")

    g.button("ending57")
    g.unlock_image("end57")

    g.button("ending58")
    g.unlock_image("end58")

    g.button("ending59")
    g.unlock_image("end59")

    g.button("ending60")
    g.unlock_image("end60")

    g.button("ending61")
    g.unlock_image("end61")

    g.button("ending62")
    g.unlock_image("end62")

    g.button("ending63")
    g.unlock_image("end63")

    g.button("ending64")
    g.unlock_image("end64")

    g.button("ending65")
    g.unlock_image("end65")

    g.button("ending66")
    g.unlock_image("end66")

    g.button("ending67")
    g.unlock_image("end67")

    g.button("ending68")
    g.unlock_image("end68")

    g.button("ending69")
    g.unlock_image("end69")

    g.button("ending70")
    g.unlock_image("end70")

    g.button("ending71")
    g.unlock_image("end71")

    g.button("ending72")
    g.unlock_image("end72")

    g.button("ending73")
    g.unlock_image("end73")

    g.button("ending74")
    g.unlock_image("end74")

    g.button("ending75")
    g.unlock_image("end75")

    g.button("ending76")
    g.unlock_image("end76")

    g.button("ending77")
    g.unlock_image("end77")

    g.button("ending78")
    g.unlock_image("end78")

    g.button("ending79")
    g.unlock_image("end79")

    g.button("ending80")
    g.unlock_image("end80")

    g.button("ending81")
    g.unlock_image("end81")

    g.button("ending82")
    g.unlock_image("end82")

    g.button("ending83")
    g.unlock_image("end83")

    g.button("ending84")
    g.unlock_image("end84")
    
    g.button("ending85")
    g.unlock_image("end85")
    g.button("ending86")
    g.unlock_image("end86")
    g.button("ending87")
    g.unlock_image("end87")

    # The transition used when switching images.
    g.transition = dissolve
    
# Step 3. The gallery screen we use.
screen gallery():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "Images/bushes_hill.png"

    # A grid of buttons.
    grid 11 8:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        
        add g.make_button("ending01", "Numbers/01_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending02", "Numbers/02_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending03", "Numbers/03_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending04", "Numbers/04_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending05", "Numbers/05_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending06", "Numbers/06_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending07", "Numbers/07_2.png", xalign=0.5, yalign=0.5) 
        add g.make_button("ending08", "Numbers/08_2.png", xalign=0.5, yalign=0.5)              
        add g.make_button("ending09", "Numbers/09_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending10", "Numbers/10_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending11", "Numbers/11_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending12", "Numbers/12_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending13", "Numbers/13_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending14", "Numbers/14_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending15", "Numbers/15_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending16", "Numbers/16_2.png", xalign=0.5, yalign=0.5)       
        add g.make_button("ending17", "Numbers/17_2.png", xalign=0.5, yalign=0.5)       
        add g.make_button("ending18", "Numbers/18_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending19", "Numbers/19_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending20", "Numbers/20_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending21", "Numbers/21_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending22", "Numbers/22_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending23", "Numbers/23_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending24", "Numbers/24_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending25", "Numbers/25_2.png", xalign=0.5, yalign=0.5)       
        add g.make_button("ending26", "Numbers/26_2.png", xalign=0.5, yalign=0.5)        
        add g.make_button("ending27", "Numbers/27_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending28", "Numbers/28_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending29", "Numbers/29_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending30", "Numbers/30_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending31", "Numbers/31_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending32", "Numbers/32_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending33", "Numbers/33_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending34", "Numbers/34_2.png", xalign=0.5, yalign=0.5)       
        add g.make_button("ending35", "Numbers/35_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending36", "Numbers/36_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending37", "Numbers/37_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending38", "Numbers/38_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending39", "Numbers/39_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending40", "Numbers/40_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending41", "Numbers/41_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending42", "Numbers/42_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending43", "Numbers/43_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending44", "Numbers/44_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending45", "Numbers/45_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending46", "Numbers/46_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending47", "Numbers/47_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending48", "Numbers/48_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending49", "Numbers/49_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending50", "Numbers/50_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending51", "Numbers/51_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending52", "Numbers/52_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending53", "Numbers/53_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending54", "Numbers/54_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending55", "Numbers/55_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending56", "Numbers/56_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending57", "Numbers/57_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending58", "Numbers/58_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending59", "Numbers/59_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending60", "Numbers/60_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending61", "Numbers/61_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending62", "Numbers/62_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending63", "Numbers/63_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending64", "Numbers/64_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending65", "Numbers/65_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending66", "Numbers/66_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending67", "Numbers/67_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending68", "Numbers/68_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending69", "Numbers/69_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending70", "Numbers/70_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending71", "Numbers/71_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending72", "Numbers/72_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending73", "Numbers/73_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending74", "Numbers/74_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending75", "Numbers/75_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending76", "Numbers/76_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending77", "Numbers/77_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending78", "Numbers/78_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending79", "Numbers/79_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending80", "Numbers/80_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending81", "Numbers/81_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending82", "Numbers/82_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending83", "Numbers/83_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending84", "Numbers/84_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending85", "Numbers/85_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending86", "Numbers/86_2.png", xalign=0.5, yalign=0.5)
        add g.make_button("ending87", "Numbers/87_2.png", xalign=0.5, yalign=0.5)
         
         
        
        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() xalign 0.5 yalign 0.5