# latex-to-github-app

<!--See https://shields.io/ for the badges-->
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/artmenlope/latex-to-github-app/blob/master/LICENSE.md)
![Version](https://img.shields.io/github/v/release/artmenlope/latex-to-github-app?include_prereleases)
![Last Commit](https://img.shields.io/github/last-commit/artmenlope/latex-to-github-app)
<!-- ![win-test](https://img.shields.io/badge/tested-windows%2010%20%7C%20ubuntu%2020.04%20LTS-lightgrey) -->

This is a small app for converting LaTeX code to a format readable by GitHub's Markdown using source URLs. It is written in Python 3.

It was inspired by the solutions provided by Alexander Rodin (username: a-rodin) at:

<p align="center">
https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b
</p>

Please, remember to read the [Notes](#Notes).

## Table of contents

- [Required packages](#Required-packages)
- [The GUI](#The-GUI)
- [GUI explanation](#GUI-explanation)
- [Example](#Example)
- [Minimalistic Jupyter notebook](#Minimalistic-Jupyter-notebook)
- [Notes](#Notes)
- [To do](#To-do)

---

## Required packages

The required Python packages are:

* tkinter
* urllib
* PIL (to import Image and ImageTk)
* io (to import BytesIO)
* cairosvg

<!--
<ul>
    <ul>
        <ul>
            <li>tkinter</li>
            <li>urllib</li>
            <li>PIL</li>
            <li>io</li>
            <li>cairosvg</li>
        </ul>
    </ul>
</ul>
-->


---

## The GUI


The GUI looks like this:

<!--
<p align="center">
<img src="https://github.com/artmenlope/latex-to-github-app/blob/master/images/main-window.PNG" width="80%">
</p>
-->

<img src="https://github.com/artmenlope/latex-to-github-app/blob/master/images/main-window.PNG" width="87%"> | <img src="https://github.com/artmenlope/latex-to-github-app/blob/master/images/main-window-ubuntu.png" width="100%">
| :------: | :-------: |
Windows 10 | Ubuntu 20.04 LTS

<br>




---

## GUI explanation

■ You can write your LaTeX formula in the frame under the label "Write yout LaTeX code:". Pressing the "Convert LaTeX code" left button under the LaTeX input frame a HTML code is generated. This code can be pasted into a GitHub README.md file so the desired formula can be generated. 
It is asumed that the input is already in math mode. You can also start writing in the LaTeX frame as soon as the app is opened.

■ The frame under the "The HTML result is:" label is where the resulting HTML code will be shown. The code will have the following form:

```html
<img src="https://render.githubusercontent.com/render/math?math=--Formatted formula here--">
```

■ The frame under the "The GitHub URL result is:" label will show the URL for GitHub to render the math formula. You can paste this URL in the adress bar of your web browser to view the resulting formula. This URL is already inside the HTML code and has the following aspect:

```
https://render.githubusercontent.com/render/math?math=--Formatted formula here--
```

■ In this app you can also view the result from the URL if internet connection is available. Keeping the "View image" checkbutton below the input frame checked, the formula can ve viewed on the "Image:" canvas on the lower right.

<br>

<p align="center">
<img src="https://github.com/artmenlope/latex-to-github-app/blob/master/images/example-animation.gif" width="55%">
</p>

■ After having obtained results like in the animation above, if you want to write a different LaTeX code you can just delete the old LaTeX code and write again. Don't worry about the output, it will be overwritten.

---

## Example

In the following image you can see an example of input and output:

<p align="center">
<img src="https://github.com/artmenlope/latex-to-github-app/blob/master/images/example1.PNG" width="80%">
</p>

Then, you can copy and paste the resulting HTML code, for example, in your README.md file like the following if you want to obtain a centered equation:

```html
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=%5Cmathbf%7BR_z%7D(%5Ctheta)%0A%3D%0A%5Cbegin%7Bpmatrix%7D%0A%5Ccos%5Ctheta%20%26%20-%5Csin%5Ctheta%20%26%200%20%5C%5C%5B2ex%5D%0A%5Csin%5Ctheta%20%26%20%20%5Ccos%5Ctheta%20%26%200%20%5C%5C%5B2ex%5D%0A0%20%20%20%20%20%20%20%20%20%20%26%20%200%20%20%20%20%20%20%20%20%20%20%26%201%0A%5Cend%7Bpmatrix%7D%0A">
</p>
```

The result of the previous HTML code will be:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=%5Cmathbf%7BR_z%7D(%5Ctheta)%0A%3D%0A%5Cbegin%7Bpmatrix%7D%0A%5Ccos%5Ctheta%20%26%20-%5Csin%5Ctheta%20%26%200%20%5C%5C%5B2ex%5D%0A%5Csin%5Ctheta%20%26%20%20%5Ccos%5Ctheta%20%26%200%20%5C%5C%5B2ex%5D%0A0%20%20%20%20%20%20%20%20%20%20%26%20%200%20%20%20%20%20%20%20%20%20%20%26%201%0A%5Cend%7Bpmatrix%7D%0A">
</p>

<br>

---

## Minimalistic Jupyter notebook

In this repository there is also included a [minimalistic Jupyter notebook](https://github.com/artmenlope/latex-to-github-app/blob/master/LaTeX%20to%20GitHub%20minimalistic%20notebook.ipynb) with the essential functionality of the code: translating from LaTeX to HTML readable by the GitHub math renderer. This notebook only requires the urllib package. The code is the following:

```python
import urllib

# Write your LaTeX code here.
string = \
r"""
\begin{cases}
a & = b \\[3ex]
a & = b
\end{cases}
"""[1:-1] # Delete initial and final \n line jumps.

encoded_string = urllib.parse.quote(str(string).encode("utf-8"), safe="~()*!.\"")
github_url = "https://render.githubusercontent.com/render/math?math=" + encoded_string
html_result = '<img src="' + github_url + '">'

print("GitHub URL:\n\n", github_url, "\n\nHTML result:\n\n", html_result)
```

You can try Jupyter in your browser without installing anything at [https://jupyter.org/try](https://jupyter.org/try). There, you can create a new notebook and run the code snippet above.

<br> 

---

## Notes

This small app was developed in Windows 10 using the Spyder IDE. It has also been tested on Ubuntu 20.04 LTS.

To copy and paste in the app you can use the <kbd>ctrl</kbd>+<kbd>c</kbd> and <kbd>ctrl</kbd>+<kbd>v</kbd> shortcuts.

At the current state of development you will need to install the needed packages and run the [latex-to-github-app.py](https://github.com/artmenlope/latex-to-github-app/blob/master/latex-to-github-app.py) script if you want to use the app.

### To do:

- [ ] Make a reset button.
- [ ] Make a mouse right click menu for copying and pasting.
- [x] Test in Ubuntu.
- [ ] Make an executable file app.

