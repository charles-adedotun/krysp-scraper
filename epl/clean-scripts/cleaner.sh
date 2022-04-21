#!/bin/bash

Rscript -e 'rmarkdown::render("teams-cpmr.Rmd")'

mv *pdf ../R-pdf/yellow-card