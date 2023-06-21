<h1 align=center>Cherry Leaf Mildew Detector</h1>

![](docs/images/page.png)

The machine learning technology provided by this website enables users to upload pictures of cherry leaves and determine if they are in a healthy state or if they have been affected by powdery mildew.

[Live application can be found here](#)

# Planning Phase

## Business Requirements

Farmy & Foods is currently facing a challenge with their cherry plantations, as they have been affected by powdery mildew. To determine if a cherry tree is infected, their current process involves manual verification. An employee dedicates approximately 30 minutes per tree, collecting leaf samples and visually inspecting them for signs of powdery mildew. If the tree is infected, the employee applies a specific compound to eliminate the fungus, taking an additional minute. With numerous cherry trees spread across multiple farms, this manual inspection process is not feasible due to the significant time investment.

To address this issue and save time, the IT team has proposed implementing a machine learning (ML) system that can instantly detect the presence of powdery mildew using images of cherry leaves. If successful, this ML solution could be extended to detect pests in other crops as well, replicating the project across the company. The dataset for training the ML model consists of cherry leaf images provided by Farmy & Foods, captured from their own crops.

### **Project Goal:**

- 1 - The client wishes to perform a research project aimed at visually distinguishing between a healthy cherry leaf and one that is affected by powdery mildew.
- 2 - The client seeks to make predictions regarding the health status of a cherry leaf, specifically whether it is healthy or affected by powdery mildew.

## Dataset Content

- The dataset used for this project was obtained from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then developed a fictional user scenario where predictive analytics can be applied to a practical workplace project.
- The dataset comprises over 4,000 images captured from the client's crop fields. These images depict both healthy cherry leaves and cherry leaves that have been infected with powdery mildew, a fungal disease that affects various plant species. The cherry plantation crop is considered one of the company's top products, and they are concerned about maintaining high-quality standards when supplying the market.

### Sample leaves

---

| healthy                                            | podwery mildew leaf                               |
| -------------------------------------------------- | ------------------------------------------------- |
| <img src="docs/images/healthy.jpg" height='180px'> | <img src="docs/images/mildew.jpg" height='180px'> |

## Hypothesis and how to validate?

- Tree leaves affected by powdery mildew exhibit visible white streaks on their surface.
  - Traditional data analysis methods will be employed to carry out a research study aimed at visually distinguishing between a healthy cherry leaf and one that is infected with powdery mildew.

## Rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Data Visualization
  In order to visually differentiate healthy and mildew-infested cherry leaves:

  - I desire to showcase images representing the average and variability of healthy cherry leaves and cherry leaves affected by powdery mildew, as a client.
  - As a client, my goal is to exhibit the disparities between a typical, healthy cherry leaf and a cherry leaf afflicted with powdery mildew.
  - In my capacity as a client, I aim to exhibit a collection of images showcasing both a healthy cherry leaf and a leaf affected by mildew.

- **Business Requirement 2**: Classification
  - As a client, my objective is to accurately determine whether a given cherry leaf is in a healthy state or affected by powdery mildew, ensuring that I avoid supplying the market with a compromised quality product.
  - As a client, I desire to create a binary classifier and produce comprehensive reports.

## ML Business Case

- As a client, my objective is to obtain a machine learning model that can accurately predict whether a cherry leaf tree is in a healthy condition or affected by powdery mildew.
- The desired result is to offer Farmy & Foods an efficient and dependable method for detecting mildew, which can be easily scaled across numerous farms throughout the country.
- The model success metric are:
  - A research project demonstrating methods to visually distinguish between a healthy cherry leaf and one that is affected by powdery mildew.
  - The ability to accurately determine whether a cherry leaf is in a healthy state or affected by powdery mildew.The capability to predict if a cherry leaf is healthy or contains powdery mildew.
  - The model accuracy on test data is 0.9988

---

## Data Understanding

The provided dataset consists of labeled images that are organized into two separate folders, representing the respective image labels. For instance, the healthy leaf images are stored in the "healthy" directory, while the mildew-infected leaves are located in the "powder_mildew" directory.

The classification dataset contains a total of 4208 records, with an equal number of instances for each class. Specifically, there are 2104 samples of healthy leaves and 2104 samples of infected leaves, ensuring a balanced dataset.

## Data Preparation

Minimal data cleaning was necessary as the folders were scanned and any non-image files were removed. To ensure effective model training and prevent overfitting, the dataset was divided into three sets: train, test, and validation. The dataset was split with a ratio of 0.7 for the training set, 0.2 for the test set, and 0.1 for the validation set.

Data augmentation techniques were applied to the training dataset using ImageDataGenerator. This process involved generating additional training images by combining various operations, such as random rotation, shifts, shearing, zooming, and flipping, within the computer's temporary memory (RAM). ImageDataGenerator was also utilized to rescale the test and validation datasets.

## Modeling

The training dataset was employed to train the sequential model, which was further validated using the validation dataset.

Subsequently, the trained model was utilized to make predictions on the unseen test dataset, and the accuracy performance metric was computed to evaluate its performance.

## Evaluation

The model achieved an accuracy of over 97% on the test dataset, meeting the desired percentage accuracy. To further assess its performance, two leaves (one healthy and one with mildew, as demonstrated in the provided sample data) that were not included in the dataset were uploaded, and the model accurately predicted their respective conditions.

[Mildew Leaf](docs/images/detector_2.png)

[Healthy Leaf](docs/images/detector_3.png)

---

## Dashboard Design (Streamlit App User Interface)

### Dashboard Wireframe

Dashboard wireframe was created using wireframeCC. The wireframe is in pdf format and can be viewed [here](docs/images/project_wireframe.pdf)

### Page 1: Quick Project Summary

- A project summary page, showing the project dataset summary and the client's requirements.
- Quick project summary

  - General Information
  - Project Dataset

    - The dataset comprises more than four thousand images captured from the client's crop fields. These images depict cherry leaves in two conditions: healthy and affected by powdery mildew, which is a fungal disease that can impact various plants. The cherry plantation crop holds significant value in the client's product portfolio, and ensuring the market receives products of uncompromised quality is a top priority for the company.

  - Business requirements
    - The client seeks to perform a research study aimed at visually distinguishing between a healthy cherry leaf and a cherry leaf affected by powdery mildew.
    - The client has a keen interest in predicting whether a cherry tree is in a healthy state or affected by powdery mildew.

### Page 2: Cherry leaf visualizer

- It will answer business requirement 1
  - This document presents the outcomes obtained from the study focused on visually distinguishing between a healthy cherry leaf and a cherry leaf affected by powdery mildew.
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between Healthy and Powdery Mildew Cherry Leaves
  - Checkbox 3 - Image Montage

### Page 3: Mildew detector

- It will answer business requirement 2
  - Link to download a set of cherry leaf images for live prediction
  - file upload widget to upload one or more images for prediction
  - Display image and prediction statement indicating whether or not a cherry leaf conatins mildew
  - Display table with image name and prediction result
  - Download button to download table

### Page 4: Project Hypothesis and Validation

- Display each project hypothesis and validation

### Page 5: ML performance metrics

- A technical page displaying the model performance

## **Features**

The application is created utilizing the streamlit library and features a sidebar menu containing five navigation links.

**Navigation**

The developed dashboard is a multi-page streamlit application that incorporates sidebar navigation with checkbox links. These navigation links enable convenient access to the five listed pages:

- **Page 1: Quick Project Summary**
  On this page, you will find a concise summary of the project requirements and an overview of the dataset.
  ![](docs/images/page_1_summary.png)

- **Page 2: Cherry leaf visualizer**
  This page provides a concise summary outlining the project requirements and an overview of the dataset.
  ![](docs/images/page_2_visualizer_difference.png)

![](docs/images/page_2_visualizer_diff.png)

- **Page 3: Mildew Detector**
  This provides the interface for the user to upload test samples and predict wether or not the samples provided are healthy or infested with powdery leaf mildew. It features a _Browse file_ button which user can use to upload one or more image files. Prediction is not made until the user clicks on the _Make Prediction_ button. The image uploaded as well as the prediction and report is displayed to the user when the prediction is complete

![](docs/images/page_2_detector.png)

![](docs/images/3_detector_2.png)

- **Page 4: Hypothesis and Visualization**
  On this page, you will find the project hypothesis and its validation methodology explained throughout the project.
  ![](docs/images/4_hypothesis.png)

- **Page 5: ML Performance Metric**
  This page presents technical details regarding the model and data used. It includes information such as:
- The distribution of labels in the training, validation, and test datasets
- Accuracy and loss charts of the training model
- Overall performance metrics on the test datasets.

![](docs/images/5_metrics.png)

---

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Gitpod Template Instructions section of this README.md file, and modify the remaining paragraphs for your own project. Please do read the Gitpod Template Instructions at least once, though! It contains some important information about Gitpod and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Gitpod from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people that provided support throughout this project.
