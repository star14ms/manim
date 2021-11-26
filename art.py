from manimlib import *
import numpy as np
import time as t
from tqdm import tqdm


class UNDERTALE(Scene):
    def construct(self):
        font = 'Comic Sans MS'
        
        text1 = 'UNDERTALE' # UNDERTALE # undertale
        text2 = 'DELTARUNE' # DELTARUNE # deltarune
        
        # source = Tex(*[c for c in source_text], font_size=256, font=font)
        # target = Tex(*[c for c in target_text], font_size=256, font=font)
        
        text_1 = Text(text1, font_size=160, font=font)
        text_2 = Text(text2, font_size=160, font=font)
    
        self.play(Write(text_1))
        self.wait()
        kw = {"run_time": 2, "path_arc": PI }
        for n in range(1, 9):
            self.play(TransformMatchingShapes(text_1, text_2, **kw), run_time=0.4+1/n)
            self.play(TransformMatchingShapes(text_2, text_1, **kw), run_time=0.4+1/n)


class Primes(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start = t.time()
        with open('data/1억 중 소수목록.txt') as f:
            primes = f.read().split(',')[:-1]
        self.primes = list(map(int, primes))
        print('소수 데이터 가져오기 완료! (소수 개수 %d개)' % len(primes))

        self.bgl_style = {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 0,
        }

    def construct(self):
        ar = 125*8.2 # 사용할 소수 범위
        zoom1 = lambda x: x/10
        zoom2 = lambda x: x/125
        zoom3 = lambda x: x/100
        
        # 좌표평면 그리기
        plane = NumberPlane(faded_line_ratio=0)
        self.play(Write(plane, lag_ratio=0.01, run_time=1))
        plane.add_coordinate_labels()
        
        dots_moved = []
        for i, info_pos in zip(range(1, 5), [UR, UL, UP, DOWN]):
            vector = Vector(X_AXIS*i)
            dot = Dot(X_AXIS*i, color=BLUE)
            self.play(FadeIn(dot), ShowCreation(vector))
            
            x_tracker = ValueTracker(i)
            arc = Arc(0, i, radius=i, color=BLUE)
            f_always(
                dot.move_to,
                lambda: plane.i2gp(x_tracker.get_value(), arc)
            )
            dots_moved.append(Dot(dot.get_center(), color=BLUE))
            text = Text(f"(r={i}, rad={i})").next_to(dot, direction=info_pos)
            
            f_always(
                vector.set_points_by_ends,
                lambda: ORIGIN,
                lambda: plane.i2gp(x_tracker.get_value(), arc),
            )
            self.play(ShowCreation(arc), x_tracker.animate.set_value(i))
            self.play(FadeIn(text), FadeIn(dots_moved[-1]), FadeOut(dot))
            self.wait()
            self.play(FadeOut(arc), FadeOut(text), FadeOut(vector))

        plane2 = NumberPlane(background_line_style=self.bgl_style, faded_line_ratio=0)
        self.play(FadeOut(plane), FadeIn(plane2))
        
        zoom_dots = [dot.animate.apply_function(zoom1) for dot in dots_moved]
        self.play(*zoom_dots)
        self.wait()
        
        # 점 추가하기
        dots_Pin100, dots_NPin100 = [], []
        texts_Pin100, texts_NPin100 = [], []
        for n in range(1, 100+1):
            dot = Dot(np.array([zoom1(n), 0, 0])).rotate(n, about_point=ORIGIN)
            
            (dots, texts) = (dots_Pin100, texts_Pin100) if n in self.primes else (dots_NPin100, texts_NPin100)
            dots.append(Dot(dot.get_center(), color=BLUE, radius=0.03))
            
            texts.append(Text(str(n), font_size=18).next_to(dots[-1], direction=UP, buff=0.1))
            self.play(
                FadeIn(dots[-1]),
                FadeIn(texts[-1]),
                run_time = 1/n
            )
            
        dots_Primes = []
        positions_zoom2, positions_zoom3 = [], []
        for n in self.primes:
            if n > ar: break
            dot = Dot(np.array([zoom1(n), 0, 0])).rotate(n, about_point=ORIGIN)
            dots_Primes.append(Dot(dot.get_center(), color=BLUE, radius=0.01))
            dot.apply_function(zoom2)
            positions_zoom2.append(dot.get_center())
            dot.apply_function(zoom3)
            positions_zoom3.append(dot.get_center())
            sys.stdout.write(f'\r{n}')
            sys.stdout.flush()
        print()
        
        # 화면 안의 소수 아닌 수들 사라지기
        text = Text('소수만 남기기', font='BM JUA_TTF', font_size=64).to_edge(UP)
        self.play(Write(text))
        self.play(
            FadeOut(VGroup(*dots_NPin100)), 
            FadeOut(VGroup(*texts_NPin100)), 
            FadeOut(VGroup(*dots_moved)), 
            run_time=3
        )
        
        # 화면 안의 소수 점만 남기기, 화면 밖의 나머지 소수도 모두 나타나기
        self.play(
            FadeOut(VGroup(*dots_Pin100)), 
            FadeOut(VGroup(*texts_Pin100)), 
            FadeIn(VGroup(*dots_Primes)),
            FadeOut(text), 
            run_time=3
        )
        
        # 화면 축소하기
        move_dots = [dot.animate.move_to(pos) \
            for dot, pos in tqdm(
                zip(dots_Primes, positions_zoom2), total=len(dots_Primes)
            )
        ]
        self.play(*move_dots, run_time=5)
        self.wait(1)
        
        move_dots = [dot.animate.move_to(pos) \
            for dot, pos in tqdm(
                zip(dots_Primes, positions_zoom3), total=len(dots_Primes)
            )
        ]
        self.play(*move_dots, run_time=4)
        self.wait(3)

        print(self.time_delta())
