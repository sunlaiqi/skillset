

Find all the pdf files, compare them with the files in one folder and then remove all those duplicate files in the folder.
find ./ -iname "*.pdf" -exec mv '{}' ../Books/ \;

find ./ -iname "*.pdf" -exec basename '{}' \; 

cat dupfile -exec mv '{}' ../duplicate \;

# Find the files in bookfile.txt but not in pdffile.txt
grep -v -f pdffile.txt bookfile.txt > difffile.txt

for file in `cat ../difffile.txt`; do mv "$file" ../Doc-bk/; done
# above will have problem with space

while read -r file; do mv "$file" /path/of/destination ; done < ../difffile.txt

while read -r file; do rm "file" ; done < pdffile.txt