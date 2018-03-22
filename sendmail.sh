if [[ $(git diff HEAD) ]]; then
  git diff HEAD > ./results/$1/changes.txt
  date >> ./results/$1/changes.txt
  curl -d '{"changed":"'$1'"}' -H "Content-Type: application/json" -X POST https://hooks.zapier.com/hooks/catch/3086942/katsqw/
  echo 'Mail Sent for changes in $1 on $(date)'
else
  echo 'No changes found'
fi