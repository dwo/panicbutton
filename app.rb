require 'rubygems'
$LOAD_PATH.unshift(File.expand_path('../vendor/gems/bundler-1.1.0/lib', __FILE__))
require 'bundler/setup'
require 'json'

$conf_file = '/tmp/panicbutton/config.json'

if File.file? $conf_file
  $config = JSON.parse(File.read $conf_file)
else
  $config = {'presets' => {'custom' => ''}}
end

Shoes.app :width => 430, :height => 160 do
  title "The Big Red Button"

  list = list_box :items => $config['presets'].keys
  list.choose $config['preset'] || $config['presets'].keys.first

  input = edit_box :width => 396, :height => 40
  input.text = $config['argument'] || ''

  button "SAVE" do
    $config['preset'] = list.text
    pre = $config['presets'][list.text]
    arg = $config['argument'] = input.text
    $config['command'] = pre =~ /\$1/ ? pre.gsub(/\$1/, arg) : arg
    File.open($conf_file, 'w') { |f| f.write JSON.pretty_generate($config) }
  end 
end

