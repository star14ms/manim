from math import sqrt
from manimlib import *
import numpy as np

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
    #     intro_words = Text("""
    #         The original motivation for manim was to
    #         better illustrate mathematical functions
    #         as transformations.
    #     """)
    #     intro_words.to_edge(UP)

    #     self.play(Write(intro_words))
    #     self.wait(2)

    #     # Linear transform
    #     grid = NumberPlane((-10, 10), (-5, 5))
    #     matrix = [[0, 0], [0, 1]]
    #     linear_transform_words = VGroup(
    #         Text("This is what the matrix"),
    #         IntegerMatrix(matrix, include_background_rectangle=True),
    #         Text("looks like")
    #     )
    #     linear_transform_words.arrange(RIGHT)
    #     linear_transform_words.to_edge(UP)
    #     linear_transform_words.set_stroke(BLACK, 10, background=True)

    #     self.play(
    #         ShowCreation(grid),
    #         FadeTransform(intro_words, linear_transform_words)
    #     )
    #     self.wait()
    #     # self.play(grid.animate.apply_matrix(matrix), run_time=3)
    #     self.play(grid.animate.apply_function(lambda z: z+1), run_time=3)
    #     self.wait()

    #     # Complex map
    #     c_grid = ComplexPlane((-15, 15), (-15, 15))
    #     moving_c_grid = c_grid.copy()
    #     moving_c_grid.prepare_for_nonlinear_transform()
    #     c_grid.set_stroke(BLUE_E, 1)
    #     c_grid.add_coordinate_labels(font_size=24)
    #     complex_map_words = TexText("""
    #         Or thinking of the plane as $\\mathds{C}$,\\\\
    #         this is the map $z \\rightarrow z^2$
    #     """)
    #     complex_map_words.to_corner(UR)
    #     complex_map_words.set_stroke(BLACK, 5, background=True)

    #     self.play(
    #         FadeOut(grid),
    #         Write(c_grid, run_time=3),
    #         FadeIn(moving_c_grid),
    #         FadeTransform(linear_transform_words, complex_map_words),
    #     )
    #     for _ in range(4):
    #         self.wait()
    #         self.play(
    #             moving_c_grid.animate.apply_complex_function(lambda z: z*1j),
    #             run_time=2,
    #         )
    #     self.wait()
    #     self.play(
    #         moving_c_grid.animate.apply_complex_function(lambda z: z**2),
    #         run_time=6,
    #     )
    #     self.wait(2)
    
    
