# Djang/BlogSite2.0 <br>
### python/django 🔰 + docker/container 🚢 + aws/S3Bucket 🪣 + heroku 🌐 => https://blogsite2v.herokuapp.com/ 😋


> **[INFO]** Simple *Django* website deployed on *heroku* with *docker container*, used *aws s3 bucket* too, so we can save our static and media files in the bucket *<br>
> **[GOALS]:** goals from this project was learning `docker` and `docker registr` further and understanding AWS `Simple Storage Service`

## Models:
1. Articles with attributes title, summary, image, author and release data.
2. Users with attributes name, username and email

## Views:🍔
1. **USER:** login, signup, change password, logout and forgot password
2. **ARTICLES:** get lists, get article by id(detailed!), post article(only posted author can delete and edit it), 


## Getting Started 🚩


### Installing Dependencies 🛠️

1. Python-3.9.5 (recommended)
2. Django v3.2.0
3. Docker v20.10.5
<br>

### Cloning from GitHub

```bash

    git clone https://github.com/AsqaraliyevFakhriyor/blogsite2.0 <PRIOJECT_DIR>
    cd <PROJECT_DIR>
    
```

### Virtual Environment 🧑‍✈️

```bash

pip install venv
python -m venv venv
source venv/Script/active

```

### PIP Dependecies 📋
> Once you have your **venv** setup and running, install dependencies by navigating
> to the root directory and running:
```bash
pip install -r requirements.txt
```
>This will install all of the required packages included in the requirements.txt
>file.


### Local Database Setup 📦
> Once you create the database, open your terminal, navigate to the root folder, and run:
```bash

python manage.py makemigrations
python manage.py migrate

```

### If you want to use project locally (without aws s3 bucket) you need to set **USE_S3** to False

# AWS S3 bucket section 🗑️

> Before beginning, you will need an AWS account. If you’re new to AWS, Amazon provides a free tier with 5GB of S3 storage.

### To create an S3 bucket, navigate to the S3 page and click "Create bucket":

![aws _ucket](/screenshots/aws_s3_1.png)


### Give the bucket a unique, DNS-compliant name and select a region:

![aws _ucket](/screenshots/aws_s3_2.png)

### Turn off "Block all public access":

![aws _ucket](/screenshots/aws_s3_5.png)

### Create the bucket. You should now see your bucket back on the main S3 page:

![aws _ucket](/screenshots/aws_s3_3.png)

### IAM Access

> Although you could use the AWS root user, it's best for security to create an IAM user that only has access to S3 or to a specific S3 bucket. What's more, by setting up a group, it makes it much easier to assign (and remove) access to the bucket. So, we'll start by setting up a group with limited permissions and then create a user and assign that user to the group.

### IAM Group

> Within the AWS Console, navigate to the main IAM page and click "User groups" on the sidebar. Then, click the "Create group" button, provide a name for the group and then search for and select the built-in policy "AmazonS3FullAccess":

![aws _ucket](/screenshots/aws_iam_1.png)

### Click "Create Group" to finish setting up the group:

![aws _ucket](/screenshots/aws_iam_2.png)

> If you'd like to limit access even more, to the specific bucket we just created, create a new policy with the following permissions:
```json
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
```
>  Be sure to replace your-bucket-name with the actual name. Then, detach the "AmazonS3FullAccess" policy from the group and attach the new policy.

### IAM User
> Back on the main IAM page, click "Users" and then "Add user". Define a user name and select "Programmatic access" under the "Access type":

![aws _ucket](/screenshots/aws_iam_3.png)

### Click the next button to move on to the "Permissions" step. Select the group we just created:

![aws _ucket](/screenshots/aws_iam_4.png)

### Click next again a few times until you're at the "Review" step. Click "Create user" to create the new user. You should now see the user's access key ID and secret access key:

![aws _ucket](/screenshots/aws_iam_5.png)

<br>

# ❗SET all variables in storage.py file and settings.py


## Runing 🏃 the Server (locally)
> From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:

```bash

    python manage.py runserver

```

# CREATING docker image 🚢

> make sure that you already have docker on your machine!

```bash

    docker build --tag image_name .
    docker run --name name_of_container -d -p 8000:8000 image_name

```

> ### CHeck local host with port 8000