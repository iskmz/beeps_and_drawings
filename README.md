# beeps and drawings

<i> last update: 2024-08-07 , 21:21 local time </i> <br/>
<i> uploaded on September , 2023 </i> <br/>
<i> originally coded on September , 2020 </i><br/>


+ each file is standalone (except the menu files)
+ beepnotes1.py & beepnotes2.py depend on [beeply module](https://pypi.org/project/beeply/)
+ all other files depend on built-in modules (in a windows system)


- - - - -


+ beepbeep.py
    + description:  a demonstration of several beeps/melodies using windows-beep
    + command:      beepbeep [# of item to play]
    + items: (1) monotone ascending (2) monotone descending (3) up and down (x3)  (4) super mario (long)   (5) Fur Elise


+ beepnotes1.py
    + description:  a demonstration of several melodies using 'beeply' module
    + command:      beepnotes1 [# of item to play]
    + items: (1) Mary Had A Little Lamb (2) Twinkle Twinkle Little Star  (3) Rock-a-Bye Baby  (4) Happy Birthday to You  (5) If You're Happy and You Know It  (6) We Wish You A Merry Christmas  (7) Ode to Joy  (8) Amazing Grace  (9) Auld Lang Syne (New Year's Eve)  (10) Imperial March


+ beepnotes2.py
    + description:   a demonstration of several melodies using 'beeply' module
        + this version has improved code, more standardized functions to play melodies with a standard DATA STRUCTURE for all melodies data.  Much less repetitions, more efficient & cleaner code.
        + just compose the melody, set the durations and play it !
    + command:        beepnotes2 [# of item to play]
    + items:  (1) Mary Had A Little Lamb (2) Twinkle Twinkle Little Star  (3) Rock-a-Bye Baby  (4) Happy Birthday to You  (5) If You're Happy and You Know It  (6) We Wish You A Merry Christmas  (7) Ode to Joy  (8) Amazing Grace  (9) Auld Lang Syne (New Year's Eve)  (10) Imperial March  (11) The Godfather Theme


+ draw.py
    + description:   a demonstration of several drawings using built-in turtle module
    + command:        draw [# of item to draw]
    + items:  (1) square  (2) circle  (3) triangle  (4) infinity  (5) spiral in-out  (6) spiral out-in  (7) square-spiral in-out  (8) square-spiral out-in  (9) star (10) star sky (11) hexagon (12) pentagon (13) septagon (14) octagon (15) nested infinity (16) ellipses colorful special (17) spiral of infinity (18) flower (19) cube (20) helix (21) Rainbow Benzene (22) Y Fractal Tree (23) sine wave

- - - - -
<b> update: 2024-08-07 , 21:21 local time </b> <br/>
+ added console menus for [beepnotes2.py](beepnotes2.py) and [draw.py](draw.py) which are respectively named: [beepnotes2__menu.py](beepnotes2__menu.py)  &  [draw__menu](draw__menu.py)
+ these two menus are derived from the repo: [python_generic_console_menu](https://github.com/iskmz/python_generic_console_menu)
+ these two menu files are <b><i> NOT STANDALONE </b></i>, as they depend on the original scripts being in the same folder to work.

<br/>

<img src="https://github.com/user-attachments/assets/19bed6d7-ce77-4cb5-9322-2c7363a42be3"/>
