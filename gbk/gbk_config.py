import os
from pathlib import Path
from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char/compose"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(30, 31),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)

train_chn_data = GeneratorCfg(
    num_image=50,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        gray=True,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "contract.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
    ),
)

test_chn_data = GeneratorCfg(
    num_image=50,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        gray=True,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "contract.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
    ),
)

c1_train_rand_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),
    ),
)

c1_test_rand_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),    
    ),
)

c1_train_same_line_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)

c1_test_same_line_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)


c1_alph_symb_arge_train_rand_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_alph_symb_arge.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),
    ),
)

c1_alph_symb_arge_test_rand_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_alph_symb_arge.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),    
    ),
)

c1_alph_symb_arge_train_same_line_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)

c1_alph_symb_arge_test_same_line_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)


c1_c2_train_rand_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_c2.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),
    ),
)

c1_c2_test_rand_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_c2.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),    
    ),
)

c1_c2_train_same_line_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_c2.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)

c1_c2_test_same_line_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_c2.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)



c1_c2_alph_symb_arge_train_rand_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),
    ),
)

c1_c2_alph_symb_arge_test_rand_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        gray=True,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
          RandCorpusCfg(
            chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
            length=(5, 30),
            char_spacing=(-0.3, 1.3),
            **font_cfg
          ),
        ),    
    ),
)

c1_c2_alph_symb_arge_train_same_line_data = GeneratorCfg(
    num_image=11,
    save_dir=OUT_DIR / "train",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)

c1_c2_alph_symb_arge_test_same_line_data = GeneratorCfg(
    num_image=12,
    save_dir=OUT_DIR / "test",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=True,
        corpus=RandCorpus(
              RandCorpusCfg(
                chars_file=CHAR_DIR / "c1_c2_alph_symb_arge.txt",
                length=(5, 30),
                char_spacing=(-0.3, 1.3),
                **font_cfg
              ),
            ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
        layout_effects=Effects(Line(p=1)),
    ),
)

# fmt: off
configs = [
    train_chn_data,
    test_chn_data,
    c1_train_rand_data,
    c1_test_rand_data,
    c1_train_same_line_data,
    c1_test_same_line_data,
    c1_alph_symb_arge_train_rand_data,
    c1_alph_symb_arge_test_rand_data,
    c1_alph_symb_arge_train_same_line_data,
    c1_alph_symb_arge_test_same_line_data,
    c1_c2_train_rand_data,
    c1_c2_test_rand_data,
    c1_c2_train_same_line_data,
    c1_c2_test_same_line_data,
    c1_c2_alph_symb_arge_train_rand_data,
    c1_c2_alph_symb_arge_test_rand_data,
    c1_c2_alph_symb_arge_train_same_line_data,
    c1_c2_alph_symb_arge_test_same_line_data,
]
# fmt: on

