if [[ $(git diff HEAD) ]]; then
  echo 'dirty'
else
  echo 'clean'
fi