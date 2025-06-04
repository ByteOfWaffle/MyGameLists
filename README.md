# 🎮 MyGameList

A website inspired by [MyAnimeList](https://myanimelist.net), where users can create and share lists of games they've played. The platform collects user ratings together to provide global scores for each game. Users will also be able to make reviews for games in their lists.

---
# Table of contents 
- [📝 Development Progress](#-development-progress)
- [🧩 Planned Features](#planned-features-️)
- [🚧 Current MVP Progress](#current-mvp-progress)
- [⚖️ Legal guidelines](#Legal-guidelines)
- [🤝 How to Contribute](#privacy-policy)

# 📝Develpment progress 

## Planned features 🗒️

- **User Profiles**: Sign up, log in, and manage user profile.
- **Game Lists**: Create and organize game list with statuses like "Playing," "Completed," or "Dropped."
- **Global Scores**: Collect game ratings from all users into a global score.
- **Game Database**: Search for games using the RAWG database API and get detailed information (Game library, title, genre, etc.).
- **Reviews** Users will be able to make reviews for games in their list.


## Current MVP progress
- Main game list site✅
- Raspberry Pi Mariadb database ✅
- Make user account creator✅
- Login sessions✅
- Save games to userlist.✅
## Prio2
- Host the database on Virtual Machine✅
# Legal guidelines
## Universal design
By law this website is designed to follow the universal design principles of Norway [§ 18](https://lovdata.no/lov/2017-06-16-51/§18)
- Color contrast are all at wecag AAA level tested through [WebAIM](https://webaim.org/resources/contrastchecker/)

## Privacy policy
- The website does distribute any personal data from users.

---

# 🤝 How to contribute
I welcome contributions to MyGameList, if you're interested in helping, here's how you can get started:

## 1. Fork and clone
1. Click the Fork button (top right) to create your own copy of the repo.
2. Clone your fork to your local machine:
```
# Clone the forked repository
git clone https://github.com/YOUR_USERNAME/MyGameLists.git
```
Or clone by downloading the project as ZIP here in your own fork:<img width="904" alt="image" src="https://github.com/user-attachments/assets/582e567c-d52f-4688-a6f2-8328bf159226" />
- navigate to the project folder through the terminal: cd MyGameLists
- initialize git
```bash
git init
```

3. Install dependencies
```
# Install dependencies
pip install -r requirements.txt
```

## 2. Making Contributions
1. Create a new branch for your feature:
```bash
git checkout -b NameOfYourFeature
```

2. Make your changes and commit them:
```bash
# Stage all changes
git add .
# Commit staged changes with a message/description
git commit -m "Description of your changes"
```

3. Push to your branch:
```bash
git push origin your-feature-name
```

4. Create a Pull Request
1. You can either copy and paste the link from the terminal here:
![image](https://github.com/user-attachments/assets/83a370e1-e4ca-4068-9d90-5c386bb26f4a)
or go to your forked repository on GitHub and click the "compare and pull request" button like here:
![image](https://github.com/user-attachments/assets/e6d4ce3c-c674-4b05-b46c-46e7589e4362)
3. Add a clear title and description of your changes.
4. Submit the pull request.

## 3. Set up MariaDB database.
1. Set up the database and tables
- You can do this in whichever way you prefer i hosted it on from Ubuntu on a virtual machine for my project.
- The SQL used for the database and tables are in the project folder as "database.sql"

2. Listen to all networks 
⚠️This may be different on different Linux distros.⚠️
- Open your terminal and write: sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
- In here change the bind-address to 0.0.0.0
- It should look like this
```bash
bind-address = 0.0.0.0
```

3. Open ports
- Open port 8080, this is the port waitress uses to access the database.
Note: If you are planning on running the static on apache you might wanna enable port 80 as well.
```bash
sudo ufw allow 8080
```

4. Change ip on python file
- In the app1.py file change the host ip to mach the one of your database.

### Contribution Guidelines
- Follow the existing code style
- Test your changes thoroughly
- Update documentation if you're adding new features
- Create issues for major changes and enhancements
We appreciate your interest in making MyGameList better!

---
