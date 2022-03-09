import glob
import hashlib
import os
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

sha1 = hashlib.sha1()
sha1.update(b"mariecurie")

distPublicDir = "dist/"
correctHash = sha1.hexdigest()
distdir = distPublicDir + correctHash + "/"
excluded_pages = "base.html"

public_page_dir = "public_page/"

env = Environment(
    loader=FileSystemLoader("pages"),
    autoescape=select_autoescape(["html"]),
)


pages = glob.glob("pages/*.html")
pages = [os.path.basename(path) for path in pages]
pages = [page for page in pages if page not in excluded_pages]

try:
    shutil.rmtree(distPublicDir)
except FileNotFoundError:
    pass

shutil.copytree(public_page_dir, distPublicDir)

os.makedirs(distdir)

for page in pages:
    template = env.get_template(page)
    outputText = template.render()

    with open("{}{}".format(distdir, page), "w", encoding='utf-8') as outfile:
        outfile.write(outputText)

for f in ["assets", "jslib"]:
    shutil.copytree(f, "{}{}".format(distdir, f))

shutil.copy("assets/favicon.ico", "{}favicon.ico".format(distdir))
