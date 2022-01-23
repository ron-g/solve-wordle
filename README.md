# solve-wordle
Solve Wordle

Using the dictionary included with Ubuntu 20, I removed punctuation, wrapped to lower case, and kept only five letter words.

I then performed a character analysis for most to least common occurring characters at positions one through five. These are included in the PY script as variables p*X*_precedence.

There're five arguments to the script, *--p1* through *--p5*. They take unbracketed RegEx character(s), character sets/ranges, and negated character sets/ranges.

    $ ./solve_wordle.py -h
    usage: solve_wordle.py [-h] [--p1 P1] [--p2 P2] [--p3 P3]
                           [--p4 P4] [--p5 P5]

    Suggest words for wordle. pX can be a single char, char class/range, or negated char class/range.

    optional arguments:
      -h, --help  show this help message and exit
      --p1 P1     Position 1 character set.
      --p2 P2     Position 2 character set.
      --p3 P3     Position 3 character set.
      --p4 P4     Position 4 character set.
      --p5 P5     Position 5 character set.

Example

    $ ./solve_wordle.py \
      --p1 '^a-vx-z' \
      --p2 'ao' \
      --p3 'rstln' \
      --p4 '^a-ce-ln-z' \
      --p5 s

    -=-=-=-=-=-=-=-=-=-= GUESSES =-=-=-=-=-=-=-=-=-=-
    words
    worms
    wards
    warms
    walds
    wands
    -=-=-=-=-=-=-=-=-=-=-=-= =-=-=-=-=-=-=-=-=-=-=-=-

