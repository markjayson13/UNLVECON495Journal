SHELL := /bin/bash

serve:
\tbundle exec jekyll serve --livereload

build:
\tbundle exec jekyll build
