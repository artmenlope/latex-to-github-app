# LaTeX-to-GitHub-app

This is a small app for converting LaTeX code to a format readable by GitHub's Markdown using source URLs.

It was inspired by the solutions provided by Alexander Rodin (username: a-rodin) at:

	https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b

■ You can write your LaTeX formula in the frame under the label "Write yout LaTeX code:". Pressing the "Convert LaTeX code" left button under the LaTeX input frame a HTML code is generated. This code can be pasted into a GitHub README.md file so the desired formula can be generated. 
It is asumed that the input is already in math mode. You can also start writing in the LaTeX frame as soon as the app is opened.

■ The frame under the "The HTML result is:" label is where the resulting HTML code will be shown. The code will have the following form:

<img src="https://render.githubusercontent.com/render/math?math=--Formatted formula here--">

■ The frame under the "The GitHub URL result is:" label will show the URL for GitHub to render the math formula. You can paste this URL in the adress bar of your web browser to view the resulting formula. This URL is already inside the HTML code and has the following aspect:

https://render.githubusercontent.com/render/math?math=--Formatted formula here--

■ In this app you can also view the result from the URL if internet connection is available. Keeping the "View image" checkbutton below the input frame checked, the formula can ve viewed on the "Image:" canvas on the lower right.