# class TexTransformExample(Scene):
    # def construct(self):
    #     to_isolate = ["B", "C", "=", "(", ")"]
    #     lines = VGroup(
    #         # Passing in muliple arguments to Tex will result
    #         # in the same expression as if those arguments had
    #         # been joined together, except that the submobject
    #         # hierarchy of the resulting mobject ensure that the
    #         # Tex mobject has a subject corresponding to
    #         # each of these strings.  For example, the Tex mobject
    #         # below will have 5 subjects, corresponding to the
    #         # expressions [A^2, +, B^2, =, C^2]
    #         Tex("A^2", "+", "B^2", "=", "C^2"),
    #         # Likewise here
    #         Tex("A^2", "=", "C^2", "-", "B^2"),
    #         # Alternatively, you can pass in the keyword argument
    #         # "isolate" with a list of strings that should be out as
    #         # their own submobject.  So the line below is equivalent
    #         # to the commented out line below it.
    #         Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
    #         # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
    #         Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
    #     )
    #     lines.arrange(DOWN, buff=LARGE_BUFF)
    #     for line in lines:
    #         line.set_color_by_tex_to_color_map({
    #             "A": BLUE,
    #             "B": TEAL,
    #             "C": GREEN,
    #         })

    #     play_kw = {"run_time": 2}
    #     self.add(lines[0])
    #     # The animation TransformMatchingTex will line up parts
    #     # of the source and target which have matching tex strings.
    #     # Here, giving it a little path_arc makes each part sort of
    #     # rotate into their final positions, which feels appropriate
    #     # for the idea of rearranging an equation
    #     self.play(
    #         TransformMatchingTex(
    #             lines[0].copy(), lines[1],
    #             path_arc=90 * DEGREES,
    #         ),
    #         **play_kw
    #     )
    #     self.wait()

    #     # Now, we could try this again on the next line...
    #     self.play(
    #         TransformMatchingTex(lines[1].copy(), lines[2]),
    #         **play_kw
    #     )
    #     self.wait()
        
    #     # ...and this looks nice enough, but since there's no tex
    #     # in lines[2] which matches "C^2" or "B^2", those terms fade
    #     # out to nothing while the C and B terms fade in from nothing.
    #     # If, however, we want the C^2 to go to C, and B^2 to go to B,
    #     # we can specify that with a key map.
    #     self.play(FadeOut(lines[2]))
    #     self.play(
    #         TransformMatchingTex(
    #             lines[1].copy(), lines[2],
    #             key_map={
    #                 "C^2": "C",
    #                 "B^2": "B",
    #             }
    #         ),
    #         **play_kw
    #     )
    #     self.wait()

    #     # And to finish off, a simple TransformMatchingShapes would work
    #     # just fine.  But perhaps we want that exponent on A^2 to transform into
    #     # the square root symbol.  At the moment, lines[2] treats the expression
    #     # A^2 as a unit, so we might create a new version of the same line which
    #     # separates out just the A.  This way, when TransformMatchingTex lines up
    #     # all matching parts, the only mismatch will be between the "^2" from
    #     # new_line2 and the "\sqrt" from the final line.  By passing in,
    #     # transform_mismatches=True, it will transform this "^2" part into
    #     # the "\sqrt" part.
    #     new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
    #     new_line2.replace(lines[2])
    #     new_line2.match_style(lines[2])

    #     self.play(
    #         TransformMatchingTex(
    #             new_line2, lines[3],
    #             transform_mismatches=True,
    #         ),
    #         **play_kw
    #     )
    #     self.wait(3)
    #     self.play(FadeOut(lines, RIGHT))

    #     # Alternatively, if you don't want to think about breaking up
    #     # the tex strings deliberately, you can TransformMatchingShapes,
    #     # which will try to line up all pieces of a source mobject with
    #     # those of a target, regardless of the submobject hierarchy in
    #     # each one, according to whether those pieces have the same
    #     # shape (as best it can).
    #     source = Text("the morse code", height=1)
    #     target = Text("here come dots", height=1)

    #     self.play(Write(source))
    #     self.wait()
    #     kw = {"run_time": 3, "path_arc": PI / 2}
    #     self.play(TransformMatchingShapes(source, target, **kw))
    #     self.wait()
    #     self.play(TransformMatchingShapes(target, source, **kw))
    #     self.wait()
        
        
# class UNDERTALE(Scene):
    # def construct(self):
    #     font = 'Determination Sans'
        
    #     text1 = 'UNDERTALE' # UNDERTALE # undertale
    #     text2 = 'DELTARUNE' # DELTARUNE # deltarune
        
    #     # source = Tex(*[c for c in source_text], font_size=256, font=font)
    #     # target = Tex(*[c for c in target_text], font_size=256, font=font)
        
    #     text_1 = Text(text1, font_size=200, font=font)
    #     text_2 = Text(text2, font_size=200, font=font)
    
    #     self.play(Write(text1))
    #     self.wait()
    #     kw = {"run_time": 2, "path_arc": PI }
    #     for _ in range(2):
    #         self.play(TransformMatchingShapes(text_1, text_2, **kw))
    #         self.wait()
    #         self.play(TransformMatchingShapes(text_2, text_1, **kw))
    #         self.wait()


# class Positions(Scene):
    # def construct(self):
    #     plane = NumberPlane(background_stroke_opacity=0, faded_line_ratio=0)
    #     self.play(Write(plane, lag_ratio=0.01, run_time=1))
        
    #     dot = Dot()
    #     self.play(FadeIn(dot))
    #     self.wait()
        
    #     self.play(dot.animate.move_to(np.array([1, 2, 0])))
    #     self.wait()
        
    #     self.play(
    #         dot.animate.apply_complex_function(lambda x: x*1j),
    #         plane.animate.apply_complex_function(lambda x: x*1j),
    #         run_time=2,
    #     )


# class Primes(Scene):
    # def construct(self):
        # with open('data/1억 중 소수목록.txt') as f:
        #     primes = f.read().split(',')[:-1]
        # primes = list(map(int, primes))
        # print('소수 데이터 가져오기 완료! (소수 개수 %d개)' % len(primes))
        
        # ar = 5000
        # zoom = lambda x: x/500
        # axes_range = (-ar, ar), (-ar//2, ar//2)
        
        # plane = NumberPlane(*axes_range,
        #     background_stroke_opacity=0, faded_line_ratio=0)
        # plane.apply_function(zoom),
        # # labels = [n if abs(n)%10==0 else 0 for n in range(*axes_range[0])]
        # # plane.add_coordinate_labels(labels, labels)
        # self.play(Write(plane, lag_ratio=0.01, run_time=1))
        
        # for n in primes:
        #     if n > ar: break
            
        #     dot = Dot(np.array([n, 0, 0])).rotate(n, about_point=ORIGIN)
        #     dot.apply_function(zoom)
        #     dot = Dot(dot.get_center(), color=BLUE, radius=0.04)
        #     # text = Text(str(n), font_size=18).next_to(dot)
            
        #     self.play(
        #         FadeIn(dot),
        #         # FadeIn(text),
        #         run_time = 1/n
        #     )
        #     print(n)
            

