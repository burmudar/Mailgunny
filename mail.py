import requests, os

__MAILGUN_BASE_URL = ""
__MAILGUN_SECRET = ""
__FROM_ADDRESS = ""

def mail(dest, content):
    return requests.post(
        __MAILGUN_BASE_URL+"/messages",
        auth=("api",__MAILGUN_SECRET),
        data={"from": __FROM_ADDRESS,
              "to": dest,
              "subject": "Hello! From our new home",
              "html": content}
    )

def load_recipients(loc):
    recipients = []
    with open(loc) as recp_file:
        for line in recp_file:
            recipients.append(line.strip())
    return recipients

def load_mail_content(loc):
    mail = open(loc)
    with open(loc) as mail_content:
        return mail_content.read()

def load_env_vars():
    __FROM_ADDRESS = os.getenv("FROM_ADDRESS")
    __MAILGUN_BASE_URL = os.getenv("MAILGUN_BASE_URL")
    __MAILGUN_SECRET = os.getenv("MAILGUN_SECRET")
    if __FROM_ADDRESS is None:
        raise Exception("Environment variable FROM_ADDRESS cannot be empty")
    if __MAILGUN_BASE_URL is None:
        raise Exception("Environment variable MAILGUN_BASE_URL cannot be empty")
    if __MAILGUN_SECRET is None:
        raise Exception("Environment variable MAILGUN_SECRET cannot be empty")

def main():
    load_env_vars()
    recipients = load_recipients("recipients.txt")
    mail_content = load_mail_content("mail.html")
    output = open("mail_result.txt", 'w')
    for dest in recipients:
        result = mail(dest, mail_content)
        if result.status_code == 200:
            output.write("{} : {}\n".format(dest, result.json()))
        else:
            print("Mailgun reported an error sending mail to {} -> {}".format(dest, result.text))
    output.close()

if __name__ == "__main__":
    main()
