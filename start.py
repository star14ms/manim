from manimlib import *
import numpy as np
import time as t
from tqdm import tqdm

# class SquareToCircle(Scene):
    # def construct(self):
    #     circle = Circle()
    #     circle.set_fill(BLUE, opacity=0.5)
    #     circle.set_stroke(BLUE_E, width=4)

    #     square = Square()

    #     self.play(ShowCreation(square))
    #     self.wait()
    #     self.play(ReplacementTransform(square, circle))
    #     self.wait()
        
    #     self.embed()


# class GraphExample(Scene):
    # def construct(self):
    #     axes = NumberPlane((-8, 8), (-5, 5), 0)
    #     axes.add_coordinate_labels()
    #     axes.set_stroke(BLUE, 1)

    #     self.play(Write(axes, lag_ratio=0.01, run_time=1))

    #     sin_graph = axes.get_graph(
    #         lambda x: math.sin(x),
    #         color=BLUE,
    #     )
    #     cos_graph = axes.get_graph(
    #         lambda x: math.cos(x),
    #         color=RED,
    #     )
    #     relu_graph = axes.get_graph(
    #         lambda x: max(x, 0),
    #         use_smoothing=False,
    #         color=YELLOW,
    #     )
    #     step_graph = axes.get_graph(
    #         lambda x: 1.0 if x > 0 else 0.0,
    #         discontinuities=[0],
    #         color=GREEN,
    #     )
    #     sigmoid_graph = axes.get_graph(
    #         lambda x: 1 / (1 + np.exp(-x)),
    #         color=TEAL,
    #     )
    #     tanh_graph = axes.get_graph(
    #         lambda x: np.tanh(x),
    #         color=PURPLE,
    #     )

    #     sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
    #     cos_label = axes.get_graph_label(cos_graph, "\\cos(x)")
    #     relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
    #     step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)
    #     sigmoid_label = axes.get_graph_label(sigmoid_graph, Text("sigmoid(x)"), x=4)
    #     tanh_label = axes.get_graph_label(tanh_graph, Text("tanh(x)"), x=4)
        
    #     self.play(
    #         ShowCreation(sin_graph),
    #         FadeIn(sin_label, RIGHT),
    #     )
    #     self.wait()
        
    #     # labels = [sin_label, cos_label, relu_label, step_label, sigmoid_label, tanh_label]
    #     # graphs = [sin_graph, cos_graph, relu_graph, step_graph, sigmoid_graph, tanh_graph]
    #     labels = [sin_label, tanh_label]
    #     graphs = [sin_graph, tanh_graph]
    #     for i in range(len(labels)-1):
    #         self.play(
    #             ReplacementTransform(labels[i], labels[i+1]),
    #             FadeTransform(graphs[i], graphs[i+1]),
    #         )
    #         self.wait()

    #     # parabola = axes.get_graph(lambda x: 0.25 * x**2)
    #     parabola = axes.get_graph(lambda x: np.exp(x))
    #     exp_label = axes.get_graph_label(sigmoid_graph, Tex("e^x", font_size=100), x=1.5, direction=LEFT)
        
    #     times = 10
    #     ar = times*8
    #     axes_range = (-ar, ar), (-ar//2, ar//2)
    #     axes2 = NumberPlane(*axes_range, 0)
    #     labels = [n if abs(n)%times==0 else 0 for n in range(*axes_range[0])]
    #     axes2.add_coordinate_labels(labels, labels, font_size=24*times)
    #     self.play(
    #         FadeOut(tanh_graph),
    #         FadeOut(tanh_label),
    #         ShowCreation(parabola),
    #         FadeIn(exp_label),
    #         run_time=1
    #     )

    #     dot = Dot(color=RED)
    #     dot.move_to(axes.i2gp(2, parabola))
    #     self.play(FadeIn(dot, scale=0.5))
        
    #     x_tracker = ValueTracker(1)
    #     f_always(
    #         dot.move_to,
    #         lambda: axes.i2gp(x_tracker.get_value(), parabola)
    #     )

    #     self.play(x_tracker.animate.set_value(0), run_time=1)
    #     self.play(x_tracker.animate.set_value(-2), run_time=1)
    
    #     self.play(FadeOut(dot), FadeOut(axes), FadeIn(axes2), run_time=0.5)
    #     self.play(
    #         axes2.animate.apply_function(lambda z: z/times),
    #         parabola.animate.apply_function(lambda z: z/times), 
    #         run_time=3
    #     )


