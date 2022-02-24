python ./cyk.py
for x in tree*.dot; do
    dot -Tpdf < $x > $x.pdf
done
pdfjam tree*.pdf --outfile out.pdf
rm tree*.pdf *.dot
