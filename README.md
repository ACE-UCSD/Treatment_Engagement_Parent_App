# Treatment Engagement Parent App

## Example Screens

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <img src="lib/images/IMG_4655.PNG" alt="login" width="250"/>
    <img src="lib/images/IMG_4656.PNG" alt="home" width="250"/>
    <img src="lib/images/IMG_4650.PNG" alt="times of day" width="250"/>
    <img src="lib/images/IMG_4649.PNG" alt="trends" width="250"/>
    <img src="lib/images/IMG_4651.PNG" alt="strategies" width="250"/>
    <img src="lib/images/IMG_4652.PNG" alt="chat" width="250"/>
</div>

## Instructions for Phone Setup
1. Visit https://track-it-app-b875b.web.app/ from your mobile browser (i.e. Chrome, Safari, etc.)
2. Tap on the share website icon
3. Choose 'Add to Home Screen' (Optionally rename the shortcut)
4. Sign up via email and wait for an authentication link
   1. If link is not sent please reach out
5. After successful sign up and log in, the app is ready for logging data, and you will be connected with your expected contacts shortly

## General App Notes
- 'Trends' will not function properly until a sufficient amount of data has been logged
- Parents do not have the ability to create new contacts
  - If you are not a parent and do not have access, please reach out
- 'ASE Strategies' will be consistently updated according to current research
- 'Goals' and 'ASE Manual' have note yet been implemented as of September 2024

## Bug Tracking and To Do (Sept. 2024)

#### Times of Day

- No known issues

#### Trends

- Axis label disappearance solved 09/04/2024

#### ASE Strategies

- No known issues

#### ASE Manual

- Not implemented

#### Goals

- Not implemented

#### Contact Us

- No known issues
- Order by most recent message
- Add notification of message

## Exporting Data

From this repository, in your terminal/command prompt run:

`python export.py \path\to\credentials.json {collection_name}`

## Instructions for Installation

1. Install and setup Git, IntelliJ via JetBrains, FlutterSDK (for web)
    - Unzip this repository and FlutterSDK
2. Turn on developer mode on your system if applicable
3. After logging into IntelliJ, from the plugins tab, install Flutter
4. Add the FlutterSDK bin file (in unzipped folder) to your Path in your system's environment variables
5. In IntelliJ, add your FlutterSDK path (unzipped folder) at Settings > Languages and Frameworks > Flutter
6. From your terminal, load firebase by executing `.\firebase`, then `firebase login`, to deploy any changes to production `firebase deploy`
7. After successful deployment, from your terminal in this repo run `git add .`, `git commit -m 'insert relevant message'`, `git push`