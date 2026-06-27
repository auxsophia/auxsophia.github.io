# www.philosopherscholar.com - Personal Website

This is the source code for my [webpage](www.philosopherscholar.com).

# Now, when you want to work on the site locally, you will run the following command:
# bundle exec jekyll serve --config _config.yml,_config_dev.yml --livereload

# Install fresh:

sudo apt-get update
sudo apt-get install ruby-full build-essential zlib1g-dev

cd ~/Programs/auxsophia.github.io  # Adjust path as necessary
bundle config set --local path 'vendor/bundle'

bundle install

bundle exec jekyll serve --config _config.yml,_config_dev.yml --livereload