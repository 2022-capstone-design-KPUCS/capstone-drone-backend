# Capstone Drone Backend

[![Build Status](https://travis-ci.org/KKodiac/drone-wrapper-api.svg?branch=master)](https://travis-ci.org/KKodiac/drone-wrapper-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

**Djano REST API for Tello drone SDK. Check out the project's [documentation](http://KKodiac.github.io/capstone-drone-backend/).**

Capstone Design Project at TU Korea


This is an on-going capstone design project for final year students in TU Korea. Tello drones provide a  Python SDK for their drone interface. However, their SDK lack compatibility when it comes to linking current drone stats with web/mobile interfaces(though they do provide a mobile app to use instead of physical controllers). 

While developing our capstone design project for AutoDriving Fire Dectection Drone use in Industrial complex, we needed a API wrapper for the SDK specific to those needs, and decided to make one. 

## Getting Started

### Dependencies

Tested in Ubuntu 20.04 LTS 

* Python 3.8.10
* Django 4.0.2
* DjangoRestFramework 4.10.1
* PostgreSQL 12.9
* Check out full documentation of Tello SDK [here](https://github.com/dji-sdk/Tello-Python).

### Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

### Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

Check out API documentation at [http://localhost:8001/](http://localhost:8001/)

## TODO
- [ ] Create RESTful API
- [ ] Test binding with actual working drone.
- [ ] Dockerize postgres and django


<!-- ## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
``` -->

## Authors

[Sean Hong(홍성민)](https://github.com/KKodiac)

<!-- ## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release -->

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

<!-- ## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46) -->
