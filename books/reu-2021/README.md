# Instructions

printreport.py is a script that downloads the reports
from the cybertraining-dsc website as PDF using selenium;
it also adds a cover page to the PDF.

To run it properly, stand in the root dir of the book
repository and run the following commands.

```bash
git pull
pip install -e .
cd books/reu-2021
python printreport.py
```

This script has been tested and successfully works on
Linux and Windows. Theoretically, it should work for
macOS, but has been untested.

Sometimes the pdf generation fails and this is sometimes
fixed by rerunning the script and trying again.

For optimal experience, Windows users should have
chocolatey installed and macOS users should have brew
installed. Chrome is also necessary.