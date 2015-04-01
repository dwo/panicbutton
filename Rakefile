require 'fileutils'

task :install do
  puts 'You need to install Shoes for the config panel'
  puts 'http://shoesrb.com/downloads'
  `./vendor/gems/bundler-1.1.0/bin/bundle --path vendor/bundle`
  FileUtils.mkdir_p '/tmp/panicbutton'
  FileUtils.cp File.expand_path('../config.sample.json', __FILE__), '/tmp/panicbutton/config.json'
end

task :default => :install

