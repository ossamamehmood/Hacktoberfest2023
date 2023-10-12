# Contribution Rules📚:

Before you start contributing, please read our [Code of Conduct](codeofconduct.md). We expect all contributors to follow these guidelines to ensure a positive and inclusive community.

- You are allowed to make pull requests that break the rules. We just merge it ;)
- Do NOT add any build steps e.g npm install (we want to keep this a simple static site)
- Do NOT remove other content.
- Styling/code can be pretty, ugly or stupid, big or small as long as it works
- Add your name to the contributorsList file
- Try to keep pull requests small to minimize merge conflicts

<br>

## FAQs

If you have any questions, please check our [FAQs](faqs.md) for answers.

## Language-Specific Folders

We have organized the project into different folders for various programming languages and web development. Choose the folder that suits your skills and interests:

- [Python](Python/)
- [C](C/)
- [C++](C++/)
- [Java](Java/)
- [Web Development](Web-Development/)

If you are new to programming, we recommend starting with the "Web Development" folder.

## Getting Started 🤩🤗:

- Fork this repo (button on top)
- Clone on your local machine

```terminal
git clone https://github.com/fineanmol/Hacktoberfest2022.git
```

- Navigate to project directory.

```terminal
cd Hacktoberfest2023
```

- Create a new Branch

```markdown
git checkout -b my-new-branch
```

- Add your Name to `contributors/contributorsList.js`

```markdown
git add .
```

- Commit your changes.

```markdown
git commit -m "Relevant message"
```

- Then push

```markdown
git push origin my-new-branch
```

- Create a new pull request from your forked repository

<br>

## Avoid Conflicts {Syncing your fork}

An easy way to avoid conflicts is to add an 'upstream' for your git repo, as other PR's may be merged while you're working on your branch/fork.

```terminal
git remote add upstream https://github.com/fineanmol/Hacktoberfest2022
```

You can verify that the new remote has been added by typing

```terminal
git remote -v
```

To pull any new changes from your parent repo simply run

```terminal
git merge upstream/master
```

This will give you any eventual conflicts and allow you to easily solve them in your repo. It's a good idea to use it frequently in between your own commits to make sure that your repo is up to date with its parent.
