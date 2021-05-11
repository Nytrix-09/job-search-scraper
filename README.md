# job-search-scraper
A web scraping tool written in **python** using the **Beautiful Soup 4** library. The script essentially scrapes a job portal for all the jobs posted in the last **"few"** days. It takes input for the job role that is to be serarched and the skills the user is not fimiliar with, related to the job role (2 unfamiliar skills are permitted).  

Then, the script filters out the results according to the parameters set by the user and a list of all filtered results is displayed in seperate text files that contain the following information:  *Company Name: 
 *Key Skills Required:
 *More info: he script filters out the results according to the parameters set by the user and a list of all filtered results is displayed in seperate text files that contain the following information:  
  * Company Name: Displays the name of the Company that posted the job. 
  
  * Key Skills Required: Displays all the skills that are required by the employer as per their requirements.
  
  * More Info: Gives a clickable link to the job posting to attain more information about any specific post.

The script runs every 10 minutes (time class is used to force the script to sleep for the specified time) and pulls the data from the site to be displayed to the User. The script works for any job profile that the user enters.
