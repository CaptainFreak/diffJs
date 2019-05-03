if [ "$(git diff HEAD)" ]; then
  
  git diff HEAD > ./results/$1/changes.txt
  date >> ./results/$1/changes.txt
  curl -d '{"changed":"'$1'"}' -H "Content-Type: application/json" -X POST MY_OWN_WEBHOOK_URL_HERE
  echo -e '\n [+] Mail Sent for changes in $1 on '$(date)''
else
  echo 'No changes found in '$1''
fi
