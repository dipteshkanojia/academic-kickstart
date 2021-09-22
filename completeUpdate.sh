#!/bin/bash

git add .
git commit -m "updates"
git push
hugo
cd public
git add .
git commit -m "updates"
git push
cd ..

