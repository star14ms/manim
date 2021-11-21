from manimlib import *

class _01_WriteText(Scene): 
    def construct(self): 
        text = Text("This is a regular text")
        self.play(Write(text))
        self.wait(3)

class _02_AddText(Scene): 
    def construct(self): 
        text = Text("This is a regular text")
        self.add(text)
        self.wait(3)

class _03_Formula(Scene): 
    def construct(self): 
        formula = Tex("This is a formula")
        self.play(Write(formula))
        self.wait(3)

class _04_TypesOfText(Scene): 
    def construct(self): 
        tipesOfText = Text("""
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class _05_TypesOfText2(Scene): 
    def construct(self): 
        tipesOfText = Text("""
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class _06_DisplayFormula(Scene): 
    def construct(self): 
        tipesOfText = Text("""
            This is a regular text,
            $\\displaystyle\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class _07_TextInCenter(Scene):
    def construct(self):
        text = Text("Text")
        self.play(Write(text))
        self.wait(3)

class _08_TextOnTopEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(3)

class _09_TextOnBottomEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(3)

class _10_TextOnRightEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(RIGHT)
        self.play(Write(text))
        self.wait(3)

class _11_TextOnLeftEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(LEFT)
        self.play(Write(text))
        self.wait(3)

class _12_TextInUpperRightCorner(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)

class _13_TextInLowerLeftCorner(Scene): 
    def construct(self): 
        text = Text("Text") 
        text.to_edge(LEFT+DOWN)
        self.play(Write(text))
        self.wait(3)

class _14_CustomPosition1(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(0.25*UP) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class _15_CustomPosition2(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)

class _16_RelativePosition1(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class _17_RelativePosition2(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

class _18_RotateObject(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)

class _19_FlipObject(Scene):
    def construct(self):
        textM = Text("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

class _20_SizeTextOnLaTeX(Scene):
    def construct(self):
        textHuge = Text("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = Text("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = Text("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = Text("{\\Large Large Text 012.\\#!?} Text")
        textlarge = Text("{\\large large Text 012.\\#!?} Text")
        textNormal = Text("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = Text("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = Text("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = Text("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = Text("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)

class _21_TextFonts(Scene):
    def construct(self):
        textNormal = Text("{Roman serif text 012.\\#!?} Text")
        textItalic = Text("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = Text("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = Text("\\textbf{Bold text 012.\\#!?} Text")
        textSL = Text("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = Text("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)
