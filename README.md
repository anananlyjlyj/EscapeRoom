# Girlsday Webpage

This is an interactive online physics tutorial for soon-to-be physicists created for the [Girlsday](https://www.girls-day.de/).
The whole tutorial currently is in German. It features various interactive elements/experiments that need to be done off-screen.

The webpage effectively is generated via a static page generator: the script `make_page.py` collects various assets and generates html pages from jinja templates. The relevant folders are:
* The folder `public_page` contains the public-facing webpage that explains the project for teachers and students
* The folder `pages` contains all the subpages of the interactive physics tutorial
* `assets` contains various assets (images, sounds, css)
* `jslib` contains multiple javascript libraries. Only `jslib/scripts.js` is custom-made, the rest are off-the-shelf libraries
* The script `make_page.py` collects templates and assets from these folders and generates the webpage in the folder `dist`. Its content is the actual webpage that needs to be uploaded.

## Further info
* The password to access the tutorial currently is `mariecurie`. It won't work locally due to some security restrictions (CORS). To start go to `/80dbac4b4517075112d2f981a8c41b1de43c67c8/index.html`.
* Videos are currently embedded from (vimeo)[https://vimeo.com/], but private there, so they don't work at the moment.
* There is a page `/80dbac4b4517075112d2f981a8c41b1de43c67c8/help.html`, that allows you to jump between the various rooms.
