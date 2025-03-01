<p align="center">
  <img width=200px height=200px src="./docs/images/logoLetrus.svg" alt="Letrus logo"></a>
</p>

<h3 align="center">
  <!-- 👉 CHANGE THIS PROJECT TITLE -->
  FastAPI Template
</h3>

---

<p align="center"> 
  <!-- 👉 CHANGE THIS PROJECT DESCRIPTION -->
  This repo provides a template for creating a new API.
  <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Performance](#performance)
- [Getting Started](#getting_started)
- [Usage](#usage)

## 💡 About <a name = "about"></a>

<!-- 👉 REPLACE HERE THE "About" DESCRIPTION OF YOUR PROJECT -->

This about section is a placeholder for the about section of your project, where you can describe your project and its goals, alongside the techniques used to achieve them.

### 👉 FAQ

- I just copied this template, what do I need to change to become a real project?
  - Change this README!!! And you can probably remove this FAQ section
  - Edit the `app/core/resources.py` file, add your own necessary variables (database connection, model, file loading, etc...)
  - Edit the `app/core/config.py` file, add your own necessary variables (database server port, model name, etc...) and edit the API name
  - Remember to edit the `requirements.txt` with needed packages, and the `docker-compose.yml` and `Dockerfile` should be revised as well
  - Change the files in `app/core/routers/v1` to match your needs
  - Create proper schemas for your models and router inputs/outputs
  - Organize your code in the proper folders: `app/core/` for internal needs of your service, `app/core/services/` for your business logic that will be reflected in the `app/core/routers`

- How to connect to a database?
  - Create a new variable in the `app/core/resources.py` file which will how the connection
  - See preprocessor-api for an example

- How to download a model from S3 and load it into memory?
  - See preprocessor-api for an example

- I want to edit/create a new route, how do I do it?
  - Edit/create a new file in the `app/routers/v1/` directory, use the existing files as a guide on how to set it up.
  - Go to `app/routers/v1/__init__.py`, import the file and do an `router.include_router(filename.router)`



## 🚀 Performance Analysis <a name = "performance"></a>

This section is a placeholder for the performance analysis of your project. A network/load test is a good place to start.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project in your local machine.

### Prerequisites

We use Python 3.8 in this project. The Python's libraries used are documented in requirements.txt.

We suggest to use VSCode as the main editor, to take advantage of code completion and other useful extensions.

We use Black for formatting code. If you contribute to this repository you should format your files with this linter.

If you are running in your local machine we recommend using some Python environment tool such as Venv or Poetry to avoid messing around with your OS Python installation and breaking stuff.

### Installing

1. First clone the repository. 
2. In the root directory run `cp .env.example .env` and fill in the environment variables accordingly.
3. **(docker)** Just `docker-compose up` and all dependencies are installed (and cached on subsequent executions) and the service starts.
4. **(local)** Create and enter your virtual environment, then run `set -a && source .env && set +a`
5. **(local)** Install project dependencies `make devinstall`.
6. **(local)** If everything goes well you can run the application using `make run`.

### Environment variables

Environment variables are defined in [.env](.env) file.

Exactly what each of the variables does is documented in the [.env.example](.env.example) file.

## 🎯 Usage <a name="usage"></a>

```
make run
```
This will run the app itself. The host and port on which the app is running will be shown on the console and you can start making requests to it. You can open the shown url in your browser, this will automatically open the API documentation.
# HealthService
