cd jpg
if compgen -G "*.jpg" > /dev/null; then
  for f in *.jpg; do
    SVG="../svg/${f::-4}.svg"
    if [ ! -f "$SVG" ]; then
      convert $f ../tmp.ppm
      potrace -s -o $SVG ../tmp.ppm
      rm ../tmp.ppm
    fi
  done
fi
cd ..

python3 extract-paths.py