class Primes2(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('data/1억 중 소수목록.txt') as f:
            primes = f.read().split(',')[:-1]
        self.primes = list(map(int, primes))
        print('소수 데이터 가져오기 완료! (소수 개수 %d개)' % len(primes))
    
    def construct(self):
        ar = 100*8 # 사용할 소수 범위
        axes_range = (-ar, ar), (-ar//2, ar//2)
        zoom1 = lambda x: x/10
        zoom2 = lambda x: x/10
        
        background_line_style = {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 0,
        }
        
        # 좌표평면 그리기
        plane = NumberPlane(faded_line_ratio=0)
        self.play(Write(plane, lag_ratio=0.01, run_time=1))
        plane.add_coordinate_labels()
        
        dots0 = []
        for i in range(1, 5):
            vector = Vector(X_AXIS*i)
            arc = Arc(0, i, radius=i, color=BLUE)
            dots0.append(Dot(X_AXIS*i, color=BLUE).rotate_about_origin(i, axis=Z_AXIS))
            text = Text(f"(r={i}, rad={i})").next_to(dots0[-1], direction=UR)

            self.play(ShowCreation(vector))
            self.play(ShowCreation(arc),
                      vector.animate.rotate_about_origin(i, axis=Z_AXIS))
            self.play(FadeIn(dots0[-1]), FadeIn(text))
            self.wait()
            self.play(FadeOut(arc), FadeOut(text), FadeOut(vector))
        return 
            
        plane2 = NumberPlane(*axes_range,
            background_line_style=background_line_style, faded_line_ratio=0)
        self.play(FadeOut(plane), FadeIn(plane2))
        
        zoom_dots = [dot.animate.apply_function(zoom1) for dot in dots0]
        self.play(plane2.animate.apply_function(zoom1), *zoom_dots)
        self.wait()
        
        # 점 추가하기
        dots_primes = []
        dots_no_primes = []
        dots_primes_zoom2 = []
        texts_primes = []
        texts_no_primes = []
        for n in range(1, ar+1):
            dot = Dot(np.array([n, 0, 0])).rotate(n, about_point=ORIGIN)
            dot.apply_function(zoom1)
            
            (dots, texts) = (dots_primes, texts_primes) if n in self.primes else (dots_no_primes, texts_no_primes)

            if n in self.primes:
                dots.append(Dot(dot.get_center(), color=BLUE, radius=0.02))
                dot_zoom2 = Dot(dots[-1].get_center())
                dot_zoom2.apply_function(zoom2)
                dots_primes_zoom2.append(dot_zoom2)
                print('\r', n)
            elif n < 100:
                dots.append(Dot(dot.get_center(), color=BLUE, radius=0.02))
            
            if n < 100:
                texts.append(Text(str(n), font_size=18).next_to(dots[-1], direction=UP, buff=0.1))
                self.play(
                    FadeIn(dots[-1]),
                    FadeIn(texts[-1]),
                    run_time = 1/n
                )
        
        # 화면 안의 소수 아닌 수들 사라지기
        fadeOut_dots = [FadeOut(dot) for dot in dots_no_primes[:100]]
        FadeOut_dots0 = [FadeOut(dot) for dot in dots0]
        fadeOut_texts = [FadeOut(text) for text in texts_no_primes]
        text = Text('소수만 남기기', font='BM JUA_TTF').to_corner(UR)
        self.play(Write(text))
        self.play(*fadeOut_dots, *fadeOut_texts, *FadeOut_dots0, run_time=3)
        
        # 화면 안의 소수 숫자만 사라지기, 화면 밖의 나머지 소수들 모두 나타나기
        fadeOut_texts = [FadeOut(text) for text in texts_primes]
        fadeIn_dots = [FadeIn(dot) for dot in dots_primes[100:]]
        self.play(*fadeOut_texts, *fadeIn_dots, FadeOut(text), run_time=3)
        
        # 화면 축소하기
        move_dots = [dot.animate.move_to(zdot.get_center()) for dot, zdot in zip(dots_primes, dots_primes_zoom2)]
        self.play(*move_dots, plane2.animate.apply_function(zoom2), run_time=3)
        self.wait()


        