#!/bin/bash

Rscript -e 'rmarkdown::render("teams-cpmr.Rmd")'

mkdir -p ../R-pdf/yellow-card
mv *pdf ../R-pdf/yellow-card