# FastApi Docker Quickstart Application

[![Docker Compose Actions Workflow](https://github.com/KenMwaura1/fastapi_docker_starter/actions/workflows/fastapi-starter-docker.yml/badge.svg)](https://github.com/KenMwaura1/fastapi_docker_starter/actions/workflows/fastapi-starter-docker.yml)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<!--Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `KenMwaura1`, `fastapi_docker_starter
`, `Ken_Mwaura1`, `kennedy-mwaura`, `kemwaura@gmail.com`, `kemwaura@gmail.com_client`, `FastApi Docker Quickstart`, `Quick and easy way to dckerize a fastapi app` -->

[![Product Name Screen Shot][product-screenshot]]()

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [GitHub Actions](https://github.com/actions)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You the following prerequisites to get started with this project.

1. [Install Python 3.9.7](https://www.python.org/downloads/)
2. [Install Docker](https://docs.docker.com/install/)
3. [Install Docker Compose](https://docs.docker.com/compose/install/)
4. [Install PostgreSQL](https://www.postgresql.org/download/)
5. [Install SQLAlchemy](https://www.sqlalchemy.org/docs/05/index.html)
6. [Install FastAPI](https://fastapi.tiangolo.com/tutorial/installation.html)
7. [Create a GitHub repository](https://help.github.com/en/github/getting-started-with-github/creating-a-repository)

### Installation

1. Clone GitHub repository

    ```shell
    git clone https://github.com/KenMwaura1/fastapi_docker_starter
    ```

2. Change into the folder

    ```shell
   cd fastapi_docker_starter
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./venv/bin/activate
   ```

   * For Fish shell

   ```shell
   . venv/bin/activate.fish
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv fastapi
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate fastapi
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```

5. Add your credentials to the `.env` file

   OR

   ```
   export DATABASE_URL=postgres://username:password@localhost:5432/database_name
   ```

6. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

7. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```

8. Run the app

    ```shell
   ./run.sh
    ```

   OR
   run with [uvicorn](https://uvicorn.org/):

    ```shell
   uvicorn app.main:app --reload
    ```

## Docker Compose

To run the app and the database in a Docker Compose file follow these steps.

Open a terminal and run the following commands.

```shell
docker-compose up
```

To stop the app and the database run the following commands.

```shell
docker-compose down
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

-- TODO: Add usage examples

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

[@Ken_Mwaura1](https://twitter.com/Ken_Mwaura1
) - kemwaura@gmail.com

Project Link: [https://github.com/KenMwaura1/fastapi_docker_starter](https://github.com/KenMwaura1/fastapi_docker_starter
)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/KenMwaura1/fastapi_docker_starter.svg?style=for-the-badge
[contributors-url]: https://github.com/KenMwaura1/fastapi_docker_starter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/KenMwaura1/fastapi_docker_starter.svg?style=for-the-badge
[forks-url]: https://github.com/KenMwaura1/fastapi_docker_starter/network/members
[stars-shield]: https://img.shields.io/github/stars/KenMwaura1/fastapi_docker_starter.svg?style=for-the-badge
[stars-url]: https://github.com/KenMwaura1/fastapi_docker_starter/stargazers
[issues-shield]: https://img.shields.io/github/issues/KenMwaura1/fastapi_docker_starter.svg?style=for-the-badge
[issues-url]: https://github.com/KenMwaura1/fastapi_docker_starter/issues
[license-shield]: https://img.shields.io/github/license/KenMwaura1/fastapi_docker_starter.svg?style=for-the-badge
[license-url]: https://github.com/KenMwaura1/fastapi_docker_starter/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kennedy-mwaura
[product-screenshot]: app/static/images/Screenshot_Zoo%20Anime%20—%20Mozilla%20Firefox_1.png

## Author

[Ken Mwaura](http://github.com/KenMwaura1)
