# reVerbarius
## intro

reVerbarius is a fun pet project on modification of [Lebedev's verbarius clock](http://store.artlebedev.com/electronics/verbarius/).

Here you can find some scripts, helpful for analysis and generation of verbarius firmware.
The major dependence for all scripts is [the pygame library](http://www.pygame.org/), used for drawing.

The solid description and some demos could be found on [the project's page](http://altsoph.com/projects/reverbarius/).

## firmware analysis script
> tune_format.py

I used it to get some information about the frame format in the firmware file.
Actually, it is just a bitmap viewer with several controlled settings (such as frame width, bit order & etc.).

The only parameter is the filename (with path if necessary) of the firmware file. 
You could obtain some official files from [artlebedev.com](http://www.artlebedev.com/everything/verbarius/languages/).

## firmware generation scripts

All scripts in this section organised in the same way: they use pygame library to generate the set of frames and pack them into the valid verbarius firmware.

* build_analogue_clock.py -- builds the analogue-like clock firmware.
* build_cities_clock.py -- builds the ["3 cities" analogue clock](https://raw.githubusercontent.com/altsoph/reVerbarius/master/pics/rvAn3.jpg) firmware.
* build_led_clock.py -- compiles digital ['LED'-styled](https://raw.githubusercontent.com/altsoph/reVerbarius/master/pics/rvDig.jpg) clock firmware. Requires [Digit.TTF](http://www.dafont.com/digit.font) font by paldave.
* build_bcd_clock.py -- for [binary coded decimal clock](http://en.wikipedia.org/wiki/Binary_clock#Binary-coded_decimal_clocks) firmware generation.
* build_babylon_clock.py -- for generation of the babylonian numerals clock firmware. I used [the wikipedia's image](http://en.wikipedia.org/wiki/Babylonian_numerals) of the babylonian numerals for [the custom font image](https://raw.githubusercontent.com/altsoph/reVerbarius/master/babylon_font.png).

