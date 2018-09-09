# Graphviz

* <https://graphviz.gitlab.io/resources/>


## Installation 

### OSX

On OSX you can install graphviz with 

	brew install graphviz

On OSX there is also a graphviz version available that includes a GUI. THe link to this software is:

* <http://www.pixelglow.com/graphviz/>

It can be downloaded from 

* <http://www.pixelglow.com/downloads/graphviz-1.13-v16.dmg>

There is also an additional tool that is distributed by the community that is called doteditor and can be installed with 

	brew cask install doteditor
	
If you have issues with brew cask install, you can also install it by hand while going to 

* <https://vincenthee.github.io/DotEditor/>
	
Online versions of graphviz are also available, but we have not tested them

* <http://www.webgraphviz.com/>
* https://dreampuf.github.io/GraphvizOnline/
* http://viz-js.com/
* http://graphviz.it/#/gallery/unix.gv

There are many more

## Usage

To use Graphviz create a dot and run the following command.

	dot -Tpng filename.dot -o filename.png

This will create a png file. Other formats are also possible such as svg, or PDF 


	dot -Tsvg filename.dot -o filename.svg
	dot -TPDF filename.dot -o filename.pdf

For inclusion in latex documents we recommend you create PDF output as it has a much better quality and is smaller in size than png.

## The Dot Format

Put an example dot file here

## Exercise

\begin{exercise}
Develop a REST service that takes a graph as input and returns a rendered version of the graph in a specified format. Make sure you can pass the format as a parameter.
\end{exercise}

\begin{exercise}
Develop a REST service that takes a graph as input and returns a URL of the rendered graph while storing the output onto a data server. The data server is another rest service, from which the result can be picked up. 
\end{exercise}

\begin{exercise}
For IU students. Develop a REST service that takes a graph as input and returns a URL of the rendered graph while storing the output onto a data server. The data server is another rest service, from which the result can be picked up. Use box and/or google drive that are offered by IU as services. Make sure not to expose your passwords or access keys
\end{exercise}