# class CoordinatePlane(Scene):
    # def construct(self):
        # intro_words = Text("""
        #     The original motivation for manim was to
        #     better illustrate mathematical functions
        #     as transformations.
        # """)
        # intro_words.to_edge(UP)

        # self.play(Write(intro_words))
        # self.wait(2)

        # # Linear transform
        # grid = NumberPlane((-10, 10), (-5, 5))
        # matrix = [[0, 0], [0, 1]]
        # linear_transform_words = VGroup(
        #     Text("This is what the matrix"),
        #     IntegerMatrix(matrix, include_background_rectangle=True),
        #     Text("looks like")
        # )
        # linear_transform_words.arrange(RIGHT)
        # linear_transform_words.to_edge(UP)
        # linear_transform_words.set_stroke(BLACK, 10, background=True)

        # self.play(
        #     ShowCreation(grid),
        #     FadeTransform(intro_words, linear_transform_words)
        # )
        # self.wait()
        # self.play(grid.animate.apply_matrix(matrix), run_time=3)
        # # self.play(grid.animate.apply_function(lambda z: z+1), run_time=3)
        # self.wait()

        # # Complex map
        # c_grid = ComplexPlane((-15, 15), (-15, 15))
        # moving_c_grid = c_grid.copy()
        # moving_c_grid.prepare_for_nonlinear_transform()
        # c_grid.set_stroke(BLUE_E, 1)
        # c_grid.add_coordinate_labels(font_size=24)
        # complex_map_words = TexText("""
        #     Or thinking of the plane as $\\mathds{C}$,\\\\
        #     this is the map $z \\rightarrow z^2$
        # """)
        # complex_map_words.to_corner(UR)
        # complex_map_words.set_stroke(BLACK, 5, background=True)

        # self.play(
        #     FadeOut(grid),
        #     Write(c_grid, run_time=3),
        #     FadeIn(moving_c_grid),
        #     FadeTransform(linear_transform_words, complex_map_words),
        # )
        # for _ in range(4):
        #     self.wait()
        #     self.play(
        #         moving_c_grid.animate.apply_complex_function(lambda z: z*1j),
        #         run_time=2,
        #     )
        # self.wait()
        # self.play(
        #     moving_c_grid.animate.apply_complex_function(lambda z: z**2),
        #     run_time=6,
        # )
        # self.wait(2)
    
    
