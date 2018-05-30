height=0.9

\forestset{
  skan tree/.style={
    for tree={
      drop shadow,
      text width=3cm,
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
skan tree \[E516 \[Assignments \[Accounts
([\[a:accounts\]](#a:accounts){reference-type="ref"
reference="a:accounts"}) \[Futuresystems Github Chameleon Cloud IU
google
([\[E:e616-iu-google-services\]](#E:e616-iu-google-services){reference-type="ref"
reference="E:e616-iu-google-services"}) Piazza, \] \] \[Survey
([\[a:survey-entry\]](#a:survey-entry){reference-type="ref"
reference="a:survey-entry"})\] \[Writing Assignments \[Bio
([\[a:616-bio\]](#a:616-bio){reference-type="ref"
reference="a:616-bio"}), \] \[Plagiarizm
([\[S:plagiarism\]](#S:plagiarism){reference-type="ref"
reference="S:plagiarism"}) , \] \[Project Report
([\[E:project\]](#E:project){reference-type="ref"
reference="E:project"}), \] \[Tutorial
([\[E:616-tutorial\]](#E:616-tutorial){reference-type="ref"
reference="E:616-tutorial"}), \] \[2 p. Paper
([\[E:616-tech-paper\]](#E:616-tech-paper){reference-type="ref"
reference="E:616-tech-paper"}), \] \[Abstracts
([\[E:616-new-tech-abstract\]](#E:616-new-tech-abstract){reference-type="ref"
reference="E:616-new-tech-abstract"}), \] \] \[Programming Assignments
\[REST ([\[E:rest-eve\]](#E:rest-eve){reference-type="ref"
reference="E:rest-eve"})([\[E:REST-a\]](#E:REST-a){reference-type="ref"
reference="E:REST-a"})([\[E:REST-swagger\]](#E:REST-swagger){reference-type="ref"
reference="E:REST-swagger"})\] \[Project
([\[E:project\]](#E:project){reference-type="ref"
reference="E:project"}), \] \] \] \[Scientific Writing
([\[p:writing\]](#p:writing){reference-type="ref"
reference="p:writing"})
\[LaTeX([\[C:latex\]](#C:latex){reference-type="ref"
reference="C:latex"}) \[bibtex
([\[C:bibtex\]](#C:bibtex){reference-type="ref" reference="C:bibtex"})\
jabref ([\[s:jabref\]](#s:jabref){reference-type="ref"
reference="s:jabref"})\
LaTeX ([\[C:latex\]](#C:latex){reference-type="ref"
reference="C:latex"}), \] \] \] \[Prerequisits Review \[Python
([\[C:python\]](#C:python){reference-type="ref" reference="C:python"})
\[Language
([\[C:python-language\]](#C:python-language){reference-type="ref"
reference="C:python-language"}), \] \[pyenv
([\[C:python-install\]](#C:python-install){reference-type="ref"
reference="C:python-install"})\
pip ([\[C:python-install\]](#C:python-install){reference-type="ref"
reference="C:python-install"}), \] \] \[Advanced Python
([\[P:python-advanced\]](#P:python-advanced){reference-type="ref"
reference="P:python-advanced"}) \[Numpy
([\[s:numpy\]](#s:numpy){reference-type="ref" reference="s:numpy"})\
Scipy ([\[s:scipy\]](#s:scipy){reference-type="ref"
reference="s:scipy"})\
OpenCV ([\[c:opencv\]](#c:opencv){reference-type="ref"
reference="c:opencv"}), \] \[Face Detection
([\[c:face\]](#c:face){reference-type="ref" reference="c:face"})
Fingerprint
([\[c:python-fingerprint\]](#c:python-fingerprint){reference-type="ref"
reference="c:python-fingerprint"}), \] \[CMD5
([\[C:python-cmd5\]](#C:python-cmd5){reference-type="ref"
reference="C:python-cmd5"}), \] \] \[ssh
([\[C:ssh\]](#C:ssh){reference-type="ref" reference="C:ssh"}) \[Keys
([\[s:generate-a-ssh-key\]](#s:generate-a-ssh-key){reference-type="ref"
reference="s:generate-a-ssh-key"}), \] \] \[Linux
([\[C:linux\]](#C:linux){reference-type="ref" reference="C:linux"})
\[Commands
([\[c:linux-commands\]](#c:linux-commands){reference-type="ref"
reference="c:linux-commands"}), \] \] \] \[IaaS \[VM
([\[?\]](#?){reference-type="ref" reference="?"}) \[Virtual Box
([\[S:virtual-box\]](#S:virtual-box){reference-type="ref"
reference="S:virtual-box"}), \] \[Openstack
([\[C:chameleon\]](#C:chameleon){reference-type="ref"
reference="C:chameleon"}), \] \[QEMU ([\[?\]](#?){reference-type="ref"
reference="?"}), \] \[KVM ([\[?\]](#?){reference-type="ref"
reference="?"}), \] \] \[Container
([\[p:container\]](#p:container){reference-type="ref"
reference="p:container"})([\[c:container\]](#c:container){reference-type="ref"
reference="c:container"}) \[Docker
([\[s:motivation-docker\]](#s:motivation-docker){reference-type="ref"
reference="s:motivation-docker"})\
Docker Swarm
([\[s:motivation-docker\]](#s:motivation-docker){reference-type="ref"
reference="s:motivation-docker"})\
Kubernetes
([\[s:motivation-docker-kubernetes\]](#s:motivation-docker-kubernetes){reference-type="ref"
reference="s:motivation-docker-kubernetes"}), \] \] \] \[PaaS
\[MapReduce ([\[p:mapreduce\]](#p:mapreduce){reference-type="ref"
reference="p:mapreduce"}) \[Hadoop
([\[c:hadoop\]](#c:hadoop){reference-type="ref" reference="c:hadoop"})\
Spark ([\[c:spark\]](#c:spark){reference-type="ref"
reference="c:spark"}), \] \[Harp
([\[s:harp\]](#s:harp){reference-type="ref" reference="s:harp"})\
Twister ([\[s:twister\]](#s:twister){reference-type="ref"
reference="s:twister"}), \] \] \[Servers
([\[p:servertech\]](#p:servertech){reference-type="ref"
reference="p:servertech"}) \[REST
([\[c:rest\]](#c:rest){reference-type="ref" reference="c:rest"}), \]
\[MQTT ([\[c:mqtt\]](#c:mqtt){reference-type="ref" reference="c:mqtt"}),
\] \] \] \[SaaS \[e616\
Applications ([\[p:bigdata\]](#p:bigdata){reference-type="ref"
reference="p:bigdata"})([\[s:nist-usecase\]](#s:nist-usecase){reference-type="ref"
reference="s:nist-usecase"}) \[Physics
([\[c:physics\]](#c:physics){reference-type="ref"
reference="c:physics"}), \] \[Helath Care
([\[c:health-informatics\]](#c:health-informatics){reference-type="ref"
reference="c:health-informatics"}), \] \[Life Style
([\[c:e-commerce\]](#c:e-commerce){reference-type="ref"
reference="c:e-commerce"}), \] \[Sensors
([\[s:a-sensors\]](#s:a-sensors){reference-type="ref"
reference="s:a-sensors"}), \] \[Sports
([\[c:sports\]](#c:sports){reference-type="ref" reference="c:sports"}),
\] \[Web Search\
Text Minining
([\[s:web-search-and-text-mining\]](#s:web-search-and-text-mining){reference-type="ref"
reference="s:web-search-and-text-mining"}), \] \] \] \]
