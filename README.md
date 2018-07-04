# DIffJS
DiffJs is a script to monitor changes in javascript files on domains.
### Installation
1. Register your account at [Zapier] and setup the Webhook [here] for email delivery.
2. Note down Webhook URL.
3. Run `chmod +x install.sh`
4. Run `./install.sh`
5. Replace "MY_OWN_WEBHOOK_URL_HERE" with your Webhook URL from `step #2`in `sendmail.sh`.
6. Setup [CRON] job for your system to run `./diffJs.py domain.com subdomains_list.txt` as required. 
   
   Thanks to Prateek Tiwari a.k.a. [@prateek_0490] for this awesome idea and cont.
  
   Note : This tool is built upon following awesome tools :
   1. [relative-url-extractor] by [@jobert]
   2. [003Recon] by [@003Random]
   
Kudos to the authors.


   [Zapier]: <https://zapier.com/>
   [here]: <https://zapier.com/apps/email/integrations/webhook/62/turn-webhooks-into-sent-emails>
   [CRON]: <http://www.adminschoice.com/crontab-quick-reference>
   [relative-url-extractor]: <https://github.com/jobertabma/relative-url-extractor>
   [@jobert]: <https://github.com/jobertabma>
   [003Recon]: <https://github.com/003random/003Recon>
   [@003Random]: <https://github.com/003random>
   [@prateek_0490]: <https://twitter.com/prateek_0490>
