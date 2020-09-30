#!/bin/bash
app="fibonacci2_python"
docker build -t ${app} .
docker run -p 56732:80 -t -i ${app}
