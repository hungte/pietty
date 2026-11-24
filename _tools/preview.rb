#!/usr/bin/env ruby
# Minimal local preview without Jekyll: renders the pages with kramdown (GFM)
# into _preview/ using a crude Liquid substitution. GitHub Pages uses real
# Jekyll; this is only for checking the content locally.
require 'kramdown'
require 'kramdown-parser-gfm'
require 'fileutils'
require 'yaml'

root = File.expand_path('..', __dir__)
out = File.join(root, '_preview')
FileUtils.rm_rf(out)
FileUtils.mkdir_p(out)
FileUtils.cp_r(File.join(root, 'assets'), out)
config = YAML.load_file(File.join(root, '_config.yml'))
layout = File.read(File.join(root, '_layouts', 'default.html'))

def rel(path)
  path = path.sub(%r{^/}, '')
  path.empty? ? 'index.html' : path
end

%w[index download faq].each do |name|
  src = File.read(File.join(root, "#{name}.md"))
  _, fm, body = src.split(/^---\s*$/, 3)
  meta = YAML.safe_load(fm)
  body = body.gsub(/\{\{\s*["']([^"']+)["']\s*\|\s*relative_url\s*\}\}/) { rel($1) }
  html = Kramdown::Document.new(body, input: 'GFM', hard_wrap: false).to_html
  nav = config['nav'].map do |item|
    cls = item['url'] == meta['permalink'] ? ' class="active"' : ''
    %(<a href="#{rel(item['url'])}"#{cls}>#{item['title']}</a>)
  end.join("\n")
  page = layout.dup
  page.sub!(/\{% for item in site.nav %\}.*?\{% endfor %\}/m, nav)
  page.gsub!(/\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}/) { rel($1) }
  page.gsub!(/<title>.*?<\/title>/m, "<title>#{config['title']} - #{meta['title']}</title>")
  page.gsub!('{{ site.title }}', config['title'])
  page.gsub!('{{ site.description }}', config['description'])
  page.gsub!(/\{\{ site.lang[^}]*\}\}/, config['lang'])
  page.sub!('{{ content }}', html)
  File.write(File.join(out, "#{name}.html"), page)
  puts "wrote _preview/#{name}.html"
end
