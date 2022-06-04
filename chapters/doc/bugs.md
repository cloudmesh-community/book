# Known Bugs

1. The figure prefix in the main section is currently set to fig. 1, 
   however, we want that to be Fiure 1. This is a 
   configuration in pandoc-crossref.
2. Much of the IU section on plagiarizm is copied. We may not have put 
   in quotes to indicate the copied sections.
3. The instalation instructions may be outdted or wrong. For example we no longer use 
   vagrant but have a docker container.
4. The current book has only been tested to be created on ubuntu 20.04
5. We like to move the entire book creation into a docker container so it is more portable
6. Images from graphviz and mermaide are not included.
7. The tables in the plagiarizm section are not properly formatted
8. The docker image generation has not been tested recently.
9. The dockerfiles are outdated.