# class TexTransformExample(Scene):
    # def construct(self):
        # to_isolate = ["B", "C", "=", "(", ")"]
        # lines = VGroup(
        #     # Passing in muliple arguments to Tex will result
        #     # in the same expression as if those arguments had
        #     # been joined together, except that the submobject
        #     # hierarchy of the resulting mobject ensure that the
        #     # Tex mobject has a subject corresponding to
        #     # each of these strings.  For example, the Tex mobject
        #     # below will have 5 subjects, corresponding to the
        #     # expressions [A^2, +, B^2, =, C^2]
        #     Tex("A^2", "+", "B^2", "=", "C^2"),
        #     # Likewise here
        #     Tex("A^2", "=", "C^2", "-", "B^2"),
        #     # Alternatively, you can pass in the keyword argument
        #     # "isolate" with a list of strings that should be out as
        #     # their own submobject.  So the line below is equivalent
        #     # to the commented out line below it.
        #     Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
        #     # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
        #     Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        # )
        # lines.arrange(DOWN, buff=LARGE_BUFF)
        # for line in lines:
        #     line.set_color_by_tex_to_color_map({
        #         "A": BLUE,
        #         "B": TEAL,
        #         "C": GREEN,
        #     })

        # play_kw = {"run_time": 2}
        # self.add(lines[0])
        # # The animation TransformMatchingTex will line up parts
        # # of the source and target which have matching tex strings.
        # # Here, giving it a little path_arc makes each part sort of
        # # rotate into their final positions, which feels appropriate
        # # for the idea of rearranging an equation
        # self.play(
        #     TransformMatchingTex(
        #         lines[0].copy(), lines[1],
        #         path_arc=90 * DEGREES,
        #     ),
        #     **play_kw
        # )
        # self.wait()

        # # Now, we could try this again on the next line...
        # self.play(
        #     TransformMatchingTex(lines[1].copy(), lines[2]),
        #     **play_kw
        # )
        # self.wait()
        
        # # ...and this looks nice enough, but since there's no tex
        # # in lines[2] which matches "C^2" or "B^2", those terms fade
        # # out to nothing while the C and B terms fade in from nothing.
        # # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # # we can specify that with a key map.
        # self.play(FadeOut(lines[2]))
        # self.play(
        #     TransformMatchingTex(
        #         lines[1].copy(), lines[2],
        #         key_map={
        #             "C^2": "C",
        #             "B^2": "B",
        #         }
        #     ),
        #     **play_kw
        # )
        # self.wait()

        # # And to finish off, a simple TransformMatchingShapes would work
        # # just fine.  But perhaps we want that exponent on A^2 to transform into
        # # the square root symbol.  At the moment, lines[2] treats the expression
        # # A^2 as a unit, so we might create a new version of the same line which
        # # separates out just the A.  This way, when TransformMatchingTex lines up
        # # all matching parts, the only mismatch will be between the "^2" from
        # # new_line2 and the "\sqrt" from the final line.  By passing in,
        # # transform_mismatches=True, it will transform this "^2" part into
        # # the "\sqrt" part.
        # new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        # new_line2.replace(lines[2])
        # new_line2.match_style(lines[2])

        # self.play(
        #     TransformMatchingTex(
        #         new_line2, lines[3],
        #         transform_mismatches=True,
        #     ),
        #     **play_kw
        # )
        # self.wait(3)
        # self.play(FadeOut(lines, RIGHT))

        # # Alternatively, if you don't want to think about breaking up
        # # the tex strings deliberately, you can TransformMatchingShapes,
        # # which will try to line up all pieces of a source mobject with
        # # those of a target, regardless of the submobject hierarchy in
        # # each one, according to whether those pieces have the same
        # # shape (as best it can).
        # source = Text("the morse code", height=1)
        # target = Text("here come dots", height=1)

        # self.play(Write(source))
        # self.wait()
        # kw = {"run_time": 3, "path_arc": PI / 2}
        # self.play(TransformMatchingShapes(source, target, **kw))
        # self.wait()
        # self.play(TransformMatchingShapes(target, source, **kw))
        # self.wait()
        
        
# class Positions(Scene):
    # def construct(self):
        # plane = NumberPlane(faded_line_ratio=0)
        # self.play(Write(plane, lag_ratio=0.01, run_time=1))
        
        # dot = Dot()
        # self.play(FadeIn(dot))
        # self.wait()
        
        # self.play(dot.animate.move_to(np.array([1, 2, 0])))
        # self.wait()
        
        # self.play(
        #     dot.animate.apply_complex_function(lambda x: x*1j),
        #     plane.animate.apply_complex_function(lambda x: x*1j),
        #     run_time=2,
        # )
        # self.play(dot.animate.move_to(np.array([1, 0, 0])))
        
        # value = PI / 2
        # radius = 1
        # arc = Arc(0, value, radius=radius, color=BLUE)
        # x_tracker = ValueTracker(radius)
        # f_always(
        #     dot.move_to,
        #     lambda: plane.i2gp(min(radius, x_tracker.get_value()), arc)
        # )
        # f_always(
        #     plane.rotate,
        #     lambda: 1-min(radius, x_tracker.get_value())
        # )
        # self.play(
        #     ShowCreation(arc),
        #     x_tracker.animate.set_value(value),
        # )


