mkdir temp
mkdir dependency
mkdir results
chmod +x ./diffJs.py
chmod +x ./javascript_files_extractor.py
chmod +x ./javascript_files_link_extractor.sh
cd dependency
git clone https://github.com/jobertabma/relative-url-extractor.git
cd ..
git config diff.nodiff.command /bin/true
echo "results/*/changes.txt diff=nodiff" >> .git/info/attributes