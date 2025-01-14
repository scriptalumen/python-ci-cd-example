# python-ci-cd-example

## **Steps for Creating and Setting Up the Repository**

### **1. Create a GitHub Repository**
1. Log in to your [GitHub account](https://github.com).
2. Navigate to the **Repositories** section and click **New**.
3. Name your repository, e.g., `python-ci-cd-example`.
4. Select the **Public** or **Private** option based on your preference.
5. Check the box for **Add a README file** to initialize the repository.
6. Click **Create Repository** to finalize the creation.

---

### **2. Clone the Repository Locally**
1. Open your terminal or command prompt.
2. Clone the repository using the following command (replace `your-username` with your GitHub username):

   ```bash
   git clone https://github.com/your-username/python-ci-cd-example.git
   ```

3. Navigate into the project directory:

   ```bash
   cd python-ci-cd-example
   ```

---

### **3. Create a DockerHub Repository**
1. Log in to your [DockerHub account](https://hub.docker.com).
2. Click on **Repositories** in the top navigation menu and select **Create Repository**.
3. Provide a name for the repository, e.g., `python-ci-cd-example`.
4. Ensure the **Namespace** matches your DockerHub username.
5. Choose whether to make the repository **Public** or **Private**.
6. Click **Create** to save the repository.

---

### **4. Add Your Project Files**
1. Place your Python application files (e.g., `app.py`) and test files (e.g., `test_app.py`) in the local project directory.
2. Create a `Dockerfile` in the root of the project .
3. Use the following commands to stage and commit the files to the repository:

   ```bash
   git add .
   git commit -m "Add application files and Dockerfile"
   git push origin main
   ```

---

### **5. Set Up GitHub Actions Workflow**
1. In the root of your project, create the following directory structure: `.github/workflows/`.
2. Create a file named `docker-publish.yml` in the `workflows` folder and add the workflow configuration.
3. Push the workflow file to the repository:

   ```bash
   git add .github/workflows/docker-publish.yml
   git commit -m "Add GitHub Actions workflow for CI/CD"
   git push origin main
   ```

---

### **6. Configure GitHub Secrets**
1. Go to your repository on GitHub and navigate to **Settings > Secrets and variables > Actions**.
2. Add the following secrets:
   - `DOCKER_USERNAME`: Your DockerHub username.
   - `DOCKER_PASSWORD`: Your DockerHub access token.

---

### **7. Test the CI/CD Pipeline**
1. Make any change in your project (e.g., edit `app.py` or add a new file) to trigger the pipeline.
2. Push the change to the `main` branch:

   ```bash
   git add .
   git commit -m "Test CI/CD pipeline"
   git push origin main
   ```

3. Go to the **Actions** tab in your GitHub repository to monitor the workflow progress.