# class Plane_Transform(Scene):
    # def construct(self):
        # ar = 15 # 사용할 소수 범위
        # axes_range = (-ar, ar), (-ar//2, ar//2)
        # zoom_out = lambda x: x/4
        # x_square = lambda x: x**2

        # background_line_style = {
        #     "stroke_color": BLUE_D,
        #     "stroke_width": 2,
        #     "stroke_opacity": 1,
        # }
        
        # # plane = NumberPlane(*axes_range, 
        # #     background_line_style=background_line_style, faded_line_ratio=0)
        # plane = ComplexPlane()
        # plane.prepare_for_nonlinear_transform()
        # self.play(Write(plane, lag_ratio=0.01, run_time=1))
        
        # # labels = [n if abs(n)%100==0 or abs(n) in range(-10,11) else 0 for n in range(*axes_range[0])]
        # # plane.add_coordinate_labels(labels, labels, font_size=100)
        # self.play(plane.animate.apply_function(zoom_out), run_time=1)
        # self.play(plane.animate.apply_complex_function(x_square), run_time=10)
        
        
class Equations(Scene):
    def construct(self):
        font = 'BM JUA_TTF'
        
        to_isolate = ['a','b','c','\\sqrt','\\pm','\\over ','^2','+','-','=','x']
        kw = {"isolate": [*to_isolate], "font_size": 80}
        # lines = VGroup(
        #     # Text("일차방정식 (Linear Equation)", font=font),
        #     Tex("ax + b = 0", **kw),
        #     Tex("ax = b", **kw),
        #     Tex("x = {b \\over a}", **kw),
        # )
        lines = VGroup(
            Tex('ax^2+bx+c=0', **kw),
            Tex('ax^2+bx=-c', **kw),
            # Tex('x^2+{b\\over a}x=-{c\\over a}', **kw),
            # Tex('x^2+{b\\over a}x+\\left({b\\over 2a}\\right)^2=-{c\\over a}+\\left({b\\over 2a}\\right)^2', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2=-{c\\over a}+\\left({b\\over 2a}\\right)^2', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2=-{c\\over a}+{b^2\\over 4a^2}', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2={b^2\\over 4a^2}-{c\\over a}', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2={b^2\\over 4a^2}-{4c\\over 4a}', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2={b^2\\over 4a^2}-{4ac\\over 4a^2}', **kw),
            # Tex('\\left(x+{b\\over 2a}\\right)^2={b^2-4ac\\over 4a^2}', **kw),
            # Tex('\\sqrt{\\left(x+{b\\over 2a}\\right)^2}=\\pm\\sqrt{{b^2-4ac\\over 4a^2}}', **kw),  
            # Tex('x+{b\\over 2a}=\\pm\\sqrt{{b^2-4ac\\over 4a^2}}', **kw),
            # Tex('x=-{b\\over 2a}\\pm\\sqrt{{b^2-4ac\\over 4a^2}}', **kw),
            # Tex('x=-{b\\over 2a}\\pm{\\sqrt{b^2-4ac}\\over 2a}', **kw),
            # Tex('x={-b\\pm\\sqrt{b^2-4ac}\\over 2a}', **kw),
        )
        key_maps = [
            {'+':'-'},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
            # {},
        ]
        for line in lines:
            line.set_color_by_tex_to_color_map({
            "a": BLUE,
            "b": TEAL,
            "c": GREEN,
        })
        play_kw = {"run_time": 10}
        self.play(FadeIn(lines[0]))
        
        for i in range(len(lines)-1):
            self.play(
                    TransformMatchingTex(
                        lines[i], lines[i+1],
                        transform_mismatches=True,
                        key_map=key_maps[i],
                    ),
                    **play_kw
                )


            
