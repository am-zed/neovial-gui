### neovial-gui

Based on Vial 0.7.1 with select applied pending requests.
Bumped version to 0.7.2 and called it NeoVial for my own usage and fun.

- Compiled using Python 3.12.8 + pyinstaller (instead of fbs).
- Export layout to SVG format.
- Tool-tip over Tap Dance and Macros.
- All thanks to the following PR's and couple of tweaks to make it work:

vial-kb#79
| vial-kb#120
| vial-kb#132
| vial-kb#214
| vial-kb#238

# Docs and getting started

### Please visit [get.vial.today](https://get.vial.today/) to get started with Vial

Vial is an open-source cross-platform (Windows, Linux and Mac) GUI and a QMK fork for configuring your keyboard in real time.

*NeoVial*

![NeoVial](https://github.com/user-attachments/assets/f9d8e947-442a-49a7-b098-30ffff784352)

*Vial*

![Vial](https://get.vial.today/img/vial-win-1.png)


---


#### Releases

Check releases section in here for NeoVial 0.7.2 (patched Vial 0.7.1),
Or visit https://get.vial.today/ to download a binary release of Vial.

#### Development

Python 3.12 is recommended.

Install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To launch the application afterwards:

```
source venv/bin/activate
pyinstaller misc/Vial.spec
./dist/Vial/Vial
```
