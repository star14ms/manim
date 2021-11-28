from manimlib import *
from io import *
 
FILE = "linear" # linear quadratic
TEX_CLASS = Tex
 
formula_file = open(f"FORMULAS/TXT/{FILE}.txt","r")
formula_file = formula_file.readlines()

color_config = {'a': BLUE, 'b': TEAL, 'c': GREEN, 'x': YELLOW }

color_map_1 = [
    {'a': [0], 'b': [3], 'x': [1]},
    {'a': [0], 'b': [4], 'x': [1]},
    {'a': [5], 'b': [3], 'x': [0]},
]
color_map_2 = [
    {'a': [0], 'b': [4], 'c':[7], 'x': [1, 5]},
    {'a': [0], 'b': [4], 'c':[8], 'x': [1, 5]},
    {'a': [5, 11], 'b': [3], 'c':[9], 'x': [0, 6]},
    {'a': [5, 12, 19, 25], 'b': [3, 9, 22], 'c':[17], 'x': [0, 6]},
    {'a': [6, 13, 19], 'b': [3, 16], 'c':[11], 'x': [1]},
    {'a': [6, 13, 19], 'b': [3, 15], 'c':[11], 'x': [1]},
    {'a': [6, 14, 19], 'b': [3, 10], 'c':[17], 'x': [1]},
    {'a': [6, 14, 21], 'b': [3, 10], 'c':[18], 'x': [1]},
    {'a': [6, 14, 18, 22], 'b': [3, 10], 'c':[19], 'x': [1]},
    {'a': [6, 14, 18], 'b': [3, 10], 'c':[15], 'x': [1]},
    {'a': [8, 19, 23], 'b': [5, 15], 'c':[20], 'x': [3]},
    {'a': [5, 14, 18], 'b': [2, 10], 'c':[15], 'x': [0]},
    {'a': [6, 14, 18], 'b': [3, 10], 'c':[15], 'x': [0]},
    {'a': [6, 14, 18], 'b': [3, 10], 'c':[15], 'x': [0]},
    {'a': [11, 15], 'b': [3, 7], 'c':[12], 'x': [0]},
]

set_of_changes_1 = [
  # STEP 1
    [[
    (0, 1, 2, 3, 4),
    (0, 1, 3, 4, 2),
    ]],
  # STEP 2
    [[
    (0, 1, 2, 3, 4),
    (5, 0, 1, 2, 3),
    ]],
]
set_of_changes_2 = [
  # STEP 1
    [[
    (   0,  1,  2,  3,  4,  5,  6,  8,  7,  ),
    (   0,  1,  2,  3,  4,  5,  7,  6,  8,  ),
    ]],
  # STEP 2
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  ),
    (   5,  0,  1,  2,  3,  6,  7,  8,  9,  )
    ]],
  # STEP 3
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, ),
    (   0,  1,  2,  3,  4,  5,  6,  15, 16, 17, 18, 19, )
    ]],
  # STEP 4
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, ),
    (   1,  8,  2,  3,  4,  6,  1,  2,  0,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, )
    ]],
  # STEP 5
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 16, 17, 18, 19, 21, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 17, 18, 19, 16, )
    ]],
  # STEP 6
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 15, 16, 17, 18, 19, 20, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  16, 17, 18, 19, 10, 11, 12, 13, 14, 15, )
    ]],
  # STEP 7
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 18, 19, 21, )
    ]],
  # STEP 8
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, )
    ]],
  # STEP 9
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 16, 17, 18, 19, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 16, 17, 18, 19, 16, 17, 18, 19, 12, 13, 14, 15, )
    ]],
  # STEP 10
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ),
    (   2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, )
    ]],
  # STEP 11
    [[
    (   3,  4,  5,  6,  7,  8,  11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, )
    ]],
  # STEP 12
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ),
    (   0,  2,  3,  4,  5,  6,  1,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, )
    ]],
  # STEP 13
    [[
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, ),
    (   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, )
    ]],
  # STEP 14
    [[
    (   0,  1,  2,  3,  4,  5,  6,  16, 17, 18, 7,  8,  9,  10, 11, 12, 13, 14, 15, ),
    (   0,  1,  2,  3,  13, 14, 15, 13, 14, 15, 4,  5,  6,  7,  8,  9,  10, 11, 12, )
    ]],
]

