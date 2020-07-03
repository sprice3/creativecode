!pip install weasyprint
!pip install tracery

import tracery
from tracery.modifiers import base_english
import markdown
import random
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

rules = {
    "chapter_title": ["All Is Lost", "Found", "Killer", "Help", "Confused", "Where To Turn Next?", "Finally","What's Going On", "The Truth", "It's Finished", "Going In Circles","Stop","In Your Dreams","Murder","We're Ready","Give Up","Stay Alive","What Happened?","Victim","Suffer","Him"],
    "sentence":[
                "I couldn't beleive what I had done! ",
                "He walked away as if he didn't have a care in the world. ",
                "She had been missing for over 2 weeks and my hope was draining. ",
                "I finally figured out who had killed her, but it was too late. ",
                "Before I could turn him in, he struck his next victim. ",
                "I tried to move on and forget what happened, but it wasn't that simple. ",
                "I vowed to never give up till I found the man who killed her. ",
                "My friends and I came together to try and solve this murder, once and for all. ",
                "Before I knew what was happening, I was alone. ",
                "He clearly wanted to go. ",
                "I wanted you to be the first to know. ",
                "Hunger is our bodies' way of driving us to find food and eat to stay alive. ",
                "Don't be angry, it won't help you. ",
                "I want you to suffer. ",
                "She fell, and there was nothing we could do about it. ",
                "It won't be easy. "
                "Don't worry, it won't happen again! ",
                "I just saw him! ",
                "We had better figured out what is going on. ",
                "She's missing and it's like you don't even care! ",
                "If you aren't going to help, you should leave. ",
                "Get out!! ",
                "He is going to hurt someone else if we don't stop him! ",
                "I'll give you want you want! ",
                "Turn around and open your eyes. ",
                "The answer was right in front of me the whole time! ",
                "I'm nothing like him, I am trying to help. ",
                "I would do anything to have her back! ",
                "Tell me what I need to do to stop him! "
    ],
    "paragraph":[
                "#sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n",
                "#sentence##sentence##sentence##sentence##sentence##sentence##sentence#\n\n"
    ],
    "chapter":[
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#"
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#",
               "#paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph##paragraph#"
    ],
     "origin":"""
      
\# All Is Lost

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter# 

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter# 

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter# 

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter# 

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#

\#\# #chapter_title#

#chapter#


    """
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

novel = grammar.flatten("#origin#")
