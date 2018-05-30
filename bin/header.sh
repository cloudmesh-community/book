#! /bin/sh
pandoc $1 --base-header-level=$2 -o /tmp/convert.md
cp /tmp/convert.md $1


