#! /bin/sh -x
echo "File:" $1
echo "Level:" $2
rm -f /tmp/convert.md
pandoc $1 --base-header-level=$2 -o /tmp/convert.md
cp /tmp/convert.md dest/chapters/$1


