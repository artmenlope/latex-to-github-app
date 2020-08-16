# LaTeX-to-GitHub-app

This is a small app for converting LaTeX code to a format readable by GitHub's Markdown using source URLs. It is written in Python 3.

It was inspired by the solutions provided by Alexander Rodin (username: a-rodin) at:

<p align="center">
https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b
</p>

The required Python packages are:

* tkinter
* urllib
* PIL
* io
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

The GUI looks like this:

<p align="center">
<img src="https://github.com/artmenlope/LaTeX-to-GitHub-app/blob/master/images/main-window.PNG" width="80%">
</p>

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

---

## Example

The following image is an example of use:

<p align="center">
<img src="https://github.com/artmenlope/LaTeX-to-GitHub-app/blob/master/images/example1.PNG" width="80%">
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

In this repository there is also included a [minimalistic Jupyter notebook](https://github.com/artmenlope/LaTeX-to-GitHub-app/blob/master/LaTeX%20to%20GitHub%20minimalistic%20notebook.ipynb) with the essential functionality of the code: translating from LaTeX to HTML readable by the GitHub math renderer. This notebook only requires the urllib package. The code is the following:

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
html_result = '<img src="' + github_url + encoded_string + '">'

print("GitHub URL:\n\n", github_url, "\n\nHTML result:\n\n", html_result)
```

<br> 

---

## Notes

This small app was developed in Windows 10 using the Spyder 4 IDE. It hasn't been tested on Linux.

### To do:

- [ ] Test in Ubuntu.
- [ ] Make an executable file app.

