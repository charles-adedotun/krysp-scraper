#!/bin/bash

Rscript -e 'rmarkdown::render("teams-cpmr.Rmd")'
Rscript -e 'rmarkdown::render("referees-cpmr.Rmd")'

mkdir -p ../R-pdf/yellow-card
mv *pdf ../R-pdf/yellow-card