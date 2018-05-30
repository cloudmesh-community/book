height=0.9

\forestset{
  skan tree/.style={
    for tree={
      drop shadow,
      text width=2cm,
      grow'=0,
      rounded corners,
      draw,
      top color=white,
      bottom color=blue!20,
      edge={Latex-},
      child anchor=parent,
      %parent anchor=children,
      anchor=parent,
      tier/.wrap pgfmath arg={tier ##1}{level()},
      s sep+=2.5pt,
      l sep+=2.5pt,
      edge path'={
        (.child anchor) -- ++(-10pt,0) -- (!u.parent anchor)
      },
      node options={ align=center },
    },
    before typesetting nodes={
      for tree={
        content/.wrap value={\strut ##1},
      },
    },
  },
}
skan tree \[E616 \[Administration \[Accounts \[Futuresystems Github
Chameleon Cloud IU google Piazza, \] \] \] \[Scientific Writing
\[Assignments \[Project Report, \] \[2 p. Paper, \] \[Abstracts, \] \]
\[LaTeX \[bibtex\
jabref [\[s:a\]](#s:a){reference-type="ref" reference="s:a"}\
LaTeX, \] \] \] \[Prerequisits Review \[Python \[Language, \] \[pyenv\
pip, \] \] \[Advanced Python \[Numpy\
Scipy\
OpenCV, \] \[Face Detection Fingerprint, \] \[CMD5, \] \] \[ssh \[Keys,
\] \] \[Linux \[Commands, \] \] \] \[IaaS \[VM \[Virtual Box, \]
\[Openstack, \] \[QEMU, \] \[KVM, \] \] \[Container \[Docker\
Docker Swarm\
Kubernetes, \] \] \] \[PaaS \[MapReduce \[E516\
Hadoop\
Spark, \] \[E516\
Harp\
Twister, \] \] \[Servers \[REST, \] \[MQTT, \] \] \] \[SaaS
\[Applications \[Physics, \] \[Helath Care, \] \[Life Style, \]
\[Sensors, \] \[Sports, \] \[Web Search\
Text Minining, \] \] \] \]