kwargs_step_formula_1 = {
    1: {'fade': (5,)},
    2: {'pos_write': (4,)},
}
kwargs_step_formula_2 = {
    1: {'fade': (9,)},
    2: {'pre_copy':(0,), 'pos_copy':(11,), 'pos_write':( 4,  10, ),},
    3: {'pos_write':( 7,  8,  9,  10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27, )},
    4: {},
    5: {'fade':(  15, 20, ), 'pre_copy':(  21, ), 'pos_copy':(  20, )},
    6: {'fade':(  14, )},
    7: {'pos_write':( 17, 20, )},
    8: {'pos_write':( 18, 23  )},
    9: {},
    10:{'pos_write':( 0,  1,  12, 13, 14, )},
    11:{'fade':(  0,  1,  2,  9,  10, )},
    12:{},
    13:{'fade':(19,)},
    14:{},
}

config_Linear = ("일차방정식의 근의공식\n(Linear Formula)", color_map_1, set_of_changes_1, kwargs_step_formula_1)
config_Quadratic = ("이차방정식의 근의공식\n(Quadratic Formula)", color_map_2, set_of_changes_2, kwargs_step_formula_2)

(titles, color_map, set_of_changes, kwargs_step_formula) = \
       config_Linear if FILE == "linear" else \
    config_Quadratic if FILE == "quadratic" else \
    print('FILE 이름을 확인해주세요')


class Linear_Formula(Scene):
    def construct(self):
        self.import_formulas(formula_file)
        self.set_colors(color_map, color_config)
        self.set_of_changes = set_of_changes
        self.kwargs_step_formula = kwargs_step_formula
        self.titles = titles
        
        self.write_formula_0()
        
        # STEP 1 ~ 14
        for i in range(1, len(self.formulas)):
            self.step_formula(**self.kwargs_step_formula[i], n_step=i)
        self.wait(2)

    def import_formulas(self, formula_file, scale=1.8):
        self.formulas = VGroup(*[
            TEX_CLASS(f)[0] for f in formula_file
        ])
        self.formulas.scale(scale)
 
    def set_colors(self, color_map, color_config):
        for (formula, map) in zip(self.formulas, color_map):
            for key in map.keys():
                color = color_config[key]
                for idx in map[key]:
                    formula[idx].set_color(color)

    def write_formula_0(self):
        title_splited = titles.split('\n')
        title = VGroup(
            Text(title_splited[0], font='BM JUA_TTF', font_size=100),
            Text(title_splited[1], font='BM JUA_TTF', font_size=100),
        )
        title.arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(title))
        self.wait()
        self.play(FadeTransform(title, self.formulas[0]))
 
    def step_formula(self,
                            pre_write=[],
                            pos_write=[],
                            pre_fade=[],
                            pos_fade=[],
                            fade=[],
                            write=[],
                            changes=[[]],
                            path_arc=0,
                            n_step=0,
                            pre_copy=[],
                            pos_copy=[],
                            time_pre_changes=0.3,
                            time_pos_changes=0.3,
                            run_time=2,
                            time_end=0.3,
                            pre_order=["w","f"],
                            pos_order=["w","f"]
                            ):
        print(f"step: {n_step}")
        formula_copy=[]
        for c in pre_copy:
            formula_copy.append(self.formulas[n_step-1][c].copy())
 
        for ani_ in pre_order:
            if len(pre_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step-1][w])for w in pre_write])
            if len(pre_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step-1][w])for w in pre_fade])
 
        self.wait(time_pre_changes)
 
        for pre_ind,post_ind in self.set_of_changes[n_step-1]:
            # for i,j in zip(pre_ind,post_ind):
            #     what = self.formulas[n_step-1][i]
            #     print(dir(what))
            #     print(type(what))
            self.play(*[
                ReplacementTransform(
                    self.formulas[n_step-1][i],self.formulas[n_step][j],
                    path_arc=path_arc
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                *[FadeOut(self.formulas[n_step-1][f])for f in fade if len(fade)>0],
                *[Write(self.formulas[n_step][w])for w in write if len(write)>0],
                *[ReplacementTransform(formula_copy[j],self.formulas[n_step][f])
                for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
                ],
                run_time=run_time
            )
 
        self.wait(time_pos_changes)
 
        for ani_ in pos_order:
            if len(pos_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step][w])for w in pos_write])
            if len(pos_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step][w])for w in pos_fade])
        self.wait(time_end)
         