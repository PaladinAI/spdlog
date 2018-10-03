# spdlog

spdlog is a fast C++ logging library used by the
[Platform](https://github.com/PaladinAI/ddat-platform).

# Syncing with the upstream master branch

First, make sure the `upstream` remote is configured:

    git remote -v

    # If the upstream remote doesn't exist, add it:
    git remote add upstream https://github.com/gabime/spdlog.git

Then merge the upstream changes from the `v1.x` branch:

    git fetch upstream
    git checkout develop
    git merge upstream/v1.x

# Publishing to the Conan server

To update the package, update the version number in `conanfile.py` then run:

    conan create . paladin/develop
    conan upload spdlog/1.1.0@paladin/develop -r paladin
