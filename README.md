# Text Renderer
Generate text images for training deep learning OCR model (e.g. [CRNN](https://github.com/bgshih/crnn)). ![example](./image/example.gif)

- [x] Modular design. You can easily add [Corpus](https://oh-my-ocr.github.io/text_renderer/corpus/index.html), [Effect](https://oh-my-ocr.github.io/text_renderer/effect/index.html), [Layout](https://oh-my-ocr.github.io/text_renderer/layout/index.html).
- [x] Support generate `lmdb` dataset which compatible with [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), see [Dataset](https://oh-my-ocr.github.io/text_renderer/dataset.html)
- [x] Support render multi corpus on image with different font, font size or font color. [Layout](https://oh-my-ocr.github.io/text_renderer/layout/index.html) is responsible for the layout between multiple corpora
- [ ] Generate vertical text
- [ ] Corpus sampler: helpful to perform character balance

## Quick Start

See [Quick Start](https://oh-my-ocr.github.io/text_renderer/note/quick_start.html) to run the example.

Learn more at [documentation](https://oh-my-ocr.github.io/text_renderer/index.html)


```
pip install -r requirements.txt

python main.py --config config/config.py

python ./gen_config/label2lmdb.py 
```
